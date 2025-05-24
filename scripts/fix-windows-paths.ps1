# Windows Long Path Fix Script for Saturn Project
# This script provides solutions for Windows filename length limitations

Write-Host "Saturn Project - Windows Long Path Fix" -ForegroundColor Green
Write-Host "=======================================" -ForegroundColor Green

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

Write-Host "`nCurrent Status:" -ForegroundColor Yellow
Write-Host "- Running as Administrator: $isAdmin"
Write-Host "- Current Location: $PWD"

# Solution 1: Clean build directories
Write-Host "`n1. Cleaning build directories..." -ForegroundColor Cyan
if (Test-Path "build") {
    Write-Host "   Removing build/ directory..."
    Remove-Item -Recurse -Force "build" -ErrorAction SilentlyContinue
    Write-Host "   Build directory removed." -ForegroundColor Green
} else {
    Write-Host "   No build directory found." -ForegroundColor Green
}

if (Test-Path "dist") {
    Write-Host "   Removing dist/ directory..."
    Remove-Item -Recurse -Force "dist" -ErrorAction SilentlyContinue
    Write-Host "   Dist directory removed." -ForegroundColor Green
}

if (Test-Path "*.egg-info") {
    Write-Host "   Removing *.egg-info directories..."
    Get-ChildItem -Path "*.egg-info" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "   Egg-info directories removed." -ForegroundColor Green
}

# Solution 2: Enable long paths (requires admin)
Write-Host "`n2. Long Path Policy Check..." -ForegroundColor Cyan
try {
    $longPathEnabled = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -ErrorAction SilentlyContinue
    if ($longPathEnabled.LongPathsEnabled -eq 1) {
        Write-Host "   Long paths are already enabled on this system." -ForegroundColor Green
    } else {
        Write-Host "   Long paths are NOT enabled on this system." -ForegroundColor Yellow
        if ($isAdmin) {
            Write-Host "   Would you like to enable long paths? (y/n): " -NoNewline -ForegroundColor Yellow
            $response = Read-Host
            if ($response -eq 'y' -or $response -eq 'Y') {
                Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1
                Write-Host "   Long paths enabled! A restart may be required." -ForegroundColor Green
            }
        } else {
            Write-Host "   To enable long paths, run this script as Administrator." -ForegroundColor Yellow
        }
    }
} catch {
    Write-Host "   Could not check long path policy." -ForegroundColor Red
}

# Solution 3: Git configuration for long paths
Write-Host "`n3. Git Long Path Configuration..." -ForegroundColor Cyan
try {
    $gitLongPaths = git config --global core.longpaths 2>$null
    if ($gitLongPaths -eq "true") {
        Write-Host "   Git long paths already enabled." -ForegroundColor Green
    } else {
        Write-Host "   Enabling Git long paths..."
        git config --global core.longpaths true
        Write-Host "   Git long paths enabled." -ForegroundColor Green
    }
} catch {
    Write-Host "   Git not found or error configuring." -ForegroundColor Yellow
}

# Solution 4: Alternative build command
Write-Host "`n4. Recommended Build Process:" -ForegroundColor Cyan
Write-Host "   Use the following commands to build safely:" -ForegroundColor White
Write-Host "   pip install -e . --no-build-isolation" -ForegroundColor Gray
Write-Host "   OR" -ForegroundColor White
Write-Host "   python -m pip install -e ." -ForegroundColor Gray

Write-Host "`n5. If problems persist:" -ForegroundColor Cyan
Write-Host "   - The google-cloud-python directory has been excluded from builds" -ForegroundColor White
Write-Host "   - Use shorter working directory paths" -ForegroundColor White
Write-Host "   - Consider using WSL2 for development" -ForegroundColor White

Write-Host "`nScript completed!" -ForegroundColor Green 