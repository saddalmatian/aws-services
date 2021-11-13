from models.schemas import category as category_schema
from db import category as category_db


def get_category(category_name:str):
    return category_db.get_category(category_name)

def create_category(category: category_schema.CategoryIn):
    return category_db.create_category(category)

def add_category_like(user_id:str,category_name:str):
    return category_db.add_category_like(user_id,category_name)

def add_category_watch(user_id:str,category_name:str):
    return category_db.add_category_watch(user_id,category_name)

def add_featured_deals(deal_list:list,category_name:str):
    return category_db.add_featured_deals(deal_list,category_name)