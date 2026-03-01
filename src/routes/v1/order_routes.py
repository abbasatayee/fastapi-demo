from typing import List
from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["orders"] , )

fake_orders = [
    {"id": 1, "item": "Widget", "quantity": 3},
    {"id": 2, "item": "Gadget", "quantity": 5},
]

@router.get("/", response_model=List[dict])
def list_orders():
    return fake_orders

@router.get("/{order_id}")
def get_order(order_id: int):
    for o in fake_orders:
        if o["id"] == order_id:
            return o
    return {"error": "Order not found"}
