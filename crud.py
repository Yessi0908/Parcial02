from sqlalchemy.orm import Session
from models import Producto, CategoriaEnum
from schemas import ProductoCreate, ProductoUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def get_producto_by_sku(db: Session, sku: str):
    return db.query(Producto).filter(Producto.sku == sku).first()

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producto).offset(skip).limit(limit).all()

def create_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    try:
        db.commit()
        db.refresh(db_producto)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="SKU ya existe")
    return db_producto

def update_producto(db: Session, producto_id: int, producto: ProductoUpdate):
    db_producto = get_producto(db, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for var, value in producto.dict(exclude_unset=True).items():
        setattr(db_producto, var, value)
    try:
        db.commit()
        db.refresh(db_producto)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="SKU ya existe")
    return db_producto

def delete_producto(db: Session, producto_id: int):
    db_producto = get_producto(db, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(db_producto)
    db.commit()
    return db_producto
