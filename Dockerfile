FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

ENV BUILD=$Build

CMD [ "python3", "app.py" ]

EXPOSE 5000
