# 🌎 AirSense LATAM

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Plataforma de Data Science end-to-end para monitoreo, análisis y predicción de la calidad del aire en América Latina con Machine Learning.

**Autora:** Carla Daniela Loredo Arancibia  
**Stack:** Python · Pandas · Scikit-learn · XGBoost · Prophet · FastAPI · Streamlit · MLflow

---

## 🎯 Objetivo

América Latina enfrenta desafíos significativos de calidad del aire en ciudades como Cochabamba, Buenos Aires, Santiago, Lima y Bogotá. Este proyecto:

- 📊 **Extrae** datos reales desde OpenAQ API y WAQI
- 🧹 **Limpia** series temporales de contaminantes (PM2.5, PM10, NO2, CO, O3, SO2)
- 🤖 **Predice** el Índice de Calidad del Aire (ICA) con modelos ML
- 📈 **Visualiza** patrones con dashboards interactivos
- 🚀 **Despliega** como API REST + dashboard web

---

## 🌍 Cobertura geográfica

| País | Ciudad | Fuente |
|---|---|---|
| 🇧🇴 Bolivia | Cochabamba, Santa Cruz | WAQI |
| 🇦🇷 Argentina | Buenos Aires y otras | OpenAQ v3 |
| 🇨🇱 Chile | Santiago y otras | OpenAQ v3 |
| 🇵🇪 Perú | Lima y otras | OpenAQ v3 |
| 🇨🇴 Colombia | Bogotá y otras | OpenAQ v3 |

---

## ⚙️ Instalación

```bash
git clone https://github.com/carladanie11/AirSense-LATAM.git
cd AirSense-LATAM
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🔑 APIs requeridas

| API | Uso | Registro |
|---|---|---|
| OpenAQ v3 | Datos LATAM | https://explore.openaq.org/register |
| WAQI | Datos Bolivia | https://aqicn.org/data-platform/token/ |

---

## 📁 Estructura
airsense-latam/
├── data/           # Datos crudos y procesados
├── notebooks/      # Análisis exploratorio
├── src/            # Código fuente
│   ├── ingestion/  # Clientes OpenAQ y WAQI
│   ├── processing/ # Limpieza y features
│   ├── models/     # Modelos ML
│   └── api/        # FastAPI
├── config/         # Configuración central
└── reports/        # Visualizaciones

---

*Proyecto de portfolio — Data Science aplicado al medio ambiente en América Latina 🌎*

