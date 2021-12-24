from fastapi import APIRouter,Body
from models.schemas import page as page_schema
from services import page as page_service


router = APIRouter(
    prefix="/pages",
    tags=["Page"]
)

@router.put("/")
def add_featured_deals(Page:page_schema.PageIn):
    return page_service.add_featured_deals(Page)

@router.get("/{page_name}",response_model=page_schema.PageResp)
def get_featured_deals(page_name:str):
    return page_service.get_featured_deals(page_name)

