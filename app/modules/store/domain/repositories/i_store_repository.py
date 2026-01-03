from abc import ABC, abstractmethod

from app.modules.store.domain.models.item import Item


class IStoreRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Item]: ...

    @abstractmethod
    def get_by_id(self, item_id: int) -> Item | None: ...

    @abstractmethod
    def create(self, item: Item) -> Item: ...

    @abstractmethod
    def delete(self, item_id: int) -> bool: ...

    @abstractmethod
    def update(self, item: Item) -> Item | None: ...

    @abstractmethod
    def update_qty(self, item_id: int, qty: int) -> Item | None: ...
