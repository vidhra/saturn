# Git Hooks for Saturn Project

This directory contains git hooks that help maintain code quality and prevent issues before they reach the repository.

## Available Hooks

### Pre-commit Hook (`pre-commit`)

Runs automatically before each commit and performs the following checks:

- **Python syntax validation**: Ensures all Python files compile correctly
- **Code formatting**: Uses Black formatter to maintain consistent code style
- **Import sorting**: Uses isort to organize imports
- **Linting**: Runs flake8 and/or ruff to catch code quality issues
- **Security checks**: Uses bandit to identify potential security vulnerabilities
- **Type checking**: Runs mypy if configuration is present
- **Test validation**: Validates test file syntax if test files are being committed
- **Common issue detection**: Checks for debugging statements, large files, etc.

### Pre-push Hook (`pre-push`)

Runs automatically before pushing to a remote repository and performs comprehensive checks:

- **Full test suite**: Runs all tests using pytest or unittest
- **Comprehensive linting**: Checks entire codebase for code quality issues
- **Security scanning**: Deep security analysis with bandit
- **Dependency checks**: Validates dependencies and checks for vulnerabilities
- **Code quality analysis**: Detects anti-patterns and performance issues
- **Documentation validation**: Ensures proper documentation is present
- **Configuration validation**: Validates YAML and JSON configuration files
- **Environment compatibility**: Checks Python version compatibility

## Installation

### Option 1: Automatic Installation

Run the installation script from the project root:

```bash
./githooks/install-hooks.sh
```

### Option 2: Manual Installation

```bash
# From the project root directory
cp githooks/pre-commit .git/hooks/pre-commit
cp githooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-commit .git/hooks/pre-push
```

## Required Dependencies

For optimal functionality, install these development dependencies:

```bash
# Essential tools
pip install black isort flake8 pytest

# Additional recommended tools
pip install ruff bandit mypy safety

# Alternative: Install all at once
pip install black isort flake8 ruff bandit mypy safety pytest
```

## Configuration

### Customizing Checks

You can customize the behavior by:

1. **Modifying the hook files**: Edit `githooks/pre-commit` or `githooks/pre-push`
2. **Adding configuration files**: Create `.flake8`, `pyproject.toml` sections, etc.
3. **Environment variables**: Some checks respect environment variables

### Tool-specific Configuration

#### Black (Code Formatting)
Create a `pyproject.toml` section:
```toml
[tool.black]
line-length = 88
target-version = ['py39']
```

#### isort (Import Sorting)
Add to `pyproject.toml`:
```toml
[tool.isort]
profile = "black"
multi_line_output = 3
```

#### flake8 (Linting)
Create a `.flake8` file:
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

#### Ruff (Fast Linter)
Add to `pyproject.toml`:
```toml
[tool.ruff]
line-length = 88
target-version = "py39"
```

## Usage

### Normal Workflow

Once installed, the hooks run automatically:

```bash
# Pre-commit hook runs automatically
git commit -m "Your commit message"

# Pre-push hook runs automatically
git push origin main
```

### Bypassing Hooks

**Not recommended**, but you can bypass hooks when necessary:

```bash
# Bypass pre-commit hook
git commit --no-verify -m "Emergency fix"

# Bypass pre-push hook
git push --no-verify origin main
```

### Running Hooks Manually

You can run the hooks manually for testing:

```bash
# Test pre-commit hook
.git/hooks/pre-commit

# Test pre-push hook (requires git push context)
echo "refs/heads/main $(git rev-parse HEAD) refs/heads/main 0000000000000000000000000000000000000000" | .git/hooks/pre-push origin https://github.com/your/repo.git
```

## Troubleshooting

### Common Issues

1. **"Permission denied"**: Make sure hook files are executable
   ```bash
   chmod +x .git/hooks/pre-commit .git/hooks/pre-push
   ```

2. **"Command not found"**: Install missing dependencies
   ```bash
   pip install black flake8 pytest  # etc.
   ```

3. **Hooks not running**: Ensure you're in the git repository root and hooks are installed

### Disabling Specific Checks

To temporarily disable specific checks, you can:

1. Comment out sections in the hook files
2. Set environment variables (if supported)
3. Use tool-specific ignore patterns

### Performance Issues

If hooks are too slow:

1. Limit the scope of checks in pre-commit to only changed files
2. Move comprehensive checks to pre-push only
3. Use faster alternatives (e.g., ruff instead of flake8)

## Best Practices

1. **Install dependencies early**: Set up the development environment with all tools
2. **Keep hooks fast**: Pre-commit should complete in seconds, not minutes
3. **Provide feedback**: Ensure hooks give clear, actionable error messages
4. **Test changes**: Test hook modifications on a sample commit/push
5. **Document exceptions**: If bypassing hooks, document why in the commit message

## Uninstalling

To remove the hooks:

```bash
rm .git/hooks/pre-commit .git/hooks/pre-push
```

## Contributing

When modifying hooks:

1. Test thoroughly with various scenarios
2. Ensure backwards compatibility
3. Update this documentation
4. Consider performance impact
5. Provide clear error messages 