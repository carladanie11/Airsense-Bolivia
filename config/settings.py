"""
Configuración central del proyecto AirSense Bolivia.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── Rutas del proyecto ──────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed"
DATA_EXTERNAL_DIR = BASE_DIR / "data" / "external"
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# ── API OpenAQ ──────────────────────────────────────
OPENAQ_API_KEY = os.getenv("OPENAQ_API_KEY", "")
OPENAQ_BASE_URL = "https://api.openaq.org/v3"

# ── Bolivia ─────────────────────────────────────────
BOLIVIA_COUNTRY_ID = 26

CITIES_OF_INTEREST = [
    "Cochabamba",
    "La Paz",
    "Santa Cruz",
    "Oruro",
    "Potosí",
]

PARAMETERS = {
    "pm25": "Material Particulado PM2.5 (µg/m³)",
    "pm10": "Material Particulado PM10 (µg/m³)",
    "no2":  "Dióxido de Nitrógeno NO2 (µg/m³)",
    "o3":   "Ozono O3 (µg/m³)",
    "co":   "Monóxido de Carbono CO (ppm)",
    "so2":  "Dióxido de Azufre SO2 (µg/m³)",
}

# ── MLflow ───────────────────────────────────────────
MLFLOW_TRACKING_URI = str(BASE_DIR / "mlruns")
EXPERIMENT_NAME = "airsense-bolivia-air-quality"

print(f"✅ Configuración cargada | AirSense Bolivia | {os.getenv('ENV', 'development')}")
