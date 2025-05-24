#!/usr/bin/env python3
"""
Simple test script for Saturn's File Operations and Build Tooling System

This script tests basic functionality without requiring Docker or complex build tools.
"""

import asyncio
import shutil
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

# Import our new file build executor
from saturn.file_build_executor import FileBuildExecutor

async def test_basic_file_operations():
    """Test basic file operations without external dependencies."""
    
    console = Console()
    console.print(Panel.fit(
        "[bold cyan]Testing Basic File Operations[/bold cyan]\n"
        "Testing read, write, list, copy, and template operations",
        title="🧪 File Operations Test"
    ))
    
    config = {
        'working_directory': 'test_workspace'
    }
    
    executor = FileBuildExecutor(config)
    
    # Create test workspace
    Path('test_workspace').mkdir(exist_ok=True)
    
    success_count = 0
    total_tests = 0
    
    # Test 1: Write JSON file
    console.print("\n[bold]Test 1: Writing JSON file[/bold]")
    total_tests += 1
    
    success, result = await executor.execute(
        "write_file",
        {
            "file_path": "config.json",
            "content": {
                "name": "Saturn Test",
                "version": "1.0.0",
                "debug": True
            }
        },
        console,
        "test_write_json"
    )
    
    if success:
        success_count += 1
        console.print("[green]✓ JSON write test passed[/green]")
    else:
        console.print("[red]✗ JSON write test failed[/red]")
    
    # Test 2: Read JSON file
    console.print("\n[bold]Test 2: Reading JSON file[/bold]")
    total_tests += 1
    
    success, result = await executor.execute(
        "read_file",
        {"file_path": "config.json"},
        console,
        "test_read_json"
    )
    
    if success and isinstance(result.get('content'), dict):
        success_count += 1
        console.print("[green]✓ JSON read test passed[/green]")
        console.print(f"[dim]Content: {result['content']}[/dim]")
    else:
        console.print("[red]✗ JSON read test failed[/red]")
    
    # Test 3: Write YAML file
    console.print("\n[bold]Test 3: Writing YAML file[/bold]")
    total_tests += 1
    
    success, result = await executor.execute(
        "write_file",
        {
            "file_path": "settings.yaml",
            "content": {
                "database": {
                    "host": "localhost",
                    "port": 5432
                },
                "cache": {
                    "enabled": True,
                    "ttl": 3600
                }
            }
        },
        console,
        "test_write_yaml"
    )
    
    if success:
        success_count += 1
        console.print("[green]✓ YAML write test passed[/green]")
    else:
        console.print("[red]✗ YAML write test failed[/red]")
    
    # Test 4: List files
    console.print("\n[bold]Test 4: Listing files[/bold]")
    total_tests += 1
    
    success, result = await executor.execute(
        "list_files",
        {"directory": ".", "pattern": "*.json"},
        console,
        "test_list_files"
    )
    
    if success and result.get('count', 0) > 0:
        success_count += 1
        console.print("[green]✓ File listing test passed[/green]")
    else:
        console.print("[red]✗ File listing test failed[/red]")
    
    # Test 5: Copy file
    console.print("\n[bold]Test 5: Copying file[/bold]")
    total_tests += 1
    
    success, result = await executor.execute(
        "copy_file",
        {"source": "config.json", "destination": "config_backup.json"},
        console,
        "test_copy_file"
    )
    
    if success:
        success_count += 1
        console.print("[green]✓ File copy test passed[/green]")
    else:
        console.print("[red]✗ File copy test failed[/red]")
    
    # Test 6: Template processing
    console.print("\n[bold]Test 6: Template processing[/bold]")
    total_tests += 1
    
    # Create template
    template_content = "Hello {{name}}! Version: {{version}}"
    
    await executor.execute(
        "write_file",
        {"file_path": "greeting.template", "content": template_content},
        console,
        "create_template"
    )
    
    success, result = await executor.execute(
        "template_file",
        {
            "template_path": "greeting.template",
            "output_path": "greeting.txt",
            "variables": {
                "name": "Saturn",
                "version": "2.0.0"
            }
        },
        console,
        "test_template"
    )
    
    if success:
        success_count += 1
        console.print("[green]✓ Template processing test passed[/green]")
    else:
        console.print("[red]✗ Template processing test failed[/red]")
    
    # Test 7: Project detection
    console.print("\n[bold]Test 7: Project type detection[/bold]")
    total_tests += 1
    
    # Create a requirements.txt to make it look like a Python project
    await executor.execute(
        "write_file",
        {"file_path": "requirements.txt", "content": "requests==2.31.0\nfastapi==0.104.1"},
        console,
        "create_requirements"
    )
    
    success, result = await executor.execute(
        "detect_project",
        {},
        console,
        "test_detect_project"
    )
    
    if success and result.get('primary_type') != 'unknown':
        success_count += 1
        console.print("[green]✓ Project detection test passed[/green]")
        console.print(f"[dim]Detected: {result.get('primary_type')}[/dim]")
    else:
        console.print("[red]✗ Project detection test failed[/red]")
    
    # Test 8: Dockerfile generation
    console.print("\n[bold]Test 8: Dockerfile generation[/bold]")
    total_tests += 1
    
    success, result = await executor.execute(
        "generate_dockerfile",
        {
            "base_image": "python:3.11-slim",
            "dependencies_file": "requirements.txt",
            "output_path": "Dockerfile"
        },
        console,
        "test_dockerfile_gen"
    )
    
    if success:
        success_count += 1
        console.print("[green]✓ Dockerfile generation test passed[/green]")
    else:
        console.print("[red]✗ Dockerfile generation test failed[/red]")
    
    # Test Summary
    console.print(f"\n[bold]Test Results: {success_count}/{total_tests} tests passed[/bold]")
    
    if success_count == total_tests:
        console.print(Panel.fit(
            "[bold green]🎉 All tests passed![/bold green]\n"
            "The file build tooling system is working correctly.",
            title="✅ Success"
        ))
    else:
        console.print(Panel.fit(
            f"[bold yellow]⚠️ {total_tests - success_count} tests failed[/bold yellow]\n"
            "Some functionality may not be working correctly.",
            title="⚠️ Warning"
        ))
    
    return success_count == total_tests

async def test_supported_operations():
    """Test that all operations are properly registered."""
    
    console = Console()
    console.print(Panel.fit(
        "[bold blue]Testing Supported Operations[/bold blue]\n"
        "Verifying all operations are available",
        title="📋 Operations Test"
    ))
    
    config = {'working_directory': 'test_workspace'}
    executor = FileBuildExecutor(config)
    
    operations = executor.get_supported_operations()
    console.print(f"\n[bold]Supported Operations ({len(operations)}):[/bold]")
    
    for op in operations:
        schema = executor.get_operation_schema(op)
        console.print(f"• [cyan]{op}[/cyan] - {schema.get('description', 'No description')}")
    
    console.print(f"\n[green]✓ Found {len(operations)} supported operations[/green]")
    
    return len(operations) > 0

async def main():
    """Run all tests."""
    
    console = Console()
    console.print(Panel.fit(
        "[bold white]🧪 Saturn File Build Tooling Tests[/bold white]\n\n"
        "Running comprehensive tests for the file operations and build tooling system.",
        title="Test Suite"
    ))
    
    try:
        # Run tests
        file_ops_success = await test_basic_file_operations()
        operations_success = await test_supported_operations()
        
        # Overall result
        if file_ops_success and operations_success:
            console.print(Panel.fit(
                "[bold green]🎉 All tests completed successfully![/bold green]\n"
                "The Saturn File Build Tooling system is ready for use.",
                title="🏆 Test Suite Complete"
            ))
        else:
            console.print(Panel.fit(
                "[bold red]❌ Some tests failed[/bold red]\n"
                "Please check the error messages above.",
                title="💥 Test Failures"
            ))
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Tests interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"\n[red]Test error: {str(e)}[/red]")
        import traceback
        traceback.print_exc()
    finally:
        # Cleanup
        if Path('test_workspace').exists():
            console.print("\n[dim]Cleaning up test workspace...[/dim]")
            shutil.rmtree('test_workspace', ignore_errors=True)

if __name__ == "__main__":
    asyncio.run(main()) 