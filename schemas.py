from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float

class ProductOutput(Product):
    id: int