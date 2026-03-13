from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from schema.user_input import UserInput
from model.predict import predict_out

app = FastAPI()


    
@app.get('/')
def home():
    return {'message': 'Welcome to Water Scarcity Label Predict APP'}

@app.get('/health')
def health_check():
    return {
        'status' : 'OK',
    }

@app.post('/predict')
def predicted(data: UserInput):

    user_input = pd.DataFrame([{
        'Country':data.country,
        'Year':data.year,
        'Total Water Consumption (Billion m3)':data.total_water,
        'Per Capita Water Use (L/Day)':data.per_capital,
        'Agricultural Water Use (%)':data.agricultural,
        'Industrial Water Use (%)': data.industrial,
        'Household Water Use (%)':data.household,
        'Rainfall Impact (mm)':data.rainfall,
        'Groundwater Depletion Rate (%)':data.groundwater
    }])
    

    return JSONResponse(status_code=200, content={'predicted': predict_out(user_input)})