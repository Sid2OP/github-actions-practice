# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY scripts/ ./scripts/

RUN pip install --no-cache-dir pytest

CMD ["python", "scripts/test_math.py"]