FROM python:3

WORKDIR /app

COPY . .
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt 

ENV FLASK_APP src

CMD flask run --host 0.0.0.0 --port 80