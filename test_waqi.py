import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("WAQI_TOKEN")

# Buscar por UID directo de La Paz (IDs conocidos)
uids = [6941, 6942, 6943, 7000, 7001, 5023, 5024]

print("🔍 Probando UIDs cercanos a La Paz:")
for uid in uids:
    url = f"https://api.waqi.info/feed/@{uid}/?token={token}"
    r = requests.get(url)
    data = r.json()
    if data.get("status") == "ok":
        nombre = data["data"].get("city", {}).get("name", "")
        aqi = data["data"].get("aqi")
        print(f"  ✅ UID:{uid} | {nombre} | AQI:{aqi}")
        