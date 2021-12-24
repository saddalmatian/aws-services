from fastapi import APIRouter
from models.schemas import user as user_schema
from services import user as user_service


router = APIRouter(
    prefix="/users",
    tags=["User"]
)

@router.post("/")
def create_user(user:user_schema.UserIn):
    return user_service.create_user(user)


@router.get("/{user_name}",response_model=user_schema.UserResp)
def get_user(user_name:str):
    return user_service.get_user(user_name)

