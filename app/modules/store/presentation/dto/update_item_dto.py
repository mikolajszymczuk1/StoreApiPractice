from pydantic import BaseModel


class UpdateItemDTO(BaseModel):
    name: str
    weight: str
    qty: int
    price: int
