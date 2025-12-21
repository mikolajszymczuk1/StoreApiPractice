from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    item_id: int
    name: str
    description: str


app = FastAPI()

@app.get("/hello/{name}")
async def hello(name: str, age: int = 0):
    return {
        "msg": f"Hello {name}!",
        "age": age
    }

@app.post("/create_item")
async def create_item(item: Item):
    return {
        "item_id": item.item_id,
        "name": item.name,
        "description": item.description
    }
