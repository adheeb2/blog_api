from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

# from .import models, schemas
from .routers import users
from .database import SessionLocal, engine, Base, get_db, SQLALCHEMY_DATABASE_URL


app = FastAPI()

app.include_router(users.router)

@app.get("/")
def hello():
    print(SQLALCHEMY_DATABASE_URL)
    return {"message" : "hello world"}