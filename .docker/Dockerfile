FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/src \
    && set -ex \
    && apk add postgresql-libs zlib libjpeg-turbo libpng \
    && apk add --no-cache --virtual .build-deps \
    gcc musl-dev postgresql-dev zlib-dev libjpeg-turbo-dev libpng-dev

COPY requirements.txt /app/src/
RUN cd /app/src \
    && pip install --disable-pip-version-check --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY src /app/src/
WORKDIR /app/src/

EXPOSE 8000

CMD ["gunicorn", "-w", "9", "--bind", ":8000", "project.wsgi:application"]
