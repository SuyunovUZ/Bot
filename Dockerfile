# ✅ Use a clean environment with Rust preinstalled
FROM python:3.11-slim

# 🔧 Install build tools and Rust
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    rustc \
    cargo \
    && apt-get clean

# 🧠 Set work directory
WORKDIR /app

# 🗃 Copy files into the container
COPY . .

# 💾 Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ▶️ Start your bot
CMD ["python", "main.py"]
