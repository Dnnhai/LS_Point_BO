FROM mcr.microsoft.com/playwright/python:v1.53.0

WORKDIR /app

# Copy và cài requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Chạy pytest khi container start
CMD ["pytest", "-v"]
