# MLWorkflowWithAirflow

This is an example of machine learning workflow using [Airflow](https://airflow.apache.org/).

## Installation

### Prerequisites:
 - docker :whale:
 - docker-compose

Run
```bash
make install
```

This will create three containers:
 - a Postgres database
 - a Python container running the scheduler
 - a Python container running the webserver

Additionaly, it will initialize the database.

## Usage
To start the webserver, the database and the scheduler, run:
```bash
make start
```

:tada: Browse http://localhost:8080/ to get started!
