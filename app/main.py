from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .import models, schemas
from .database import SessionLocal, engine, Base, get_db


app = FastAPI()
get_db()

@app.get("/")
def hello(db: Session = Depends(get_db)):
    print(db.is_active)
    return {"message" : "hello world"}