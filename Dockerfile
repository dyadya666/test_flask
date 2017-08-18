FROM ubuntu:16.04

MAINTAINER schepurnov <gpgmailry@gmail.com>

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev python3-venv

COPY . /test_flask_docker2/

WORKDIR /test_flask_docker2

RUN python3 -m venv myvenv

RUN . myvenv/bin/activate && \
	pip3 install --upgrade pip && \
	pip3 install -r requirements.txt

EXPOSE 5000