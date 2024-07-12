# stress_test/Dockerfile
FROM ubuntu:20.04

WORKDIR /app

COPY run_stress.sh /app/

RUN apt-get update && apt-get install -y stress-ng

ENTRYPOINT ["sh", "/app/run_stress.sh"]
