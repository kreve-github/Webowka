from pydantic import BaseModel

class Order(BaseModel):
    customer_id: int
    products: list
    id: int