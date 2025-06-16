from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.product import ProductCreate, ProductOut, ProductUpdate
from app.crud.product import create_product, get_product_by_id, get_all_products, update_product, delete_product


from app.db import get_db

#router = APIRouter(prefix="/products", tags=["Products"])
router = APIRouter()

@router.post("/", response_model=ProductOut)
def add_product(product: ProductCreate, db: Session= Depends(get_db)):
    return create_product(db, product)


@router.get("/{id}", response_model=ProductOut)
def get_product(id:int, db: Session = Depends(get_db)):
    return get_product_by_id(db=db, id=id)


@router.get("/", response_model=List[ProductOut])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_products(db, skip=skip, limit=limit)

@router.put("/{id}", response_model=ProductOut)
def product_update(product: ProductUpdate, id:int, db: Session = Depends(get_db)):
    return update_product(db, id, product)


@router.delete("/{id}")
def remove_product(id: int, db: Session = Depends(get_db)):
    return delete_product(db, id)
     