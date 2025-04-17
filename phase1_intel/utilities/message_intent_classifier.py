# message_intent_classifier.py
# Tags each message with likely system intent (build, validate, plan, launch, etc.)

import csv

INTENT_MAP = {
    "build": ["build", "generate", "construct", "create", "scaffold"],
    "validate": ["validate", "check", "confirm", "test"],
    "plan": ["strategy", "plan", "outline", "design"],
    "launch": ["launch", "run", "execute", "start"],
    "package": ["package", "zip", "bundle", "deploy"]
}

def classify_messages(input_csv="parsed_thread_output.csv", output_csv="classified_messages.csv"):
    with open(input_csv, 'r') as infile:
        reader = csv.DictReader(infile)
        messages = list(reader)

    results = []
    for msg in messages:
        content = msg["content"].lower()
        matched = [intent for intent, keywords in INTENT_MAP.items() if any(k in content for k in keywords)]
        results.append({
            "thread_id": msg["thread_id"],
            "msg_id": msg["msg_id"],
            "intent_class": ", ".join(matched) if matched else "unknown"
        })

    with open(output_csv, 'w', newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["thread_id", "msg_id", "intent_class"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"✅ Intent classification complete: {len(results)} messages → {output_csv}")

if __name__ == "__main__":
    classify_messages()
