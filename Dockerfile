FROM python:3.12.6-slim

RUN apt-get update && apt-get install -y

WORKDIR /app

COPY . ./app

RUN python -m pip install -r app/requirements.txt \
  --no-cache-dir \
  --upgrade \
  --force-reinstall

CMD ["python", "app/main.py"]