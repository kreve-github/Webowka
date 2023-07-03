from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import customers, products, orders

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customers.router, prefix="/customers")
app.include_router(products.router, prefix="/products")
app.include_router(orders.router, prefix="/orders")