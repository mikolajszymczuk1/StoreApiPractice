from app.modules.store.domain.models.item import Item
from app.modules.store.infrastructure.orm.item_orm import Item as ItemORM


class ItemMapper:
    @staticmethod
    def to_domain(item_orm: ItemORM) -> Item:
        return Item(
            id=item_orm.id or 0,
            name=item_orm.name,
            weight=item_orm.weight,
            qty=item_orm.qty,
        )

    @staticmethod
    def to_orm(item: Item) -> ItemORM:
        return ItemORM(
            id=item.id if item.id != 0 else None,
            name=item.name,
            weight=item.weight,
            qty=item.qty,
        )
