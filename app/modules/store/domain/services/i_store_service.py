from abc import ABC, abstractmethod

from app.modules.store.domain.models.item import Item
from app.modules.store.presentation.dto import CreateItemDTO, UpdateItemDTO


class IStoreService(ABC):
    @abstractmethod
    def get_all_items(self) -> list[Item]: ...

    @abstractmethod
    def get_item_by_id(self, item_id: int) -> Item: ...

    @abstractmethod
    def create_item(self, itemDto: CreateItemDTO) -> Item: ...

    @abstractmethod
    def delete_item(self, item_id: int) -> int: ...

    @abstractmethod
    def update_item(self, item_id: int, itemDto: UpdateItemDTO) -> Item: ...

    @abstractmethod
    def update_item_qty(self, item_id: int, qty: int) -> Item: ...
