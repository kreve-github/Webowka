from fastapi import APIRouter, HTTPException
import sys
sys.path.append("..")
from customers.storage import get_customers_storage
from products.storage import get_products_storage
from .storage import get_orders_storage
from .schema import Order
router = APIRouter()

CUSTOMER_STORAGE = get_customers_storage()
ORDERS_STORAGE = get_orders_storage()
PRODUCTS_STORAGE = get_products_storage()

@router.get("/")
async def get_orders() -> list[Order]:
    return list(get_orders_storage().values())

@router.get("/{order_id}")
async def get_order_by_id(order_id: int):
    try:
        return ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )
    
@router.post("/add-order")
async def create_order(customer_id: int, product_id: int):
    if product_id in list(PRODUCTS_STORAGE.keys()) and customer_id in list(CUSTOMER_STORAGE):
        if ORDERS_STORAGE:
            order_id = max(list(ORDERS_STORAGE.keys()))+1
        else:
            order_id = 1
        product = PRODUCTS_STORAGE[product_id]
        order = Order(id = order_id, customer_id = customer_id, products = [product])
        ORDERS_STORAGE[order_id] = order
        return order
    else:
        return {"message": f"Invalid value of customer_id or product_id"}
    
@router.patch("/{order_id}")
async def update_order(order_id: int, product_id: int):
    if order_id in list(ORDERS_STORAGE.keys()) and product_id in list(PRODUCTS_STORAGE.keys()):
        ORDERS_STORAGE[order_id].products.append(PRODUCTS_STORAGE[product_id])
    else:
        return {"message": f"Invalid value of order_id or product_id"}
    
@router.delete("/{order_id}")
async def delete_order(order_id: int) -> None:
    try:
        del ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )