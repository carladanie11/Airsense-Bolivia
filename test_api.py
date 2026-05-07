import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAQ_API_KEY")
headers = {"X-API-Key": key}

# Países LATAM con datos en OpenAQ v3
paises = {"AR": "Argentina", "CL": "Chile", "PE": "Perú", "CO": "Colombia"}

for iso, nombre in paises.items():
    url = f"https://api.openaq.org/v3/locations?iso={iso}&limit=3"
    r = requests.get(url, headers=headers)
    data = r.json()
    found = data.get("meta", {}).get("found", 0)
    print(f"🌎 {nombre}: {found} estaciones")
    
