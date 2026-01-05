from abc import ABC, abstractmethod

from app.modules.store.domain.models.item import Item
from app.modules.store.presentation.dto import CreateItemDTO, UpdateItemDTO


class IStoreService(ABC):
    @abstractmethod
    async def get_all_items(self) -> list[Item]: ...

    @abstractmethod
    async def get_item_by_id(self, item_id: int) -> Item: ...

    @abstractmethod
    async def create_item(self, item_dto: CreateItemDTO) -> Item: ...

    @abstractmethod
    async def delete_item(self, item_id: int) -> int: ...

    @abstractmethod
    async def update_item(self, item_id: int, item_dto: UpdateItemDTO) -> Item: ...

    @abstractmethod
    async def update_item_qty(self, item_id: int, qty: int) -> Item: ...
