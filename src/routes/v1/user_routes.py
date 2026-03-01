from typing import List
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

# simple in-memory users list for demonstration
fake_users_db = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

@router.get("/", response_model=List[dict])
def list_users():
    """Return all users"""
    return fake_users_db

@router.get("/{user_id}")
def get_user(user_id: int):
    """Return a single user by ID"""
    for user in fake_users_db:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}
