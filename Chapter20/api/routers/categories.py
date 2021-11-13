from typing import List
from fastapi import APIRouter
from models.schemas import category as category_schema
from services import category as category_service



router = APIRouter(
    prefix="/categories",
    tags=["Category"]
) 

@router.get("/{category_name}",response_model=category_schema.CategoryResp)
def get_category(category_name:str):
    return category_service.get_category(category_name)

@router.put("/fetured-deal/")
def add_fetured_deals(deal_list:list,category_name:str):
    return category_service.add_featured_deals(deal_list,category_name)

@router.post("/")
def create_category(category:category_schema.CategoryIn):
    return category_service.create_category(category)

@router.post("/like/")
def add_category_like(user_id:str,category_name:str):
    return category_service.add_category_like(user_id,category_name)

@router.post("/watch/")
def add_category_watch(user_id:str,category_name:str):
    return category_service.add_category_watch(user_id,category_name)
