# Makefile para API Panadería

up:
	docker-compose up --build

down:
	docker-compose down

test:
	docker-compose exec api pytest

migrate:
	docker-compose exec api alembic upgrade head

makemigration:
	docker-compose exec api alembic revision --autogenerate -m "Nueva migración"

