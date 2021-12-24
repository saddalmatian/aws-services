from pydantic import BaseModel,Field
from decimal import Decimal


class Deal(BaseModel):
    title:str = Field(...,alias="Title")
    link:str = Field(...,alias="Link")
    price:Decimal = Field(...,alias="Price")
    category:str = Field(...,alias="Category")
    brand:str = Field(...,alias="Brand")
    

class DealInDB(Deal):
    deal_id:str = Field(...,alias="DealID")
    created_at:str = Field(...,alias="CreatedAt")

 