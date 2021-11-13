from fastapi import APIRouter
from app.models.schemas import user as _userschemas
from app.services.user import UserService

user_service = UserService

router = APIRouter(
    prefix="/users",
    tags=["User"]
) 

@router.get("/{user_id}",response_model=_userschemas.UserResp,status_code=200)
def get_user(user_id):
    return user_service.get_user(user_id)

    