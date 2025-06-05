# Release Checklist for YouTube Trimmer MCP

## 📋 Pre-Release Checklist

### 1. Code Quality
- [ ] All tests pass: `python -m pytest`
- [ ] Code formatted: `black src/`
- [ ] Imports sorted: `isort src/`
- [ ] Linting clean: `flake8 src/`
- [ ] Type checks pass: `mypy src/`

### 2. Documentation
- [ ] README.md updated with new features
- [ ] INSTALL.md covers all installation methods
- [ ] Version number updated in `pyproject.toml`
- [ ] Changelog updated (if exists)

### 3. Testing
- [ ] Manual testing of CLI commands
- [ ] MCP server starts correctly
- [ ] All MCP tools work as expected
- [ ] Test on clean environment

## 🚀 Release Process

### Option 1: Automated (GitHub Actions)

1. **Create a Git Tag**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. **Create GitHub Release**
   - Go to GitHub repository
   - Click "Releases" → "Create a new release"
   - Choose the tag you just created
   - Add release notes
   - Publish release
   - GitHub Actions will automatically publish to PyPI

### Option 2: Manual Release

1. **Clean and Build**
   ```bash
   python scripts/publish.py clean
   python scripts/publish.py build
   ```

2. **Test the Build**
   ```bash
   python scripts/publish.py check
   python scripts/publish.py test-install
   ```

3. **Publish to Test PyPI First**
   ```bash
   python scripts/publish.py publish-test
   
   # Test installation from Test PyPI
   pip install --index-url https://test.pypi.org/simple/ youtube-trimmer-mcp
   ```

4. **Publish to PyPI**
   ```bash
   python scripts/publish.py publish
   ```

## 🔧 Setup Required (One-time)

### 1. PyPI Account Setup
- Create account at [pypi.org](https://pypi.org)
- Enable 2FA
- Create API token in account settings

### 2. GitHub Actions Setup (for automated releases)
- Go to [PyPI Trusted Publishers](https://pypi.org/manage/account/publishing/)
- Add new pending publisher:
  - **Project name**: `youtube-trimmer-mcp`
  - **Owner**: `your-github-username`
  - **Repository name**: `youtube-trimmer-mcp`
  - **Workflow filename**: `publish-to-pypi.yml`

### 3. Local Development Setup
```bash
# Install development dependencies
pip install -e ".[dev]"

# Install build tools
pip install build twine

# Configure PyPI credentials (for manual publishing)
pip install keyring
```

## 📦 Post-Release Checklist

### 1. Verify Release
- [ ] Package appears on [PyPI](https://pypi.org/project/youtube-trimmer-mcp/)
- [ ] Installation works: `pip install youtube-trimmer-mcp`
- [ ] CLI commands work after fresh install
- [ ] MCP server starts correctly

### 2. Update Documentation
- [ ] Update version badges in README
- [ ] Create release announcement
- [ ] Update any external documentation

### 3. Announce
- [ ] Social media announcement
- [ ] Community forums (if applicable)
- [ ] Update project websites

## 🔄 Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Examples:
- `1.0.0` → `1.0.1`: Bug fix
- `1.0.0` → `1.1.0`: New feature  
- `1.0.0` → `2.0.0`: Breaking change

## 🚨 Emergency Procedures

### If Bad Release is Published:
1. **Yank the release** (makes it unavailable for new installs):
   ```bash
   twine upload --skip-existing dist/*
   # Or use PyPI web interface
   ```

2. **Publish fixed version immediately**:
   ```bash
   # Increment patch version
   # Fix the issue
   # Follow normal release process
   ```

## 📝 Release Notes Template

```markdown
## [1.0.0] - 2024-01-XX

### Added
- New MCP server functionality
- Enhanced CLI interface
- Docker support

### Changed
- Improved error handling
- Better installation process

### Fixed
- Bug in video trimming logic
- MCP protocol compatibility issues

### Security
- Updated dependencies for security fixes
```

## 📞 Getting Help

If you encounter issues during release:

1. Check the [GitHub Actions logs](https://github.com/your-username/youtube-trimmer-mcp/actions)
2. Verify PyPI credentials and permissions
3. Test locally first with the publish script
4. Check PyPI trusted publisher configuration

## 🎯 Success Metrics

After release, monitor:
- [ ] Download counts on PyPI
- [ ] GitHub issues for installation problems
- [ ] User feedback and adoption 