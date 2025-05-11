# utils/status_checker.py

from models.schema import Order

def update_order_status(order: Order):
    """
    根据订单中所有菜品的状态更新订单状态。
    """
    item_statuses = [item.status for item in order.items]

    if all(s == "Ready" for s in item_statuses):
        order.status = "Completed"
    elif all(s in ("Ready", "Preparing") for s in item_statuses):
        order.status = "Ready"
    elif any(s == "Preparing" for s in item_statuses):
        order.status = "Preparing"
    else:
        order.status = "Pending"
