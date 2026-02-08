# Explainable Cardiovascular Disease Risk Prediction (ML Project)

## Overview
This project implements **explainable machine learning models** for cardiovascular disease assessment using two well-known clinical datasets:
- **Framingham Heart Study dataset**
- **UCI Heart Disease dataset**

The focus of the project is **model interpretability, ethical risk communication, and correct clinical framing**, rather than only maximizing performance metrics.

---

## Models Implemented

### 1. Framingham Model (Basic Assessment)
- **Purpose:** Estimate **10-year cardiovascular disease (CVD) risk**
- **Dataset:** Framingham Heart Study
- **Model:** Logistic Regression
- **Features used (basic & interpretable):**
  - Sex, Age
  - Systolic Blood Pressure
  - Smoking status
  - Diabetes
  - BMI
- **Evaluation Metric:** ROC-AUC
- **Performance:** ROC-AUC ≈ **0.72**
- **Output:**
  - 10-year CVD risk percentage
  - Risk category (Low / Medium / High)
  - Human-readable explanation and lifestyle guidance

> Note: A limited feature set was intentionally used to preserve interpretability.

---

### 2. UCI Heart Disease Model (Advanced Assessment)
- **Purpose:** Estimate **probability of heart disease presence**
- **Dataset:** UCI Heart Disease dataset
- **Model:** Logistic Regression (with preprocessing pipeline)
- **Features used:**
  - Demographic, clinical, ECG, and exercise-related variables
- **Preprocessing:**
  - Missing value imputation
  - Scaling of numerical features
  - One-hot encoding of categorical features
- **Evaluation Metric:** ROC-AUC
- **Performance:** ROC-AUC ≈ **0.91**
- **Output:**
  - Probability of heart disease
  - Risk category (Low / Moderate / High)
  - Interpretable explanation based on clinical factors

---

## Methodology
- End-to-end **scikit-learn Pipelines**
- **ColumnTransformer** for mixed data types
- **Stratified 5-fold cross-validation**
- Logistic Regression chosen for **explainability**
- Odds ratios computed for clinical interpretability
- Clear distinction between:
  - Time-based risk prediction (Framingham)
  - Cross-sectional disease probability (UCI)

---

## Explainability & Ethics
- Model outputs are explained using:
  - Feature contributions
  - Risk-increasing and protective factors
- No diagnostic or clinical claims are made
- Clear medical disclaimer included in outputs

---

## Project Structure
cvd-ml-project/
│
├── framingham_basic_model.py
├── uci_heart_advanced_model.py
├── requirements.txt
├── README.md
└── models/
├── framingham_basic_model.pkl
└── uci_heart_lr_model.pkl

## Disclaimer
This project is intended **for educational and research purposes only**.  
It does **not** replace professional medical advice, diagnosis, or treatment.

