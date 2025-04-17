# gpt_message_wrapper.py
# Converts unstructured GPT messages into Vault Intelligence compliant outputs

import csv
import re

def wrap_messages(input_csv="parsed_thread_output.csv", output_csv="wrapped_messages.csv"):
    wrapped = []

    with open(input_csv, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            content = row["content"]
            if "#META:" not in content:
                meta_block = (
                    "\n\n#META:\n"
                    f"assistant_id: UNKNOWN\n"
                    f"phase_created: P1\n"
                    f"status: draft\n"
                    f"value_class[]: []"
                )
                content += meta_block

            wrapped.append({
                "thread_id": row["thread_id"],
                "msg_id": row["msg_id"],
                "formatted_content": content
            })

    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["thread_id", "msg_id", "formatted_content"])
        writer.writeheader()
        for row in wrapped:
            writer.writerow(row)

    print(f"✅ Wrapped {len(wrapped)} messages → {output_csv}")

if __name__ == "__main__":
    wrap_messages()
