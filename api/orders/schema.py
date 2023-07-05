from pydantic import BaseModel

class Order(BaseModel):
    customer_id: int
    customer_name: str
    products: list
    products_names: str
    sum: int
    id: int