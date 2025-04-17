# thread_merge_tool.py
# Merges multiple GPT-exported conversation.json files into one combined archive

import json

def merge_thread_exports(input_files, output_file='merged_conversation.json'):
    merged = {"conversations": []}
    for input_file in input_files:
        with open(input_file, 'r') as f:
            data = json.load(f)
            merged["conversations"].extend(data.get("conversations", []))

    with open(output_file, 'w') as f:
        json.dump(merged, f, indent=2)

    print(f"✅ Merged {len(merged['conversations'])} conversations → {output_file}")

if __name__ == "__main__":
    # Example usage
    merge_thread_exports(["conversation_part1.json", "conversation_part2.json"])
