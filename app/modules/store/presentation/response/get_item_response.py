from pydantic import BaseModel, ConfigDict


class GetItemResponse(BaseModel):
    id: int
    name: str
    weight: str
    qty: int
    price: int

    model_config = ConfigDict(from_attributes=True)
