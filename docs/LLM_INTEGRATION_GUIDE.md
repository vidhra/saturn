# Saturn File Build Tools - LLM Integration Guide

This guide explains how to integrate Saturn's file operations and build tools with Large Language Models (LLMs) for automated development workflows.

## Overview

The Saturn File Build Tools provide a comprehensive set of capabilities that can be exposed as tools for LLMs to use:

- **File Operations**: Read, write, list, copy files in multiple formats
- **Build Tools**: Auto-detect and build projects (Python, Node.js, Rust, Go, Java, etc.)
- **Docker Integration**: Generate Dockerfiles, build images, run containers
- **Template Processing**: Variable substitution in configuration files

## Available Tools

### File Operations

#### `read_file`
Read content from any supported file format.
```json
{
  "type": "function",
  "function": {
    "name": "read_file",
    "arguments": {
      "file_path": "config.json"
    }
  }
}
```

#### `write_file`
Write content to files with automatic format detection.
```json
{
  "type": "function",
  "function": {
    "name": "write_file",
    "arguments": {
      "file_path": "config.yaml",
      "content": {"database": {"host": "localhost", "port": 5432}},
      "format": ".yaml"
    }
  }
}
```

#### `list_files`
List files with pattern matching and recursive options.
```json
{
  "type": "function",
  "function": {
    "name": "list_files",
    "arguments": {
      "pattern": "*.py",
      "recursive": true
    }
  }
}
```

#### `copy_file`
Copy files from source to destination.
```json
{
  "type": "function",
  "function": {
    "name": "copy_file",
    "arguments": {
      "source": "config.template.json",
      "destination": "config.json"
    }
  }
}
```

#### `template_file`
Process template files with variable substitution.
```json
{
  "type": "function",
  "function": {
    "name": "template_file",
    "arguments": {
      "template_path": "app.template.py",
      "output_path": "app.py",
      "variables": {
        "app_name": "MyApp",
        "version": "1.0.0"
      }
    }
  }
}
```

### Project Detection and Building

#### `detect_project_type`
Auto-detect project type based on indicator files.
```json
{
  "type": "function",
  "function": {
    "name": "detect_project_type",
    "arguments": {}
  }
}
```

#### `build_project`
Build project using appropriate build tool.
```json
{
  "type": "function",
  "function": {
    "name": "build_project",
    "arguments": {
      "project_type": "auto"
    }
  }
}
```

#### `test_project`
Run tests using appropriate test runner.
```json
{
  "type": "function",
  "function": {
    "name": "test_project",
    "arguments": {
      "project_type": "python"
    }
  }
}
```

#### `lint_project`
Run linting/code quality checks.
```json
{
  "type": "function",
  "function": {
    "name": "lint_project",
    "arguments": {
      "project_type": "auto"
    }
  }
}
```

### Docker Operations

#### `generate_dockerfile`
Generate Dockerfile based on project structure.
```json
{
  "type": "function",
  "function": {
    "name": "generate_dockerfile",
    "arguments": {
      "base_image": "python:3.11-slim",
      "dependencies_file": "requirements.txt",
      "start_command": "[\"uvicorn\", \"app:app\", \"--host\", \"0.0.0.0\"]"
    }
  }
}
```

#### `build_docker_image`
Build Docker image from Dockerfile.
```json
{
  "type": "function",
  "function": {
    "name": "build_docker_image",
    "arguments": {
      "image_name": "my-app:latest",
      "build_context": "."
    }
  }
}
```

#### `run_docker_container`
Run Docker container with specified configuration.
```json
{
  "type": "function",
  "function": {
    "name": "run_docker_container",
    "arguments": {
      "image_name": "my-app:latest",
      "ports": {"8000": "8000"},
      "environment": {"ENV": "production"}
    }
  }
}
```

#### `docker_compose_up`
Run docker-compose for multi-container applications.
```json
{
  "type": "function",
  "function": {
    "name": "docker_compose_up",
    "arguments": {
      "compose_file": "docker-compose.yml",
      "build": true
    }
  }
}
```

## Integration Examples

### OpenAI GPT Integration

```python
import openai
from saturn.file_build_tools import create_file_build_tools_for_llm

# Initialize tools
tools_interface = create_file_build_tools_for_llm("/path/to/project")
tools_schema = tools_interface["tools_schema"]
handler = tools_interface["handler"]

# Create OpenAI client
client = openai.OpenAI(api_key="your-api-key")

# Chat completion with tools
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Build and containerize this Python project"}
    ],
    tools=tools_schema,
    tool_choice="auto"
)

# Process tool calls
if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        result = await handler.handle_tool_call({
            "type": "function",
            "function": {
                "name": tool_call.function.name,
                "arguments": tool_call.function.arguments
            }
        })
        print(f"Tool {tool_call.function.name}: {result}")
```

### Anthropic Claude Integration

```python
import anthropic
from saturn.file_build_tools import create_file_build_tools_for_llm

# Initialize tools
tools_interface = create_file_build_tools_for_llm("/path/to/project")
tools_schema = tools_interface["tools_schema"]
handler = tools_interface["handler"]

# Convert to Anthropic format
anthropic_tools = []
for tool in tools_schema:
    anthropic_tools.append({
        "name": tool["function"]["name"],
        "description": tool["function"]["description"],
        "input_schema": tool["function"]["parameters"]
    })

# Create Anthropic client
client = anthropic.Anthropic(api_key="your-api-key")

# Chat completion with tools
response = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1000,
    tools=anthropic_tools,
    messages=[
        {"role": "user", "content": "Analyze and build this project"}
    ]
)

# Process tool use
for content in response.content:
    if content.type == "tool_use":
        result = await handler.handle_tool_call({
            "type": "function",
            "function": {
                "name": content.name,
                "arguments": content.input
            }
        })
        print(f"Tool {content.name}: {result}")
```

## Common Workflows

### 1. Project Analysis and Setup

```python
workflow_steps = [
    # Analyze existing project
    {"name": "list_files", "args": {"recursive": True}},
    {"name": "detect_project_type", "args": {}},
    
    # Setup configuration
    {"name": "write_file", "args": {
        "file_path": ".env",
        "content": "DEBUG=true\nPORT=8000"
    }},
    
    # Generate Docker setup
    {"name": "generate_dockerfile", "args": {
        "dependencies_file": "requirements.txt"
    }}
]
```

### 2. Build and Test Pipeline

```python
pipeline_steps = [
    # Build project
    {"name": "build_project", "args": {"project_type": "auto"}},
    
    # Run tests
    {"name": "test_project", "args": {}},
    
    # Check code quality
    {"name": "lint_project", "args": {}},
    
    # Build Docker image
    {"name": "build_docker_image", "args": {
        "image_name": "my-app:latest"
    }}
]
```

### 3. Configuration Management

```python
config_steps = [
    # Read existing config
    {"name": "read_file", "args": {"file_path": "config.template.yaml"}},
    
    # Process template with environment-specific values
    {"name": "template_file", "args": {
        "template_path": "config.template.yaml",
        "output_path": "config.yaml",
        "variables": {
            "environment": "production",
            "database_url": "postgresql://prod-db:5432/app"
        }
    }},
    
    # Copy to deployment directory
    {"name": "copy_file", "args": {
        "source": "config.yaml",
        "destination": "deploy/config.yaml"
    }}
]
```

## Error Handling

All tools return a consistent response format:

```python
{
    "success": bool,          # Whether operation succeeded
    "result": any,           # Operation result (if successful)
    "error": str,            # Error message (if failed)
    "tool": str              # Tool name that was called
}
```

### Handling Tool Failures

```python
async def handle_tool_with_retry(handler, tool_call, max_retries=3):
    """Handle tool call with retry logic."""
    
    for attempt in range(max_retries):
        result = await handler.handle_tool_call(tool_call)
        
        if result["success"]:
            return result
        
        print(f"Attempt {attempt + 1} failed: {result['error']}")
        
        if attempt < max_retries - 1:
            # Modify tool call based on error if needed
            await asyncio.sleep(1)  # Brief delay before retry
    
    return result  # Return final failed result
```

## Performance Considerations

### Async Operations
All file and build operations are asynchronous for better performance:

```python
# Sequential execution
results = []
for tool_call in tool_calls:
    result = await handler.handle_tool_call(tool_call)
    results.append(result)

# Parallel execution (where appropriate)
import asyncio
tasks = [handler.handle_tool_call(call) for call in independent_calls]
results = await asyncio.gather(*tasks)
```

### File Size Limits
- Text files: No specific limit, but consider memory usage
- Binary files: Consider streaming for large files
- Build artifacts: Clean up temporary files after operations

### Caching
Consider implementing caching for:
- Project type detection results
- Build dependencies
- Docker image layers

## Security Considerations

### File Access
- Tools operate within specified working directory
- Path traversal attacks are prevented by Path validation
- Consider implementing file access allowlists for production

### Command Execution
- Build commands are predefined and validated
- Custom commands should be sanitized
- Consider running in containerized environments

### Docker Operations
- Docker commands require appropriate permissions
- Consider using Docker rootless mode
- Validate image names and tags

## Best Practices

### Tool Selection
```python
# Let LLM choose appropriate tools
user_message = "Build and deploy this Python application"

# Provide context about available tools
system_message = """
You have access to file operations, build tools, and Docker capabilities.
Always start by detecting project type and listing files to understand the codebase.
"""
```

### Error Recovery
```python
# Implement graceful degradation
if build_result["success"]:
    # Proceed with Docker build
    docker_result = await build_docker_image(...)
else:
    # Try alternative build method or provide manual instructions
    print(f"Build failed: {build_result['error']}")
    print("Manual build steps: ...")
```

### Progress Tracking
```python
# Use rich console for progress feedback
from rich.progress import Progress

async def execute_workflow_with_progress(steps):
    with Progress() as progress:
        task = progress.add_task("Executing workflow...", total=len(steps))
        
        for step in steps:
            result = await handler.handle_tool_call(step)
            progress.advance(task)
            
            if not result["success"]:
                progress.stop()
                break
```

## Troubleshooting

### Common Issues

1. **Tool Not Found**
   - Verify tool name spelling
   - Check available tools with `get_available_tools()`

2. **Permission Errors**
   - Check file/directory permissions
   - Ensure Docker daemon is accessible

3. **Build Failures**
   - Verify dependencies are installed
   - Check project structure and configuration files

4. **Docker Issues**
   - Ensure Docker is running
   - Check image names and tags
   - Verify network connectivity for image pulls

### Debug Mode

```python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Test individual tools
tools_interface = create_file_build_tools_for_llm(".", debug=True)
```

## Extensions

### Adding Custom Tools

```python
class CustomFileBuildToolCaller(FileBuildToolCaller):
    def _register_tools(self):
        tools = super()._register_tools()
        
        # Add custom tool
        tools["custom_deploy"] = {
            "function": self.custom_deploy,
            "description": "Deploy application to custom platform",
            "parameters": {
                "type": "object",
                "properties": {
                    "platform": {"type": "string"},
                    "config": {"type": "object"}
                },
                "required": ["platform"]
            }
        }
        
        return tools
    
    async def custom_deploy(self, platform: str, config: dict = None):
        # Implementation here
        pass
```

### Integration with CI/CD

```python
# GitHub Actions integration
def create_github_workflow():
    return {
        "name": "Saturn Build",
        "on": ["push"],
        "jobs": {
            "build": {
                "runs-on": "ubuntu-latest",
                "steps": [
                    {"uses": "actions/checkout@v2"},
                    {"name": "Setup Saturn", "run": "pip install saturn-tools"},
                    {"name": "Build with Saturn", "run": "python -m saturn.build"}
                ]
            }
        }
    }
```

This guide provides comprehensive information for integrating Saturn's file build tools with LLMs, enabling powerful automated development workflows. 