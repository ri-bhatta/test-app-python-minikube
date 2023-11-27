# Dockerfile

FROM python:3.9
WORKDIR /app
COPY test.py /app/test.py
CMD ["python", "/app/test.py"]