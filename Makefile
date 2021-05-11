set_console_env:
	chmod +x ./scripts/create_console_dev_env.py
	./scripts/create_console_dev_env.py
	. ./variables/console_dev.env
	export $(cut -d= -f1 ./variables/console_dev.env)

makemigrations:
	docker-compose -p literal_makemigrations run --rm --entrypoint "./manage.py makemigrations" app

migrate:
	docker-compose -p literal_migrate run --rm --entrypoint "./manage.py migrate" app

build:
	docker stop literal_app_1 || docker rm literal_app_1 || docker rmi literal_app -f
	docker-compose -f docker-compose.yml up --build -d

start:
	make build
	make makemigrations
	make migrate

down:
	docker-compose down --remove-orphans
