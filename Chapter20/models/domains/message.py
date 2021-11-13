from pydantic import BaseModel
from pydantic.fields import Field

class Message(BaseModel):
    subject: str = Field(...,alias="Subject")
    body: str = Field(...,alias="Body")
    

class MessageInDB(Message):
    message_id: str = Field(...,alias="Message")
    unread: bool = Field(...,alias="Unread")

 