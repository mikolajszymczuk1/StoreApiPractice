from pydantic import BaseModel


class UpdatedItemResponse(BaseModel):
    updated_item_id: int
