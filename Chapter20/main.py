from fastapi import FastAPI
from api.routers import deals,brands,categories


app = FastAPI()

app.include_router(
    deals.router,
)
app.include_router(
    brands.router
)
app.include_router(
    categories.router
)
