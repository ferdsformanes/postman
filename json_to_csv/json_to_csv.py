import json
import pandas as pd

json_file = "response.json"
csv_file = "devices.csv"

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.json_normalize(data["data"])

columns = [
    "host-name",
    "system-ip",
    "site-id",
    "site-name",
    "device-model",
    "personality",
    "version",
    "reachability",
    "controlConnections",
    "bfdSessions",
    "state",
]

# Keep only columns that actually exist
df = df[[c for c in columns if c in df.columns]]

df.to_csv(csv_file, index=False)
