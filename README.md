# MLWorkflowWithAirflow

This is an example of machine learning workflow using [Airflow](https://airflow.apache.org/).

## Installation

Run

```bash
export AIRFLOW_HOME=/path/to/this/directory
pip install -r requirements.txt
make db/init
```

## Usage
To start the webserver, run `make run/webserver`. You'll be able to see Airflow's interface on `http://localhost:8080/`.

To start the scheduler and start the tasks, run:
```bash
make run/scheduler
```
