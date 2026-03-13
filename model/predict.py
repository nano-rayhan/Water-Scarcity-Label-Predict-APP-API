import pickle
import pandas as pd

with open('model/water.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_out(user_input : dict ):
    
    df = pd.DataFrame(user_input)


    prediction = int(model.predict(user_input)[0])

    labels = {0:"Low",1:"Moderate",2:"High",3:"Critical"}
    return str(labels[prediction])