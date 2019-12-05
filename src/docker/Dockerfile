FROM python:3.6-alpine

RUN adduser -D user

WORKDIR /home/user

COPY requirements.txt requirements.txt
COPY app ./app
COPY main.py ./main.py

RUN pip install -r requirements.txt

ENV FLASK_APP main.py

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
