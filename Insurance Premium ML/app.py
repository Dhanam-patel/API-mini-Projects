from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated  
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
import pandas as pd
import pickle

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class InsuranceData(BaseModel):
    age: Annotated[int, Field(..., gt=0, description="Age of the individual")]
    weight: Annotated[float, Field(..., gt=0, description="Weight in kilograms")]
    height: Annotated[float, Field(..., gt=0, description="Height in meters")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Income in Lakhs Per Annum")]
    smoker: Annotated[bool, Field(..., description="Whether the individual is a smoker")]
    city: Annotated[str, Field(..., description="City of residence")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the individual")]
    
    @computed_field()
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "Young"
        elif self.age < 45:
            return "Middle-Aged"    
        elif self.age < 65:
            return "middle_aged"
        return "senior"
    
    @computed_field()
    @property
    def Life_risk(self) -> str:
        if self.smoker == True and self.bmi > 30:
            return "high"
        elif self.smoker == True and self.bmi > 27:
            return "medium"
        else:
            return "low"   
        
    @computed_field()
    @property
    def city_tier(self) -> int:
        Tier_1 = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune']
        Tier_2 = [
        "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
        "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
        "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
        "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
        "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
        "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
        ]
        
        if self.city in Tier_1:
            return 1
        elif self.city in Tier_2:
            return 2
        else:
            return 3

@app.post("/predict")   
def predict_premium_category(data: InsuranceData):
    input_df = pd.DataFrame([{
        "bmi": data.bmi,
        "age_group": data.age_group,
        "Life_risk": data.Life_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation,  
        
    }])

    prediction = model.predict(input_df)[0]
    return JSONResponse(status_code=200, content={"predicted_premium_category": prediction})