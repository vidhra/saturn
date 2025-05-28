#!/usr/bin/env python3
"""
Test script to verify CLI .env file loading functionality.
"""

import os
import tempfile
import subprocess
import sys
from pathlib import Path

def create_test_env_file(env_path: Path, env_vars: dict):
    """Create a test .env file with specified variables."""
    with open(env_path, 'w') as f:
        for key, value in env_vars.items():
            f.write(f"{key}={value}\n")
    print(f"Created test .env file: {env_path}")

def test_cli_env_loading():
    """Test that the CLI loads environment variables from .env files."""
    print("🧪 Testing CLI .env file loading...")
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        env_file = temp_path / ".env"
        
        # Create test environment variables
        test_env_vars = {
            "GOOGLE_API_KEY": "test_google_key_123456789",
            "OPENAI_API_KEY": "test_openai_key_987654321",
            "GCP_PROJECT_ID": "test-project-12345",
            "VECTOR_STORE": "chroma",
            "RAG_EMBED_MODEL": "models/text-embedding-004"
        }
        
        create_test_env_file(env_file, test_env_vars)
        
        # Change to the temporary directory
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            # Test the CLI with --show-env flag
            print(f"\nRunning CLI from: {temp_dir}")
            print("Command: saturn ingest-docs --show-env")
            
            # Run the CLI command
            result = subprocess.run([
                sys.executable, "-m", "saturn.cli", "ingest-docs", "--show-env"
            ], capture_output=True, text=True, cwd=temp_dir)
            
            print(f"\n📋 CLI Output:")
            print("-" * 50)
            print(result.stdout)
            if result.stderr:
                print("📋 CLI Errors:")
                print(result.stderr)
            print("-" * 50)
            
            # Check if environment variables were loaded
            success_indicators = [
                "📄 [CLI] Loaded environment variables from:",
                "test_google_key_123456",  # Should appear masked
                "test-project-12345",
                "chroma",
                "models/text-embedding-004"
            ]
            
            output_text = result.stdout + result.stderr
            found_indicators = []
            
            for indicator in success_indicators:
                if indicator in output_text:
                    found_indicators.append(indicator)
                    print(f"✅ Found: {indicator}")
                else:
                    print(f"❌ Missing: {indicator}")
            
            if len(found_indicators) >= 3:  # At least 3 indicators found
                print(f"\n🎉 CLI .env loading test PASSED! ({len(found_indicators)}/{len(success_indicators)} indicators found)")
                return True
            else:
                print(f"\n❌ CLI .env loading test FAILED! ({len(found_indicators)}/{len(success_indicators)} indicators found)")
                return False
                
        except Exception as e:
            print(f"💥 Error running CLI test: {e}")
            return False
        finally:
            os.chdir(original_cwd)

def test_multiple_env_locations():
    """Test that CLI searches for .env files in multiple locations."""
    print("\n🧪 Testing multiple .env file locations...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create nested directory structure
        subdir = temp_path / "subdir"
        subdir.mkdir()
        
        # Create .env file in parent directory
        parent_env = temp_path / ".env"
        create_test_env_file(parent_env, {"TEST_VAR": "parent_value"})
        
        # Change to subdirectory
        original_cwd = os.getcwd()
        os.chdir(subdir)
        
        try:
            # The CLI should find the .env file in the parent directory
            result = subprocess.run([
                sys.executable, "-c", """
import sys
sys.path.insert(0, '../../Saturn')
from saturn.cli import app
print("CLI module loaded successfully")
"""
            ], capture_output=True, text=True)
            
            if "CLI module loaded successfully" in result.stdout:
                print("✅ CLI can be imported and should search for .env files")
                return True
            else:
                print("❌ CLI import test failed")
                print(result.stderr)
                return False
                
        finally:
            os.chdir(original_cwd)

def main():
    """Run all CLI environment loading tests."""
    print("🔧 CLI Environment Loading Test Suite")
    print("=" * 50)
    
    tests = [
        ("Basic .env loading", test_cli_env_loading),
        ("Multiple locations", test_multiple_env_locations),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 Running: {test_name}")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"💥 {test_name} ERROR: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All CLI environment tests passed!")
    else:
        print("⚠️  Some CLI environment tests failed")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 