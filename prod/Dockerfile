# Stage 1: Build stage
FROM python:3.9-slim-buster AS build-stage

# Set the working directory
WORKDIR /app

# Install build dependencies and clean up afterwards
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    ffmpeg \
    libsm6 \
    libxext6 \
    python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage caching
COPY requirements.txt .

# Create a virtual environment and install dependencies
RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu && \
    /venv/bin/pip cache purge

# Copy the application files
COPY . .

# Stage 2: Final stage
FROM gcr.io/distroless/python3-debian12

# Set the working directory
WORKDIR /app

# Copy the virtual environment from the build stage
COPY --from=build-stage /venv /venv

# Copy the necessary application files
COPY --from=build-stage /app /app

# Ensure the virtual environment's Python is used
ENV PATH="/venv/bin:$PATH"

# Copy the Google credentials file to the container
COPY superchatbill-0e602de15713.json /app/superchatbill-0e602de15713.json

# Expose the port Streamlit runs on
EXPOSE 8501

# Set healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the Streamlit app
CMD ["/venv/bin/streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
