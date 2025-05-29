# File operations and build tooling executor for Saturn architecture
import os
import json
import asyncio
import tempfile
import subprocess
import shutil
import re
import yaml
import toml
from datetime import datetime
from typing import Dict, Any, Tuple, Optional, List, Union
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, TaskID
from rich.table import Table
from rich.panel import Panel
from abc import ABC, abstractmethod

class FileOperationsManager:
    """
    Advanced file operations manager for reading, writing, and manipulating files.
    """
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path).resolve()
        self.supported_formats = {
            '.json': self._read_json,
            '.yaml': self._read_yaml, 
            '.yml': self._read_yaml,
            '.toml': self._read_toml,
            '.txt': self._read_text,
            '.md': self._read_text,
            '.py': self._read_text,
            '.js': self._read_text,
            '.ts': self._read_text,
            '.sh': self._read_text,
            '.dockerfile': self._read_text,
            '.env': self._read_env
        }
    
    def read_file(self, file_path: str) -> Dict[str, Any]:
        """Read any supported file format and return structured data."""
        
        try:
            full_path = self.base_path / file_path
            if not full_path.exists():
                return {
                    "success": False,
                    "error": f"File not found: {file_path}",
                    "path": str(full_path)
                }
            
            suffix = full_path.suffix.lower()
            if suffix in self.supported_formats:
                content = self.supported_formats[suffix](full_path)
            else:
                # Default to text reading
                content = self._read_text(full_path)
            
            return {
                "success": True,
                "content": content,
                "path": str(full_path),
                "size": full_path.stat().st_size,
                "modified": datetime.fromtimestamp(full_path.stat().st_mtime).isoformat(),
                "format": suffix
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error reading file {file_path}: {str(e)}",
                "path": file_path
            }
    
    def write_file(self, file_path: str, content: Any, format_type: str = "auto") -> Dict[str, Any]:
        """Write content to file in specified format."""
        
        try:
            full_path = self.base_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            if format_type == "auto":
                format_type = full_path.suffix.lower()
            
            if format_type in ['.json']:
                self._write_json(full_path, content)
            elif format_type in ['.yaml', '.yml']:
                self._write_yaml(full_path, content)
            elif format_type in ['.toml']:
                self._write_toml(full_path, content)
            else:
                self._write_text(full_path, str(content))
            
            return {
                "success": True,
                "path": str(full_path),
                "size": full_path.stat().st_size,
                "format": format_type
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error writing file {file_path}: {str(e)}",
                "path": file_path
            }
    
    def list_files(self, directory: str = ".", pattern: str = "*", recursive: bool = False) -> Dict[str, Any]:
        """List files in directory with optional pattern matching."""
        
        try:
            full_dir = self.base_path / directory
            if not full_dir.exists():
                return {
                    "success": False,
                    "error": f"Directory not found: {directory}"
                }
            
            if recursive:
                files = list(full_dir.rglob(pattern))
            else:
                files = list(full_dir.glob(pattern))
            
            file_info = []
            for file_path in files:
                if file_path.is_file():
                    file_info.append({
                        "name": file_path.name,
                        "path": str(file_path.relative_to(self.base_path)),
                        "size": file_path.stat().st_size,
                        "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                        "extension": file_path.suffix
                    })
            
            return {
                "success": True,
                "files": file_info,
                "directory": str(full_dir),
                "count": len(file_info)
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error listing files in {directory}: {str(e)}"
            }
    
    def copy_file(self, source: str, destination: str) -> Dict[str, Any]:
        """Copy file from source to destination."""
        
        try:
            src_path = self.base_path / source
            dst_path = self.base_path / destination
            
            if not src_path.exists():
                return {
                    "success": False,
                    "error": f"Source file not found: {source}"
                }
            
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, dst_path)
            
            return {
                "success": True,
                "source": str(src_path),
                "destination": str(dst_path),
                "size": dst_path.stat().st_size
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error copying file: {str(e)}"
            }
    
    def template_file(self, template_path: str, output_path: str, variables: Dict[str, Any]) -> Dict[str, Any]:
        """Process template file with variable substitution."""
        
        try:
            template_content = self.read_file(template_path)
            if not template_content["success"]:
                return template_content
            
            content = template_content["content"]
            
            # Simple template variable substitution
            for var_name, var_value in variables.items():
                content = content.replace(f"{{{{{var_name}}}}}", str(var_value))
            
            return self.write_file(output_path, content)
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error processing template: {str(e)}"
            }
    
    def _read_json(self, path: Path) -> Any:
        """Read JSON file."""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _read_yaml(self, path: Path) -> Any:
        """Read YAML file."""
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def _read_toml(self, path: Path) -> Any:
        """Read TOML file."""
        with open(path, 'r', encoding='utf-8') as f:
            return toml.load(f)
    
    def _read_text(self, path: Path) -> str:
        """Read text file."""
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _read_env(self, path: Path) -> Dict[str, str]:
        """Read .env file as key-value pairs."""
        env_vars = {}
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip().strip('"\'')
        return env_vars
    
    def _write_json(self, path: Path, content: Any) -> None:
        """Write JSON file."""
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
    
    def _write_yaml(self, path: Path, content: Any) -> None:
        """Write YAML file."""
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(content, f, default_flow_style=False, allow_unicode=True)
    
    def _write_toml(self, path: Path, content: Any) -> None:
        """Write TOML file."""
        with open(path, 'w', encoding='utf-8') as f:
            toml.dump(content, f)
    
    def _write_text(self, path: Path, content: str) -> None:
        """Write text file."""
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

class DockerBuilder:
    """
    Comprehensive Docker build and management system.
    """
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path).resolve()
        self.file_manager = FileOperationsManager(base_path)
    
    async def build_image(
        self, 
        dockerfile_path: str = "Dockerfile",
        image_name: str = "saturn-build",
        build_context: str = ".",
        build_args: Dict[str, str] = None,
        console: Console = None
    ) -> Dict[str, Any]:
        """Build Docker image from Dockerfile."""
        
        try:
            dockerfile_full = self.base_path / dockerfile_path
            context_full = self.base_path / build_context
            
            if not dockerfile_full.exists():
                return {
                    "success": False,
                    "error": f"Dockerfile not found: {dockerfile_path}"
                }
            
            if not context_full.exists():
                return {
                    "success": False,
                    "error": f"Build context not found: {build_context}"
                }
            
            # Build command
            cmd = ["docker", "build", "-t", image_name, "-f", str(dockerfile_full)]
            
            # Add build args
            if build_args:
                for key, value in build_args.items():
                    cmd.extend(["--build-arg", f"{key}={value}"])
            
            cmd.append(str(context_full))
            
            if console:
                console.print(f"[bold blue]Building Docker image: {image_name}[/bold blue]")
                console.print(f"[dim]Command: {' '.join(cmd)}[/dim]")
            
            # Execute build
            result = await self._run_command(cmd, console)
            
            if result["success"]:
                # Get image info
                image_info = await self._get_image_info(image_name)
                result.update(image_info)
            
            return result
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Docker build error: {str(e)}"
            }
    
    async def run_container(
        self,
        image_name: str,
        container_name: str = None,
        ports: Dict[str, str] = None,
        volumes: Dict[str, str] = None,
        environment: Dict[str, str] = None,
        command: str = None,
        detached: bool = True,
        console: Console = None
    ) -> Dict[str, Any]:
        """Run Docker container."""
        
        try:
            cmd = ["docker", "run"]
            
            if detached:
                cmd.append("-d")
            
            if container_name:
                cmd.extend(["--name", container_name])
            
            # Add port mappings
            if ports:
                for host_port, container_port in ports.items():
                    cmd.extend(["-p", f"{host_port}:{container_port}"])
            
            # Add volume mounts
            if volumes:
                for host_path, container_path in volumes.items():
                    cmd.extend(["-v", f"{host_path}:{container_path}"])
            
            # Add environment variables
            if environment:
                for key, value in environment.items():
                    cmd.extend(["-e", f"{key}={value}"])
            
            cmd.append(image_name)
            
            if command:
                cmd.extend(command.split())
            
            if console:
                console.print(f"[bold green]Running Docker container from: {image_name}[/bold green]")
                console.print(f"[dim]Command: {' '.join(cmd)}[/dim]")
            
            result = await self._run_command(cmd, console)
            
            if result["success"] and container_name:
                container_info = await self._get_container_info(container_name)
                result.update(container_info)
            
            return result
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Docker run error: {str(e)}"
            }
    
    async def compose_up(
        self,
        compose_file: str = "docker-compose.yml",
        detached: bool = True,
        build: bool = False,
        console: Console = None
    ) -> Dict[str, Any]:
        """Run docker-compose up."""
        
        try:
            compose_path = self.base_path / compose_file
            if not compose_path.exists():
                return {
                    "success": False,
                    "error": f"Docker Compose file not found: {compose_file}"
                }
            
            cmd = ["docker-compose", "-f", str(compose_path), "up"]
            
            if detached:
                cmd.append("-d")
            
            if build:
                cmd.append("--build")
            
            if console:
                console.print(f"[bold cyan]Running Docker Compose: {compose_file}[/bold cyan]")
                console.print(f"[dim]Command: {' '.join(cmd)}[/dim]")
            
            return await self._run_command(cmd, console)
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Docker Compose error: {str(e)}"
            }
    
    def generate_dockerfile(
        self,
        base_image: str = "python:3.11-slim",
        working_dir: str = "/app",
        dependencies_file: str = None,
        start_command: str = None,
        output_path: str = "Dockerfile"
    ) -> Dict[str, Any]:
        """Generate a Dockerfile based on project structure."""
        
        try:
            dockerfile_content = f"FROM {base_image}\n\n"
            dockerfile_content += f"WORKDIR {working_dir}\n\n"
            
            # Copy dependencies file first for better layer caching
            if dependencies_file:
                dockerfile_content += f"COPY {dependencies_file} .\n"
                
                # Install dependencies based on file type
                if dependencies_file.endswith('requirements.txt'):
                    dockerfile_content += "RUN pip install -r requirements.txt\n\n"
                elif dependencies_file.endswith('package.json'):
                    dockerfile_content += "RUN npm install\n\n"
                elif dependencies_file.endswith('Cargo.toml'):
                    dockerfile_content += "RUN cargo build --release\n\n"
                elif dependencies_file.endswith('go.mod'):
                    dockerfile_content += "RUN go mod download\n\n"
            
            dockerfile_content += "COPY . .\n\n" 
            dockerfile_content += "EXPOSE 8000\n\n"
            
            if start_command:
                dockerfile_content += f"CMD {start_command}\n"
            else:
                dockerfile_content += "CMD [\"python\", \"app.py\"]\n"
            
            return self.file_manager.write_file(output_path, dockerfile_content)
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error generating Dockerfile: {str(e)}"
            }
    
    async def _run_command(self, cmd: List[str], console: Console = None) -> Dict[str, Any]:
        """Run shell command asynchronously."""
        
        try:
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=self.base_path
            )
            
            stdout, stderr = await process.communicate()
            
            output = stdout.decode().strip()
            error = stderr.decode().strip()
            
            success = process.returncode == 0
            
            if console:
                if success:
                    console.print(f"[green]✓ Command completed successfully[/green]")
                else:
                    console.print(f"[red]✗ Command failed with exit code {process.returncode}[/red]")
                
                if output:
                    console.print(f"[dim]Output: {output[:200]}{'...' if len(output) > 200 else ''}[/dim]")
                if error:
                    console.print(f"[red]Error: {error[:200]}{'...' if len(error) > 200 else ''}[/red]")
            
            return {
                "success": success,
                "output": output,
                "error": error,
                "exit_code": process.returncode,
                "command": " ".join(cmd)
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Command execution failed: {str(e)}",
                "command": " ".join(cmd)
            }
    
    async def _get_image_info(self, image_name: str) -> Dict[str, Any]:
        """Get Docker image information."""
        
        try:
            cmd = ["docker", "inspect", image_name]
            result = await self._run_command(cmd)
            
            if result["success"]:
                image_data = json.loads(result["output"])[0]
                return {
                    "image_id": image_data["Id"],
                    "image_size": image_data["Size"],
                    "created": image_data["Created"],
                    "architecture": image_data["Architecture"]
                }
            
            return {}
            
        except Exception:
            return {}
    
    async def _get_container_info(self, container_name: str) -> Dict[str, Any]:
        """Get Docker container information."""
        
        try:
            cmd = ["docker", "inspect", container_name]
            result = await self._run_command(cmd)
            
            if result["success"]:
                container_data = json.loads(result["output"])[0]
                return {
                    "container_id": container_data["Id"],
                    "status": container_data["State"]["Status"],
                    "started_at": container_data["State"]["StartedAt"],
                    "ports": container_data["NetworkSettings"]["Ports"]
                }
            
            return {}
            
        except Exception:
            return {}

class BuildToolExecutor:
    """
    Universal build tool executor for various project types.
    """
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path).resolve()
        self.file_manager = FileOperationsManager(base_path)
        
        # Build tool configurations
        self.build_tools = {
            'python': {
                'requirements_files': ['requirements.txt', 'pyproject.toml', 'setup.py'],
                'build_commands': ['pip install -r requirements.txt', 'python setup.py install'],
                'test_commands': ['pytest', 'python -m pytest', 'python -m unittest'],
                'lint_commands': ['flake8', 'black --check', 'pylint']
            },
            'node': {
                'requirements_files': ['package.json', 'yarn.lock'],
                'build_commands': ['npm install', 'npm run build', 'yarn install', 'yarn build'],
                'test_commands': ['npm test', 'yarn test'],
                'lint_commands': ['npm run lint', 'yarn lint']
            },
            'rust': {
                'requirements_files': ['Cargo.toml'],
                'build_commands': ['cargo build', 'cargo build --release'],
                'test_commands': ['cargo test'],
                'lint_commands': ['cargo clippy']
            },
            'go': {
                'requirements_files': ['go.mod', 'go.sum'],
                'build_commands': ['go build', 'go mod download'],
                'test_commands': ['go test ./...'],
                'lint_commands': ['go vet', 'golint']
            },
            'java': {
                'requirements_files': ['pom.xml', 'build.gradle'],
                'build_commands': ['mvn compile', 'gradle build'],
                'test_commands': ['mvn test', 'gradle test'],
                'lint_commands': ['mvn checkstyle:check']
            },
            'make': {
                'requirements_files': ['Makefile'],
                'build_commands': ['make', 'make build'],
                'test_commands': ['make test'],
                'lint_commands': ['make lint']
            }
        }
    
    def detect_project_type(self) -> Dict[str, Any]:
        """Auto-detect project type based on files present."""
        
        detected_types = []
        
        for project_type, config in self.build_tools.items():
            for req_file in config['requirements_files']:
                if (self.base_path / req_file).exists():
                    detected_types.append({
                        'type': project_type,
                        'confidence': 1.0,
                        'indicator_file': req_file
                    })
                    break
        
        return {
            "detected_types": detected_types,
            "primary_type": detected_types[0]['type'] if detected_types else 'unknown',
            "base_path": str(self.base_path)
        }
    
    async def build_project(
        self,
        project_type: str = "auto",
        build_command: str = None,
        console: Console = None
    ) -> Dict[str, Any]:
        """Build project using appropriate build tool."""
        
        try:
            if project_type == "auto":
                detection = self.detect_project_type()
                project_type = detection["primary_type"]
                
                if project_type == "unknown":
                    return {
                        "success": False,
                        "error": "Could not auto-detect project type"
                    }
            
            if project_type not in self.build_tools:
                return {
                    "success": False,
                    "error": f"Unsupported project type: {project_type}"
                }
            
            config = self.build_tools[project_type]
            
            if build_command:
                commands = [build_command]
            else:
                commands = config['build_commands']
            
            results = []
            
            for cmd in commands:
                if console:
                    console.print(f"[bold blue]Executing: {cmd}[/bold blue]")
                
                result = await self._run_build_command(cmd, console)
                results.append(result)
                
                if not result["success"]:
                    break
            
            overall_success = all(r["success"] for r in results)
            
            return {
                "success": overall_success,
                "project_type": project_type,
                "commands_executed": [r["command"] for r in results],
                "results": results,
                "build_artifacts": self._find_build_artifacts(project_type)
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Build error: {str(e)}"
            }
    
    async def test_project(
        self,
        project_type: str = "auto",
        test_command: str = None,
        console: Console = None
    ) -> Dict[str, Any]:
        """Run tests for the project."""
        
        try:
            if project_type == "auto":
                detection = self.detect_project_type()
                project_type = detection["primary_type"]
            
            if project_type not in self.build_tools:
                return {
                    "success": False,
                    "error": f"Unsupported project type: {project_type}"
                }
            
            config = self.build_tools[project_type]
            
            if test_command:
                commands = [test_command]
            else:
                commands = config['test_commands']
            
            results = []
            
            for cmd in commands:
                if console:
                    console.print(f"[bold green]Testing: {cmd}[/bold green]")
                
                result = await self._run_build_command(cmd, console)
                results.append(result)
                
                if result["success"]:
                    break  # Stop on first successful test command
            
            # At least one test command should succeed
            overall_success = any(r["success"] for r in results)
            
            return {
                "success": overall_success,
                "project_type": project_type,
                "test_results": results
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Test error: {str(e)}"
            }
    
    async def lint_project(
        self,
        project_type: str = "auto",
        lint_command: str = None,
        console: Console = None
    ) -> Dict[str, Any]:
        """Run linting for the project."""
        
        try:
            if project_type == "auto":
                detection = self.detect_project_type()
                project_type = detection["primary_type"]
            
            if project_type not in self.build_tools:
                return {
                    "success": False,
                    "error": f"Unsupported project type: {project_type}"
                }
            
            config = self.build_tools[project_type]
            
            if lint_command:
                commands = [lint_command]
            else:
                commands = config['lint_commands']
            
            results = []
            
            for cmd in commands:
                if console:
                    console.print(f"[bold yellow]Linting: {cmd}[/bold yellow]")
                
                result = await self._run_build_command(cmd, console)
                results.append(result)
            
            # Linting can have warnings, so we check if any major errors occurred
            major_failures = [r for r in results if not r["success"] and r.get("exit_code", 0) > 1]
            overall_success = len(major_failures) == 0
            
            return {
                "success": overall_success,
                "project_type": project_type,
                "lint_results": results,
                "warnings": len([r for r in results if r.get("exit_code") == 1]),
                "errors": len(major_failures)
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Lint error: {str(e)}"
            }
    
    def _find_build_artifacts(self, project_type: str) -> List[str]:
        """Find common build artifacts for project type."""
        
        artifacts = []
        
        artifact_patterns = {
            'python': ['dist/*', 'build/*', '*.egg-info'],
            'node': ['dist/*', 'build/*', 'node_modules'],
            'rust': ['target/*'],
            'go': ['*.exe', 'main'],
            'java': ['target/*', 'build/*', '*.jar'],
            'make': ['*.o', '*.so', 'build/*']
        }
        
        if project_type in artifact_patterns:
            for pattern in artifact_patterns[project_type]:
                artifacts.extend([str(p) for p in self.base_path.glob(pattern)])
        
        return artifacts
    
    async def _run_build_command(self, command: str, console: Console = None) -> Dict[str, Any]:
        """Run a build command."""
        
        try:
            cmd_parts = command.split()
            
            process = await asyncio.create_subprocess_exec(
                *cmd_parts,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=self.base_path
            )
            
            stdout, stderr = await process.communicate()
            
            output = stdout.decode().strip()
            error = stderr.decode().strip()
            
            success = process.returncode == 0
            
            if console:
                if success:
                    console.print(f"[green]✓ {command} completed[/green]")
                else:
                    console.print(f"[red]✗ {command} failed (exit {process.returncode})[/red]")
                
                if output and len(output) < 500:
                    console.print(f"[dim]{output}[/dim]")
                elif output:
                    console.print(f"[dim]{output[:200]}... (truncated)[/dim]")
                
                if error:
                    console.print(f"[red]{error[:200]}{'...' if len(error) > 200 else ''}[/red]")
            
            return {
                "success": success,
                "command": command,
                "output": output,
                "error": error,
                "exit_code": process.returncode
            }
            
        except Exception as e:
            return {
                "success": False,
                "command": command,
                "error": f"Command execution failed: {str(e)}"
            }

class FileBuildExecutor:
    """
    Main file operations and build executor that combines all capabilities.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.base_path = config.get('working_directory', '.')
        
        # Initialize component managers
        self.file_manager = FileOperationsManager(self.base_path)
        self.docker_builder = DockerBuilder(self.base_path)
        self.build_executor = BuildToolExecutor(self.base_path)
        
        print(f"File Build Executor initialized")
        print(f"Base path: {self.base_path}")
        print(f"Capabilities: File operations, Docker builds, Multi-language builds")
    
    async def execute(
        self,
        operation: str,
        params: Dict[str, Any],
        console: Console,
        step_id: str
    ) -> Tuple[bool, Any]:
        """Execute file operation or build task."""
        
        try:
            console.print(f"\n[bold cyan]Executing file/build operation: {operation}[/bold cyan]")
            console.print(f"Step ID: {step_id}")
            console.print(f"Parameters: {params}")
            
            if operation == "read_file":
                return await self._execute_read_file(params, console)
            elif operation == "write_file":
                return await self._execute_write_file(params, console)
            elif operation == "list_files":
                return await self._execute_list_files(params, console)
            elif operation == "copy_file":
                return await self._execute_copy_file(params, console)
            elif operation == "template_file":
                return await self._execute_template_file(params, console)
            elif operation == "build_docker":
                return await self._execute_build_docker(params, console)
            elif operation == "run_docker":
                return await self._execute_run_docker(params, console)
            elif operation == "docker_compose":
                return await self._execute_docker_compose(params, console)
            elif operation == "generate_dockerfile":
                return await self._execute_generate_dockerfile(params, console)
            elif operation == "build_project":
                return await self._execute_build_project(params, console)
            elif operation == "test_project":
                return await self._execute_test_project(params, console)
            elif operation == "lint_project":
                return await self._execute_lint_project(params, console)
            elif operation == "detect_project":
                return await self._execute_detect_project(params, console)
            else:
                return False, f"Unknown operation: {operation}"
                
        except Exception as e:
            error_msg = f"Exception during file/build operation: {str(e)}"
            console.print(f"[bold red]  {error_msg}[/bold red]")
            return False, error_msg
    
    async def _execute_read_file(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute file reading operation."""
        
        file_path = params.get('file_path', params.get('path'))
        if not file_path:
            return False, "file_path parameter required"
        
        result = self.file_manager.read_file(file_path)
        
        if result["success"]:
            console.print(f"[green]✓ Successfully read file: {file_path}[/green]")
            console.print(f"[dim]Size: {result['size']} bytes, Format: {result['format']}[/dim]")
        else:
            console.print(f"[red]✗ Failed to read file: {result['error']}[/red]")
        
        return result["success"], result
    
    async def _execute_write_file(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute file writing operation."""
        
        file_path = params.get('file_path', params.get('path'))
        content = params.get('content')
        format_type = params.get('format', 'auto')
        
        if not file_path or content is None:
            return False, "file_path and content parameters required"
        
        result = self.file_manager.write_file(file_path, content, format_type)
        
        if result["success"]:
            console.print(f"[green]✓ Successfully wrote file: {file_path}[/green]")
            console.print(f"[dim]Size: {result['size']} bytes[/dim]")
        else:
            console.print(f"[red]✗ Failed to write file: {result['error']}[/red]")
        
        return result["success"], result
    
    async def _execute_list_files(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute file listing operation."""
        
        directory = params.get('directory', '.')
        pattern = params.get('pattern', '*')
        recursive = params.get('recursive', False)
        
        result = self.file_manager.list_files(directory, pattern, recursive)
        
        if result["success"]:
            console.print(f"[green]✓ Found {result['count']} files in {directory}[/green]")
            
            # Display file table
            if result['files']:
                table = Table(title="Files Found")
                table.add_column("Name", style="cyan")
                table.add_column("Size", justify="right")
                table.add_column("Modified", style="dim")
                
                for file_info in result['files'][:10]:  # Show first 10
                    table.add_row(
                        file_info['name'],
                        f"{file_info['size']} bytes",
                        file_info['modified'][:19]
                    )
                
                console.print(table)
                
                if len(result['files']) > 10:
                    console.print(f"[dim]... and {len(result['files']) - 10} more files[/dim]")
        else:
            console.print(f"[red]✗ Failed to list files: {result['error']}[/red]")
        
        return result["success"], result
    
    async def _execute_copy_file(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute file copy operation."""
        
        source = params.get('source')
        destination = params.get('destination')
        
        if not source or not destination:
            return False, "source and destination parameters required"
        
        result = self.file_manager.copy_file(source, destination)
        
        if result["success"]:
            console.print(f"[green]✓ Successfully copied: {source} → {destination}[/green]")
        else:
            console.print(f"[red]✗ Failed to copy file: {result['error']}[/red]")
        
        return result["success"], result
    
    async def _execute_template_file(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute template processing operation."""
        
        template_path = params.get('template_path')
        output_path = params.get('output_path')
        variables = params.get('variables', {})
        
        if not template_path or not output_path:
            return False, "template_path and output_path parameters required"
        
        result = self.file_manager.template_file(template_path, output_path, variables)
        
        if result["success"]:
            console.print(f"[green]✓ Successfully processed template: {template_path} → {output_path}[/green]")
            console.print(f"[dim]Variables: {list(variables.keys())}[/dim]")
        else:
            console.print(f"[red]✗ Failed to process template: {result['error']}[/red]")
        
        return result["success"], result
    
    async def _execute_build_docker(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute Docker image build."""
        
        dockerfile_path = params.get('dockerfile_path', 'Dockerfile')
        image_name = params.get('image_name', 'saturn-build')
        build_context = params.get('build_context', '.')
        build_args = params.get('build_args', {})
        
        result = await self.docker_builder.build_image(
            dockerfile_path, image_name, build_context, build_args, console
        )
        
        return result["success"], result
    
    async def _execute_run_docker(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute Docker container run."""
        
        image_name = params.get('image_name')
        if not image_name:
            return False, "image_name parameter required"
        
        container_name = params.get('container_name')
        ports = params.get('ports', {})
        volumes = params.get('volumes', {})
        environment = params.get('environment', {})
        command = params.get('command')
        detached = params.get('detached', True)
        
        result = await self.docker_builder.run_container(
            image_name, container_name, ports, volumes, environment, command, detached, console
        )
        
        return result["success"], result
    
    async def _execute_docker_compose(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute Docker Compose operation."""
        
        compose_file = params.get('compose_file', 'docker-compose.yml')
        detached = params.get('detached', True)
        build = params.get('build', False)
        
        result = await self.docker_builder.compose_up(compose_file, detached, build, console)
        
        return result["success"], result
    
    async def _execute_generate_dockerfile(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute Dockerfile generation."""
        
        base_image = params.get('base_image', 'python:3.11-slim')
        working_dir = params.get('working_dir', '/app')
        dependencies_file = params.get('dependencies_file')
        start_command = params.get('start_command')
        output_path = params.get('output_path', 'Dockerfile')
        
        result = self.docker_builder.generate_dockerfile(
            base_image, working_dir, dependencies_file, start_command, output_path
        )
        
        if result["success"]:
            console.print(f"[green]✓ Generated Dockerfile: {output_path}[/green]")
        else:
            console.print(f"[red]✗ Failed to generate Dockerfile: {result['error']}[/red]")
        
        return result["success"], result
    
    async def _execute_build_project(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute project build."""
        
        project_type = params.get('project_type', 'auto')
        build_command = params.get('build_command')
        
        result = await self.build_executor.build_project(project_type, build_command, console)
        
        return result["success"], result
    
    async def _execute_test_project(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute project tests."""
        
        project_type = params.get('project_type', 'auto')
        test_command = params.get('test_command')
        
        result = await self.build_executor.test_project(project_type, test_command, console)
        
        return result["success"], result
    
    async def _execute_lint_project(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute project linting."""
        
        project_type = params.get('project_type', 'auto')
        lint_command = params.get('lint_command')
        
        result = await self.build_executor.lint_project(project_type, lint_command, console)
        
        return result["success"], result
    
    async def _execute_detect_project(self, params: Dict[str, Any], console: Console) -> Tuple[bool, Any]:
        """Execute project type detection."""
        
        result = self.build_executor.detect_project_type()
        
        console.print(f"[green]✓ Detected project types: {[t['type'] for t in result['detected_types']]}[/green]")
        console.print(f"[dim]Primary type: {result['primary_type']}[/dim]")
        
        return True, result
    
    def get_supported_operations(self) -> List[str]:
        """Get list of supported operations."""
        
        return [
            "read_file", "write_file", "list_files", "copy_file", "template_file",
            "build_docker", "run_docker", "docker_compose", "generate_dockerfile",
            "build_project", "test_project", "lint_project", "detect_project"
        ]
    
    def get_operation_schema(self, operation: str) -> Dict[str, Any]:
        """Get parameter schema for an operation."""
        
        schemas = {
            "read_file": {
                "required": ["file_path"],
                "optional": [],
                "description": "Read content from a file"
            },
            "write_file": {
                "required": ["file_path", "content"],
                "optional": ["format"],
                "description": "Write content to a file"
            },
            "list_files": {
                "required": [],
                "optional": ["directory", "pattern", "recursive"],
                "description": "List files in directory"
            },
            "copy_file": {
                "required": ["source", "destination"],
                "optional": [],
                "description": "Copy file from source to destination"
            },
            "template_file": {
                "required": ["template_path", "output_path"],
                "optional": ["variables"],
                "description": "Process template file with variable substitution"
            },
            "build_docker": {
                "required": [],
                "optional": ["dockerfile_path", "image_name", "build_context", "build_args"],
                "description": "Build Docker image"
            },
            "run_docker": {
                "required": ["image_name"],
                "optional": ["container_name", "ports", "volumes", "environment", "command", "detached"],
                "description": "Run Docker container"
            },
            "docker_compose": {
                "required": [],
                "optional": ["compose_file", "detached", "build"],
                "description": "Run Docker Compose"
            },
            "generate_dockerfile": {
                "required": [],
                "optional": ["base_image", "working_dir", "dependencies_file", "start_command", "output_path"],
                "description": "Generate Dockerfile"
            },
            "build_project": {
                "required": [],
                "optional": ["project_type", "build_command"],
                "description": "Build project using detected or specified build tool"
            },
            "test_project": {
                "required": [],
                "optional": ["project_type", "test_command"],
                "description": "Run tests for project"
            },
            "lint_project": {
                "required": [],
                "optional": ["project_type", "lint_command"],
                "description": "Run linting for project"
            },
            "detect_project": {
                "required": [],
                "optional": [],
                "description": "Auto-detect project type"
            }
        }
        
        return schemas.get(operation, {}) 