FROM python:3.8.0-slim

WORKDIR /usr/src/app

COPY src/requirements.txt /usr/src/app/

RUN pip install -r /usr/src/app/requirements.txt

COPY src/* /usr/src/app/

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]