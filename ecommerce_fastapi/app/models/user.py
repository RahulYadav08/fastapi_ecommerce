from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base

class User(Base):
    __tablename__ = "Users"  # Table name in postgresql

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password=Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    
