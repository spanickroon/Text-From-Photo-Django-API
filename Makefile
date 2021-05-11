set_console_env:
	chmod +x ./scripts/create_console_dev_env.py
	./scripts/create_console_dev_env.py
	. ./variables/console_dev.env
	export $(cut -d= -f1 ./variables/console_dev.env)

migrations:
	docker-compose  run --rm --entrypoint "./manage.py makemigrations" app

migrate:
	docker-compose  run --rm --entrypoint "./manage.py migrate" app

build:
	docker stop literal_postres || docker rm literal_postres || echo "Deleted postres"
	docker stop literal_app || docker rm literal_app || docker rmi literal -f || echo "Deleted app"
	docker-compose -f docker-compose.yml up --build -d

start:
	make build
	make makemigrations
	make migrate

down:
	docker-compose down --remove-orphans
