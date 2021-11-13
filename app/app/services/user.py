from app.db.users.get_user import get_user


class UserService:
    def get_user(request):
        response = get_user(request)
        return response 
