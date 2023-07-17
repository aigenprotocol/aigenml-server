FROM python:3.10-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5001

CMD [ "python", "run_server.py" ]
