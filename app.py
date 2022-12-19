from logging import debug
from flask import Flask, render_template, request 
import utils  
from utils import preprocessdata 

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html') 
@app.route('/predict/', methods=['GET', 'POST'])

def predict():  
    if request.method == 'POST': 
        Gender = request.form.get('gender')
        Married = request.form.get('ever_married')
        Hypertension = request.form.get('hypertension')
        HeartDisease = request.form.get('heart_disease')  
        WorkType = request.form.get('work_type')  
        ResidenceType = request.form.get('Residence_type') 
        AvgGlucoseLevel = request.form.get('avg_glucose_level')   
        Bmi = request.form.get('bmi')   
        SmokingStatus = request.form.get('smoking_status')   
        Stroke = request.form.get('stroke')  
        
        # gender,ever_married,hypertension,heart_disease,work_type,Residence_type, avg_glucose_level, bmi, smoking_status, stroke]]

    prediction = utils.preprocessdata(Gender, Married, Hypertension, HeartDisease, WorkType,
       ResidenceType, AvgGlucoseLevel, Bmi, SmokingStatus,
       Stroke)

    return render_template('predict.html', prediction=prediction) 

if __name__ == '__main__': 
    app.run() 

# mari kita prediksi hasilnya
# oh iya kita mau memprediksi penyakit stroke ya 
# let's goconda 