#!/usr/bin/env python3
"""
Publishing helper script for YouTube Trimmer MCP.

This script helps with building, testing, and publishing the package to PyPI.
"""
import argparse
import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    return subprocess.run(cmd, check=check)


def clean():
    """Clean build artifacts."""
    print("🧹 Cleaning build artifacts...")
    
    artifacts = [
        "dist/",
        "build/", 
        "*.egg-info/",
        "src/*.egg-info/",
        "__pycache__/",
        "**/__pycache__/",
        "*.pyc",
        "*.pyo",
    ]
    
    import shutil
    import glob
    
    for pattern in artifacts:
        for path in glob.glob(pattern, recursive=True):
            path_obj = Path(path)
            if path_obj.exists():
                if path_obj.is_dir():
                    shutil.rmtree(path_obj)
                    print(f"Removed directory: {path_obj}")
                else:
                    path_obj.unlink()
                    print(f"Removed file: {path_obj}")


def build():
    """Build the package."""
    print("🔨 Building package...")
    run_command([sys.executable, "-m", "build"])


def check():
    """Check the built package."""
    print("🔍 Checking package...")
    run_command([sys.executable, "-m", "twine", "check", "dist/*"])


def test_install():
    """Test installation in a clean virtual environment."""
    print("🧪 Testing installation...")
    
    # Create test virtual environment
    run_command([sys.executable, "-m", "venv", ".test-env"])
    
    # Activate and install
    if sys.platform == "win32":
        pip_path = ".test-env/Scripts/pip"
        python_path = ".test-env/Scripts/python"
    else:
        pip_path = ".test-env/bin/pip"
        python_path = ".test-env/bin/python"
    
    # Install the built package
    dist_files = list(Path("dist").glob("*.whl"))
    if not dist_files:
        print("❌ No wheel file found. Run build first.")
        return False
        
    latest_wheel = max(dist_files, key=lambda p: p.stat().st_mtime)
    
    run_command([pip_path, "install", str(latest_wheel)])
    
    # Test the installation
    result = run_command([python_path, "-c", 
                         "import youtube_trimmer; print('✅ Import successful')"], 
                        check=False)
    
    # Test CLI
    result2 = run_command([python_path, "-m", "youtube_trimmer.cli", "--help"], 
                         check=False)
    
    # Cleanup
    import shutil
    shutil.rmtree(".test-env")
    
    if result.returncode == 0 and result2.returncode == 0:
        print("✅ Installation test passed!")
        return True
    else:
        print("❌ Installation test failed!")
        return False


def publish_test():
    """Publish to Test PyPI."""
    print("📤 Publishing to Test PyPI...")
    run_command([
        sys.executable, "-m", "twine", "upload", 
        "--repository", "testpypi", 
        "dist/*"
    ])


def publish():
    """Publish to PyPI."""
    print("📤 Publishing to PyPI...")
    
    # Confirm publication
    response = input("Are you sure you want to publish to PyPI? (yes/no): ")
    if response.lower() != "yes":
        print("❌ Publication cancelled.")
        return
        
    run_command([sys.executable, "-m", "twine", "upload", "dist/*"])
    print("✅ Successfully published to PyPI!")


def main():
    parser = argparse.ArgumentParser(description="YouTube Trimmer MCP publishing helper")
    parser.add_argument("action", choices=[
        "clean", "build", "check", "test-install", 
        "publish-test", "publish", "all"
    ], help="Action to perform")
    
    args = parser.parse_args()
    
    if args.action == "clean":
        clean()
    elif args.action == "build":
        build()
    elif args.action == "check":
        check()
    elif args.action == "test-install":
        test_install()
    elif args.action == "publish-test":
        publish_test()
    elif args.action == "publish":
        publish()
    elif args.action == "all":
        print("🚀 Running full build and check pipeline...")
        clean()
        build()
        check()
        if test_install():
            print("\n✅ All checks passed! Ready for publishing.")
            print("Run 'python scripts/publish.py publish-test' to test on TestPyPI")
            print("Run 'python scripts/publish.py publish' to publish to PyPI")
        else:
            print("\n❌ Tests failed. Please fix issues before publishing.")
            sys.exit(1)


if __name__ == "__main__":
    main() 