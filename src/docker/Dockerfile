FROM python:3.6-alpine

RUN adduser -D user

WORKDIR /home/user

COPY requirements.txt requirements.txt
COPY app.py ./app.py

RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt

RUN chmod a+x app.py

ENTRYPOINT ["./app.py"]
