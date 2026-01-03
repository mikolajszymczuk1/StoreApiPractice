from pydantic import BaseModel


class DeleteItemResponse(BaseModel):
    removed_item_id: int
