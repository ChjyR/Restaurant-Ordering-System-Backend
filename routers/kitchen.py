from fastapi import APIRouter, HTTPException
from storage.memory import ORDERS
from models.schema import Order
from utils.status_checker import update_order_status

router = APIRouter()

@router.get("/orders", response_model=list[Order])
def get_all_orders():
    """
    获取所有未完成的订单。
    """
    return [order for order in ORDERS.values() if order.status != "Completed"]

@router.post("/orders/{order_id}/items/{item_id}/start")
def start_preparing(order_id: str, item_id: int):
    order = ORDERS.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="订单不存在")

    item = next((i for i in order.items if i.item_id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="菜品不存在")
    item.status = "Preparing"

    update_order_status(order)
    return {"message": "已开始处理该菜品"}

@router.post("/orders/{order_id}/items/{item_id}/complete")
def complete_item(order_id: str, item_id: int):
    order = ORDERS.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="订单不存在")

    item = next((i for i in order.items if i.item_id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="菜品不存在")
    item.status = "Ready"

    update_order_status(order)
    return {"message": "该菜品已完成处理"}
