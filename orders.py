from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Order(BaseModel):
    id: int
    customer_name: str
    items: List[str]
    status: str

orders_db = []

@router.post("/orders/", response_model=Order)
def create_order(order: Order):
    orders_db.append(order)
    return order

@router.get("/orders/", response_model=List[Order])
def get_orders():
    return orders_db

@router.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@router.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, updated_order: Order):
    for i, order in enumerate(orders_db):
        if order.id == order_id:
            orders_db[i] = updated_order
            return updated_order
    raise HTTPException(status_code=404, detail="Order not found")

@router.delete("/orders/{order_id}")
def delete_order(order_id: int):
    for i, order in enumerate(orders_db):
        if order.id == order_id:
            del orders_db[i]
            return {"message": "Order deleted"}
    raise HTTPException(status_code=404, detail="Order not found")
