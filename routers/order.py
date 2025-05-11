from fastapi import APIRouter, HTTPException
from models.schema import CreateOrderRequest, Order, OrderItem
from storage.memory import ORDERS
from uuid import uuid4

router = APIRouter()

@router.post("/", response_model=Order)
def create_order(order_request: CreateOrderRequest):
    order_id = str(uuid4())
    order_items = [OrderItem(item_id=item_id) for item_id in order_request.items]

    order = Order(
        order_id=order_id,
        user_id=order_request.user_id,
        items=order_items,
        status="Pending"
    )

    ORDERS[order_id] = order
    return order

@router.get("/{user_id}", response_model=list[Order])
def get_user_orders(user_id: str):
    user_orders = [order for order in ORDERS.values() if order.user_id == user_id]
    return user_orders
