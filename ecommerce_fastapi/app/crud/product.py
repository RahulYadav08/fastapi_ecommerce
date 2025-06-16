from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductOut, ProductUpdate

from fastapi import HTTPException
from typing import List


def create_product(db: Session, product: ProductCreate):

    product_obj = Product(
        name=product.name, 
        description=product.description, 
        price=product.price, 
        stock=product.stock, 
        category=product.category)
    db.add(product_obj)
    db.commit()
    db.refresh(product_obj)

    return product_obj

def update_product(db: Session, product_id: int, product: ProductUpdate):
    product_obj = db.query(Product).filter(Product.id == product_id).first()

    if not product_obj:
        raise HTTPException(status_code=404, detail="Product not found")
    
    #Use model_dump() with exclude_unset=True to avoid overwriting fields with None
    update_data = product.model_dump(exclude_unset = True)

    for field, value in update_data.items():
        setattr(product_obj, field, value)

    db.commit()
    db.refresh(product_obj)
    return product_obj


def get_product_by_id(db: Session, product_id: int) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def get_all_products(db: Session, skip: int=0, limit: int=0)->List[Product]:
    return db.query(Product).offset(skip).limit(limit).all()


def delete_product(db: Session, product_id: int) -> dict:
    product_obj = db.query(Product).filter(Product.id == product_id).first()
    if not product_obj:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product_obj)
    db.commit()
    return {"message": "Product deleted successfully"}