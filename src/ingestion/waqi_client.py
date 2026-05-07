"""
Cliente para la API de WAQI (World Air Quality Index).
Extrae datos de calidad del aire para Bolivia.

Autor: Carla Daniela Loredo Arancibia
Proyecto: AirSense LATAM
"""
import logging
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Optional

import sys
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from config.settings import WAQI_TOKEN, DATA_RAW_DIR

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

# Estaciones confirmadas de Bolivia
BOLIVIA_STATIONS = {
    "Parque Kanata - Cochabamba": 6938,
    "Fuerza Aerea - Cochabamba":  11265,
    "Semapa - Cochabamba":        6939,
    "Coña Coña - Cochabamba":     6940,
}


class WAQIClient:
    """Cliente para WAQI API."""

    def __init__(self, token: str = WAQI_TOKEN):
        if not token:
            raise ValueError("❌ WAQI_TOKEN no encontrado en .env")
        self.token = token
        self.base_url = "https://api.waqi.info"
        logger.info("✅ Cliente WAQI inicializado")

    def get_station_data(self, uid: int) -> dict:
        """Obtiene datos actuales de una estación por UID."""
        url = f"{self.base_url}/feed/@{uid}/?token={self.token}"
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.json()

    def get_bolivia_current(self) -> pd.DataFrame:
        """Obtiene datos actuales de todas las estaciones de Bolivia."""
        logger.info("🇧🇴 Obteniendo datos actuales de Bolivia...")
        records = []
        for nombre, uid in BOLIVIA_STATIONS.items():
            try:
                data = self.get_station_data(uid)
                if data.get("status") == "ok":
                    d = data["data"]
                    iaqi = d.get("iaqi", {})
                    records.append({
                        "station":   nombre,
                        "uid":       uid,
                        "city":      "Cochabamba",
                        "country":   "Bolivia",
                        "aqi":       d.get("aqi"),
                        "pm25":      iaqi.get("pm25", {}).get("v"),
                        "pm10":      iaqi.get("pm10", {}).get("v"),
                        "no2":       iaqi.get("no2",  {}).get("v"),
                        "o3":        iaqi.get("o3",   {}).get("v"),
                        "co":        iaqi.get("co",   {}).get("v"),
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    })
                    logger.info(f"  ✅ {nombre}: AQI={d.get('aqi')}")
            except Exception as e:
                logger.error(f"  ❌ Error en {nombre}: {e}")

        df = pd.DataFrame(records)
        logger.info(f"✅ {len(df)} estaciones obtenidas")
        return df

    def save_data(self, df: pd.DataFrame, filename: str) -> Path:
        """Guarda datos en CSV."""
        DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)
        path = DATA_RAW_DIR / filename
        df.to_csv(path, index=False)
        logger.info(f"💾 Guardado: {path}")
        return path


if __name__ == "__main__":
    client = WAQIClient()
    df = client.get_bolivia_current()
    print(df)
    