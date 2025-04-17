# thread_parser.py
# Extracts message content from GPT-exported conversation.json format

import json
import csv

def parse_thread_json(input_file="conversation.json", output_csv="parsed_thread_output.csv"):
    with open(input_file, 'r') as f:
        data = json.load(f)

    messages = []
    for convo in data.get("conversations", []):
        for idx, msg in enumerate(convo.get("messages", [])):
            text = msg.get("text") or msg.get("content", "")
            if text:
                messages.append({
                    "thread_id": convo.get("id", "unknown"),
                    "msg_id": f"{convo.get('id', 'unknown')}_{idx}",
                    "content": text.strip()
                })

    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["thread_id", "msg_id", "content"])
        writer.writeheader()
        for msg in messages:
            writer.writerow(msg)

    print(f"✅ Parsed {len(messages)} messages → {output_csv}")

if __name__ == "__main__":
    parse_thread_json()
