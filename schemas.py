from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from models import CategoriaEnum

class ProductoBase(BaseModel):
    nombre: str = Field(..., max_length=150)
    sku: str = Field(..., max_length=20)
    categoria: CategoriaEnum
    precio_unitario: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    disponible: Optional[bool] = True

    @validator("sku")
    def sku_format(cls, v):
        if not v:
            raise ValueError("SKU obligatorio")
        return v

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=150)
    categoria: Optional[CategoriaEnum]
    precio_unitario: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    disponible: Optional[bool]

class ProductoOut(ProductoBase):
    id: int
    fecha_registro: datetime
    fecha_actualizacion: Optional[datetime]

    class Config:
        orm_mode = True
