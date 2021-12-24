from db import page as page_db


def add_featured_deals(page):
    page = page.dict(by_alias=True)
    return page_db.add_featured_deals(page)

def get_featured_deals(page_name:str):
    return page_db.get_featured_deals(page_name)
