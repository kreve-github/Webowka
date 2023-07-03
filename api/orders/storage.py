from functools import lru_cache

from .schema import Order

OrderStorageType = dict[int, Order]

ORDERS: OrderStorageType = {}


@lru_cache(maxsize=1)
def get_orders_storage() -> OrderStorageType:
    return ORDERS
