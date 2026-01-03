from app.modules.store.domain.models.item import Item
from app.modules.store.domain.repositories.i_store_repository import IStoreRepository


class StoreRepository(IStoreRepository):
    def __init__(self) -> None:
        self.id: int = 0
        self.items: list[Item] = []

    def get_all(self) -> list[Item]:
        return self.items

    def get_by_id(self, item_id: int) -> Item | None:
        for item in self.items:
            if item.id == item_id:
                return item

        return None

    def create(self, item: Item) -> Item:
        self.id += 1
        newItem: Item = Item(self.id, item.name, item.weight, item.qty)
        self.items.append(newItem)
        return newItem

    def delete(self, item_id: int) -> bool:
        for i, item in enumerate(self.items):
            if item.id == item_id:
                del self.items[i]
                print("siema")
                return True

        return False

    def update(self, item: Item) -> Item | None:
        for i, existing_item in enumerate(self.items):
            if existing_item.id == item.id:
                self.items[i] = item
                return item

        return None

    def update_qty(self, item_id: int, qty: int) -> Item | None:
        for i, item in enumerate(self.items):
            if item.id == item_id:
                self.items[i].qty = qty
                return self.items[i]

        return None
