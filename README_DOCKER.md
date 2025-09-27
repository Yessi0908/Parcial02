# Docker README for Panadería API

Este proyecto contiene una API REST para la gestión de productos de panadería, desarrollada con FastAPI, PostgreSQL, SQLAlchemy y Alembic. Incluye pruebas automáticas y está preparado para ejecutarse en Docker.

## Requisitos
- Docker
- Docker Compose

## Instrucciones rápidas

1. **Clonar el repositorio**

2. **Construir y levantar los servicios:**

```sh
docker-compose up --build
```

Esto levantará tanto la API como la base de datos PostgreSQL.

3. **Acceso a la API:**
- Documentación Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

4. **Ejecutar tests:**

```sh
docker-compose exec api pytest
```

## Variables de entorno
Configura las variables necesarias en un archivo `.env` (ver ejemplo `.env.example`).

## Migraciones
Para aplicar migraciones con Alembic:

```sh
docker-compose exec api alembic upgrade head
```

---

## Estructura esperada
- `main.py`: Entrypoint de la API
- `models.py`, `schemas.py`, `crud.py`: Lógica de negocio y acceso a datos
- `alembic/`: Migraciones
- `tests/`: Pruebas automáticas

---

## Notas
- El contenedor de la API espera que la base de datos esté disponible en `db:5432`.
- El usuario y contraseña de la base de datos se configuran en el archivo `.env`.

---

## Makefile (opcional)
Puedes usar un Makefile para simplificar comandos comunes (build, test, migrate, etc).

---

## Autoría
- [Tu nombre]
- [URL del repositorio]
