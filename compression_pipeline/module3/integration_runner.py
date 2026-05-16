# import json
# import os
# import sys
# import logging
# import time

# # Turn on INFO logs to track BART model downloads and pipeline progress
# logging.basicConfig(level=logging.INFO, format='%(message)s')

# # Ensure the local summarizer package can be imported
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# from summarizer.pipeline import run_pipeline

# # ---------------------------------------------------------------------------
# # Configuration — tune these to control performance vs. quality
# # ---------------------------------------------------------------------------
# CHUNKS_PER_SECTION = 20   
# AWS_DOMAIN_TERMS = ["aws", "s3", "bucket", "object", "api", "endpoint", "iam", "policy", "token", "credentials", "upload", "amazon"]

# def build_production_input():
#     """Reads REAL Module 1 and Module 2 outputs to feed into Module 3."""
#     m1_dir = os.path.abspath("compression_pipeline/module1/s3/intermediate/")
#     m2_dir = os.path.abspath("compression_pipeline/module2/")
    
#     chunks_path = os.path.join(m1_dir, "chunks.json")
#     akus_path = os.path.join(m1_dir, "akus.json")
#     kg_path = os.path.join(m2_dir, "knowledge_graph.json")

#     logging.info(f"Loading Module 1 & 2 data from:\n - {m1_dir}\n - {m2_dir}")
    
#     with open(chunks_path, 'r',encoding='utf-8') as f:
#         m1_chunks = json.load(f)
#     with open(akus_path, 'r',encoding='utf-8') as f:
#         m1_akus = json.load(f)
#     with open(kg_path, 'r',encoding='utf-8') as f:
#         m2_kg = json.load(f)
#     # 1. Format Chunks and attach REAL AKUs
#     formatted_chunks = []
#     raw_chunk_list = m1_chunks if isinstance(m1_chunks, list) else list(m1_chunks.values())
    
    
#     chunk_list = []
#     for i, c in enumerate(raw_chunk_list):
#         if isinstance(c, dict):
#             flat_c = {**c, **c.get("metadata", {})} # Bring metadata to the top level
#             flat_c["chunk_id"] = flat_c.get("chunk_id", f"chunk_{i}") # Safe ID fallback
#             flat_c["text"] = flat_c.get("content", flat_c.get("text", str(c))) # Fix text key mismatch
#             chunk_list.append(flat_c)
#         else:
#             chunk_list.append({"chunk_id": f"chunk_{i}", "text": str(c)})

#     chunk_list = chunk_list # Keeps execution fast for local testing
#     aku_list = m1_akus if isinstance(m1_akus, list) else list(m1_akus.values())

#     # Map edges to chunks so we know which relationships belong to which chunk
#     chunk_relationships = {c['chunk_id']: [] for c in chunk_list}
#     chunk_entities = {c['chunk_id']: set() for c in chunk_list}
    
#     for edge in m2_kg.get('edges', []):
#         for c_id in edge.get('source_chunks', []):
#             if c_id in chunk_relationships:
#                 chunk_relationships[c_id].append({
#                     "source": edge["source"],
#                     "relation": edge["predicate"],
#                     "target": edge["target"]
#                 })
#                 chunk_entities[c_id].add(edge["source"])
#                 chunk_entities[c_id].add(edge["target"])

#     for i, chunk_data in enumerate(chunk_list):
#         chunk_id = chunk_data.get("chunk_id", f"c{i}")
#         text = chunk_data.get("text", str(chunk_data))
        
#         # Match AKUs
#         chunk_aku = aku_list[i].get("akus", []) if i < len(aku_list) and isinstance(aku_list[i], dict) else []
        
#         # FILTER: Only keep entities that have real technical value
#         raw_entities = list(chunk_entities.get(chunk_id, set()))
#         filtered_entities = [e for e in raw_entities if any(term in e.lower() for term in AWS_DOMAIN_TERMS)]
        
#         formatted_chunks.append({
#             "chunk_id": chunk_id,
#             "text": text,
#             "akus": [{"subject": a[0], "predicate": a[1], "object": a[2]} for a in chunk_aku if len(a) == 3],
#             "entities": filtered_entities, # Pass the clean entities
#             "relationships": chunk_relationships.get(chunk_id, []),
#             "importance_score": 0.8
#         })

#     # 2. Format REAL Topics from Module 2
#     formatted_topics = []
#     for t in m2_kg.get("topics", []):
#         label = t.get("heading_path", ["General"])[-1] if t.get("heading_path") else "General"
#         formatted_topics.append({
#             "topic_id": t["topic_id"],
#             "label": label,
#             "related_docs": ["AWS-Document"]
#         })

#     # 3. Wrap in the master schema
#     input_data = {
#         "documents": [
#             {
#                 "doc_id": "AWS-Document",
#                 "sections": [
#                     {
#                         "section_id": "sec_master",
#                         "chunks": formatted_chunks
#                     }
#                 ]
#             }
#         ],
#         "topics": formatted_topics,
#         "categories": {
#             "Storage": [t["topic_id"] for t in formatted_topics] # Map all discovered topics to a category
#         }
#     }
    
#     return input_data


# def main():
#     t_start = time.time()

    
#     print("  Module 3 — Hierarchical Summarization (Integration Test)")
#     print("=" * 60)

#     print("\nStep 1: Data from M1 and M2: ")
#     input_data = build_production_input()

#     print("\nStep 2: Triggering Hierarchical Summarization Pipeline...")
#     print("  Pipeline: L4 (Sections) → L3 (Documents) → L2 (Topics) → L1 (Categories) → L0 (Global)\n")

#     # This will run L4 -> L3 -> L2 -> L1 -> L0 automatically
#     final_output = run_pipeline(
#         input_data,
#         level_4_max_tokens=500,
#         level_3_max_tokens=200,
#         level_2_max_tokens=100,
#         level_1_max_tokens=50,
#         level_0_max_tokens=25,
#     )

#     # Save raw pipeline output (for comparison)
#     raw_output_path = "compression_pipeline/integration_output.json"
#     with open(raw_output_path, 'w', encoding='utf-8') as f:
#         json.dump(final_output, f, indent=2, ensure_ascii=False)

#     # Step 3: Transform into clean structured format
#     print(f"\nStep 3: Transforming into structured output format...")
#     from transform_output import transform_output
#     structured = transform_output(final_output)

#     structured_output_path = "compression_pipeline/structured_output.json"
#     with open(structured_output_path, 'w', encoding='utf-8') as f:
#         json.dump(structured, f, indent=2, ensure_ascii=False)

#     # Summary stats
#     # 1. Total Original Tokens (From the raw AWS Markdown chunks)
#     total_doc_tokens = 0
#     for doc in input_data.get("documents", []):
#         for sec in doc.get("sections", []):
#             for chunk in sec.get("chunks", []):
#                 # Grab the token_count that tiktoken generated in Module 1
#                 total_doc_tokens += chunk.get("token_count", 0)

#     # 2. Total Final Tokens (From the fully summarized, structured output)
#     total_final_tokens = sum(s["token_count"] for s in structured.get("level_4", []))

#     # 3. Overall Document Compression Ratio
#     if total_doc_tokens > 0:
#         overall_compression_ratio = total_final_tokens / total_doc_tokens
#         reduction_percentage = (1.0 - overall_compression_ratio) * 100
#     else:
#         overall_compression_ratio = 0.0
#         reduction_percentage = 0.0

#     elapsed = round(time.time() - t_start, 1)
#     print(f"\n  Integration Test Complete!")
#     print(f"  Raw output:        {os.path.abspath(raw_output_path)}")
#     print(f"  Structured output: {os.path.abspath(structured_output_path)}")
#     print(f"  Sections Generated: {len(structured['level_4'])}")
#     print(f"  Tokens: {total_doc_tokens:,} (AWS Source) → {total_final_tokens:,} (Final Summary)")
#     print(f"  Total Document Compression: {reduction_percentage:.1f}% reduction (Final size is {overall_compression_ratio:.1%} of original)")
#     print(f"  Total time: {elapsed}s")
    

# if __name__ == "__main__":
#     main()

import json
import os
import sys
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import individual level summarizers directly
from summarizer.section_summarizer   import summarize_sections
from summarizer.document_summarizer  import summarize_documents
from summarizer.topic_summarizer     import summarize_topics
from summarizer.category_summarizer  import summarize_categories
from summarizer.global_summarizer    import generate_global_summary
from summarizer.validator            import validate_summary

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
CHUNKS_PER_SECTION = 30
AWS_DOMAIN_TERMS = ["aws", "s3", "bucket", "object", "api", "endpoint", "iam",
                    "policy", "token", "credentials", "upload", "amazon"]

LEVEL_4_MAX_TOKENS = 650
LEVEL_3_MAX_TOKENS = 230
LEVEL_2_MAX_TOKENS = 150
LEVEL_1_MAX_TOKENS = 100
LEVEL_0_MAX_TOKENS = 75


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def build_chunk_list():
    """Load and format all chunks, topics, and categories from M1 and M2."""
    m1_dir = os.path.abspath("compression_pipeline/module1/s3/intermediate/")
    m2_dir = os.path.abspath("compression_pipeline/module2/")

    logging.info(f"Loading data from:\n  M1: {m1_dir}\n  M2: {m2_dir}")

    with open(os.path.join(m1_dir, "chunks.json"), 'r', encoding='utf-8') as f:
        m1_chunks = json.load(f)
    with open(os.path.join(m1_dir, "akus.json"), 'r', encoding='utf-8') as f:
        m1_akus = json.load(f)
    with open(os.path.join(m2_dir, "knowledge_graph.json"), 'r', encoding='utf-8') as f:
        m2_kg = json.load(f)

    raw_chunk_list = m1_chunks if isinstance(m1_chunks, list) else list(m1_chunks.values())
    aku_list = m1_akus if isinstance(m1_akus, list) else list(m1_akus.values())

    chunk_list = []
    for i, c in enumerate(raw_chunk_list):
        if isinstance(c, dict):
            flat_c = {**c, **c.get("metadata", {})}
            flat_c["chunk_id"] = flat_c.get("chunk_id", f"chunk_{i}")
            flat_c["text"]     = flat_c.get("content", flat_c.get("text", str(c)))
            chunk_list.append(flat_c)
        else:
            chunk_list.append({"chunk_id": f"chunk_{i}", "text": str(c)})

    # Build relationship/entity maps from M2 knowledge graph
    chunk_relationships = {c['chunk_id']: [] for c in chunk_list}
    chunk_entities      = {c['chunk_id']: set() for c in chunk_list}

    for edge in m2_kg.get('edges', []):
        for c_id in edge.get('source_chunks', []):
            if c_id in chunk_relationships:
                chunk_relationships[c_id].append({
                    "source":   edge["source"],
                    "relation": edge["predicate"],
                    "target":   edge["target"]
                })
                chunk_entities[c_id].add(edge["source"])
                chunk_entities[c_id].add(edge["target"])

    formatted_chunks = []
    for i, chunk_data in enumerate(chunk_list):
        chunk_id = chunk_data.get("chunk_id", f"c{i}")
        chunk_aku = (aku_list[i].get("akus", [])
                     if i < len(aku_list) and isinstance(aku_list[i], dict) else [])
        raw_entities      = list(chunk_entities.get(chunk_id, set()))
        filtered_entities = [e for e in raw_entities
                             if any(t in e.lower() for t in AWS_DOMAIN_TERMS)]
        formatted_chunks.append({
            "chunk_id":         chunk_id,
            "text":             chunk_data.get("text", ""),
            "akus":             [{"subject": a[0], "predicate": a[1], "object": a[2]}
                                  for a in chunk_aku if len(a) == 3],
            "entities":         filtered_entities,
            "relationships":    chunk_relationships.get(chunk_id, []),
            "importance_score": 0.8,
            "token_count":      chunk_data.get("token_count", 0),
        })

    # Topics and categories from M2
    formatted_topics = []
    for t in m2_kg.get("topics", []):
        label = (t.get("heading_path", ["General"])[-1]
                 if t.get("heading_path") else "General")
        formatted_topics.append({
            "topic_id":     t["topic_id"],
            "label":        label,
            "related_docs": ["AWS-Document"]
        })

    categories = {"Storage": [t["topic_id"] for t in formatted_topics]}
    return formatted_chunks, formatted_topics, categories


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _count_tokens(text):
    return len(text.split()) if isinstance(text, str) else 0


def compression_ratio(final_tokens, original_tokens):
    if original_tokens == 0:
        return 0.0, 0.0
    ratio     = final_tokens / original_tokens
    reduction = (1.0 - ratio) * 100
    return ratio, reduction


def _collect_source_text(chunks):
    return " ".join(c.get("text", "") for c in chunks)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    t_start = time.time()

    print("=" * 65)
    print("  Module 3 — Hierarchical Summarization (Optimized Batch Mode)")
    print("=" * 65)

    # ---- Step 1: Load ----
    print("\nStep 1: Loading data from M1 and M2...")
    all_chunks, topics, categories = build_chunk_list()

    total_chunks       = len(all_chunks)
    total_input_tokens = sum(c.get("token_count", 0) for c in all_chunks)
    n_batches          = (total_chunks + CHUNKS_PER_SECTION - 1) // CHUNKS_PER_SECTION

    print(f"  Chunks         : {total_chunks}")
    print(f"  Input tokens   : {total_input_tokens:,}")
    print(f"  Topics         : {len(topics)}")
    print(f"  Batch size     : {CHUNKS_PER_SECTION} chunks")
    print(f"  Total batches  : {n_batches}")

    batch_dir = "compression_pipeline/module3/batch_outputs"
    os.makedirs(batch_dir, exist_ok=True)

    source_text = _collect_source_text(all_chunks)

    # ---- Step 2: L4 + L3 per batch ----
    print(f"\nStep 2: Running L4 (Sections) + L3 (Documents) — {n_batches} batches...")
    print(f"  {'Batch':>5}  {'Chunks':>12}  {'Input Tok':>10}  {'L4 Tok':>8}  {'L3 Tok':>8}  {'Time':>6}")
    print(f"  {'-' * 58}")

    all_l4 = []
    all_l3 = []
    validation_reports = {}
    timing = {}
    batch_rows = []

    for batch_idx in range(n_batches):
        start        = batch_idx * CHUNKS_PER_SECTION
        end          = min(start + CHUNKS_PER_SECTION, total_chunks)
        batch_chunks = all_chunks[start:end]

        batch_input_tokens = sum(c.get("token_count", 0) for c in batch_chunks)
        t_batch = time.time()

        # Build document structure for this batch
        batch_doc = [{
            "doc_id": "AWS-Document",
            "sections": [{
                "section_id": f"sec_batch_{batch_idx:03d}",
                "chunks":     batch_chunks,
            }]
        }]

        # L4 — Section summaries (extractive / TextRank)
        t0 = time.time()
        batch_l4 = summarize_sections(batch_doc, max_tokens=LEVEL_4_MAX_TOKENS)
        timing["level_4"] = timing.get("level_4", 0) + round(time.time() - t0, 3)

        for sec in batch_l4:
            vr = validate_summary(
                sec.get("summary", ""),
                entities=sec.get("preserved_entities"),
                akus=sec.get("preserved_akus"),
                source_text=source_text,
            )
            validation_reports[f"L4_{sec.get('section_id', '')}"] = vr

        # L3 — Document summaries (hybrid)
        t0 = time.time()
        batch_l3 = summarize_documents(batch_doc, batch_l4, max_tokens=LEVEL_3_MAX_TOKENS)
        timing["level_3"] = timing.get("level_3", 0) + round(time.time() - t0, 3)

        for doc_sum in batch_l3:
            vr = validate_summary(
                doc_sum.get("summary", ""),
                entities=doc_sum.get("top_entities"),
                relationships=doc_sum.get("top_relationships"),
                source_text=source_text,
            )
            validation_reports[f"L3_batch{batch_idx}_{doc_sum.get('doc_id', '')}"] = vr

        all_l4.extend(batch_l4)
        all_l3.extend(batch_l3)

        b_l4_tok = sum(s.get("token_count", 0) for s in batch_l4)
        b_l3_tok = sum(d.get("token_count", 0) for d in batch_l3)
        elapsed_batch = round(time.time() - t_batch, 1)

        print(f"  {batch_idx+1:>5}  {start+1:>5}–{end:<5}      {batch_input_tokens:>10,}  "
              f"{b_l4_tok:>8,}  {b_l3_tok:>8,}  {elapsed_batch:>5.1f}s")

        # Save batch output
        batch_file = os.path.join(batch_dir, f"batch_{batch_idx:03d}.json")
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump({"level_4_sections": batch_l4, "level_3_documents": batch_l3}, f,
                      indent=2, ensure_ascii=False)

        batch_rows.append({
            "batch": batch_idx + 1,
            "input_tokens": batch_input_tokens,
            "l4": b_l4_tok, "l3": b_l3_tok,
        })

    print(f"\n  L4 + L3 complete. Total sections: {len(all_l4)}  Total doc summaries: {len(all_l3)}")

    # ---- Step 3: L2 once on all topics ----
    print(f"\nStep 3: Running L2 (Topics) — {len(topics)} topics using merged L3...")
    t0 = time.time()
    all_entities = list(dict.fromkeys(
        e for c in all_chunks for e in c.get("entities", [])
    ))
    level_2 = summarize_topics(topics, all_l3, max_tokens=LEVEL_2_MAX_TOKENS)
    timing["level_2"] = round(time.time() - t0, 3)

    for topic_sum in level_2:
        vr = validate_summary(topic_sum.get("summary", ""), entities=all_entities)
        validation_reports[f"L2_{topic_sum.get('topic_id', '')}"] = vr

    l2_tok = sum(t.get("token_count", 0) for t in level_2)
    print(f"  Done. Topics summarized: {len(level_2)}  Tokens: {l2_tok:,}  ({timing['level_2']}s)")

    # ---- Step 4: L1 once on all categories ----
    print(f"\nStep 4: Running L1 (Categories)...")
    t0 = time.time()
    level_1 = summarize_categories(categories, level_2, max_tokens=LEVEL_1_MAX_TOKENS)
    timing["level_1"] = round(time.time() - t0, 3)

    for cat_sum in level_1:
        vr = validate_summary(cat_sum.get("summary", ""), entities=all_entities)
        validation_reports[f"L1_{cat_sum.get('category', '')}"] = vr

    l1_tok = sum(c.get("token_count", 0) for c in level_1)
    print(f"  Done. Categories: {len(level_1)}  Tokens: {l1_tok:,}  ({timing['level_1']}s)")

    # ---- Step 5: L0 global summary ----
    print(f"\nStep 5: Running L0 (Global Summary)...")
    t0 = time.time()
    level_0 = generate_global_summary(level_1, max_tokens=LEVEL_0_MAX_TOKENS)
    timing["level_0"] = round(time.time() - t0, 3)

    vr = validate_summary(level_0, entities=all_entities, source_text=source_text)
    validation_reports["L0_global"] = vr

    l0_tok = _count_tokens(level_0)
    print(f"  Done. Global summary tokens: {l0_tok}  ({timing['level_0']}s)")
    print(f"  Global: \"{level_0}\"")

    # ---- Assemble and save final output ----
    final_output = {
        "level_4_sections":  all_l4,
        "level_3_documents": all_l3,
        "level_2_topics":    level_2,
        "level_1_categories": level_1,
        "level_0_global":    level_0,
        "validation_reports": validation_reports,
        "timing":            timing,
    }

    raw_output_path = "compression_pipeline/integration_output.json"
    with open(raw_output_path, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, indent=2, ensure_ascii=False)

    # ---- Step 6: Transform ----
    print(f"\nStep 6: Transforming into structured output format...")
    from transform_output import transform_output
    structured = transform_output(final_output)

    structured_output_path = "compression_pipeline/structured_output.json"
    with open(structured_output_path, 'w', encoding='utf-8') as f:
        json.dump(structured, f, indent=2, ensure_ascii=False)

    # ---- Compression stats ----
    l4_tok = sum(s.get("token_count", 0) for s in all_l4)
    l3_tok = sum(d.get("token_count", 0) for d in all_l3)

    l4_ratio, l4_red = compression_ratio(l4_tok,  total_input_tokens)
    l3_ratio, l3_red = compression_ratio(l3_tok,  total_input_tokens)
    l2_ratio, l2_red = compression_ratio(l2_tok,  total_input_tokens)
    l1_ratio, l1_red = compression_ratio(l1_tok,  total_input_tokens)
    l0_ratio, l0_red = compression_ratio(l0_tok,  total_input_tokens)

    total_compressed_tokens = l4_tok + l3_tok + l2_tok + l1_tok + l0_tok
    overall_ratio = total_input_tokens / total_compressed_tokens if total_compressed_tokens > 0 else 0
    overall_reduction = (1.0 - (total_compressed_tokens / total_input_tokens)) * 100 if total_input_tokens > 0 else 0
    elapsed = round(time.time() - t_start, 1)

    print(f"\n  {'=' * 70}")
    print(f"   OVERALL COMPRESSION RATIO (ALL LEVELS) — CORRECT METRIC")
    print(f"  {'=' * 70}")
    print(f"  Module 1 Input (chunks)              : {total_input_tokens:>10,} tokens")
    print(f"  Module 3 Output (L4+L3+L2+L1+L0)     : {total_compressed_tokens:>10,} tokens")
    print(f"  Overall Compression Ratio            : {overall_ratio:>10.2f}:1")
    print(f"  Overall Token Reduction              : {overall_reduction:>9.1f}%")
    print(f"  {'=' * 70}")
    
    print(f"\n   BREAKDOWN BY LEVEL (% of total compressed)")
    print(f"  {'-' * 50}")
    if total_compressed_tokens > 0:
        print(f"  L4 (Sections):   {l4_tok:>8,} tokens ({l4_tok/total_compressed_tokens*100:>5.1f}%)")
        print(f"  L3 (Documents):  {l3_tok:>8,} tokens ({l3_tok/total_compressed_tokens*100:>5.1f}%)")
        print(f"  L2 (Topics):     {l2_tok:>8,} tokens ({l2_tok/total_compressed_tokens*100:>5.1f}%)")
        print(f"  L1 (Categories): {l1_tok:>8,} tokens ({l1_tok/total_compressed_tokens*100:>5.1f}%)")
        print(f"  L0 (Global):     {l0_tok:>8,} tokens ({l0_tok/total_compressed_tokens*100:>5.1f}%)")
    
    print(f"\n  {'=' * 70}")
    print(f"  TARGET CHECK")
    print(f"  {'=' * 70}")
    print(f"  Target range:    15:1 to 20:1")
    print(f"  Current ratio:   {overall_ratio:.2f}:1")
    
    if 15 <= overall_ratio <= 20:
        print(f"  Status:          WITHIN TARGET RANGE")
    elif overall_ratio > 20:
        print(f"  Status:            TOO AGGRESSIVE - Increase token budgets")
    else:
        print(f"  Status:           NOT ENOUGH COMPRESSION - Decrease token budgets")
    
    print(f"  {'=' * 70}")
    print(f"  Total pipeline time: {elapsed}s")


if __name__ == "__main__":
    main()