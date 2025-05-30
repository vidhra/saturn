#!/bin/bash
# install-hooks.sh
# Script to install git hooks for the Saturn project

echo "Installing git hooks for Saturn project..."

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "Error: Not in a git repository root directory."
    echo "Please run this script from the root of your git repository."
    exit 1
fi

# Create .git/hooks directory if it doesn't exist
mkdir -p .git/hooks

# Copy and install pre-commit hook
if [ -f "githooks/pre-commit" ]; then
    cp githooks/pre-commit .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    echo "✓ Pre-commit hook installed"
else
    echo "⚠ Warning: githooks/pre-commit not found"
fi

# Copy and install pre-push hook
if [ -f "githooks/pre-push" ]; then
    cp githooks/pre-push .git/hooks/pre-push
    chmod +x .git/hooks/pre-push
    echo "✓ Pre-push hook installed"
else
    echo "⚠ Warning: githooks/pre-push not found"
fi

echo ""
echo "Git hooks installation complete!"
echo ""
echo "The following hooks are now active:"
echo "  • pre-commit: Runs linting, formatting, and basic checks before each commit"
echo "  • pre-push: Runs comprehensive tests and checks before pushing to remote"
echo ""
echo "Recommended development dependencies to install:"
echo "  pip install black isort flake8 ruff bandit mypy safety pytest"
echo ""
echo "To bypass hooks (not recommended):"
echo "  git commit --no-verify"
echo "  git push --no-verify"
echo ""
echo "To uninstall hooks:"
echo "  rm .git/hooks/pre-commit .git/hooks/pre-push" 