# Windows Long Path Fix Documentation

## Problem
Windows systems have a default path length limitation of 260 characters. The Saturn project contained a `google-cloud-python` repository in `internal/ast/` that had extremely long sample filenames, causing build failures with errors like:

```
error: unable to create file build/lib/internal/ast/google-cloud-python/packages/google-cloud-securitycentermanagement/samples/generated_samples/securitycentermanagement_v1_generated_security_center_management_get_effective_event_threat_detection_custom_module_async.py: Filename too long
```

## Solutions Implemented

### 1. Package Configuration Updates
Updated `pyproject.toml` to exclude the problematic directory:
```toml
[tool.setuptools.packages.find]
where = ["."]  
include = ["saturn*", "model*","internal*"] 
exclude = ["tests*", "venv*", "embeddings_env*", "internal.ast.google-cloud-python*", "internal/ast/google-cloud-python/*"]
```

### 2. Manifest File
Created `MANIFEST.in` to explicitly exclude the directory from package distribution:
```
include saturn/**/*.py
include model/**/*.py
include internal/**/*.py
include internal/tools/**/*
include internal/states/**/*
include internal/dag/**/*
include internal/assets/**/*
exclude internal/ast/google-cloud-python/**/*
recursive-exclude internal/ast/google-cloud-python *
prune internal/ast/google-cloud-python
```

### 3. Updated .gitignore
Added Python build artifacts to `.gitignore`:
```
# Python build artifacts
build/
dist/
*.egg-info/
__pycache__/
*.pyc
*.pyo
*.pyd
```

### 4. PowerShell Script
Created `scripts/fix-windows-paths.ps1` that:
- Cleans build directories
- Checks and optionally enables Windows long path support
- Configures Git for long paths
- Provides recommended build commands

## Recommended Build Process

Use one of these commands for safe building:
```powershell
# Option 1 (recommended)
pip install -e . --no-build-isolation

# Option 2
python -m pip install -e .
```

## Additional Solutions

### Enable Long Paths System-Wide (Optional)
If you have administrator rights and want to enable long paths system-wide:

1. Run PowerShell as Administrator
2. Execute: `scripts/fix-windows-paths.ps1`
3. Choose 'y' when prompted to enable long paths
4. Restart your computer

### Git Configuration
The script automatically configures Git to handle long paths:
```bash
git config --global core.longpaths true
```

## Alternative Workarounds

1. **Use WSL2**: Develop in Windows Subsystem for Linux 2 where path limits are not an issue
2. **Shorter Working Directory**: Use a shorter base path like `C:\saturn\` instead of `C:\Users\Username\Documents\Projects\saturn\`
3. **Junction/Symlinks**: Create Windows junctions to shorter paths

## Verification

After applying the fixes, verify:
1. Build succeeds: `pip install -e . --no-build-isolation`
2. Package imports: `python -c "import saturn; print('Success!')"`
3. No long path errors in build output
4. `build/lib/internal/ast/google-cloud-python/` directory should not exist

## Status: ✅ RESOLVED

The long filename issue has been resolved through package configuration exclusions and proper build procedures. 