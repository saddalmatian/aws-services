from fastapi import APIRouter
from models.schemas import page as page_schema
from services import page as page_service


router = APIRouter(
    prefix="/pages",
    tags=["Page"]
)

@router.put("/{page_type}")
def add_featured_deals(page:page_schema.PageIn,page_type:str):
    return page_service.add_featured_deals(page,page_type)

