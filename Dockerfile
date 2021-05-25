FROM python:3.9.5-slim-buster

ARG SQLALCHEMY_DATABASE_URI
ENV SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI}

RUN apt-get update
RUN apt-get install git gcc python3-dev libpq-dev -y

RUN pip install -U pip

RUN apt-get clean -y

WORKDIR /opt/app/cash_back_plataform/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /opt/app/cash_back_plataform/


