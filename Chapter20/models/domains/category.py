from pydantic import BaseModel,Field


class Category(BaseModel):
    category_name:str = Field(...,alias="CategoryName")
    featured_deals:list = Field(...,alias="FeaturedDeals")
 
    
 