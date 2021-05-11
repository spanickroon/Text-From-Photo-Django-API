set_console_env:
	chmod +x ./scripts/create_console_dev_env.py
	./scripts/create_console_dev_env.py
	. ./variables/console_dev.env
	export $(cut -d= -f1 ./variables/console_dev.env)

start:
	docker stop literal_app_1 || docker rm literal_app_1 || docker rmi literal_app -f
	docker-compose -f docker-compose.yml up --build -d