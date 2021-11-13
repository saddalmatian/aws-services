from datetime import date
from db import page as page_db


def add_featured_deals(page,page_type:str):
    return page_db.add_featured_deals(page,page_type)

