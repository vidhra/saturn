# Test suite for File Build Tools LLM interface
import asyncio
import json
import tempfile
import os
from pathlib import Path
from saturn.file_build_tools import (
    FileBuildToolCaller, 
    FileBuildToolHandler, 
    create_file_build_tools_for_llm
)
from rich.console import Console
import pytest

@pytest.mark.asyncio
async def test_file_build_tools():
    """Comprehensive test of file build tools for LLM integration."""
    
    console = Console()
    console.print("[bold blue]Testing File Build Tools for LLM Integration[/bold blue]\n")
    
    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        console.print(f"Using temporary directory: {temp_dir}")
        
        # Initialize tools interface
        tools_interface = create_file_build_tools_for_llm(temp_dir)
        handler = tools_interface["handler"]
        
        # Test 1: Get tools schema
        console.print("\n[cyan]Test 1: Tools Schema Generation[/cyan]")
        tools_schema = tools_interface["tools_schema"]
        console.print(f"✓ Generated schema for {len(tools_schema)} tools")
        
        # Verify each tool has required fields
        for tool in tools_schema:
            assert "type" in tool
            assert "function" in tool
            assert "name" in tool["function"]
            assert "description" in tool["function"]
            assert "parameters" in tool["function"]
        
        console.print("✓ All tools have valid schema structure")
        
        # Test 2: Project type detection
        console.print("\n[cyan]Test 2: Project Type Detection[/cyan]")
        detect_call = {
            "type": "function",
            "function": {
                "name": "detect_project_type",
                "arguments": {}
            }
        }
        
        result = await handler.handle_tool_call(detect_call)
        assert result["success"], f"Project detection failed: {result.get('error')}"
        console.print("✓ Project type detection successful")
        
        # Test 3: Write and read files
        console.print("\n[cyan]Test 3: File Operations[/cyan]")
        
        # Write a test file
        test_content = {"name": "Saturn", "version": "1.0", "type": "file_build_test"}
        write_call = {
            "type": "function",
            "function": {
                "name": "write_file",
                "arguments": {
                    "file_path": "test_config.json",
                    "content": test_content,
                    "format": ".json"
                }
            }
        }
        
        result = await handler.handle_tool_call(write_call)
        assert result["success"], f"File write failed: {result.get('error')}"
        console.print("✓ File write successful")
        
        # Read the file back
        read_call = {
            "type": "function",
            "function": {
                "name": "read_file",
                "arguments": {
                    "file_path": "test_config.json"
                }
            }
        }
        
        result = await handler.handle_tool_call(read_call)
        assert result["success"], f"File read failed: {result.get('error')}"
        assert result["result"]["content"] == test_content
        console.print("✓ File read successful and content matches")
        
        # Test 4: List files
        console.print("\n[cyan]Test 4: File Listing[/cyan]")
        list_call = {
            "type": "function",
            "function": {
                "name": "list_files",
                "arguments": {
                    "pattern": "*.json",
                    "recursive": False
                }
            }
        }
        
        result = await handler.handle_tool_call(list_call)
        assert result["success"], f"File listing failed: {result.get('error')}"
        assert len(result["result"]["files"]) > 0
        console.print("✓ File listing successful")
        
        # Test 5: Template processing
        console.print("\n[cyan]Test 5: Template Processing[/cyan]")
        
        # Create template file
        template_content = "Hello {{name}}! Welcome to {{project}}."
        template_write = {
            "type": "function",
            "function": {
                "name": "write_file",
                "arguments": {
                    "file_path": "template.txt",
                    "content": template_content
                }
            }
        }
        
        result = await handler.handle_tool_call(template_write)
        assert result["success"]
        
        # Process template
        template_call = {
            "type": "function",
            "function": {
                "name": "template_file",
                "arguments": {
                    "template_path": "template.txt",
                    "output_path": "processed.txt",
                    "variables": {
                        "name": "Developer",
                        "project": "Saturn File Tools"
                    }
                }
            }
        }
        
        result = await handler.handle_tool_call(template_call)
        assert result["success"], f"Template processing failed: {result.get('error')}"
        console.print("✓ Template processing successful")
        
        # Test 6: Copy file
        console.print("\n[cyan]Test 6: File Copy[/cyan]")
        copy_call = {
            "type": "function",
            "function": {
                "name": "copy_file",
                "arguments": {
                    "source": "test_config.json",
                    "destination": "backup_config.json"
                }
            }
        }
        
        result = await handler.handle_tool_call(copy_call)
        assert result["success"], f"File copy failed: {result.get('error')}"
        console.print("✓ File copy successful")
        
        # Test 7: Dockerfile generation
        console.print("\n[cyan]Test 7: Dockerfile Generation[/cyan]")
        
        # Create requirements.txt for Python project
        reqs_write = {
            "type": "function",
            "function": {
                "name": "write_file",
                "arguments": {
                    "file_path": "requirements.txt",
                    "content": "fastapi\nuvicorn\nrequests"
                }
            }
        }
        
        result = await handler.handle_tool_call(reqs_write)
        assert result["success"]
        
        dockerfile_call = {
            "type": "function",
            "function": {
                "name": "generate_dockerfile",
                "arguments": {
                    "base_image": "python:3.11-slim",
                    "dependencies_file": "requirements.txt",
                    "start_command": "[\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\"]"
                }
            }
        }
        
        result = await handler.handle_tool_call(dockerfile_call)
        assert result["success"], f"Dockerfile generation failed: {result.get('error')}"
        console.print("✓ Dockerfile generation successful")
        
        # Test 8: Error handling
        console.print("\n[cyan]Test 8: Error Handling[/cyan]")
        
        # Try to read non-existent file
        error_call = {
            "type": "function",
            "function": {
                "name": "read_file",
                "arguments": {
                    "file_path": "non_existent_file.txt"
                }
            }
        }
        
        result = await handler.handle_tool_call(error_call)
        assert not result["success"], "Should have failed for non-existent file"
        console.print("✓ Error handling working correctly")
        
        # Test 9: Invalid tool call
        console.print("\n[cyan]Test 9: Invalid Tool Handling[/cyan]")
        
        invalid_call = {
            "type": "function",
            "function": {
                "name": "invalid_tool_name",
                "arguments": {}
            }
        }
        
        result = await handler.handle_tool_call(invalid_call)
        assert not result["success"], "Should have failed for invalid tool"
        console.print("✓ Invalid tool handling working correctly")
        
        # Test 10: Tool sequence execution
        console.print("\n[cyan]Test 10: Tool Sequence Execution[/cyan]")
        
        sequence = [
            {
                "type": "function",
                "function": {
                    "name": "write_file",
                    "arguments": {
                        "file_path": "sequence_test.txt",
                        "content": "Test file for sequence"
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "read_file",
                    "arguments": {
                        "file_path": "sequence_test.txt"
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "copy_file",
                    "arguments": {
                        "source": "sequence_test.txt",
                        "destination": "sequence_copy.txt"
                    }
                }
            }
        ]
        
        results = await handler.execute_tool_sequence(sequence)
        assert len(results) == 3
        assert all(result["success"] for result in results)
        console.print("✓ Tool sequence execution successful")
        
        console.print(f"\n[bold green]All 10 tests passed! File build tools are ready for LLM integration.[/bold green]")
        return True

def test_tools_schema_validation():
    """Test that tools schema follows OpenAI format."""
    
    console = Console()
    console.print("\n[cyan]Schema Validation Test[/cyan]")
    
    tools_interface = create_file_build_tools_for_llm(".")
    schema = tools_interface["tools_schema"]
    
    # Validate OpenAI tools format
    for tool in schema:
        # Each tool should have type and function
        assert tool["type"] == "function"
        assert "function" in tool
        
        func = tool["function"]
        
        # Function should have name, description, parameters
        assert "name" in func
        assert "description" in func
        assert "parameters" in func
        
        # Parameters should be object type with properties
        params = func["parameters"]
        assert params["type"] == "object"
        assert "properties" in params
        
        console.print(f"✓ {func['name']}: Valid schema")
    
    console.print(f"✓ All {len(schema)} tools have valid OpenAI-compatible schemas")

def display_available_tools():
    """Display all available tools with their descriptions."""
    
    console = Console()
    console.print("\n[bold yellow]Available File Build Tools for LLM[/bold yellow]\n")
    
    tools_interface = create_file_build_tools_for_llm(".")
    
    for tool in tools_interface["tools_schema"]:
        func = tool["function"]
        console.print(f"[bold cyan]{func['name']}[/bold cyan]")
        console.print(f"  {func['description']}")
        
        # Show required parameters
        params = func["parameters"]
        required = params.get("required", [])
        if required:
            console.print(f"  Required: {', '.join(required)}")
        
        console.print()

async def demo_real_world_scenario():
    """Demo real-world scenario: LLM building and containerizing a project."""
    
    console = Console()
    console.print("\n[bold green]Demo: Real-World LLM Scenario[/bold green]")
    console.print("Scenario: LLM receives task to build and containerize a Python project\n")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        tools_interface = create_file_build_tools_for_llm(temp_dir)
        handler = tools_interface["handler"]
        
        # Simulate LLM receiving a task and making tool calls
        scenario_steps = [
            # Step 1: Check what's in the current directory
            {
                "type": "function",
                "function": {
                    "name": "list_files",
                    "arguments": {"recursive": True}
                }
            },
            
            # Step 2: Detect project type
            {
                "type": "function",
                "function": {
                    "name": "detect_project_type",
                    "arguments": {}
                }
            },
            
            # Step 3: Create a simple Python app
            {
                "type": "function",
                "function": {
                    "name": "write_file",
                    "arguments": {
                        "file_path": "app.py",
                        "content": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef read_root():\n    return {'message': 'Hello from Saturn!'}"
                    }
                }
            },
            
            # Step 4: Create requirements file
            {
                "type": "function",
                "function": {
                    "name": "write_file",
                    "arguments": {
                        "file_path": "requirements.txt",
                        "content": "fastapi==0.104.1\nuvicorn==0.24.0"
                    }
                }
            },
            
            # Step 5: Generate Dockerfile
            {
                "type": "function",
                "function": {
                    "name": "generate_dockerfile",
                    "arguments": {
                        "dependencies_file": "requirements.txt",
                        "start_command": "[\"uvicorn\", \"app:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]"
                    }
                }
            },
            
            # Step 6: Read generated Dockerfile to verify
            {
                "type": "function",
                "function": {
                    "name": "read_file",
                    "arguments": {
                        "file_path": "Dockerfile"
                    }
                }
            }
        ]
        
        console.print("LLM executing automated build workflow...")
        results = await handler.execute_tool_sequence(scenario_steps)
        
        success_count = sum(1 for r in results if r["success"])
        console.print(f"\n[bold blue]Workflow completed: {success_count}/{len(results)} steps successful[/bold blue]")
        
        # Show final project structure
        final_list = {
            "type": "function",
            "function": {
                "name": "list_files",
                "arguments": {"recursive": True}
            }
        }
        
        final_result = await handler.handle_tool_call(final_list)
        if final_result["success"]:
            console.print("\nFinal project structure:")
            for file_info in final_result["result"]["files"]:
                console.print(f"  {file_info['name']} ({file_info['size']} bytes)")

async def main():
    """Run all tests and demos."""
    
    console = Console()
    console.print("[bold magenta]Saturn File Build Tools - LLM Integration Test Suite[/bold magenta]\n")
    
    # Run comprehensive tests
    await test_file_build_tools()
    
    # Validate schema format
    test_tools_schema_validation()
    
    # Display available tools
    display_available_tools()
    
    # Run real-world demo
    await demo_real_world_scenario()
    
    console.print("\n[bold green]🎉 All tests completed successfully![/bold green]")
    console.print("[dim]File build tools are ready for LLM integration![/dim]")

if __name__ == "__main__":
    asyncio.run(main()) 