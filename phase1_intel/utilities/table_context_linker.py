# table_context_linker.py
# Connects tables to their likely assistant or prompt based on content similarity

import csv

def link_tables_to_assistants(tables_csv='extracted_tables.csv', assistants_csv='assistant_registry.csv', output_csv='linked_tables.csv'):
    assistants = []
    with open(assistants_csv, 'r') as f:
        reader = csv.DictReader(f)
        assistants = list(reader)

    linked_rows = []
    with open(tables_csv, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            content = row['raw_table'].lower()
            linked_id = "unknown"
            for assistant in assistants:
                if assistant['name'].lower() in content:
                    linked_id = assistant['assistant_id']
                    break
            linked_rows.append({
                "thread_id": row["thread_id"],
                "msg_id": row["msg_id"],
                "raw_table": row["raw_table"],
                "linked_assistant": linked_id
            })

    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["thread_id", "msg_id", "raw_table", "linked_assistant"])
        writer.writeheader()
        for row in linked_rows:
            writer.writerow(row)

    print(f"✅ Linked {len(linked_rows)} tables → {output_csv}")

if __name__ == "__main__":
    link_tables_to_assistants()
