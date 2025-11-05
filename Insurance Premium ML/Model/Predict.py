import pandas as pd
import pickle

with open("Model/model.pkl", "rb") as f:
    model = pickle.load(f)

Model_Version = "1.0.0"

Model_Loaded = model is not None

def Predict(User_Input: dict):
    input_df = pd.DataFrame([User_Input])
    
    prediction = model.predict(input_df)[0]
    return prediction