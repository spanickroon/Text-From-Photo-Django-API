set_console_env:
	chmod +x ./scripts/create_console_dev_env.py
	./scripts/create_console_dev_env.py
	. ./variables/console_dev.env
	export $(cut -d= -f1 ./variables/console_dev.env)

migrations:
	docker-compose  run --rm --entrypoint "./manage.py makemigrations" app

migrate:
	docker-compose  run --rm --entrypoint "./manage.py migrate --no-input" app

static:
	docker-compose  run --rm --entrypoint "./manage.py collectstatic --no-input" app

build:
	docker stop literal_postres || docker rm literal_postres || echo "Deleted postres"
	docker stop literal_app || docker rm literal_app || docker rmi literal -f || echo "Deleted app"
	docker stop literal_nginx || docker rm literal_nginx || echo "Deleted nginx"
	docker-compose -f docker-compose.yaml up --build -d

start:
	make build
	make migrations
	make migrate
	make static

down:
	docker-compose down --remove-orphans

test:
	docker-compose run --rm --entrypoint "./manage.py test" app

test-coverage:
	docker-compose run --rm --entrypoint "coverage run manage.py test" app
	docker-compose run --rm app coverage report

isort:
	docker-compose run --rm app isort /app

black:
	docker-compose run --rm app black /app

mypy:
	docker-compose run --rm app mypy /app

pylint:
	docker-compose run --rm app pylint apps literal

prepare-commit:
	make isort
	make black
	make pylint
	make mypy

literal-shell:
	docker exec -it literal_app bash

literal-postgres-shell:
	docker exec -it literal_postgres bash

logs:
	docker-compose logs -f --tail 100

logs-app:
	docker-compose logs -f --tail 100 app

build-prod:
	docker stop literal_postres || docker rm literal_postres || echo "Deleted postres"
	docker stop literal_app || docker rm literal_app || docker rmi literal -f || echo "Deleted app"
	docker stop literal_nginx || docker rm literal_nginx || echo "Deleted nginx"
	docker-compose -f docker-compose.prod.yaml up --build -d

start-prod:
	make build-prod
	make migrations
	make migrate
	make static
