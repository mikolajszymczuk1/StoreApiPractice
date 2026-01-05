from fastapi import HTTPException, status

from app.modules.store.domain.models.item import Item
from app.modules.store.domain.repositories.i_store_repository import IStoreRepository
from app.modules.store.domain.services.i_store_service import IStoreService
from app.modules.store.presentation.dto import CreateItemDTO, UpdateItemDTO


class StoreService(IStoreService):
    def __init__(self, store_repository: IStoreRepository) -> None:
        """
        Initializes the StoreService with a repository implementation.

        :param storeRepository: Repository responsible for Item persistence.
        """

        self.store_repository: IStoreRepository = store_repository

    async def get_all_items(self) -> list[Item]:
        """
        Retrieves all items available in the store.

        :return: List of Item domain objects.
        """

        return await self.store_repository.get_all()

    async def get_item_by_id(self, item_id: int) -> Item:
        """
        Retrieves a single item by its unique identifier.

        :param item_id: Unique identifier of the item.
        :return: Item domain object.
        :raises HTTPException: If the item does not exist.
        """

        item: Item | None = await self.store_repository.get_by_id(item_id)
        if item:
            return item

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item_not_found")

    async def create_item(self, item_dto: CreateItemDTO) -> Item:
        """
        Creates a new item based on the provided input data.

        The method:
        - maps the incoming DTO to a domain entity,
        - delegates persistence to the repository,
        - returns the created Item with an assigned ID.

        :param itemDto: Data transfer object containing item data.
        :return: Created Item domain object.
        """

        newItem: Item = Item(0, item_dto.name, item_dto.weight, item_dto.qty, item_dto.price)
        return await self.store_repository.create(newItem)

    async def delete_item(self, item_id: int) -> int:
        """
        Deletes an existing item from the store.

        :param item_id: Identifier of the item to be deleted.
        :return: ID of the deleted item.
        :raises HTTPException: If the item does not exist.
        """

        result: bool = await self.store_repository.delete_item(item_id)
        if result:
            return item_id

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item_not_found")

    async def update_item(self, item_id: int, item_dto: UpdateItemDTO) -> Item:
        """
        Updates all properties of an existing item.

        The method:
        - creates a new Item entity with updated values,
        - delegates the update operation to the repository,
        - returns the updated Item.

        :param item_id: Identifier of the item to update.
        :param itemDto: DTO containing updated item data.
        :return: Updated Item domain object.
        :raises HTTPException: If the item does not exist.
        """

        updatedItem: Item = Item(
            item_id, item_dto.name, item_dto.weight, item_dto.qty, item_dto.price
        )
        item: Item | None = await self.store_repository.update_item(updatedItem)

        if item:
            return item

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item_not_found")

    async def update_item_qty(self, item_id: int, qty: int) -> Item:
        """
        Updates only the quantity (qty) of an existing item.

        This method is useful for partial updates such as inventory
        or stock adjustments without modifying other fields.

        :param item_id: Identifier of the item.
        :param qty: New quantity value.
        :return: Updated Item domain object.
        :raises HTTPException: If the item does not exist.
        """

        item: Item | None = await self.store_repository.update_qty(item_id, qty)

        if item:
            return item

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item_not_found")
