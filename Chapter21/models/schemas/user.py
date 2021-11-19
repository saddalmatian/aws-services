from models.domains import user

class UserIn(user.User):
    pass

class UserResp(user.UserInDB):
    pass

class OrgIn(user.Org):
    pass

class OrgResp(user.OrgInDB):
    pass