FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
COPY . /code/
EXPOSE 8000
VOLUME /data
CMD gunicorn wsgi:application --bind 0.0.0.0:$PORT
