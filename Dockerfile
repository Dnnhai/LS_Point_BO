FROM python:3.11-slim

# 1. Cài gói hệ thống cần thiết
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    gnupg \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxss1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libgbm-dev \
    libxshmfence-dev \
    libgtk-3-0 \
 && rm -rf /var/lib/apt/lists/*


# 2. Tạo thư mục làm việc
WORKDIR /app

# 3. Copy requirements
COPY requirements.txt .

# 4. Cài Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Cài browsers cho Playwright
RUN playwright install --with-deps

# 6. Copy toàn bộ source code vào container
COPY . .

# 7. Default: chạy pytest, generate báo cáo Allure
CMD ["pytest", "--alluredir=allure-results"]
