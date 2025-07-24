from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any
from uuid import UUID
import functions as fn

router = APIRouter()

@router.post("/orders/")
def create_order(order: Dict[str, Any] = Body(...)):
    return fn.create_order(order)

@router.get("/orders/")
def get_orders():
    return fn.fetch_orders()

@router.get("/orders/{order_id}")
def get_order(order_id: UUID):
    order = fn.get_order(str(order_id))
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/orders/{order_id}")
def update_order(order_id: UUID, updated_order: Dict[str, Any] = Body(...)):
    order = fn.update_order(str(order_id), updated_order)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/orders/{order_id}")
def delete_order(order_id: UUID):
    result = fn.delete_order(str(order_id))
    if result is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return result
