# Base image ổn định (không dùng latest để tránh lỗi repo)
FROM ubuntu:20.04

# Tránh apt hỏi cấu hình (timezone, keyboard...)
ENV DEBIAN_FRONTEND=noninteractive

# Cập nhật và cài các gói cần thiết
RUN apt-get update -o Acquire::Retries=3 && \
    apt-get install -y --no-install-recommends \
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
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Đặt thư mục làm việc
WORKDIR /app

# Copy toàn bộ code vào container
COPY . .

# Nếu có requirements.txt thì cài
# (bỏ nếu bạn không dùng Python)
RUN if [ -f "requirements.txt" ]; then pip3 install --no-cache-dir -r requirements.txt; fi

# Lệnh mặc định khi chạy container
CMD ["bash"]
