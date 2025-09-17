from pydantic import BaseModel
import uuid

class TableCreateDTO(BaseModel):
    name: str
    location: str
    code: str | None = None

class TableReadDTO(BaseModel):
    id: uuid.UUID
    name: str
    location: str
    code: str | None

    class Config:
        orm_mode = True
