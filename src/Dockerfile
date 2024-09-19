FROM python:3.12.6-slim

RUN apt-get update && apt-get install -y

WORKDIR /app

COPY . /app

ENV PYTHONPATH=/app

RUN apt update && apt upgrade -y && apt install build-essential libpq-dev -y

RUN python -m pip install -r requirements.txt \
  --no-cache-dir \
  --upgrade \
  --force-reinstall

CMD ["python", "main.py"]