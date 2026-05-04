"""
Cliente para la API de OpenAQ v3.
Extrae datos de calidad del aire para Bolivia.

Autor: Carla Daniela Loredo Arancibia
Proyecto: AirSense Bolivia
"""
import time
import logging
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

import sys
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from config.settings import (
    OPENAQ_API_KEY,
    OPENAQ_BASE_URL,
    BOLIVIA_COUNTRY_ID,
    DATA_RAW_DIR,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class OpenAQClient:
    """Cliente para OpenAQ API v3."""

    def __init__(self, api_key: str = OPENAQ_API_KEY):
        if not api_key:
            raise ValueError(
                "❌ API Key no encontrada. "
                "Copia .env.example a .env y agrega tu OPENAQ_API_KEY."
            )
        self.api_key = api_key
        self.base_url = OPENAQ_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "X-API-Key": self.api_key,
            "Accept": "application/json",
        })
        logger.info("✅ Cliente OpenAQ v3 inicializado")

    def _get(self, endpoint: str, params: dict = None, retries: int = 3) -> dict:
        """GET request con manejo de errores y retry."""
        url = f"{self.base_url}/{endpoint}"
        for attempt in range(retries):
            try:
                response = self.session.get(url, params=params, timeout=30)
                if response.status_code == 429:
                    wait = 2 ** attempt
                    logger.warning(f"⚠️ Rate limit. Esperando {wait}s...")
                    time.sleep(wait)
                    continue
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                logger.error(f"❌ Error intento {attempt+1}/{retries}: {e}")
                if attempt == retries - 1:
                    raise
                time.sleep(2)
        return {}

    def get_bolivia_locations(self, limit: int = 100) -> pd.DataFrame:
        """Obtiene estaciones de monitoreo en Bolivia."""
        logger.info("🔍 Buscando estaciones en Bolivia...")
        data = self._get(
            "locations",
            params={"countries_id": BOLIVIA_COUNTRY_ID, "limit": limit}
        )
        results = data.get("results", [])
        if not results:
            logger.warning("⚠️ No se encontraron estaciones.")
            return pd.DataFrame()

        records = []
        for loc in results:
            coords = loc.get("coordinates", {})
            records.append({
                "location_id":   loc.get("id"),
                "name":          loc.get("name"),
                "city":          loc.get("locality", ""),
                "latitude":      coords.get("latitude"),
                "longitude":     coords.get("longitude"),
                "sensors_count": len(loc.get("sensors", [])),
            })

        df = pd.DataFrame(records)
        logger.info(f"✅ {len(df)} estaciones encontradas en Bolivia")
        return df

    def get_measurements(
        self,
        location_id: int,
        parameter: str = "pm25",
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        limit: int = 1000,
    ) -> pd.DataFrame:
        """Obtiene mediciones para una ubicación y parámetro."""
        if date_from is None:
            date_from = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        if date_to is None:
            date_to = datetime.now().strftime("%Y-%m-%d")

        logger.info(f"📥 {parameter.upper()} | Ubicación {location_id} | {date_from} → {date_to}")

        data = self._get(
            f"locations/{location_id}/measurements",
            params={
                "parameter": parameter,
                "date_from":  f"{date_from}T00:00:00Z",
                "date_to":    f"{date_to}T23:59:59Z",
                "limit":      limit,
            }
        )

        results = data.get("results", [])
        if not results:
            logger.warning(f"⚠️ Sin datos para {location_id}/{parameter}")
            return pd.DataFrame()

        records = []
        for m in results:
            records.append({
                "location_id": location_id,
                "parameter":   m.get("parameter", {}).get("name", parameter),
                "value":       m.get("value"),
                "unit":        m.get("parameter", {}).get("units", ""),
                "datetime":    m.get("period", {}).get("datetimeFrom", {}).get("utc"),
            })

        df = pd.DataFrame(records)
        df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
        df = df.dropna(subset=["value", "datetime"]).sort_values("datetime")
        logger.info(f"✅ {len(df)} mediciones extraídas")
        return df

    def save_raw_data(self, df: pd.DataFrame, filename: str) -> Path:
        """Guarda datos crudos en CSV."""
        DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)
        path = DATA_RAW_DIR / filename
        df.to_csv(path, index=False)
        logger.info(f"💾 Guardado: {path}")
        return path
    