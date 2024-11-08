# Makefile for setting up Redis and PostgreSQL
REDIS_CONTAINER_NAME=artera-redis
POSTGRES_CONTAINER_NAME=artera-postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=postgres
POSTGRES_PORT=5433
REDIS_PORT=6379

run_postgres_local:
	docker run --name $(POSTGRES_CONTAINER_NAME) -d \
		-e POSTGRES_USER=$(POSTGRES_USER) \
		-e POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) \
		-e POSTGRES_DB=$(POSTGRES_DB) \
		-p $(POSTGRES_PORT):5432 postgres:latest

run_redis_local:
	docker run --name $(REDIS_CONTAINER_NAME) -d \
		-p $(REDIS_PORT):6379 redis:latest

run: 
	make run_postgres_local  
	make run_redis_local