start:
	docker-compose up

install:
	docker-compose build && docker-compose run scheduler airflow initdb
