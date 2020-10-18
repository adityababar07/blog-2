# Pull image base

From python:3.7

# set enviornment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

# setting the works directory
WORKDIR /code/python/django_projects/blog_projects

# install dependencies
COPY Pipfile Pipfile.lock /code/python/django_projects/blog_projects/
RUN pip install pipenv && pipenv install --system

# copy the project
COPY . /code/python/django_projects/blog_projects/
