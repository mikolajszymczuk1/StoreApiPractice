from fastapi import APIRouter, status

from app.core.container import storeService
from app.modules.store.domain.models.item import Item
from app.modules.store.presentation.dto import CreateItemDTO, UpdateItemDTO
from app.modules.store.presentation.response import (
    CreateItemResponse,
    DeleteItemResponse,
    GetItemResponse,
    UpdatedItemResponse,
)

router = APIRouter(prefix="/items", tags=["Items"])

# ====== Store controller ======

# ===============================


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[GetItemResponse])
async def get_items() -> list[Item]:
    items: list[Item] = storeService.get_all_items()
    return items


# ===============================


@router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=GetItemResponse)
async def get_item(item_id: int) -> Item:
    item: Item = storeService.get_item_by_id(item_id)
    return item


# ===============================


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CreateItemResponse)
async def create_item(item: CreateItemDTO) -> dict[str, int]:
    created_item: Item = storeService.create_item(item)
    return {"created_item_id": created_item.id}


# ===============================


@router.delete("/{item_id}", status_code=status.HTTP_200_OK, response_model=DeleteItemResponse)
async def delete_item(item_id: int) -> dict[str, int]:
    deleted_item_id: int = storeService.delete_item(item_id)
    return {"removed_item_id": deleted_item_id}


# ===============================


@router.put("/{item_id}", status_code=status.HTTP_200_OK, response_model=UpdatedItemResponse)
async def update_item(item_id: int, item: UpdateItemDTO) -> dict[str, int]:
    updated_item: Item = storeService.update_item(item_id, item)
    return {"updated_item_id": updated_item.id}


# ===============================
