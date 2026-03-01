from ..models import User

users  = []

def create_user(user : User):
    # Logic to create a user
    users.append(user)  
    return {"message": "User created", "user": user}


def get_user(user_id: int):
    # Logic to get a user by ID
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}


def list_users():
    return users