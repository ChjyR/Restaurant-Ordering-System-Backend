# storage/memory.py

from models.schema import MenuItem, Order
from typing import List, Dict

# 模拟菜单数据
MENU_ITEMS: List[MenuItem] = [
    MenuItem(id=1, name="菜1", price=25.0),
    MenuItem(id=2, name="菜2", price=20.0),
    MenuItem(id=3, name="菜3", price=15.0),
    MenuItem(id=4, name="菜4", price=10.0),
]

# 模拟订单存储
ORDERS: Dict[str, Order] = {}
