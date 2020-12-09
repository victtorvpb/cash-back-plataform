SHELL=/bin/bash
DOCKER_COMPOSE=docker-compose.yml
SUDO=sudo
CONTAINER_NAME=cash_back_plataform

install:
	$(info ************  Not command ************)
build:
	docker-compose -f $(DOCKER_COMPOSE) build --force-rm --no-cache ${CONTAINER_NAME}

start: 
	docker-compose -f $(DOCKER_COMPOSE) up -d

stop:
	docker-compose -f $(DOCKER_COMPOSE) down; true

exec:
	docker-compose -f $(DOCKER_COMPOSE) exec -T ${CONTAINER_NAME} $(COMMAND)

install-requirements:
	pip install -r requirements.txt

pep8:
	make exec COMMAND="flake8 . --exit-zero"

test:
	make exec COMMAND="py.test --cov=apps --cov-config .coveragerc"
	make exec COMMAND="coverage html"

formatter: pep8
	make exec COMMAND="black . -S -v -t py38 --exclude '\alembic/' -l 100 "
	# make pep8