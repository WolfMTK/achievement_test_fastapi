build:
	docker compose -f docker-compose.yml build
run:
	docker compose -f docker-compose.yml up
migration:
	docker compose -f docker-compose.yml exec backend alembic upgrade head
