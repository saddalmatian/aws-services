from pydantic import BaseModel
from datetime import datetime
from pydantic.fields import Field


class User(BaseModel):
    username:str = Field(...,alias="Username")


class UserInDB(User):
    created_at:str = Field(...,alias="CreatedAt")
    organization:dict = Field(...,alias="Organization")
    type:str = Field(...,alias="Type")

class Org(BaseModel):
    orgname:str = Field(...,alias="OrganizationName")

class OrgInDB(Org):
    created_at:str = Field(...,alias="CreatedAt")
    type:str = Field(...,alias="Type")