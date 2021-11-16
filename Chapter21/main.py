from fastapi import FastAPI
from api.routers import repos,comments


app = FastAPI()

app.include_router(repos.router)
app.include_router(comments.router)