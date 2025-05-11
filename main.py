# main.py
from fastapi import FastAPI
from routers import menu, order, kitchen

app = FastAPI(title="餐厅点餐系统")

# 注册路由模块
app.include_router(menu.router, prefix="/menu", tags=["菜单"])
app.include_router(order.router, prefix="/orders", tags=["订单"])
app.include_router(kitchen.router, prefix="/kitchen", tags=["厨房处理"])

@app.get("/")
def read_root():
    return {"message": "餐厅点餐系统后台已启动"}
