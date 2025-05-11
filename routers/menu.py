# routers/menu.py
from fastapi import APIRouter
from typing import List
from models.schema import MenuItem
from storage.memory import MENU_ITEMS

router = APIRouter()

@router.get("/", response_model=List[MenuItem])
def get_menu():
    """
    返回菜单。
    """
    return MENU_ITEMS
