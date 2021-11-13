from fastapi import FastAPI
from api.routers import deals,brands,categories,pages,users


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
app.include_router(
    pages.router
)

app.include_router(
    users.router
)
