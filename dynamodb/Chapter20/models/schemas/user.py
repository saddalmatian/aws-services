from models.domains import user as user_domain


class UserIn(user_domain.User):
    pass

class UserResp(user_domain.UserInDB):
    pass