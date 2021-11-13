from typing import List
from fastapi import APIRouter
from starlette import responses
from services import customer as customer_service
from models.schemas import customer as customer_schema
from models.schemas import order as order_schema



router = APIRouter(
    prefix="/customers",
    tags=["Customer"]
)

@router.get("/{id}",response_model=customer_schema.CustomerResp,status_code=200)
def get_customer(id):
    return customer_service.get_customer(id)

@router.get("/orderlist/{customer_id}",response_model=List[order_schema.OrderResp],status_code=200)
def get_customer_order(customer_id):
    return customer_service.get_customer_order(customer_id)

@router.post("/")
def create_customer(customer:customer_schema.CustomerIn):
    customer_dict=customer.dict()
    return customer_service.create_customer(customer_dict)
    
@router.post("/{customer_email}")
def create_customer_email(customer_name,customer_email):
    return customer_service.create_customer_email(customer_name,customer_email)

@router.put("/{customer_email}")
def update_email(customer_name,customer_email):
    return customer_service.update_email(customer_name,customer_email)

@router.delete("/{customer_email}")
def delete_email(customer_name):
    return customer_service.delete_email(customer_name)