import json
import os
import sys
import logging

# Turn on INFO logs to track BART model downloads and pipeline progress
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Ensure the local summarizer package can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from summarizer.pipeline import run_pipeline

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
    chunk_list = m1_chunks if isinstance(m1_chunks, list) else list(m1_chunks.values())
    chunk_list = chunk_list[:5]
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
        
        formatted_chunks.append({
            "chunk_id": chunk_id,
            "text": text,
            "akus": [{"subject": a[0], "predicate": a[1], "object": a[2]} for a in chunk_aku if len(a) == 3],
            "entities": list(chunk_entities.get(chunk_id, set())),
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
    logging.info("Step 1: Building production input data from M1 & M2...")
    input_data = build_production_input()

    logging.info("\nStep 2: Triggering Hierarchical Summarization Pipeline...")
    final_output = run_pipeline(
        input_data,
        level_4_max_tokens=500,
        level_3_max_tokens=200,
        level_2_max_tokens=100,
        level_1_max_tokens=50,
        level_0_max_tokens=25
    )

    output_path = "final_pipeline_output.json"
    with open(output_path, 'w') as f:
        json.dump(final_output, f, indent=2)
        
    logging.info(f"\n✅ Full Pipeline Complete! Output saved to: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    main()