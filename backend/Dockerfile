# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only dependencies first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app.py .

# Expose Flask port
EXPOSE 5000

# Run Flask
CMD ["python", "app.py"]