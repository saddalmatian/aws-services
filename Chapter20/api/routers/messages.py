from fastapi import APIRouter
from models.schemas import message as message_schema
from services import message as message_service


router = APIRouter(
    prefix="/messages",
    tags=["Message"]
)

@router.post("/")
def create_message(user_name:str,message:message_schema.MessageIn):
    return message_service.create_message(user_name,message)


@router.get("/{message_name}",response_model=message_schema.MessageResp)
def get_message(message_name:str):
    return message_service.get_message(message_name)


