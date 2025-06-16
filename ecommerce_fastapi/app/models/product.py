from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.sql import func

from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default= func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
