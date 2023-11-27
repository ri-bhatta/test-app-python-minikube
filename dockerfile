# Dockerfile

FROM python:3.9
WORKDIR /app
RUN useradd -m appuser
USER appuser
COPY test.py /app/test.py
CMD ["python", "/app/test.py"]
