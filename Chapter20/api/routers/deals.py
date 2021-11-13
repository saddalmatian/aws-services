from datetime import date
from typing import List
from fastapi import APIRouter
from models.schemas import deal as deal_schema
from services import deal as deal_service



router = APIRouter(
    prefix="/deals",
    tags=["Deal"]
)

@router.get("/{deal_id}",response_model=deal_schema.DealResp)
def get_deal(deal_id:str):
    return deal_service.get_deal(deal_id)

@router.get("/date/{date}",response_model=List[deal_schema.DealResp])
def deal_by_date(date:date):
    return deal_service.fetch_deal_date(date)

@router.get("/brand/{brand}",response_model=List[deal_schema.DealResp])
def deal_by_brand(brand:str):
    return deal_service.fetch_deal_brand(brand)

@router.get("/category/{category}",response_model=List[deal_schema.DealResp])
def deal_by_category(category:str):
    return deal_service.fetch_deal_category(category)


@router.post("/")
def create_deal(deal:deal_schema.DealIn):
    return deal_service.create_deal(deal)

