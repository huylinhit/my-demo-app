#!/bin/bash

# Dừng các container cũ nếu có
docker compose down

# Build và chạy lại
docker compose up --build -d

echo "Đang khởi động Lambda local tại cổng 9000..."
sleep 5 # Chờ container khởi động xong

# Gửi request test
echo "--- Kết quả Test ---"
curl -s -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
echo -e "\n-------------------"

# Tắt container sau khi test xong (tùy chọn)
# docker compose down