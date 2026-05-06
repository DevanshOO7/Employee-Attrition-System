import requests
import json

# API ka address
url = "http://127.0.0.1:5000/predict"

data = {
  "Age": 35,
  "DailyRate": 800,
  "DistanceFromHome": 10,
  "Education": 3,
  "EnvironmentSatisfaction": 4,
  "HourlyRate": 60,
  "JobInvolvement": 3,
  "JobLevel": 2,
  "JobSatisfaction": 4,
  "MonthlyIncome": 5000,
  "MonthlyRate": 15000,
  "NumCompaniesWorked": 2,
  "PercentSalaryHike": 15,
  "PerformanceRating": 3,
  "RelationshipSatisfaction": 3,
  "StockOptionLevel": 1,
  "TotalWorkingYears": 10,
  "TrainingTimesLastYear": 2,
  "WorkLifeBalance": 3,
  "YearsAtCompany": 5,
  "YearsInCurrentRole": 3,
  "YearsSinceLastPromotion": 1,
  "YearsWithCurrManager": 3,
  "BusinessTravel_Travel_Frequently": 0,
  "BusinessTravel_Travel_Rarely": 1,
  "Department_Research & Development": 1,
  "Department_Sales": 0,
  "EducationField_Life Sciences": 1,
  "EducationField_Marketing": 0,
  "EducationField_Medical": 0,
  "EducationField_Other": 0,
  "EducationField_Technical Degree": 0,
  "Gender_Male": 1,
  "JobRole_Human Resources": 0,
  "JobRole_Laboratory Technician": 0,
  "JobRole_Manager": 0,
  "JobRole_Manufacturing Director": 0,
  "JobRole_Research Director": 0,
  "JobRole_Research Scientist": 1,
  "JobRole_Sales Executive": 0,
  "JobRole_Sales Representative": 0,
  "MaritalStatus_Married": 1,
  "MaritalStatus_Single": 0,
  "OverTime_Yes": 0
}

print("sending data to API...")

try:
    response = requests.post(url, json=data)
    
    print("\n--- RESULT ---")
    print("Status Code:", response.status_code)
    print("Prediction:", response.json())
    print("-------------------\n")

except Exception as e:
    print("Error detected", e)