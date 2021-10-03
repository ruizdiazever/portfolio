FROM python:3.9.7
ENV PYTHONUNBUFFERED 1

RUN pip install --user --upgrade pip
RUN mkdir /home/everdev
WORKDIR /home/everdev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN cd /home/everdev && touch secret_key.txt && echo 'passwordUltraSecret123' > secret_key.txt
