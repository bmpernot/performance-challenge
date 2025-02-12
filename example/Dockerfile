FROM registry.dci.bt.com/bt-images/python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir sympy

COPY . .

VOLUME /data

ENTRYPOINT ["python", "main.py"]