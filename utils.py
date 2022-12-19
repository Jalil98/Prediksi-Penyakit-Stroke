import numpy as np 
import joblib 


def preprocessdata(Gender, Married, Hypertension, HeartDisease, WorkType,
       ResidenceType, AvgGlucoseLevel, Bmi, SmokingStatus,
       Stroke):
   #  test_data = [[Gender, Married, Education, Self_Employed, ApplicantIncome,
   #     CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
   #     Property_Area] ]  
    test_data = [[Gender, Married, Hypertension, HeartDisease, WorkType,
       ResidenceType, AvgGlucoseLevel, Bmi, SmokingStatus,
       Stroke]]
    trained_model = joblib.load("best_model_stroke.pkl") 
    prediction = trained_model.predict(test_data) 

    return prediction 
