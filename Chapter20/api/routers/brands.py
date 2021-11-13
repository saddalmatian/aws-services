from typing import List
from fastapi import APIRouter
from models.schemas import brand as brand_schema
from services import brand as brand_service



router = APIRouter(
    prefix="/brands",
    tags=["Brand"]
)

@router.get("/{brand_name}",response_model=brand_schema.BrandResp)
def get_brand(brand_name:str):
    return brand_service.get_brand(brand_name)

@router.get("/all/")
def get_all_brand():
    return brand_service.get_all_brand()    

@router.post("/")
def create_brand(brand:brand_schema.BrandIn):
    return brand_service.create_brand(brand)

@router.post("/like/")
def add_brand_like(user_id:str,brand_name:str):
    return brand_service.add_brand_like(user_id,brand_name)

@router.post("/watch/")
def add_brand_like(user_id:str,brand_name:str):
    return brand_service.add_brand_watch(user_id,brand_name)