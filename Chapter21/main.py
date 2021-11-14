from fastapi import FastAPI
from api.routers import repo


app = FastAPI()

app.include_router(repo.router)