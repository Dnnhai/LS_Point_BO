FROM python:3.11-slim

# Cài dependencies để Chromium chạy được
RUN apt-get update && apt-get install -y \
    wget \
    libnss3 \
    libx11-6 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libgtk-3-0 \
    libpango-1.0-0 \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# 🔑 Cài đặt browsers cho Playwright
RUN playwright install --with-deps chromium

COPY . .

CMD ["pytest", "-v"]
