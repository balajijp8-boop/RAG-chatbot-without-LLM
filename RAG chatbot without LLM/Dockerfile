FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system deps (needed for PDFs & torch)
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY src ./src
COPY templates ./templates

# Expose port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
