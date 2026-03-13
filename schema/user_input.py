from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Union

class UserInput(BaseModel):

    country: Annotated[str, Field(..., description='Name of the country')]
    year: Annotated[int, Field(..., description='Any year user want')]
    total_water:Annotated[Union[int, float], Field(..., description='Total Water Consumption (Billion m3)')]
    per_capital: Annotated[Union[int, float], Field(..., description='Per Capita Water Use (L/Day)')]
    agricultural:Annotated[Union[int, float], Field(...,gt=0, lt=100, description='Agricultural Water Use (%)')]
    industrial:Annotated[Union[int, float], Field(..., gt=0, lt=100, description='Industrial Water Use (%)')]
    household:Annotated[Union[int, float], Field(..., gt=0, lt=100, description='Household Water Use (%)')]
    rainfall: Annotated[Union[int, float], Field(..., description='Rainfall Impact (mm)')]
    groundwater:Annotated[Union[int, float], Field(..., gt=0, lt=10,description='Groundwater Depletion Rate (%)')]


    @field_validator('country')
    @classmethod
    def normalize_country(cls, v:str) ->str:
        v = v.strip().title()
        return v
    
    @field_validator('year')
    @classmethod
    def validate_year(cld, v):
        if v< 1000 or v > 9999:
            raise ValueError('Year must have 4 digit number')
        return v