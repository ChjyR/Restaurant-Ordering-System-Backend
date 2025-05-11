# 餐厅点餐系统后端 (Restaurant Ordering System Backend)

一个使用 **FastAPI** 实现的餐厅点餐系统后端，支持用户下单、厨房处理订单、订单状态自动更新等功能，提供标准 RESTful API 接口，可供供前端应用调用。

---

## Functions

### 用户端
- 查询菜单项（`GET /menu`）
- 提交订单（`POST /orders`）
- 查询个人订单状态（`GET /orders/{user_id}`）

### 厨房端
- 查看所有未完成订单（`GET /kitchen/orders`）
- 将订单项设置为处理中（`POST /kitchen/orders/{order_id}/items/{item_id}/start`）
- 将订单项设置为已完成（`POST /kitchen/orders/{order_id}/items/{item_id}/complete`）
- 系统自动更新订单状态：当所有菜品完成 → `Completed`

---

## How to start

```bash
uvicorn main:app --reload
```

访问接口文档：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Example

### 创建订单
```http
POST /orders
Content-Type: application/json

{
  "user_id": "jack",
  "items": [1, 3, 4]
}
```

### 处理订单项（厨房端）
```http
POST /kitchen/orders/{order_id}/items/{item_id}/start
POST /kitchen/orders/{order_id}/items/{item_id}/complete
```
