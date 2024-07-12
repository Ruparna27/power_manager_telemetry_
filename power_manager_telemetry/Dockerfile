FROM ubuntu:latest

RUN apt-get update && apt-get install -y stress

CMD ["stress", "--cpu", "4", "--io", "4", "--vm", "2", "--vm-bytes", "128M", "--timeout", "300s"]

