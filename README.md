# 📦 Store API

Simple REST API project responsible for managing store items.  
Built with **FastAPI** and structured according to **DDD / Clean Architecture** principles.

---

## 🚀 Base URL

```
/api/items
```

---

## 🧱 Item model

```json
{
  "id": 1,
  "name": "Item 1",
  "weight": "10kg",
  "qty": 5
}
```

---

## 🔍 Get all items

Returns a list of all items available in the store.

**Endpoint**
```
GET /api/items
```

**Response – 200 OK**
```json
[
  {
    "id": 1,
    "name": "Item 1",
    "weight": "10kg",
    "qty": 5
  },
  {
    "id": 2,
    "name": "Item 2",
    "weight": "20kg",
    "qty": 3
  }
]
```

---

## 🔍 Get item by ID

Returns a single item by its unique identifier.

**Endpoint**
```
GET /api/items/{item_id}
```

**Response – 200 OK**
```json
{
  "id": 1,
  "name": "Item 1",
  "weight": "10kg",
  "qty": 5
}
```

**Response – 404 Not Found**
```json
{
  "detail": "item_not_found"
}
```

---

## ➕ Create new item

**Endpoint**
```
POST /api/items
```

**Request body**
```json
{
  "name": "New Item",
  "weight": "5kg",
  "qty": 10
}
```

**Response – 201 Created**
```json
{
  "created_item_id": 4
}
```

---

## ✏️ Update item

**Endpoint**
```
PUT /api/items/{item_id}
```

**Request body**
```json
{
  "name": "Updated Item",
  "weight": "7kg",
  "qty": 12
}
```

**Response – 200 OK**
```json
{
  "updated_item_id": 1
}
```

---

## 🗑 Delete item

**Endpoint**
```
DELETE /api/items/{item_id}
```

**Response – 200 OK**
```json
{
  "removed_item_id": 1
}
```

---

## 🧩 Architecture overview

```
store/
├── domain/
├── application/
├── infrastructure/
└── presentation/
```

---

## ▶️ Running the application

### For better production experience, try uvicorn:

```bash
uvicorn app.main:app --reload
```

### For standard FastAPI development, run:

```bash
fastapi dev app/main.py
```
