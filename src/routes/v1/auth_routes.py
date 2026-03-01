from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login():
    """Dummy login endpoint"""
    return {"message": "logged in"}

@router.post("/register")
def register():
    """Dummy registration endpoint"""
    return {"message": "registered"}
