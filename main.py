from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Panadería CRUD", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/apiv1/productos/", response_model=schemas.ProductoOut, status_code=201)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db, producto)

@app.get("/apiv1/productos/", response_model=list[schemas.ProductoOut])
def listar_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_productos(db, skip=skip, limit=limit)

@app.get("/apiv1/productos/{producto_id}", response_model=schemas.ProductoOut)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.get_producto(db, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.put("/apiv1/productos/{producto_id}", response_model=schemas.ProductoOut)
def actualizar_producto(producto_id: int, producto: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    return crud.update_producto(db, producto_id, producto)

@app.delete("/apiv1/productos/{producto_id}", response_model=schemas.ProductoOut)
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    return crud.delete_producto(db, producto_id)
