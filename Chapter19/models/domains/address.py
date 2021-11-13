from pydantic import BaseModel,Field


class Address(BaseModel):
    Street:str = Field(...)
    City:str = Field(...)
    Nation:str = Field(...)
