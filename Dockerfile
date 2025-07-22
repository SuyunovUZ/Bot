FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    rustc \
    cargo \
    && apt-get clean

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
