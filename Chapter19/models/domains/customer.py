from pydantic import BaseModel,Field
from typing import Dict, Optional
from ..domains import address


class Customer(BaseModel):
    name:str = Field(...,alias="Name")
    age:str = Field(...,alias="Age")
    email: Optional[str] = Field(alias="Email")
    addresses: Dict[str,address.Address] = Field(...,alias="Addresses")
