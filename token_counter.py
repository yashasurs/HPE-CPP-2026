import os
import tiktoken
from collections import defaultdict


TARGET_DIR = "data/prototype"  
ENCODING_NAME = "cl100k_base"
OUTPUT_FILE = "tokencount.txt"


def run_token_analysis():
    print(f"Initializing tokenizer ({ENCODING_NAME})...")
    encoding = tiktoken.get_encoding(ENCODING_NAME)
    
    if not os.path.exists(TARGET_DIR):
        print(f"Error: Directory '{TARGET_DIR}' not found. Please check the path.")
        return

    total_tokens = 0
    file_counts = {}
    service_counts = defaultdict(int)

    print(f"Scanning '{TARGET_DIR}' for Markdown files...\n")

    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        text = f.read()
                        
                    tokens = len(encoding.encode(text))
                    file_counts[filepath] = tokens
                    total_tokens += tokens
                    
                    # Service grouping
                    path_parts = os.path.normpath(filepath).split(os.sep)
                    if len(path_parts) >= 3 and path_parts[0] == 'data' and path_parts[1] == 'prototype':
                        service_name = path_parts[2]
                        service_counts[service_name] += tokens
                    else:
                        service_counts["uncategorized"] += tokens
                        
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

 
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("=" * 50 + "\n")
        out.write(" TOKEN ANALYSIS REPORT\n")
        out.write("=" * 50 + "\n")
        out.write(f"Total Markdown Files: {len(file_counts)}\n")
        out.write(f"Total System Tokens:  {total_tokens:,}\n\n")

        out.write("--- Tokens by Service ---\n")
        for service, count in sorted(service_counts.items(), key=lambda x: x[1], reverse=True):
            out.write(f"{service.upper():<15} : {count:>10,} tokens\n")

        out.write("\n--- Token Count Per File ---\n")
        for filepath, count in sorted(file_counts.items(), key=lambda x: x[1], reverse=True):
            out.write(f"{count:>10,} tokens : {filepath}\n")

        out.write("\n--- Top 5 Largest Files ---\n")
        sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)
        for filepath, count in sorted_files[:5]:
            short_path = os.path.join(os.path.basename(os.path.dirname(filepath)), os.path.basename(filepath))
            out.write(f"{count:>10,} tokens : {short_path}\n")

        out.write("=" * 50 + "\n")    
    '''
    print("=" * 50)
    print(" TOKEN ANALYSIS REPORT")
    print("=" * 50)
    print(f"Total Markdown Files: {len(file_counts)}")
    print(f"Total System Tokens:  {total_tokens:,}\n")

    print("--- Token Count Per File ---")
    for filepath, count in sorted(file_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{count:>10,} tokens : {filepath}")
        '''
if __name__ == "__main__":
    run_token_analysis()