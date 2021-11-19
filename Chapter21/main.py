from fastapi import FastAPI
from api.routers import repos,comments,reactions,users


app = FastAPI()

app.include_router(repos.router)
app.include_router(comments.router)
app.include_router(reactions.router)
app.include_router(users.router)