from fastapi import FastAPI
from .routers import customer,order


app = FastAPI()

app.include_router(
    customer.router

)
app.include_router(
    order.router
)


@app.get("/")
def get_index():
    return "This is index"

