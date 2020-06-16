FROM python:3.7

ENV AIRFLOW_HOME=/usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
