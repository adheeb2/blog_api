from fastapi import APIRouter


router = APIRouter(
    prefix="/users"
)

@router.get("/me")
def get_me():
    return { "id": 1, "username": "JohnDoe", "email": "john@example.com" }