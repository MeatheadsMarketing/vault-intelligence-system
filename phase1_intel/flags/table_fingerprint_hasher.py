# table_fingerprint_hasher.py
# Hashes table headers to identify duplicate tables across GPT messages

import csv
import hashlib

def hash_table_headers(table_text):
    lines = table_text.strip().splitlines()
    header = lines[0].strip().replace(" ", "").lower() if lines else ""
    return hashlib.md5(header.encode()).hexdigest()

def deduplicate_tables(input_csv='extracted_tables.csv', output_csv='deduplicated_tables.csv'):
    seen_hashes = {}
    deduplicated_rows = []

    with open(input_csv, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            table_hash = hash_table_headers(row["raw_table"])
            duplicate_of = seen_hashes.get(table_hash, "unique")
            seen_hashes[table_hash] = row["msg_id"]
            deduplicated_rows.append({
                "thread_id": row["thread_id"],
                "msg_id": row["msg_id"],
                "table_hash": table_hash,
                "duplicate_of": duplicate_of
            })

    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["thread_id", "msg_id", "table_hash", "duplicate_of"])
        writer.writeheader()
        for row in deduplicated_rows:
            writer.writerow(row)

    print(f"✅ Checked {len(deduplicated_rows)} tables → {output_csv}")

if __name__ == "__main__":
    deduplicate_tables()
