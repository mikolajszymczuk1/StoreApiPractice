from abc import ABC, abstractmethod

from app.modules.store.domain.models.item import Item


class IStoreRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Item]: ...

    @abstractmethod
    async def get_by_id(self, item_id: int) -> Item | None: ...

    @abstractmethod
    async def create(self, item: Item) -> Item: ...

    @abstractmethod
    async def delete_item(self, item_id: int) -> bool: ...

    @abstractmethod
    async def update_item(self, item: Item) -> Item | None: ...

    @abstractmethod
    async def update_qty(self, item_id: int, qty: int) -> Item | None: ...
