import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Creating the flask app
application = Flask(__name__)
app=application

## Import linear regression model and standard scaler pickle to allow web interaction
linreg_model=pickle.load(open('models/linreg.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for data entry form (GET only)
@app.route('/predictdata', methods=['GET'])
def predict_datapoint():
    return render_template('data_entry.html')


# Route for processing data and showing results (POST only)
@app.route('/results', methods=['POST'])
def show_results():
    # Get form data
    Temperature = float(request.form.get('Temperature'))
    RH = float(request.form.get('RH'))
    Ws = float(request.form.get('Ws'))
    Rain = float(request.form.get('Rain'))
    FFMC = float(request.form.get('FFMC'))
    DMC = float(request.form.get('DMC'))
    ISI = float(request.form.get('ISI'))
    Region = float(request.form.get('Region'))

    # Process the data
    new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Region]])
    result = linreg_model.predict(new_data_scaled)

    # Render results page with the prediction
    return render_template('results.html', 
                         result=result[0],
                         input_data={
                             'Temperature': Temperature,
                             'RH': RH,
                             'Ws': Ws,
                             'Rain': Rain,
                             'FFMC': FFMC,
                             'DMC': DMC,
                             'ISI': ISI,
                             'Region': Region
                         })


# Executing the flask app
if __name__=="__main__":
    #0.0.0.0 maps to local ip address of the machine 
    app.run(host="0.0.0.0", port=5002, debug=True)
   
