from fastapi import APIRouter
from typing import List
from models.schemas import message as message_schema
from services import message as message_service


router = APIRouter(
    prefix="/messages",
    tags=["Message"]
)

@router.post("/")
def create_message(message:message_schema.MessageIn):
    return message_service.create_message(message)


@router.get("/{user_name}",response_model=List[message_schema.MessageResp])
def get_user_message(user_name:str):
    return message_service.get_user_message(user_name)

@router.get("/unread/{user_name}",response_model=List[message_schema.MessageResp])
def get_user_unread_message(user_name:str):
    return message_service.get_user_unread_message(user_name)

@router.put("/") 
def mark_message_read(message:message_schema.MessageMarkIn):
    return message_service.mark_message_read(message)