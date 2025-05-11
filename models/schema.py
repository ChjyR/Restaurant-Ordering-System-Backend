from typing import List, Literal, Optional
from uuid import uuid4
from pydantic import BaseModel

class MenuItem(BaseModel):
    id: int
    name: str
    price: float


# 订单中每一个菜
class OrderItem(BaseModel):
    item_id: int               # 菜单项的id
    status: Literal['Pending', 'Preparing', 'Ready'] = 'Pending'

# 创建订单时传入的请求体
class CreateOrderRequest(BaseModel):
    user_id: str
    items: List[int]           # 菜单项id列表

# 返回给前端的订单结构
class Order(BaseModel):
    order_id: str
    user_id: str
    items: List[OrderItem]
    status: Literal['Pending', 'Preparing', 'Ready', 'Completed'] = 'Pending'
