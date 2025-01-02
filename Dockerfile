FROM python:3.11-slim-buster

ARG DJANGO_SECRET_KEY

ENV PYTHONUNBUFFERED 1
ENV ENV ""
ENV RDS_USERNAME ""
ENV RDS_DB_NAME ""
ENV RDS_PASSWORD ""
ENV RDS_HOSTNAME ""
ENV RDS_PORT ""
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ENV EMAIL_HOST_USER ""
ENV EMAIL_HOST_PASSWORD ""
ENV EMAIL_REDIRECT_ADDRESS ""
ENV MAILCHIMP_AUTH_TOKEN ""
ENV CORS_ORIGIN_WHITELIST "http://localhost:3000,http://localhost:3001,http://localhost:5173"

WORKDIR /code

RUN apt-get update
RUN apt-get -y install gcc mariadb-client libmariadb-dev mime-support

COPY requirements.txt /code/
RUN pip install -r requirements.txt

# TODO - figure out why can't use more current version
RUN pip install --upgrade uwsgi==2.0.24

COPY . /code/

RUN mkdir /var/log/uwsgi
RUN touch /var/log/uwsgi/api.log

# collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["sh", "/code/start.sh"]