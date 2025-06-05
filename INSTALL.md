# Installation Guide for YouTube Trimmer MCP

This guide covers all the ways to install and use YouTube Trimmer MCP, from the simplest one-command installation to development setups.

## 🚀 Quick Start (Recommended)

**The easiest way to get started:**

```bash
pip install youtube-trimmer-mcp
```

That's it! You now have:
- ✅ YouTube video downloading and trimming
- ✅ MCP server for natural language interaction
- ✅ Command-line tools
- ✅ All dependencies automatically installed

## 📋 Prerequisites

### Required
- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **FFmpeg** - Required for video processing

### Installing FFmpeg

#### macOS (using Homebrew)
```bash
brew install ffmpeg
```

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

#### Windows
1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract to a folder (e.g., `C:\ffmpeg`)
3. Add `C:\ffmpeg\bin` to your PATH environment variable

#### Verify FFmpeg Installation
```bash
ffmpeg -version
```

## 🎯 Installation Methods

### Method 1: PyPI (Recommended)
```bash
# Standard installation
pip install youtube-trimmer-mcp

# Verify installation
youtube-trimmer --help
youtube-trimmer-mcp --help
```

### Method 2: pipx (Isolated Installation)
Best for CLI tools to avoid dependency conflicts:

```bash
# Install pipx if you don't have it
pip install pipx

# Install youtube-trimmer-mcp in isolation
pipx install youtube-trimmer-mcp

# Verify installation
youtube-trimmer --help
```

### Method 3: Development Installation
For contributing or modifying the code:

```bash
# Clone the repository
git clone https://github.com/manuelgomez/youtube-trimmer-mcp.git
cd youtube-trimmer-mcp

# Install in development mode
pip install -e ".[dev]"

# Or if you want to contribute
pip install -e ".[all]"
```

### Method 4: Docker
For containerized environments:

```bash
# Build the Docker image
docker build -t youtube-trimmer-mcp .

# Run the MCP server
docker run -it --rm -v "$(pwd)/output:/app/output" youtube-trimmer-mcp
```

## 🔧 Usage After Installation

### Command Line Interface
```bash
# Trim a video
youtube-trimmer trim "https://youtube.com/watch?v=example" -s 1:00 -e 2:00

# Get video info
youtube-trimmer info "https://youtube.com/watch?v=example"

# Start MCP server
youtube-trimmer-mcp
```

### MCP Integration
Add to your MCP client config (e.g., Claude Desktop):

```json
{
  "mcpServers": {
    "youtube-trimmer": {
      "command": "youtube-trimmer-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

## 🚨 Troubleshooting

### Common Issues

#### 1. "FFmpeg not found"
**Solution:** Install FFmpeg and ensure it's in your PATH
```bash
# Test FFmpeg
ffmpeg -version

# If not found, reinstall FFmpeg (see Prerequisites section)
```

#### 2. "youtube-trimmer command not found"
**Solution:** Check if the installation directory is in your PATH
```bash
# Find where pip installed it
pip show youtube-trimmer-mcp

# Add to PATH if needed (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:$HOME/.local/bin"
```

#### 3. "Permission denied" on macOS/Linux
**Solution:** Use `--user` flag or virtual environment
```bash
# Install for current user only
pip install --user youtube-trimmer-mcp

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install youtube-trimmer-mcp
```

#### 4. "Module not found" errors
**Solution:** Ensure you're using the right Python environment
```bash
# Check Python version
python --version

# Check pip version
pip --version

# Make sure they match and are 3.8+
```

#### 5. MCP server doesn't start
**Solution:** Check dependencies and logs
```bash
# Test the MCP server directly
youtube-trimmer-mcp --help

# Check if MCP is properly installed
python -c "import mcp; print('MCP OK')"
```

### Getting Help

#### 1. Check Version
```bash
pip show youtube-trimmer-mcp
```

#### 2. Verify Installation
```bash
# Test basic functionality
youtube-trimmer info "https://www.youtube.com/watch?v=jNQXAC9IVRw"
```

#### 3. Enable Debug Mode
```bash
# Run with verbose output
youtube-trimmer trim "URL" -s 0:00 -e 0:05 --verbose
```

## 🔄 Updating

### Update from PyPI
```bash
pip install --upgrade youtube-trimmer-mcp
```

### Update with pipx
```bash
pipx upgrade youtube-trimmer-mcp
```

## 🗑️ Uninstalling

### Standard pip installation
```bash
pip uninstall youtube-trimmer-mcp
```

### pipx installation
```bash
pipx uninstall youtube-trimmer-mcp
```

## 🌟 Advanced Configuration

### Custom Output Directory
```bash
# Set default output directory
export YOUTUBE_TRIMMER_OUTPUT_DIR="/path/to/output"
```

### Custom FFmpeg Path
```bash
# If FFmpeg is in a non-standard location
export FFMPEG_BINARY="/path/to/ffmpeg"
```

### Virtual Environment Setup
For isolated installations:

```bash
# Create virtual environment
python -m venv youtube-trimmer-env

# Activate it
source youtube-trimmer-env/bin/activate  # Linux/macOS
# OR
youtube-trimmer-env\Scripts\activate     # Windows

# Install
pip install youtube-trimmer-mcp

# Use it
youtube-trimmer --help

# Deactivate when done
deactivate
```

## 📚 Next Steps

After installation:

1. **Try the CLI**: `youtube-trimmer trim "https://youtube.com/watch?v=example" -s 1:00 -e 2:00`
2. **Set up MCP**: Add to your MCP client configuration
3. **Read the docs**: Check the main README.md for detailed usage
4. **Join the community**: Report issues on GitHub

## 🆘 Still Having Issues?

1. **Check the [FAQ](https://github.com/manuelgomez/youtube-trimmer-mcp#faq)**
2. **Search [existing issues](https://github.com/manuelgomez/youtube-trimmer-mcp/issues)**
3. **Create a [new issue](https://github.com/manuelgomez/youtube-trimmer-mcp/issues/new)** with:
   - Your operating system
   - Python version (`python --version`)
   - Installation method used
   - Complete error message
   - Steps to reproduce 