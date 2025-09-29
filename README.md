# Obesity Prediction App

![Python](https://img.shields.io/badge/language-Python-blue)
![Streamlit](https://img.shields.io/badge/frontend-Streamlit-brightgreen)
![FastAPI](https://img.shields.io/badge/backend-FastAPI-lightgrey)

## Overview
This repository contains a machine learning pipeline for **predicting obesity levels** based on lifestyle and health-related factors.
The project is developed as a **final project for the Model Deployment course**, aligned with:
- **SDG 3**: Good Health and Well-being

The app allows users to explore predictions interactively via a **Streamlit frontend**, powered by a **FastAPI backend** and an **XGBoost pipeline** for classification.

Live demo of the app: 
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://2702346361uas.streamlit.app/)

---

## Files
- `ObesityDataset1.csv` → original raw dataset
- `pipeline.ipynb` → notebook containing EDA, preprocessing, model training
- `xgb_pipeline.pkl` → trained XGBoost pipeline
- `backend_api.py` → FastAPI backend serving the model
- `frontend_streamlit.py` → Streamlit app for user interaction
- `requirements.txt` → dependencies for deployment
- `README.md` → this documentation
- **results/**
  - `Screenshot.png` → screenshot demonstrating app functionality  
  - **Project Explanation Video** → [View on OneDrive](https://binusianorg-my.sharepoint.com/personal/syalista_nadira_binus_ac_id/_layouts/15/guestaccess.aspx?share=ESnR3_ESYwdBuOSiHPoAnfQB3WXK4tM9T6ctKLHiKMfd-Q&e=jF1cjC)

---

## Methodology  
1. **Data Preprocessing & EDA**
   - Handling missing values
   - Encoding
   - Feature preparation

2. **Model Training**
   - XGBoost pipeline
   - Evaluation on test set

3. **Deployment**
   - FastAPI backend for predictions
   - Streamlit frontend for user interaction

---

## Key Insights
- Predictive modeling identifies key lifestyle and health factors influencing obesity risk.
- Pipeline accurately predicts obesity levels across 7 classes: `Insufficient_Weight`, `Normal_Weight`, `Overweight_Level_I`, `Overweight_Level_II`, `Obesity_Type_I`, `Obesity_Type_II`, `Obesity_Type_III`
- The deployed app demonstrates **end-to-end ML workflow**: preprocessing → model training → deployment.
- Supports awareness on SDG 3: Good Health and Well-being through data-driven insights.

---

## References
- Python libraries: pandas, scikit-learn, XGBoost, FastAPI, Streamlit

---

## Author
Syalista Galuh Nadira
