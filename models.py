from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, func, Enum
from database import Base
import enum

class CategoriaEnum(str, enum.Enum):
    Pan = "Pan"
    Pasteleria = "Pastelería"
    Bebidas = "Bebidas"
    Otros = "Otros"

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    sku = Column(String(20), unique=True, nullable=False, index=True)
    categoria = Column(Enum(CategoriaEnum), nullable=False)
    precio_unitario = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    disponible = Column(Boolean, default=True)
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
