# auto_header_mapper.py
# Aligns GPT-generated headers to system-compliant column names

import csv

RECOMMENDED_HEADERS = {
    "assistantid": "assistant_id",
    "promptid": "prompt_id",
    "door": "door_type",
    "phase": "phase_created",
    "valueclass": "value_class[]",
    "value_class": "value_class[]",
    "status": "status"
}

def normalize_headers(input_csv="wrapped_messages.csv", output_csv="mapped_headers.csv"):
    with open(input_csv, 'r') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        rows = list(reader)

    mapped_fields = []
    for field in fieldnames:
        stripped = field.lower().replace(" ", "").replace("_", "")
        new_name = RECOMMENDED_HEADERS.get(stripped, field)
        mapped_fields.append(new_name)

    with open(output_csv, 'w', newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=mapped_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"✅ Header normalization complete → {output_csv}")

if __name__ == "__main__":
    normalize_headers()
