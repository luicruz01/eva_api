FROM registry.gitlab.com/truehome/th-images/base/python:uwsgi-3.8

LABEL Description="API for EVA"
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /srv/app
WORKDIR /srv/app


COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

COPY ./uwsgi.ini /etc/uwsgi.ini
