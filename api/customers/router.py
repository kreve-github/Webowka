from fastapi import APIRouter, HTTPException, Query

from .storage import get_customers_storage
from .schema import CustomerCreateSchema, CustomerUpdateSchema, Customer

router = APIRouter()


CUSTOMERS_STORAGE = get_customers_storage()


@router.get("/")
async def get_customers() -> list[Customer]:
    return list(get_customers_storage().values())

@router.post("/add-customer")
async def create_customer(customer: CustomerCreateSchema) -> Customer:
    if CUSTOMERS_STORAGE:
        customer_id = max(list(CUSTOMERS_STORAGE.keys()))+1
    else:
        customer_id = 1
    new_customer = Customer(**customer.dict(), id = customer_id)
    CUSTOMERS_STORAGE[customer_id] = new_customer
    return new_customer

@router.get("/{customer_id}")
async def get_customer_by_id(customer_id: int) -> Customer:
    try:
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )

@router.patch("/{customer_id}")
async def update_customer(customer_id: int, updated_customer: CustomerUpdateSchema):
    if customer_id in list(CUSTOMERS_STORAGE.keys()):
        new_customer = CUSTOMERS_STORAGE[customer_id]
        for attribute, value in updated_customer.dict(exclude_unset=True).items():
            setattr(new_customer, attribute, value) 
        return new_customer
    else:
        return {"message": f"Customer with ID: {customer_id} does not exist"}


@router.delete("/{customer_id}")
async def delete_customer(customer_id: int) -> None:
    try:
        del CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


