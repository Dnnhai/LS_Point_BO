FROM mcr.microsoft.com/playwright/python:v1.53.0

# Set timezone Asia/Ho_Chi_Minh
ENV TZ=Asia/Ho_Chi_Minh
RUN apt-get update && apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy và cài requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Cài browsers Playwright (Chromium/Firefox/Webkit)
RUN playwright install --with-deps

# Copy toàn bộ code vào container
COPY . .

# Chạy pytest khi container start
CMD ["pytest", "-v"]
