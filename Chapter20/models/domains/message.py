from datetime import datetime
from pydantic import BaseModel
from pydantic.fields import Field

class Message(BaseModel):
    subject: str = Field(...,alias="Subject")
    body: str = Field(...,alias="Body")
    
class MessageMark(BaseModel):
    user_name:str = Field(...,alias="Username")
    created_at: datetime = Field(...,alias="CreatedAt")


class MessageInDB(Message):
    unread: bool = Field(...,alias="Unread")
    created_at: datetime = Field(...,alias="CreatedAt")
 