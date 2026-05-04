# 🌿 AirSense Bolivia

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Plataforma de Data Science end-to-end para monitoreo, análisis y predicción de la calidad del aire en Bolivia con Machine Learning.

**Autora:** Carla Daniela Loredo Arancibia  
**Stack:** Python · Pandas · Scikit-learn · XGBoost · Prophet · FastAPI · Streamlit · MLflow

---

## 🎯 Objetivo

Bolivia enfrenta desafíos significativos de calidad del aire en ciudades como Cochabamba, La Paz y Santa Cruz. Este proyecto:

- 📊 **Extrae** datos reales desde la API de OpenAQ
- 🧹 **Limpia** series temporales de contaminantes (PM2.5, PM10, NO2, CO, O3, SO2)
- 🤖 **Predice** el Índice de Calidad del Aire (ICA) con modelos ML
- 📈 **Visualiza** patrones con dashboards interactivos
- 🚀 **Despliega** como API REST + dashboard web

---

## ⚙️ Instalación

```bash
git clone https://github.com/carladanie11/Airsense-Bolivia.git
cd Airsense-Bolivia
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🔑 API Key de OpenAQ

1. Registrarse en https://explore.openaq.org/register
2. Copiar la API Key al archivo `.env`

---

## 📁 Estructura
airsense-bolivia/
├── data/           # Datos crudos y procesados
├── notebooks/      # Análisis exploratorio
├── src/            # Código fuente
│   ├── ingestion/  # Cliente OpenAQ
│   ├── processing/ # Limpieza y features
│   ├── models/     # Modelos ML
│   └── api/        # FastAPI
├── config/         # Configuración central
└── reports/        # Visualizaciones

---

*Proyecto de portfolio — Data Science aplicado al medio ambiente en Bolivia 🇧🇴*

