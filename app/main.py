from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from typing import List

app = FastAPI()


class Item:
    __id: int
    __name: str
    __weight: str
    __qty: int

    def __init__(self, id: int, name: str, weight: str, qty: int) -> None:
        self.__id = id
        self.__name = name
        self.__weight = weight
        self.__qty = qty


    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, value: str) -> None:
        self.__weight = value

    @property
    def qty(self) -> int:
        return self.__qty

    @qty.setter
    def qty(self, value: int) -> None:
        self.__qty = value


class CreateItemDTO(BaseModel):
    name: str
    weight: str
    qty: int


class UpdateItemDTO(BaseModel):
    name: str
    weight: str
    qty: int


class GetItemResponse(BaseModel):
    id: int
    name: str
    weight: str
    qty: int

    model_config = ConfigDict(from_attributes=True)


class CreateItemResponse(BaseModel):
    created_item_id: int


class DeleteItemResponse(BaseModel):
    removed_item_id: int


class UpdatedItemResponse(BaseModel):
    updated_item_id: int


generalId: int = 3

items: list[Item] = [
    Item(1, "Item 1", "10kg", 5),
    Item(2, "Item 2", "20kg", 3),
    Item(3, "Item 3", "15kg", 7)
] # Fake database


@app.get('/api/items', status_code=200, response_model=List[GetItemResponse])
async def get_items() -> list[Item]:
    return items


@app.get('/api/items/{item_id}', status_code=200, response_model=GetItemResponse)
async def get_item(item_id: int) -> Item:
    for item in items:
        if item.id == item_id:
            return item

    raise HTTPException(status_code=404, detail="item_not_found")


@app.post('/api/items', status_code=201, response_model=CreateItemResponse)
async def create_item(item: CreateItemDTO) -> dict[str, int]:
    global generalId
    generalId += 1
    newId: int = generalId
    newItem: Item = Item(newId, item.name, item.weight, item.qty)

    items.append(newItem)

    return {"created_item_id": newId}


@app.delete('/api/items/{item_id}', status_code=200, response_model=DeleteItemResponse)
async def delete_item(item_id: int) -> dict[str, int]:
    global items
    for i, item in enumerate(items):
        if item.id == item_id:
            del items[i]
            return {"removed_item_id": item_id}

    raise HTTPException(status_code=404, detail="item_not_found")


@app.put('/api/items/{item_id}', status_code=200, response_model=UpdatedItemResponse)
async def update_item(item_id: int, item: UpdateItemDTO) -> dict[str, int]:
    for it in items:
        if it.id == item_id:
            it.name = item.name
            it.weight = item.weight
            it.qty = item.qty

            return {"updated_item_id": item_id}

    raise HTTPException(status_code=404, detail="item_not_found")



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)
