from pydantic import BaseModel
import uuid
from typing import List

class OrderItemDTO(BaseModel):
    item_name: str
    quantity: int
    price: float

class OrderCreateDTO(BaseModel):
    table_id: uuid.UUID
    items: List[OrderItemDTO]

class OrderReadDTO(BaseModel):
    id: uuid.UUID
    table_id: uuid.UUID
    total_amount: float
    status: str

    class Config:
        orm_mode = True
