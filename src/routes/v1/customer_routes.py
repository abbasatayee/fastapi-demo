from typing import List
from fastapi import APIRouter

router = APIRouter(prefix="/customers", tags=["customers"])

fake_customers = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

@router.get("/", response_model=List[dict])
def list_customers():
    return fake_customers

@router.get("/{customer_id}")
def get_customer(customer_id: int):
    for c in fake_customers:
        if c["id"] == customer_id:
            return c
    return {"error": "Customer not found"}
