#!/bin/bash
#
# Script to run YouTube Trimmer MCP Server in Docker
# This script builds and runs the container for MCP stdio communication
#

# Build the Docker image
echo "Building YouTube Trimmer MCP Docker image..."
docker build -t youtube-trimmer-mcp .

# Run the container with stdio communication
echo "Starting YouTube Trimmer MCP Server in Docker..."
docker run -i --rm \
  --name youtube-trimmer-mcp-session \
  -v "$(pwd)/output:/app/output" \
  youtube-trimmer-mcp

echo "YouTube Trimmer MCP Server stopped." 