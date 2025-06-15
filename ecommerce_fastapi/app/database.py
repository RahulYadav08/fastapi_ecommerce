from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os 
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

#Get database URL from .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL1")

#create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#create a configured "Session" class
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

#Base class for models to inherit from
Base = declarative_base()

