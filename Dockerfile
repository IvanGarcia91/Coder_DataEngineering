FROM python:3.10.5-slim-buster

COPY . usr/src/app
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-u", "weather_etl.py"]
