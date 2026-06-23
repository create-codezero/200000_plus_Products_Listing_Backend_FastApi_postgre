from pydantic import BaseModel
from datetime import datetime


class ProductOut(BaseModel):
    public_id: str
    name: str
    brand: str
    category: str
    price: float
    updated_at: datetime

    class Config:
        from_attributes = True