from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserOut, UserCreate
from app.crud.user import create_user, authenticate_user
from app.db import get_db
from app.auth.jwt import create_access_token


router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user

@router.post('/login')
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_, detail="Invalid credentials")
    token = create_access_token(data={"sub":db_user.username})
    return {"access_token":token, "token_type": "bearer"}

