
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Si se está ejecutando pytest, forzar localhost como host de la base de datos
if any("pytest" in arg for arg in sys.argv):
	DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/panaderia"
else:
	DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/panaderia")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
