from datetime import date
from models.schemas import brand as brand_schema
from db import brand as brand_db


def create_brand(brand:brand_schema.BrandIn):
    return brand_db.create_brand(brand)

def get_brand(brand_name:str):
    return brand_db.get_brand(brand_name)

def get_all_brand():
    return brand_db.get_all_brand()

def add_brand_like(user_id:str,brand_name:str):
    return brand_db.add_brand_like(user_id,brand_name)

def add_brand_watch(user_id:str,brand_name:str):
    return brand_db.add_brand_watch(user_id,brand_name) 