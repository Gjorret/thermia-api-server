# Dockerfile for Thermia API Server

FROM python:3.12-slim

# Set working directory
WORKDIR /usr/src/app

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY src/ ./src/

# Expose port
EXPOSE 8000

# Set the default command to run the app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "src.app:app"]
