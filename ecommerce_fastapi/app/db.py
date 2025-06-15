from .database import SessionLocal
from fastapi import HTTPException, status
import logging

from sqlalchemy.exc import OperationalError

logger = logging.getLogger(__name__)

def get_db():
    
    try:
        db = SessionLocal()
        yield db
    except OperationalError as e:
        logger.error(f"Database connection failed: {e}")
        raise HTTPException(status_code = status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail = "Database is unavailable. Please try again later")
    finally:
        db.close()
