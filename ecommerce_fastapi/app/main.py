from fastapi import FastAPI

import logging
from app.routes import user


logging.basicConfig(filename="app.log",
                    filemode='a',
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

app = FastAPI()


app.include_router(user.router, prefix = "/api/v1/users", tags=["Users"])

@app.get("/")
def root():
    return {"message":"E-commerce API with FASTAPI"}