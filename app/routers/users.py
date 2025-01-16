from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from app.database import get_db
from app.models import User, Role
from app import schemas, auth


router = APIRouter(
    prefix="/users"
)

@router.post("/register", response_model=schemas.UserResponse)
def register_user(user : schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email ==user.email).first():
        raise HTTPException(
            status_code=400,
            detail= "Email is already registered"
        )
    
    hashed_password = auth.hash_password(user.password)
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login_user(form_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email ==form_data.email).first()

    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    access_token = auth.create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.UserResponse)
def get_user(
    current_user: schemas.UserResponse = Depends(auth.get_current_user)
):
    return current_user