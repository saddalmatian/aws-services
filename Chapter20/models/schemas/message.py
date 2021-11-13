from pydantic.main import BaseModel
from models.domains import message as message_domain
from pydantic.fields import Field
from datetime import datetime


class MessageIn(message_domain.Message):
    user_name:str = Field(...,alias="Username")
    pass

class MessageMarkIn(message_domain.MessageMark):
    pass

class MessageResp(message_domain.MessageInDB):
    pass 