from pydantic import BaseModel
from datetime import date, datetime
from pydantic.fields import Field

class User(BaseModel):
    user_name:str = Field(...,alias="Username")

class UserInDB(User):
    created_at:datetime = Field(...,alias="CreatedAt")
