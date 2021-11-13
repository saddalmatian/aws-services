from pydantic import BaseModel,Field


class Brand(BaseModel):
    brand_name:str = Field(...,alias="BrandName")
    brand_logo_url:str = Field(...,alias="BrandLogoUrl")
 
    
 