from typing import List
from fastapi import APIRouter
from ...models import User
from ...services import get_user , create_user , list_users
router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_all_users(response_model=List[User]):
    """Return all users"""
    users = list_users()
    return users

@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    """Return a single user by ID"""
    user = get_user(user_id)
    if user:
        return user
    return {"error": "User not found"}


@router.post("/")
def create_new_user(user: User):
    new_user = create_user(user)
    return new_user