from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.core.container import Container
from app.modules.store.domain.models.item import Item
from app.modules.store.domain.services.i_store_service import IStoreService
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
@inject
async def get_items(
    store_service: IStoreService = Depends(Provide[Container.store_service]),
) -> list[Item]:
    items: list[Item] = await store_service.get_all_items()
    return items


# ===============================


@router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=GetItemResponse)
@inject
async def get_item(
    item_id: int, store_service: IStoreService = Depends(Provide[Container.store_service])
) -> Item:
    item: Item = await store_service.get_item_by_id(item_id)
    return item


# ===============================


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CreateItemResponse)
@inject
async def create_item(
    item: CreateItemDTO,
    store_service: IStoreService = Depends(Provide[Container.store_service]),
) -> dict[str, int]:
    created_item: Item = await store_service.create_item(item)
    return {"created_item_id": created_item.id}


# ===============================


@router.delete("/{item_id}", status_code=status.HTTP_200_OK, response_model=DeleteItemResponse)
@inject
async def delete_item(
    item_id: int,
    store_service: IStoreService = Depends(Provide[Container.store_service]),
) -> dict[str, int]:
    deleted_item_id: int = await store_service.delete_item(item_id)
    return {"removed_item_id": deleted_item_id}


# ===============================


@router.put("/{item_id}", status_code=status.HTTP_200_OK, response_model=UpdatedItemResponse)
@inject
async def update_item(
    item_id: int,
    item: UpdateItemDTO,
    store_service: IStoreService = Depends(Provide[Container.store_service]),
) -> dict[str, int]:
    updated_item: Item = await store_service.update_item(item_id, item)
    return {"updated_item_id": updated_item.id}


# ===============================
