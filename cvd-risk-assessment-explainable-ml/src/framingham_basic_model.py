# ------------------- Part-1-----------------------
import pandas as pd
import numpy as np
import joblib 

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline


df = pd.read_csv("framingham.csv")

#print(df.head())
#$print(df.columns)

#Selecting only basic attributes

basic_features = [
    "male", "age", "sysBP", "currentSmoker","diabetes","BMI"]

# Seperate input(X) and output(y)

X = df[basic_features]
y = df["TenYearCHD"]

# Pipeline
model = Pipeline([
    ("imputer", SimpleImputer(strategy = "median")),
    ("scaler", StandardScaler()),
    ("lr", LogisticRegression(
        max_iter = 1000,
        solver = "lbfgs"
        ))
    ])



# Cross-validation 

cv = StratifiedKFold(
    n_splits = 5,
    shuffle = True,
    random_state = 42
    )

# Evaluating model using ROC_AUC

auc_scores = cross_val_score(
    model,
    X,
    y,
    cv=cv,
    scoring = "roc_auc"
    )


#Train model on full data

model.fit(X, y)

# Saving the trained model
joblib.dump(model, "framingham_basic_model.pkl")

# Interpret coefficients

lr_model = model.named_steps["lr"]
coefficients = lr_model.coef_[0]

coef_df = pd.DataFrame({
    "Feature": basic_features,
    "Coefficient": coefficients,
    "Odds Ratio": np.exp(coefficients)
    })

#print(coef_df.sort_values(by="Odds Ratio", ascending=False))
#print(auc_scores.mean(), "+/-", auc_scores.std())


#-------------------- Part-2 -----------------------------

# Load the trained model
model = joblib.load("framingham_basic_model.pkl")

# Ask the user for inputs

print("\nEnter patient details:")

male = int(input("Male ( 1=Male, 0=Female): "))
age= int(input("Age(years): "))
sysBP = float (input("Systolic BP (mmHg): "))
currentSmoker = int(input("Current Smoker? (1=Yes, 0=No): "))
diabetes = int(input("Diabetes?(1=Yes, 0=No): "))
BMI= float(input("BMI: "))

# Converting variables into ML model dataframe

basic_features = [
    "male",
    "age",
    "sysBP",
    "currentSmoker",
    "diabetes",
    "BMI"
    ]

person_df = pd.DataFrame([[
    male,
    age,
    sysBP,
    currentSmoker,
    diabetes,
    BMI
    ]], columns = basic_features)

# Predict Risk

risk_prob = model.predict_proba(person_df)[0][1]
risk_percent = risk_prob * 100

# Risk categorization

if risk_percent < 10:
    risk_level = "LOW"
elif risk_percent < 20:
    risk_level = "MEDIUM"

else:
    risk_level = "HIGH"


# output

print("\n----- CVD RISK RESULT ----------")
print(f"Estimated 10-year CVD Risk: {risk_percent:.1f}%")
print(f"Risk category: {risk_level}")  


#----------------- PART-3 --------------------

print("\n---------CVD RISK EXPLANATION -------- \n")

#Summary Sentence
print(f"Your estimated 10-year cardiovascular risk is {risk_percent: .1f}%.")
print(f"This places you in the {risk_level} category. \n")


#Explain why (based on the inputs)

print("Main contributors to your risk:")

if sysBP >= 130:
    print("• Blood Pressure is above the ideal range.")
if BMI >= 25:
    print("• Body weight is above the healthy range.")
if age >= 45:
    print("• Age related cardiovascular risk increase.")
if currentSmoker ==1:
    print("• Current smoking increases cardiovascular risk.")
if diabetes == 1:
    print ("• Diabetes increases cardiovascular risk.")

# Protective factors

print("\n Protective factors:")

if currentSmoker == 0:
    print ("• You are not a smoker.")
if diabetes == 0:
    print("• You do not have diabetes.")
if sysBP<130:
    print("• Blood pressure is within the recommended range.")
if BMI < 25:
    print("• Body weight is within the healthy range.")


#Actionable recommendations

print("\n What can you do to reduce your risk:")

if sysBP>= 130:
    print("• Aim to reduce systolic BP below 120 mmHg")

if BMI >= 25:
    print ("• Aim to reduce body weight to achieve a BMI below 25.")

if currentSmoker == 1:
    print("• Quitting smoking can significantly reduce risk.")

if diabetes == 1:
    print("• Tight blood sugar control is important.")

print("• Maintain a healthy diet and regular physical activity.")

#Close with reassurance

print("\nImproving these factors may help you move into a lower risk category.")
print("This tool is for awareness only and does not replace medical advice.")








































































    
























    

































    







