from sqlalchemy import Result
from sqlmodel import select
from sqlmodel.sql._expression_select_cls import SelectOfScalar

from app.modules.store.domain.models.item import Item
from app.modules.store.domain.repositories.i_store_repository import IStoreRepository
from app.modules.store.infrastructure.mappers.item_mapper import ItemMapper
from app.modules.store.infrastructure.orm.item_orm import Item as ItemORM
from app.shared.domain.services.database.i_sqlite_database_service import ISQLiteDatabaseService


class StoreRepository(IStoreRepository):
    def __init__(self, db: ISQLiteDatabaseService) -> None:
        self._db: ISQLiteDatabaseService = db

    async def get_all(self) -> list[Item]:
        async with self._db.get_session() as session:
            query: SelectOfScalar[ItemORM] = select(ItemORM)
            result: Result[tuple[ItemORM]] = await session.execute(query)
            items: list[Item] = [
                ItemMapper.to_domain(item_orm) for item_orm in result.scalars().all()
            ]

            return items

    async def get_by_id(self, item_id: int) -> Item | None:
        async with self._db.get_session() as session:
            query: SelectOfScalar[ItemORM] = select(ItemORM).where(ItemORM.id == item_id)
            result: Result[tuple[ItemORM]] = await session.execute(query)
            item_orm: ItemORM | None = result.scalar_one_or_none()
            if item_orm:
                return ItemMapper.to_domain(item_orm)

            return None

    async def create(self, item: Item) -> Item:
        async with self._db.get_session() as session:
            item_orm: ItemORM = ItemMapper.to_orm(item)

            async with session.begin():
                session.add(item_orm)
                await session.flush()

            return ItemMapper.to_domain(item_orm)

    async def delete_item(self, item_id: int) -> bool:
        async with self._db.get_session() as session, session.begin():
            query: SelectOfScalar[ItemORM] = select(ItemORM).where(ItemORM.id == item_id)
            result: Result[tuple[ItemORM]] = await session.execute(query)
            item_orm: ItemORM | None = result.scalar_one_or_none()

            if not item_orm:
                return False

            await session.delete(item_orm)
            await session.flush()

            return True

    async def update_item(self, item: Item) -> Item | None:
        async with self._db.get_session() as session, session.begin():
            query: SelectOfScalar[ItemORM] = select(ItemORM).where(ItemORM.id == item.id)
            result: Result[tuple[ItemORM]] = await session.execute(query)
            item_orm: ItemORM | None = result.scalar_one_or_none()

            if not item_orm:
                return None

            item_orm.name = item.name
            item_orm.weight = item.weight
            item_orm.qty = item.qty
            item_orm.price = item.price

            session.add(item_orm)
            await session.flush()

            return ItemMapper.to_domain(item_orm)

    async def update_qty(self, item_id: int, qty: int) -> Item | None:
        async with self._db.get_session() as session, session.begin():
            query: SelectOfScalar[ItemORM] = select(ItemORM).where(ItemORM.id == item_id)
            result: Result[tuple[ItemORM]] = await session.execute(query)
            item_orm: ItemORM | None = result.scalar_one_or_none()

            if not item_orm:
                return None

            item_orm.qty = qty

            session.add(item_orm)
            await session.flush()

            return ItemMapper.to_domain(item_orm)
