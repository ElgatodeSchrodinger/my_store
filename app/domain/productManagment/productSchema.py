from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class ProductBase(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


# Properties to receive via API on creation
class ProductCreateSchema(ProductBase):
    name: str
    sku: str
    price: float


# Properties to receive via API on update
class ProductUpdateSchema(ProductBase):
    pass


# properties to push via API
class ProductDBSchema(ProductBase):
    product_id: int

    class Config:
        orm_mode = True
