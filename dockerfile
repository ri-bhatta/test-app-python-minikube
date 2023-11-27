FROM python:3.9
WORKDIR /app
COPY test.py /app/test.py

# Create the logs directory
RUN mkdir -p /app/logs

RUN useradd -m appuser
USER appuser
CMD ["python", "/app/test.py"]
