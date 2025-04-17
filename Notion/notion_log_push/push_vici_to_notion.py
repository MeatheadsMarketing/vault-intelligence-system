import requests
import json
from datetime import datetime

NOTION_API_KEY = "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"
DATABASE_ID = "1d8bd31f046380358c00e36959166e31"

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def create_vici_entry():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("vici_log_entry.md", "r") as f:
        content = f.read()

    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": { "content": f"Vault Intelligence Completion Log – {now}" }
                    }
                ]
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": { "content": content[:2000] }
                        }
                    ]
                }
            }
        ]
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("✅ VICI log successfully pushed to Notion.")
    else:
        print("❌ Failed to push VICI log to Notion.")
        print(response.text)

if __name__ == "__main__":
    create_vici_entry()
