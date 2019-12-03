FROM python:3.6-alpine

RUN adduser -D user

WORKDIR /home/user

COPY requirements.txt requirements.txt
COPY app ./app
COPY main.py ./main.py
COPY boot.sh ./boot.sh

RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt

RUN chmod a+x main.py
RUN chmod a+x boot.sh

ENTRYPOINT ["./boot.sh"]
