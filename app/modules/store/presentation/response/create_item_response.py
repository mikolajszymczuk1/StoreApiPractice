from pydantic import BaseModel


class CreateItemResponse(BaseModel):
    created_item_id: int
