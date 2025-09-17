from pydantic import BaseModel
import uuid

class PaymentCreateDTO(BaseModel):
    order_id: uuid.UUID
    amount: float
    payment_method: str

class PaymentReadDTO(BaseModel):
    id: uuid.UUID
    order_id: uuid.UUID
    amount: float
    payment_method: str
    status: str

    class Config:
        orm_mode = True
