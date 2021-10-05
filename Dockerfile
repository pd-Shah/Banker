From python:latest

LABEL MAINTAINER="pd"

ADD . /Banker
WORKDIR /Banker

# Installing requirements
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt