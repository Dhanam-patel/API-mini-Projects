from fastapi.responses import JSONResponse
from fastapi import FastAPI  
from Schema.User_Input import InsuranceData
from Model.Predict import Predict, Model_Version, Model_Loaded

app = FastAPI()





@app.get("/")
def home():
    return {"message": "Insurance Premium Predictiom Model API "}

@app.get("/health")
def health_check():
    return{
        "status": "OK",
        "Version": Model_Version,
        "Model_loaded": Model_Loaded
    }

@app.post("/predict")   
def predict_premium_category(data: InsuranceData):
    User_Input = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "Life_risk": data.Life_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation,  
        
    }
    try:
        prediction = Predict(User_Input)
    except Exception as e:
        return JSONResponse(status_code=500, content={str(e)})