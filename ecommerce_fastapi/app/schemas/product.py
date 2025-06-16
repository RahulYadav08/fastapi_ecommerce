from pydantic import BaseModel, computed_field
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: str
    stock: int
    category: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    stock: Optional[int]
    category: Optional[str]
    price: Optional[float]

class ProductOut(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

    def summary(self) -> str:
        return f"{self.name} ({self.category}) - ₹{self.price:.2f} | Stock: {self.stock}"
    
    
    @computed_field
    @property
    def in_stock(self):
        return self.stock > 0

