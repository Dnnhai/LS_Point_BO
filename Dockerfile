FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -o Acquire::Retries=3 && \
    apt-get install -y --no-install-recommends \
      curl wget gnupg unzip \
      libglib2.0-0 libnss3 libfontconfig1 libxss1 \
      libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
      libxcomposite1 libxrandr2 libxdamage1 libgbm-dev \
      libxshmfence-dev libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /app
COPY . .
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt; fi
CMD ["pytest", "app.py"]
