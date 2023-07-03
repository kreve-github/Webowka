from pydantic import BaseModel


class ProductCreateSchema(BaseModel):
    name: str
    price: int
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Przedmiot",
                "price": 9999,
            }
        }

class ProductUpdateSchema(BaseModel):
    name: str | None
    price: int | None
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Przedmiot",
                "price": 9999,
            }
        }

class Product(ProductCreateSchema):
    id: int