# LLM Tool Calling Interface for File Operations and Build Tools
import asyncio
import json
from typing import Dict, Any, List, Optional, Callable
from rich.console import Console
from saturn.file_executor import FileBuildExecutor

class FileBuildToolCaller:
    """
    Provides LLM tool calling interface for file operations and build tools.
    Each operation from FileBuildExecutor is exposed as a separate callable tool.
    """
    
    def __init__(self, working_directory: str = "."):
        self.executor = FileBuildExecutor({
            'working_directory': working_directory
        })
        self.console = Console()
        self._tools = self._register_tools()
    
    def _register_tools(self) -> Dict[str, Dict[str, Any]]:
        """Register all available tools with their schemas."""
        
        return {
            "read_file": {
                "function": self.read_file,
                "description": "Read content from a file. Supports JSON, YAML, TOML, text files, .env files, and more.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Path to the file to read (relative to working directory)"
                        }
                    },
                    "required": ["file_path"]
                }
            },
            
            "write_file": {
                "function": self.write_file,
                "description": "Write content to a file. Auto-detects format or specify explicitly.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Path where to write the file"
                        },
                        "content": {
                            "type": ["string", "object"],
                            "description": "Content to write (string for text, object for JSON/YAML)"
                        },
                        "file_content": {
                            "type": ["string", "object"],
                            "description": "Alternative parameter name for content (for backward compatibility)"
                        },
                        "format": {
                            "type": "string",
                            "description": "File format override (auto, .json, .yaml, .toml, .txt)",
                            "default": "auto"
                        }
                    },
                    "required": ["file_path"],
                    "oneOf": [
                        {"required": ["content"]},
                        {"required": ["file_content"]}
                    ]
                }
            },
            
            "list_files": {
                "function": self.list_files,
                "description": "List files in a directory with optional pattern matching.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "directory": {
                            "type": "string",
                            "description": "Directory to list (default: current directory)",
                            "default": "."
                        },
                        "pattern": {
                            "type": "string",
                            "description": "File pattern to match (e.g., '*.py', '*.json')",
                            "default": "*"
                        },
                        "recursive": {
                            "type": "boolean",
                            "description": "Whether to search recursively in subdirectories",
                            "default": False
                        }
                    },
                    "required": []
                }
            },
            
            "copy_file": {
                "function": self.copy_file,
                "description": "Copy a file from source to destination.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source": {
                            "type": "string",
                            "description": "Source file path"
                        },
                        "destination": {
                            "type": "string",
                            "description": "Destination file path"
                        }
                    },
                    "required": ["source", "destination"]
                }
            },
            
            "template_file": {
                "function": self.template_file,
                "description": "Process a template file with variable substitution using {{variable}} syntax.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_path": {
                            "type": "string",
                            "description": "Path to template file"
                        },
                        "output_path": {
                            "type": "string",
                            "description": "Path where to write processed template"
                        },
                        "variables": {
                            "type": "object",
                            "description": "Variables for template substitution",
                            "default": {}
                        }
                    },
                    "required": ["template_path", "output_path"]
                }
            },
            
            "detect_project_type": {
                "function": self.detect_project_type,
                "description": "Auto-detect project type based on files present (Python, Node.js, Rust, Go, Java, etc.).",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            },
            
            "build_project": {
                "function": self.build_project,
                "description": "Build project using appropriate build tool (pip, npm, cargo, go build, maven, etc.).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_type": {
                            "type": "string",
                            "description": "Project type (auto, python, node, rust, go, java, make)",
                            "default": "auto"
                        },
                        "build_command": {
                            "type": "string",
                            "description": "Custom build command (overrides auto-detected command)"
                        }
                    },
                    "required": []
                }
            },
            
            "test_project": {
                "function": self.test_project,
                "description": "Run tests for the project using appropriate test runner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_type": {
                            "type": "string",
                            "description": "Project type (auto, python, node, rust, go, java, make)",
                            "default": "auto"
                        },
                        "test_command": {
                            "type": "string",
                            "description": "Custom test command (overrides auto-detected command)"
                        }
                    },
                    "required": []
                }
            },
            
            "lint_project": {
                "function": self.lint_project,
                "description": "Run linting/code quality checks for the project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_type": {
                            "type": "string",
                            "description": "Project type (auto, python, node, rust, go, java, make)",
                            "default": "auto"
                        },
                        "lint_command": {
                            "type": "string",
                            "description": "Custom lint command (overrides auto-detected command)"
                        }
                    },
                    "required": []
                }
            },
            
            "generate_dockerfile": {
                "function": self.generate_dockerfile,
                "description": "Generate a Dockerfile based on project structure and type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "base_image": {
                            "type": "string",
                            "description": "Base Docker image",
                            "default": "python:3.11-slim"
                        },
                        "working_dir": {
                            "type": "string",
                            "description": "Working directory in container",
                            "default": "/app"
                        },
                        "dependencies_file": {
                            "type": "string",
                            "description": "Dependencies file (requirements.txt, package.json, etc.)"
                        },
                        "start_command": {
                            "type": "string",
                            "description": "Command to start the application"
                        },
                        "output_path": {
                            "type": "string",
                            "description": "Where to save the Dockerfile",
                            "default": "Dockerfile"
                        }
                    },
                    "required": []
                }
            },
            
            "build_docker_image": {
                "function": self.build_docker_image,
                "description": "Build a Docker image from Dockerfile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dockerfile_path": {
                            "type": "string",
                            "description": "Path to Dockerfile",
                            "default": "Dockerfile"
                        },
                        "image_name": {
                            "type": "string",
                            "description": "Name for the Docker image",
                            "default": "saturn-build"
                        },
                        "build_context": {
                            "type": "string",
                            "description": "Build context directory",
                            "default": "."
                        },
                        "build_args": {
                            "type": "object",
                            "description": "Build arguments for Docker build",
                            "default": {}
                        }
                    },
                    "required": []
                }
            },
            
            "run_docker_container": {
                "function": self.run_docker_container,
                "description": "Run a Docker container from an image.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "image_name": {
                            "type": "string",
                            "description": "Docker image name to run"
                        },
                        "container_name": {
                            "type": "string",
                            "description": "Name for the container"
                        },
                        "ports": {
                            "type": "object",
                            "description": "Port mappings (host:container)",
                            "default": {}
                        },
                        "volumes": {
                            "type": "object",
                            "description": "Volume mounts (host:container)",
                            "default": {}
                        },
                        "environment": {
                            "type": "object",
                            "description": "Environment variables",
                            "default": {}
                        },
                        "command": {
                            "type": "string",
                            "description": "Command to run in container"
                        },
                        "detached": {
                            "type": "boolean",
                            "description": "Run in detached mode",
                            "default": True
                        }
                    },
                    "required": ["image_name"]
                }
            },
            
            "docker_compose_up": {
                "function": self.docker_compose_up,
                "description": "Run docker-compose up to start multi-container applications.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "compose_file": {
                            "type": "string",
                            "description": "Docker Compose file path",
                            "default": "docker-compose.yml"
                        },
                        "detached": {
                            "type": "boolean",
                            "description": "Run in detached mode",
                            "default": True
                        },
                        "build": {
                            "type": "boolean",
                            "description": "Build images before starting",
                            "default": False
                        }
                    },
                    "required": []
                }
            }
        }
    
    async def read_file(self, file_path: str) -> Dict[str, Any]:
        """Read content from a file."""
        success, result = await self.executor.execute(
            "read_file", 
            {"file_path": file_path}, 
            self.console, 
            "read_file"
        )
        return {
            "success": success,
            "result": result,
            "tool": "read_file"
        }
    
    async def write_file(self, file_path: str, content: Any = None, file_content: Any = None, format: str = "auto") -> Dict[str, Any]:
        """Write content to a file."""
        # Use file_content if content is None (for backward compatibility)
        actual_content = content if content is not None else file_content
        if actual_content is None:
            return {
                "success": False,
                "error": "Either 'content' or 'file_content' parameter is required",
                "tool": "write_file"
            }
            
        success, result = await self.executor.execute(
            "write_file", 
            {"file_path": file_path, "content": actual_content, "format": format}, 
            self.console, 
            "write_file"
        )
        return {
            "success": success,
            "result": result,
            "tool": "write_file"
        }
    
    async def list_files(self, directory: str = ".", pattern: str = "*", recursive: bool = False) -> Dict[str, Any]:
        """List files in directory."""
        success, result = await self.executor.execute(
            "list_files", 
            {"directory": directory, "pattern": pattern, "recursive": recursive}, 
            self.console, 
            "list_files"
        )
        return {
            "success": success,
            "result": result,
            "tool": "list_files"
        }
    
    async def copy_file(self, source: str, destination: str) -> Dict[str, Any]:
        """Copy file from source to destination."""
        success, result = await self.executor.execute(
            "copy_file", 
            {"source": source, "destination": destination}, 
            self.console, 
            "copy_file"
        )
        return {
            "success": success,
            "result": result,
            "tool": "copy_file"
        }
    
    async def template_file(self, template_path: str, output_path: str, variables: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process template file with variable substitution."""
        if variables is None:
            variables = {}
        success, result = await self.executor.execute(
            "template_file", 
            {"template_path": template_path, "output_path": output_path, "variables": variables}, 
            self.console, 
            "template_file"
        )
        return {
            "success": success,
            "result": result,
            "tool": "template_file"
        }
    
    async def detect_project_type(self) -> Dict[str, Any]:
        """Auto-detect project type."""
        success, result = await self.executor.execute(
            "detect_project", 
            {}, 
            self.console, 
            "detect_project"
        )
        return {
            "success": success,
            "result": result,
            "tool": "detect_project_type"
        }
    
    async def build_project(self, project_type: str = "auto", build_command: str = None) -> Dict[str, Any]:
        """Build project using appropriate build tool."""
        params = {"project_type": project_type}
        if build_command:
            params["build_command"] = build_command
        
        success, result = await self.executor.execute(
            "build_project", 
            params, 
            self.console, 
            "build_project"
        )
        return {
            "success": success,
            "result": result,
            "tool": "build_project"
        }
    
    async def test_project(self, project_type: str = "auto", test_command: str = None) -> Dict[str, Any]:
        """Run tests for project."""
        params = {"project_type": project_type}
        if test_command:
            params["test_command"] = test_command
            
        success, result = await self.executor.execute(
            "test_project", 
            params, 
            self.console, 
            "test_project"
        )
        return {
            "success": success,
            "result": result,
            "tool": "test_project"
        }
    
    async def lint_project(self, project_type: str = "auto", lint_command: str = None) -> Dict[str, Any]:
        """Run linting for project."""
        params = {"project_type": project_type}
        if lint_command:
            params["lint_command"] = lint_command
            
        success, result = await self.executor.execute(
            "lint_project", 
            params, 
            self.console, 
            "lint_project"
        )
        return {
            "success": success,
            "result": result,
            "tool": "lint_project"
        }
    
    async def generate_dockerfile(
        self, 
        base_image: str = "python:3.11-slim",
        working_dir: str = "/app",
        dependencies_file: str = None,
        start_command: str = None,
        output_path: str = "Dockerfile"
    ) -> Dict[str, Any]:
        """Generate Dockerfile based on project structure."""
        params = {
            "base_image": base_image,
            "working_dir": working_dir,
            "output_path": output_path
        }
        if dependencies_file:
            params["dependencies_file"] = dependencies_file
        if start_command:
            params["start_command"] = start_command
            
        success, result = await self.executor.execute(
            "generate_dockerfile", 
            params, 
            self.console, 
            "generate_dockerfile"
        )
        return {
            "success": success,
            "result": result,
            "tool": "generate_dockerfile"
        }
    
    async def build_docker_image(
        self,
        dockerfile_path: str = "Dockerfile",
        image_name: str = "saturn-build",
        build_context: str = ".",
        build_args: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """Build Docker image."""
        if build_args is None:
            build_args = {}
            
        success, result = await self.executor.execute(
            "build_docker", 
            {
                "dockerfile_path": dockerfile_path,
                "image_name": image_name,
                "build_context": build_context,
                "build_args": build_args
            }, 
            self.console, 
            "build_docker"
        )
        return {
            "success": success,
            "result": result,
            "tool": "build_docker_image"
        }
    
    async def run_docker_container(
        self,
        image_name: str,
        container_name: str = None,
        ports: Dict[str, str] = None,
        volumes: Dict[str, str] = None,
        environment: Dict[str, str] = None,
        command: str = None,
        detached: bool = True
    ) -> Dict[str, Any]:
        """Run Docker container."""
        params = {"image_name": image_name, "detached": detached}
        if container_name:
            params["container_name"] = container_name
        if ports:
            params["ports"] = ports
        if volumes:
            params["volumes"] = volumes
        if environment:
            params["environment"] = environment
        if command:
            params["command"] = command
            
        success, result = await self.executor.execute(
            "run_docker", 
            params, 
            self.console, 
            "run_docker"
        )
        return {
            "success": success,
            "result": result,
            "tool": "run_docker_container"
        }
    
    async def docker_compose_up(
        self,
        compose_file: str = "docker-compose.yml",
        detached: bool = True,
        build: bool = False
    ) -> Dict[str, Any]:
        """Run docker-compose up."""
        success, result = await self.executor.execute(
            "docker_compose", 
            {
                "compose_file": compose_file,
                "detached": detached,
                "build": build
            }, 
            self.console, 
            "docker_compose"
        )
        return {
            "success": success,
            "result": result,
            "tool": "docker_compose_up"
        }
    
    def get_tools_schema(self) -> List[Dict[str, Any]]:
        """Get OpenAI-compatible tool schema for all available tools."""
        
        tools_schema = []
        
        for tool_name, tool_info in self._tools.items():
            schema = {
                "type": "function",
                "function": {
                    "name": tool_name,
                    "description": tool_info["description"],
                    "parameters": tool_info["parameters"]
                }
            }
            tools_schema.append(schema)
        
        return tools_schema
    
    def get_tool_function(self, tool_name: str) -> Optional[Callable]:
        """Get the actual function for a tool by name."""
        
        if tool_name in self._tools:
            return self._tools[tool_name]["function"]
        return None
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Call a tool by name with given arguments."""
        
        tool_function = self.get_tool_function(tool_name)
        if not tool_function:
            return {
                "success": False,
                "error": f"Unknown tool: {tool_name}",
                "tool": tool_name
            }
        
        try:
            # Call the tool function with unpacked arguments
            result = await tool_function(**arguments)
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Tool execution failed: {str(e)}",
                "tool": tool_name
            }
    
    def get_available_tools(self) -> List[str]:
        """Get list of all available tool names."""
        return list(self._tools.keys())


class FileBuildToolHandler:
    """
    Handler for processing LLM tool calls for file operations and builds.
    This class provides the interface between LLM tool calls and the actual execution.
    """
    
    def __init__(self, working_directory: str = "."):
        self.tool_caller = FileBuildToolCaller(working_directory)
        self.console = Console()
    
    async def handle_tool_call(self, tool_call: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle a tool call from an LLM.
        
        Expected format:
        {
            "type": "function",
            "function": {
                "name": "tool_name",
                "arguments": {...}
            }
        }
        """
        
        try:
            if tool_call.get("type") != "function":
                return {
                    "success": False,
                    "error": "Invalid tool call type. Expected 'function'."
                }
            
            function_info = tool_call.get("function", {})
            tool_name = function_info.get("name")
            arguments = function_info.get("arguments", {})
            
            # If arguments is a string (JSON), parse it
            if isinstance(arguments, str):
                arguments = json.loads(arguments)
            
            self.console.print(f"\n[bold cyan]LLM Tool Call: {tool_name}[/bold cyan]")
            self.console.print(f"Arguments: {arguments}")
            
            result = await self.tool_caller.call_tool(tool_name, arguments)
            
            if result["success"]:
                self.console.print(f"[green]✓ Tool {tool_name} completed successfully[/green]")
            else:
                self.console.print(f"[red]✗ Tool {tool_name} failed: {result.get('error', 'Unknown error')}[/red]")
            
            return result
            
        except Exception as e:
            error_msg = f"Tool call handler error: {str(e)}"
            self.console.print(f"[bold red]{error_msg}[/bold red]")
            return {
                "success": False,
                "error": error_msg
            }
    
    def get_tools_for_llm(self) -> List[Dict[str, Any]]:
        """Get tool schema in format expected by LLM APIs."""
        return self.tool_caller.get_tools_schema()
    
    async def execute_tool_sequence(self, tool_calls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Execute a sequence of tool calls and return all results."""
        
        results = []
        
        for i, tool_call in enumerate(tool_calls):
            self.console.print(f"\n[bold blue]Executing tool {i+1}/{len(tool_calls)}[/bold blue]")
            result = await self.handle_tool_call(tool_call)
            results.append(result)
            
            # If a tool fails, decide whether to continue or stop
            if not result["success"]:
                self.console.print(f"[yellow]Warning: Tool failed but continuing with sequence[/yellow]")
        
        return results


def create_file_build_tools_for_llm(working_directory: str = ".") -> Dict[str, Any]:
    """
    Create file build tools interface for LLM integration.
    Returns tools schema and handler for processing tool calls.
    """
    
    handler = FileBuildToolHandler(working_directory)
    
    return {
        "tools_schema": handler.get_tools_for_llm(),
        "handler": handler,
        "available_tools": handler.tool_caller.get_available_tools()
    }

