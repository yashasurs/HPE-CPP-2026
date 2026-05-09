import json
import os
import sys
import logging
import time

# Turn on INFO logs to track BART model downloads and pipeline progress
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Ensure the local summarizer package can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from summarizer.pipeline import run_pipeline

# ---------------------------------------------------------------------------
# Configuration — tune these to control performance vs. quality
# ---------------------------------------------------------------------------
CHUNKS_PER_SECTION = 20   
AWS_DOMAIN_TERMS = ["aws", "s3", "bucket", "object", "api", "endpoint", "iam", "policy", "token", "credentials", "upload", "amazon"]

def build_production_input():
    """Reads REAL Module 1 and Module 2 outputs to feed into Module 3."""
    m1_dir = os.path.abspath("compression_pipeline/module1/s3/intermediate/")
    m2_dir = os.path.abspath("compression_pipeline/module2/")
    
    chunks_path = os.path.join(m1_dir, "chunks.json")
    akus_path = os.path.join(m1_dir, "akus.json")
    kg_path = os.path.join(m2_dir, "knowledge_graph.json")

    logging.info(f"Loading Module 1 & 2 data from:\n - {m1_dir}\n - {m2_dir}")
    
    with open(chunks_path, 'r',encoding='utf-8') as f:
        m1_chunks = json.load(f)
    with open(akus_path, 'r',encoding='utf-8') as f:
        m1_akus = json.load(f)
    with open(kg_path, 'r',encoding='utf-8') as f:
        m2_kg = json.load(f)
    # 1. Format Chunks and attach REAL AKUs
    formatted_chunks = []
    raw_chunk_list = m1_chunks if isinstance(m1_chunks, list) else list(m1_chunks.values())
    
    
    chunk_list = []
    for i, c in enumerate(raw_chunk_list):
        if isinstance(c, dict):
            flat_c = {**c, **c.get("metadata", {})} # Bring metadata to the top level
            flat_c["chunk_id"] = flat_c.get("chunk_id", f"chunk_{i}") # Safe ID fallback
            flat_c["text"] = flat_c.get("content", flat_c.get("text", str(c))) # Fix text key mismatch
            chunk_list.append(flat_c)
        else:
            chunk_list.append({"chunk_id": f"chunk_{i}", "text": str(c)})

    chunk_list = chunk_list # Keeps execution fast for local testing
    aku_list = m1_akus if isinstance(m1_akus, list) else list(m1_akus.values())

    # Map edges to chunks so we know which relationships belong to which chunk
    chunk_relationships = {c['chunk_id']: [] for c in chunk_list}
    chunk_entities = {c['chunk_id']: set() for c in chunk_list}
    
    for edge in m2_kg.get('edges', []):
        for c_id in edge.get('source_chunks', []):
            if c_id in chunk_relationships:
                chunk_relationships[c_id].append({
                    "source": edge["source"],
                    "relation": edge["predicate"],
                    "target": edge["target"]
                })
                chunk_entities[c_id].add(edge["source"])
                chunk_entities[c_id].add(edge["target"])

    for i, chunk_data in enumerate(chunk_list):
        chunk_id = chunk_data.get("chunk_id", f"c{i}")
        text = chunk_data.get("text", str(chunk_data))
        
        # Match AKUs
        chunk_aku = aku_list[i].get("akus", []) if i < len(aku_list) and isinstance(aku_list[i], dict) else []
        
        # FILTER: Only keep entities that have real technical value
        raw_entities = list(chunk_entities.get(chunk_id, set()))
        filtered_entities = [e for e in raw_entities if any(term in e.lower() for term in AWS_DOMAIN_TERMS)]
        
        formatted_chunks.append({
            "chunk_id": chunk_id,
            "text": text,
            "akus": [{"subject": a[0], "predicate": a[1], "object": a[2]} for a in chunk_aku if len(a) == 3],
            "entities": filtered_entities, # Pass the clean entities
            "relationships": chunk_relationships.get(chunk_id, []),
            "importance_score": 0.8
        })

    # 2. Format REAL Topics from Module 2
    formatted_topics = []
    for t in m2_kg.get("topics", []):
        label = t.get("heading_path", ["General"])[-1] if t.get("heading_path") else "General"
        formatted_topics.append({
            "topic_id": t["topic_id"],
            "label": label,
            "related_docs": ["AWS-Document"]
        })

    # 3. Wrap in the master schema
    input_data = {
        "documents": [
            {
                "doc_id": "AWS-Document",
                "sections": [
                    {
                        "section_id": "sec_master",
                        "chunks": formatted_chunks
                    }
                ]
            }
        ],
        "topics": formatted_topics,
        "categories": {
            "Storage": [t["topic_id"] for t in formatted_topics] # Map all discovered topics to a category
        }
    }
    
    return input_data


def main():
    t_start = time.time()

    
    print("  Module 3 — Hierarchical Summarization (Integration Test)")
    print("=" * 60)

    print("\nStep 1: Data from M1 and M2: ")
    input_data = build_production_input()

    print("\nStep 2: Triggering Hierarchical Summarization Pipeline...")
    print("  Pipeline: L4 (Sections) → L3 (Documents) → L2 (Topics) → L1 (Categories) → L0 (Global)\n")

    # This will run L4 -> L3 -> L2 -> L1 -> L0 automatically
    final_output = run_pipeline(
        input_data,
        level_4_max_tokens=500,
        level_3_max_tokens=200,
        level_2_max_tokens=100,
        level_1_max_tokens=50,
        level_0_max_tokens=25,
    )

    # Save raw pipeline output (for comparison)
    raw_output_path = "compression_pipeline/integration_output.json"
    with open(raw_output_path, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, indent=2, ensure_ascii=False)

    # Step 3: Transform into clean structured format
    print(f"\nStep 3: Transforming into structured output format...")
    from transform_output import transform_output
    structured = transform_output(final_output)

    structured_output_path = "compression_pipeline/structured_output.json"
    with open(structured_output_path, 'w', encoding='utf-8') as f:
        json.dump(structured, f, indent=2, ensure_ascii=False)

    # Summary stats
    # 1. Total Original Tokens (From the raw AWS Markdown chunks)
    total_doc_tokens = 0
    for doc in input_data.get("documents", []):
        for sec in doc.get("sections", []):
            for chunk in sec.get("chunks", []):
                # Grab the token_count that tiktoken generated in Module 1
                total_doc_tokens += chunk.get("token_count", 0)

    # 2. Total Final Tokens (From the fully summarized, structured output)
    total_final_tokens = sum(s["token_count"] for s in structured.get("level_4", []))

    # 3. Overall Document Compression Ratio
    if total_doc_tokens > 0:
        overall_compression_ratio = total_final_tokens / total_doc_tokens
        reduction_percentage = (1.0 - overall_compression_ratio) * 100
    else:
        overall_compression_ratio = 0.0
        reduction_percentage = 0.0

    elapsed = round(time.time() - t_start, 1)
    print(f"\n  Integration Test Complete!")
    print(f"  Raw output:        {os.path.abspath(raw_output_path)}")
    print(f"  Structured output: {os.path.abspath(structured_output_path)}")
    print(f"  Sections Generated: {len(structured['level_4'])}")
    print(f"  Tokens: {total_doc_tokens:,} (AWS Source) → {total_final_tokens:,} (Final Summary)")
    print(f"  Total Document Compression: {reduction_percentage:.1f}% reduction (Final size is {overall_compression_ratio:.1%} of original)")
    print(f"  Total time: {elapsed}s")
    

if __name__ == "__main__":
    main()