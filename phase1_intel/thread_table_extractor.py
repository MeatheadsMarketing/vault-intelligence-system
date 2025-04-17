# thread_table_extractor.py
# Extracts markdown-style tables from parsed GPT thread content

import csv
import re

def extract_tables(input_csv='parsed_thread_output.csv', output_csv='extracted_tables.csv'):
    tables = []

    with open(input_csv, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            content = row['content']
            # Naive check for markdown tables with 2+ pipes per line
            if '|' in content and content.count('|') >= 2:
                lines = content.strip().split('\n')
                table_lines = [line for line in lines if '|' in line]
                if len(table_lines) >= 2:
                    tables.append({
                        'thread_id': row['thread_id'],
                        'msg_id': row['msg_id'],
                        'raw_table': '\n'.join(table_lines)
                    })

    with open(output_csv, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['thread_id', 'msg_id', 'raw_table'])
        writer.writeheader()
        for table in tables:
            writer.writerow(table)

    print(f"✅ Extracted {len(tables)} tables to {output_csv}")

if __name__ == "__main__":
    extract_tables()
