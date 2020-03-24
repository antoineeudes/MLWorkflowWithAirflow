run/webserver:
	airflow webserver -p 8080

db/init:
	airflow initdb

run/scheduler:
	airflow scheduler