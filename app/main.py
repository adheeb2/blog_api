from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.routers import posts

# from .import models, schemas
from .routers import users
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.router.redirect_slashes=False

app.add_middleware(
    
    CORSMiddleware,
    
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(users.router)

app.include_router(posts.router)

@app.get("/")
def hello():
    return {"message" : "hello world"}

