from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from schema.user_input import UserInput
from model.predict import predict_out

app = FastAPI()


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
    

    return JSONResponse(status_code=200, content=predict_out(user_input))