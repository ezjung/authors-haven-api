build:
	docker compose -f local.yaml up --build -d --remove-orphans

up:
	docker compose -f local.yaml up -d

down:
	docker compose -f local.yaml down

show_logs:
	docker compose -f local.yaml logs

migrate:
	docker compose -f local.yaml run --rm api python3 manage.py migrate

makemigrations:
	docker compose -f local.yaml run --rm api python3 manage.py makemigrations

collectstatic:
	docker compose -f local.yaml run --rm api python3 manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yaml run --rm api python3 manage.py createsuperuser

down-v:
	docker compose -f local.yaml down -v

volume:
	docker volume inspect authors-src_local_postgres_data

authors-db:
	docker compose -f local.yaml exec postgres psql --username=alphaogilo --dbname=authors-live

flake8:
	docker compose -f local.yaml exec api flake8 .

black-check:
	docker compose -f local.yaml exec api black --check --exclude=migrations .

black-diff:
	docker compose -f local.yaml exec api black --diff --exclude=migrations .

black:
	docker compose -f local.yaml exec api black --exclude=migrations .

isort-check:
	docker compose -f local.yaml exec api isort . --check-only --skip env --skip migrations

isort-diff:
	docker compose -f local.yaml exec api isort . --diff --skip env --skip migrations

isort:
	docker compose -f local.yaml exec api isort . --skip env --skip migrations	





