from typing import Dict, List
from pydantic import BaseModel,Field



class PageDeals(BaseModel):
    deal_id:str = Field(...,alias="DealID"),
    link:str = Field(...,alias="Link")

class Page(BaseModel):
    featured_deals: List[PageDeals] = Field(...,alias="FeaturedDeals")
    
