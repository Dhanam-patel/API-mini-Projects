from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated  
from config.City_Tier import Tier_1, Tier_2
class InsuranceData(BaseModel):
    age: Annotated[int, Field(..., gt=0, description="Age of the individual")]
    weight: Annotated[float, Field(..., gt=0, description="Weight in kilograms")]
    height: Annotated[float, Field(..., gt=0, description="Height in meters")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Income in Lakhs Per Annum")]
    smoker: Annotated[bool, Field(..., description="Whether the individual is a smoker")]
    city: Annotated[str, Field(..., description="City of residence")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the individual")]
    
    @field_validator('city')
    @classmethod
    def validate_city(cls, value):
        return value.title()
    
    @field_validator('occupation', mode='before')
    @classmethod
    def occupation_validator(cls, value): 
        lowercased_value = value.lower()
        return lowercased_value


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
        if self.city in Tier_1:
            return 1
        elif self.city in Tier_2:
            return 2
        else:
            return 3