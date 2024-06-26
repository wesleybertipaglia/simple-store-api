# project
init: 
	@python3 -m venv venv

activate:
	@source venv/bin/activate

setup:	
	@pip3 install -r requirements.txt

requirements:
	@pip3 freeze > requirements.txt

run:	
	@uvicorn main:app --reload

test:
	@pytest

# Docker
compose-up:
	@docker compose up -d

compose-down:
	@docker compose down

# Database
db-init:
	@python3 db_init.py

# Alembic
alembic-init:
	@alembic init alembic

alembic-migrate:
	@alembic migrate

alembic-upgrade:
	@alembic upgrade head

alembic-downgrade:
	@alembic downgrade -1

alembic-history:
	@alembic history

alembic-current:
	@alembic current

alembic-revision:
	@alembic revision -m 'autogenerated' --autogenerate