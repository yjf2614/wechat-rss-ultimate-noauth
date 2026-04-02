version: "3"
services:
  wechat-rss:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./data:/app/data
    restart: always