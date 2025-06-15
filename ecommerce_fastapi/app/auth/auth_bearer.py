from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from app.crud.user import get_user_by_username
from app.database import SessionLocal
from app.models.user import User
import os


oauth2_scheme = OAuth2PasswordBearer(token_Url = "api/v1/users/login")

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenc("ALGORITHM")

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials'
    )
    try:
        payload = jwt.decode(token=token, SECRET_KEY=SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    db = SessionLocal()
    user = get_user_by_username(db, username=username)
    if user is None:
        raise credentials_exception
    
    return user