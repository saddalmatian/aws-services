from pydantic import BaseModel,Field
import decimal


class Order(BaseModel):
    status:str=Field(alias="Status")
    amount:decimal.Decimal=Field(alias="Amount")
    

class OrderInDB(Order):
    order_id:str=Field(alias="OrderId")
    number_items:int=Field(alias="NumberItems")


class OrderItems(BaseModel):
    item_id:str=Field(alias="ItemId")
    description:str=Field(alias="Description")
    price:decimal.Decimal=Field(alias="Price")