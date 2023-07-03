from functools import lru_cache

from .schema import Product

ProductsStorageType = dict[int, Product]

PRODUCTS: ProductsStorageType = {}


@lru_cache(maxsize=1)
def get_products_storage() -> ProductsStorageType:
    return PRODUCTS

