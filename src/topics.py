import json
from pathlib import Path

topics_file = Path(__file__).parent / "topics.json"

with open(topics_file, "r") as f:
    topics = json.load(f)

print(topics)
