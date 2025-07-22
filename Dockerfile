# Use official Python image with a safe version
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    rustc \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Copy your files
COPY . .

# Install Python deps
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run bot
CMD ["python", "main.py"]
