#!/usr/bin/env python3
"""
Comprehensive test runner for all Saturn test suites.
Runs LLM integration tests, RAG engine tests, and CLI tests.
"""

import asyncio
import sys
import os
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Tuple
import time

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    
    # Look for .env file in current directory and parent directories
    env_file_paths = [
        Path(".env"),
        Path("../.env"),
        Path("../../.env"),
        Path.cwd() / ".env",
        Path.cwd().parent / ".env",
        Path.cwd().parent.parent / ".env"
    ]
    
    env_loaded = False
    for env_path in env_file_paths:
        if env_path.exists():
            load_dotenv(env_path)
            print(f"📄 [Test Runner] Loaded environment variables from: {env_path.absolute()}")
            env_loaded = True
            break
    
    if not env_loaded:
        print("⚠️  [Test Runner] No .env file found. Using system environment variables only.")
        
except ImportError:
    print("⚠️  [Test Runner] python-dotenv not installed. Using system environment variables only.")

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, TaskID

console = Console()

class TestRunner:
    """Comprehensive test runner for all Saturn components."""
    
    def __init__(self):
        self.test_results: Dict[str, Dict[str, Any]] = {}
        self.start_time = time.time()
        
    def print_header(self):
        """Print test runner header."""
        console.print(Panel(
            "[bold cyan]Saturn Comprehensive Test Suite[/bold cyan]\n"
            "Testing LLM integrations, RAG engine, and CLI functionality",
            title="🧪 Test Runner",
            border_style="cyan"
        ))
    
    def print_env_summary(self):
        """Print environment variable summary."""
        console.print("\n🔧 Environment Summary:")
        console.print("-" * 50)
        
        important_vars = [
            "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GEMINI_API_KEY", 
            "MISTRAL_API_KEY", "GOOGLE_API_KEY", "GCP_PROJECT_ID"
        ]
        
        available = 0
        for var in important_vars:
            value = os.getenv(var)
            if value:
                available += 1
                masked = f"{value[:4]}...{value[-4:]}" if len(value) > 8 else "***"
                console.print(f"✅ {var}: {masked}")
            else:
                console.print(f"❌ {var}: Not set")
        
        console.print(f"\n📊 {available}/{len(important_vars)} API keys available")
        console.print("-" * 50)
    
    async def run_llm_integration_tests(self) -> Dict[str, Any]:
        """Run LLM integration tests."""
        console.print("\n🤖 Running LLM Integration Tests...")
        
        try:
            # Import and run the LLM test
            from test_llm_integrations import main as llm_test_main
            
            start_time = time.time()
            await llm_test_main()
            duration = time.time() - start_time
            
            return {
                "status": "completed",
                "duration": duration,
                "details": "LLM integration tests completed"
            }
        except ImportError as e:
            return {
                "status": "error",
                "duration": 0,
                "details": f"Could not import LLM tests: {e}"
            }
        except Exception as e:
            return {
                "status": "error",
                "duration": 0,
                "details": f"LLM test error: {e}"
            }
    
    async def run_rag_engine_tests(self) -> Dict[str, Any]:
        """Run RAG engine tests."""
        console.print("\n📚 Running RAG Engine Tests...")
        
        try:
            # Import and run the RAG test
            from test_rag_engine import main as rag_test_main
            
            start_time = time.time()
            await rag_test_main()
            duration = time.time() - start_time
            
            return {
                "status": "completed",
                "duration": duration,
                "details": "RAG engine tests completed"
            }
        except ImportError as e:
            return {
                "status": "error",
                "duration": 0,
                "details": f"Could not import RAG tests: {e}"
            }
        except Exception as e:
            return {
                "status": "error",
                "duration": 0,
                "details": f"RAG test error: {e}"
            }
    
    def run_cli_env_tests(self) -> Dict[str, Any]:
        """Run CLI environment loading tests."""
        console.print("\n⚙️  Running CLI Environment Tests...")
        
        try:
            # Run CLI test as subprocess to avoid import conflicts
            result = subprocess.run([
                sys.executable, "test_cli_env_loading.py"
            ], capture_output=True, text=True, cwd=Path(__file__).parent)
            
            if result.returncode == 0:
                return {
                    "status": "passed",
                    "duration": 0,  # CLI tests are quick
                    "details": "CLI environment loading tests passed"
                }
            else:
                return {
                    "status": "failed",
                    "duration": 0,
                    "details": f"CLI tests failed: {result.stderr}"
                }
        except Exception as e:
            return {
                "status": "error",
                "duration": 0,
                "details": f"CLI test error: {e}"
            }
    
    def run_dependency_check(self) -> Dict[str, Any]:
        """Check that all required dependencies are installed."""
        console.print("\n📦 Checking Dependencies...")
        
        required_packages = [
            "openai", "anthropic", "mistralai", "google-generativeai",
            "llama-index", "chromadb", "duckdb", "rich", "typer", "pydantic"
        ]
        
        missing = []
        installed = []
        
        for package in required_packages:
            try:
                __import__(package.replace("-", "_"))
                installed.append(package)
            except ImportError:
                missing.append(package)
        
        if missing:
            return {
                "status": "failed",
                "duration": 0,
                "details": f"Missing packages: {', '.join(missing)}"
            }
        else:
            return {
                "status": "passed",
                "duration": 0,
                "details": f"All {len(installed)} required packages installed"
            }
    
    def run_quick_import_test(self) -> Dict[str, Any]:
        """Test that main Saturn modules can be imported."""
        console.print("\n🔍 Testing Module Imports...")
        
        modules_to_test = [
            "saturn.cli",
            "saturn.config", 
            "saturn.rag_engine",
            "model.llm.openai_llm",
            "model.llm.claude_llm",
            "model.llm.gemini_llm",
            "model.llm.mistral_llm"
        ]
        
        failed_imports = []
        successful_imports = []
        
        for module in modules_to_test:
            try:
                __import__(module)
                successful_imports.append(module)
            except ImportError as e:
                failed_imports.append(f"{module}: {str(e)}")
        
        if failed_imports:
            return {
                "status": "failed",
                "duration": 0,
                "details": f"Failed imports: {'; '.join(failed_imports)}"
            }
        else:
            return {
                "status": "passed",
                "duration": 0,
                "details": f"Successfully imported {len(successful_imports)} modules"
            }
    
    async def run_all_tests(self, skip_long_tests: bool = False):
        """Run all test suites."""
        console.print("\n🚀 Starting Comprehensive Test Suite...")
        
        # Quick tests first
        self.test_results["dependencies"] = self.run_dependency_check()
        self.test_results["imports"] = self.run_quick_import_test()
        
        # CLI tests (quick)
        self.test_results["cli_env"] = self.run_cli_env_tests()
        
        if not skip_long_tests:
            # Longer integration tests
            self.test_results["llm_integration"] = await self.run_llm_integration_tests()
            self.test_results["rag_engine"] = await self.run_rag_engine_tests()
        else:
            console.print("\n⏭️ Skipping long-running tests (use --full for complete suite)")
    
    def print_summary(self):
        """Print comprehensive test results summary."""
        console.print("\n📊 Test Results Summary")
        console.print("=" * 60)
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Test Suite", style="cyan", no_wrap=True)
        table.add_column("Status", style="bold")
        table.add_column("Duration", style="dim")
        table.add_column("Details")
        
        total_duration = 0
        passed_count = 0
        failed_count = 0
        
        for test_name, result in self.test_results.items():
            status = result.get("status", "unknown")
            duration = result.get("duration", 0)
            details = result.get("details", "No details")
            
            total_duration += duration
            
            if status in ["passed", "completed"]:
                status_display = "[green]✅ PASSED[/green]"
                passed_count += 1
            elif status == "failed":
                status_display = "[red]❌ FAILED[/red]"
                failed_count += 1
            elif status == "error":
                status_display = "[red]💥 ERROR[/red]"
                failed_count += 1
            else:
                status_display = "[yellow]❓ UNKNOWN[/yellow]"
            
            duration_display = f"{duration:.1f}s" if duration > 0 else "< 1s"
            
            table.add_row(
                test_name.replace("_", " ").title(),
                status_display,
                duration_display,
                details[:80] + "..." if len(details) > 80 else details
            )
        
        console.print(table)
        
        # Summary stats
        total_tests = len(self.test_results)
        total_time = time.time() - self.start_time
        
        console.print(f"\n📈 Overall Results:")
        console.print(f"   Tests: {passed_count} passed, {failed_count} failed ({total_tests} total)")
        console.print(f"   Time: {total_time:.1f}s total runtime")
        
        if failed_count == 0:
            console.print("[bold green]🎉 All tests passed![/bold green]")
        elif passed_count > failed_count:
            console.print("[yellow]⚠️  Most tests passed, some issues found[/yellow]")
        else:
            console.print("[bold red]❌ Multiple test failures detected[/bold red]")
        
        return failed_count == 0

async def main():
    """Main test runner function."""
    # Parse command line arguments
    skip_long_tests = "--quick" in sys.argv
    full_tests = "--full" in sys.argv
    
    runner = TestRunner()
    runner.print_header()
    runner.print_env_summary()
    
    try:
        await runner.run_all_tests(skip_long_tests=skip_long_tests and not full_tests)
        success = runner.print_summary()
        
        if success:
            console.print("\n✅ All tests completed successfully!")
            return 0
        else:
            console.print("\n❌ Some tests failed. Check details above.")
            return 1
            
    except KeyboardInterrupt:
        console.print("\n⚠️  Tests interrupted by user")
        return 130
    except Exception as e:
        console.print(f"\n💥 Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    # Usage examples
    if "--help" in sys.argv or "-h" in sys.argv:
        console.print("""
🧪 Saturn Test Runner

Usage:
  python run_all_tests.py           # Run quick tests only
  python run_all_tests.py --full    # Run all tests including LLM/RAG
  python run_all_tests.py --quick   # Same as default, run quick tests only
  python run_all_tests.py --help    # Show this help

Test Suites:
  - Dependencies: Check required packages
  - Imports: Test module imports  
  - CLI Environment: Test .env loading
  - LLM Integration: Test all LLM providers (--full only)
  - RAG Engine: Test vector stores and embeddings (--full only)
""")
        sys.exit(0)
    
    exit_code = asyncio.run(main())
    sys.exit(exit_code) 