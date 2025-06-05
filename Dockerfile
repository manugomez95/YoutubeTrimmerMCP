FROM python:3.11-slim

# Install system dependencies including ffmpeg for video processing
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src/
COPY pyproject.toml .
COPY setup.py .
COPY README.md .

# Install the package
RUN pip install -e .

# Create output directory
RUN mkdir -p /app/output

# Expose the port (if needed for HTTP mode)
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

# Set the default command to run the MCP server
CMD ["youtube-trimmer-mcp"] 