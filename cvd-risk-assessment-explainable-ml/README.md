Explainable Machine Learning System for Cardiovascular Risk Assessment
This project implements a tiered (Basic, Middle, Advanced) explainable machine learning framework for cardiovascular risk assessment using clinically validated datasets. The goal is to provide risk awareness and decision support, not medical diagnosis.
Project Overview
Cardiovascular disease (CVD) remains a leading cause of mortality worldwide. Early risk awareness can significantly improve preventive outcomes. This project focuses on building an interpretable ML-based system that adapts to the amount of health information available from a user.
The system is designed in three tiers:
•	Basic: Uses easily self-reported attributes (age, sex, blood pressure, BMI, smoking, diabetes)
•	Middle: Incorporates laboratory parameters such as lipid profile and glycemic markers (planned)
•	Advanced: Incorporates clinical measurements such as ECG and echocardiography (planned)
Key Features
•	Tiered cardiovascular risk assessment (Basic → Middle → Advanced)
•	Explainable logistic regression with coefficient and odds-ratio interpretation
•	Stratified cross-validation with ROC-AUC evaluation
•	Personalized what-if risk reduction simulation
•	CLI-based user interaction (mobile-ready backend)
Current Status
•	Basic model: Completed
•	Middle model: Planned
•	Advanced model: Planned
•	Mobile app integration: Planned
Repository Structure
cvd-risk-assessment-explainable-ml/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── framingham.csv
│   └── README.md
│
├── models/
│   └── framingham_basic_model.pkl
│
├── src/
│   └── basic_model.py
│
└── app/
    └── cli_app.py
How to Run (Basic Model)
1.	Install dependencies:
2.	pip install -r requirements.txt
3.	Run the CLI application:
4.	python app/cli_app.py
Disclaimer
This tool is intended only for educational and awareness purposes. It does not replace professional medical advice, diagnosis, or treatment. Users are encouraged to consult qualified healthcare professionals for clinical decisions.
License
This project is released for academic and educational use.
