from fastapi import APIRouter, HTTPException

from .storage import get_products_storage
from .schema import ProductCreateSchema, ProductUpdateSchema, Product
router = APIRouter()


PRODUCTS_STORAGE = get_products_storage()

@router.get("/")
async def get_products() -> list[Product]:
    return list(get_products_storage().values())

@router.post("/add-product")
async def create_product(product: ProductCreateSchema) -> Product:
    if PRODUCTS_STORAGE:
        product_id = max(list(PRODUCTS_STORAGE.keys()))+1
    else:
        product_id = 1
    new_product = Product(**product.dict(), id = product_id)
    PRODUCTS_STORAGE[product_id] = new_product
    return new_product

@router.get("/{product_id}")
async def get_product_by_id(product_id: int) -> Product:
    try:
        return PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

@router.patch("/{product_id}")
async def update_product(product_id: int, updated_product: ProductUpdateSchema):
    if product_id in list(PRODUCTS_STORAGE.keys()):
        new_product = PRODUCTS_STORAGE[product_id]
        for attribute, value in updated_product.dict(exclude_unset=True).items():
            setattr(new_product, attribute, value) 
        return new_product
    else:
        return {"message": f"Product with ID: {product_id} does not exist"}


@router.delete("/{product_id}")
async def delete_product(product_id: int) -> None:
    try:
        del PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )