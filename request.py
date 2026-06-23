import requests

BASE = "http://127.0.0.1:8000"

seen = set()
cursor = None
snapshot = None

for i in range(30):
    params = {"limit": 10}
    if cursor:
        params["cursor"] = cursor
        params["snapshot"] = snapshot

    r = requests.get(f"{BASE}/products", params=params).json()

    snapshot = r["snapshot"]
    cursor = r["next_cursor"]

    for p in r["products"]:
        if p["public_id"] in seen:
            print("❌ DUPLICATE FOUND:", p["public_id"])
            exit()
        seen.add(p["public_id"])

print("✅ No duplicates found")
print("Total:", len(seen))