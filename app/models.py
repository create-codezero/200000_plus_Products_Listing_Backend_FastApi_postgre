from sqlalchemy import Column, String, Float, DateTime, BigInteger
from .db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, index=True)

    public_id = Column(String, unique=True, index=True)

    name = Column(String, index=True)
    brand = Column(String, index=True)
    category = Column(String, index=True)

    price = Column(Float)

    created_at = Column(DateTime, index=True)
    updated_at = Column(DateTime, index=True)