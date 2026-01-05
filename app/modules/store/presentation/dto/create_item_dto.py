from pydantic import BaseModel


class CreateItemDTO(BaseModel):
    name: str
    weight: str
    qty: int
    price: int
