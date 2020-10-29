# Pull image base

From python:3.7

# set enviornment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

# setting the works directory
WORKDIR /code

# install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip3 install --upgrade pip
RUN pip3 install pipenv && pipenv install --system

# copy the project
COPY . /code/
