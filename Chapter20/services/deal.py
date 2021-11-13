from datetime import date
from models.schemas import deal as deal_schema
from db import deal as deal_db


def create_deal(deal:deal_schema.DealIn):
    return deal_db.create_deal(deal)

def get_deal(deal_id:str):
    return deal_db.get_deal(deal_id)

def fetch_deal_date(date:date):
    return deal_db.fetch_deal_date(date)

def fetch_deal_brand(brand:str):
    return deal_db.fetch_deal_brand(brand)

def fetch_deal_category(category:str):
    return deal_db.fetch_deal_category(category)