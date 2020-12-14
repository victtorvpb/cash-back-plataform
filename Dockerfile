FROM python:3.7.4-slim-stretch

ARG SQLALCHEMY_DATABASE_URI
ENV SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI}

RUN apt-get update
RUN apt-get install git gcc python3-dev libpq-dev -y

RUN apt-get clean -y

WORKDIR /opt/app/cash_back_plataform/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /opt/app/cash_back_plataform/


