from typing import List
from fastapi import FastAPI, Depends
from db import SessionLocal, ProductModel
from schemas import ProductOutput

app = FastAPI()

@app.get('/products', response_model=List)
def get_products():
    fake_products = [
        ProductOutput(name=f"Produto {n}", price=n * .1, id=n)
        for n in range(100)
    ]

    return fake_products