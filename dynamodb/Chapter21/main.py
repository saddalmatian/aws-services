from fastapi import FastAPI, HTTPException
from api.routers import repos, comments, reactions, users
from services import login as service_login
from fastapi.security import HTTPBearer

app = FastAPI(
    tag=["Login"]
)

app.include_router(repos.router)
app.include_router(comments.router)
app.include_router(reactions.router)
app.include_router(users.router)

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


@app.post('/login')
def login(username: str, password: str):
    if service_login.verify_password(username, password):
        token = service_login.generate_token(username)
        return {
            'token': token
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")
