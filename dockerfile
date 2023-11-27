FROM python:3.9

WORKDIR /app
COPY test.py /app/test.py

# Create the logs directory
RUN mkdir -p /app/logs

# Set the working directory to /app
WORKDIR /app

# Switch to a non-root user
RUN useradd -m appuser
USER appuser

# CMD to run the application
CMD ["python", "/app/test.py"]
