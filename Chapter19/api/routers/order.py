from fastapi import APIRouter,Body
from typing import List
from models.schemas import order as order_schema
from services import order as order_service


router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@router.post("/")
def create_order(
                order:order_schema.OrderIn,
                order_list:List[order_schema.OrderItemIn],
                customer_id:str = Body(...),
                ):
    return order_service.create_order(order.dict(),customer_id,order_list)

@router.get("/{order_id}")
def get_order(order_id):
    return order_service.get_order_details(order_id)

@router.put("/{order_id}")
def update_order(order_status,order_id,customer_id):
    return order_service.update_order(order_status,order_id,customer_id)