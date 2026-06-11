FROM debian:stable-slim

RUN apt update && apt install -y python3

RUN apt install python-is-python3 -y

COPY main.py main.py

COPY books/ books/

CMD ["python", "main.py"]