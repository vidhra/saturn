# Saturn File Operations & Build Tooling System

## Overview

The Saturn File Operations & Build Tooling System extends Saturn's capabilities beyond cloud CLI and Terraform to include comprehensive file operations, Docker builds, and multi-language project builds. This system enables Saturn to handle complete development and deployment workflows.

## Architecture

### Core Components

```
FileBuildExecutor (Main Interface)
├── FileOperationsManager (File I/O)
├── DockerBuilder (Container Operations)
└── BuildToolExecutor (Multi-language Builds)
```

### Key Features

- **Universal File Operations**: Read, write, copy, list files in multiple formats
- **Docker Integration**: Build images, run containers, Docker Compose support
- **Multi-language Support**: Auto-detect and build Python, Node.js, Rust, Go, Java, C/Make projects
- **Template Processing**: Variable substitution for configuration files
- **Project Detection**: Automatic identification of project types
- **Build Automation**: Test, lint, and build operations

## Supported Operations

### File Operations

| Operation | Description | Required Parameters | Optional Parameters |
|-----------|-------------|-------------------|-------------------|
| `read_file` | Read content from any supported file | `file_path` | - |
| `write_file` | Write content to file in specified format | `file_path`, `content` | `format` |
| `list_files` | List files in directory with pattern matching | - | `directory`, `pattern`, `recursive` |
| `copy_file` | Copy file from source to destination | `source`, `destination` | - |
| `template_file` | Process template with variable substitution | `template_path`, `output_path` | `variables` |

### Docker Operations

| Operation | Description | Required Parameters | Optional Parameters |
|-----------|-------------|-------------------|-------------------|
| `build_docker` | Build Docker image from Dockerfile | - | `dockerfile_path`, `image_name`, `build_context`, `build_args` |
| `run_docker` | Run Docker container | `image_name` | `container_name`, `ports`, `volumes`, `environment`, `command`, `detached` |
| `docker_compose` | Run Docker Compose | - | `compose_file`, `detached`, `build` |
| `generate_dockerfile` | Generate Dockerfile for project | - | `base_image`, `working_dir`, `dependencies_file`, `start_command`, `output_path` |

### Project Build Operations

| Operation | Description | Required Parameters | Optional Parameters |
|-----------|-------------|-------------------|-------------------|
| `detect_project` | Auto-detect project type | - | - |
| `build_project` | Build project using appropriate tool | - | `project_type`, `build_command` |
| `test_project` | Run tests for project | - | `project_type`, `test_command` |
| `lint_project` | Run linting for project | - | `project_type`, `lint_command` |

## Supported File Formats

### Input/Output Formats

- **JSON** (`.json`) - Full read/write support with automatic parsing
- **YAML** (`.yaml`, `.yml`) - Full read/write support with automatic parsing
- **TOML** (`.toml`) - Full read/write support with automatic parsing
- **Text** (`.txt`, `.md`, `.py`, `.js`, `.ts`, `.sh`) - Raw text content
- **Environment** (`.env`) - Key-value pairs parsing
- **Dockerfile** - Docker configuration files

### Template Processing

Simple variable substitution using `{{variable_name}}` syntax:

```markdown
# {{app_name}} Configuration

Version: {{version}}
Environment: {{environment}}

Database: {{db_host}}:{{db_port}}
```

## Supported Project Types

### Auto-Detection Based On

| Language | Detection Files | Build Commands | Test Commands | Lint Commands |
|----------|----------------|----------------|---------------|---------------|
| **Python** | `requirements.txt`, `pyproject.toml`, `setup.py` | `pip install -r requirements.txt`, `python setup.py install` | `pytest`, `python -m unittest` | `flake8`, `black --check`, `pylint` |
| **Node.js** | `package.json`, `yarn.lock` | `npm install`, `npm run build`, `yarn install` | `npm test`, `yarn test` | `npm run lint`, `yarn lint` |
| **Rust** | `Cargo.toml` | `cargo build`, `cargo build --release` | `cargo test` | `cargo clippy` |
| **Go** | `go.mod`, `go.sum` | `go build`, `go mod download` | `go test ./...` | `go vet`, `golint` |
| **Java** | `pom.xml`, `build.gradle` | `mvn compile`, `gradle build` | `mvn test`, `gradle test` | `mvn checkstyle:check` |
| **C/Make** | `Makefile` | `make`, `make build` | `make test` | `make lint` |

## Usage Examples

### Basic File Operations

```python
from saturn.file_build_executor import FileBuildExecutor
from rich.console import Console

# Initialize
config = {'working_directory': '/path/to/project'}
executor = FileBuildExecutor(config)
console = Console()

# Write JSON configuration
success, result = await executor.execute(
    "write_file",
    {
        "file_path": "config.json",
        "content": {
            "app_name": "My App",
            "version": "1.0.0",
            "debug": True
        }
    },
    console,
    "write_config"
)

# Read and process template
success, result = await executor.execute(
    "template_file",
    {
        "template_path": "app.template",
        "output_path": "app_config.yml", 
        "variables": {
            "app_name": "Saturn Demo",
            "version": "2.0.0",
            "environment": "production"
        }
    },
    console,
    "process_template"
)

# List all Python files recursively
success, result = await executor.execute(
    "list_files",
    {
        "directory": "src",
        "pattern": "*.py",
        "recursive": True
    },
    console,
    "list_python_files"
)
```

### Docker Operations

```python
# Generate Dockerfile for Python project
success, result = await executor.execute(
    "generate_dockerfile",
    {
        "base_image": "python:3.11-slim",
        "working_dir": "/app",
        "dependencies_file": "requirements.txt",
        "start_command": '["python", "app.py"]'
    },
    console,
    "generate_dockerfile"
)

# Build Docker image
success, result = await executor.execute(
    "build_docker",
    {
        "dockerfile_path": "Dockerfile",
        "image_name": "my-app:latest",
        "build_context": ".",
        "build_args": {"PYTHON_VERSION": "3.11"}
    },
    console,
    "build_image"
)

# Run container with port mapping
success, result = await executor.execute(
    "run_docker",
    {
        "image_name": "my-app:latest",
        "container_name": "my-app-container",
        "ports": {"8000": "8000"},
        "environment": {"ENV": "production"},
        "volumes": {"/host/data": "/app/data"}
    },
    console,
    "run_container"
)

# Run Docker Compose
success, result = await executor.execute(
    "docker_compose",
    {
        "compose_file": "docker-compose.yml",
        "detached": True,
        "build": True
    },
    console,
    "compose_up"
)
```

### Project Build Operations

```python
# Auto-detect project type
success, result = await executor.execute(
    "detect_project",
    {},
    console,
    "detect_project_type"
)

print(f"Detected project type: {result['primary_type']}")

# Build project using detected type
success, result = await executor.execute(
    "build_project",
    {"project_type": "auto"},  # Uses auto-detection
    console,
    "build_project"
)

# Run tests
success, result = await executor.execute(
    "test_project",
    {"project_type": "python"},
    console,
    "run_tests"
)

# Custom build command
success, result = await executor.execute(
    "build_project",
    {
        "project_type": "python",
        "build_command": "pip install -e ."
    },
    console,
    "custom_build"
)
```

### Advanced Template Example

```python
# Create complex template
template_content = """
# {{project_name}} CI/CD Pipeline

name: Build {{project_name}}
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Setup {{language}}
      uses: actions/setup-{{language}}@v3
      with:
        {{language}}-version: '{{language_version}}'
    - name: Install dependencies
      run: {{install_command}}
    - name: Build
      run: {{build_command}}
    - name: Test
      run: {{test_command}}
"""

# Write template
await executor.execute(
    "write_file",
    {"file_path": "ci.template", "content": template_content},
    console,
    "create_template"
)

# Process with variables
await executor.execute(
    "template_file",
    {
        "template_path": "ci.template",
        "output_path": ".github/workflows/ci.yml",
        "variables": {
            "project_name": "Saturn Demo",
            "language": "python",
            "language_version": "3.11",
            "install_command": "pip install -r requirements.txt",
            "build_command": "python setup.py build",
            "test_command": "pytest"
        }
    },
    console,
    "generate_ci"
)
```

## Integration with Saturn Architecture

### With Terraform Executor

```python
# Complete deployment pipeline
async def deploy_application():
    # 1. Build application
    await file_executor.execute(
        "build_project",
        {"project_type": "auto"},
        console,
        "build_app"
    )
    
    # 2. Build Docker image
    await file_executor.execute(
        "build_docker",
        {"image_name": "my-app:latest"},
        console,
        "build_image"
    )
    
    # 3. Deploy with Terraform
    await terraform_executor.execute(
        "gcloud container clusters create my-cluster --zone=us-central1-a",
        console,
        "create_cluster"
    )
    
    # 4. Generate Kubernetes manifests
    await file_executor.execute(
        "template_file",
        {
            "template_path": "k8s.template",
            "output_path": "deployment.yaml",
            "variables": {"image": "my-app:latest"}
        },
        console,
        "generate_k8s"
    )
```

### DAG Integration

```python
# Define complex workflow DAG
workflow_dag = {
    "execution_order": [
        "detect_project",
        "build_project", 
        "test_project",
        "build_docker",
        "deploy_terraform"
    ],
    "nodes": {
        "detect_project": {
            "executor": "file_build",
            "operation": "detect_project",
            "params": {}
        },
        "build_project": {
            "executor": "file_build", 
            "operation": "build_project",
            "params": {"project_type": "auto"}
        },
        "test_project": {
            "executor": "file_build",
            "operation": "test_project", 
            "params": {"project_type": "auto"}
        },
        "build_docker": {
            "executor": "file_build",
            "operation": "build_docker",
            "params": {"image_name": "saturn-app:latest"}
        },
        "deploy_terraform": {
            "executor": "terraform",
            "operation": "execute",
            "params": {"command": "gcloud run deploy saturn-app --image=saturn-app:latest"}
        }
    }
}
```

## Error Handling

All operations return a tuple `(success: bool, result: Dict)`:

```python
success, result = await executor.execute(operation, params, console, step_id)

if success:
    # Operation completed successfully
    print(f"Success: {result}")
else:
    # Handle error
    print(f"Error: {result.get('error', 'Unknown error')}")
```

### Common Error Types

- **File Not Found**: `file_path` doesn't exist
- **Permission Denied**: Insufficient permissions for file operations
- **Invalid Format**: Unsupported file format or malformed content
- **Docker Not Available**: Docker daemon not running
- **Build Tool Missing**: Required build tools not installed
- **Template Error**: Variable substitution failed

## Configuration

### FileBuildExecutor Configuration

```python
config = {
    'working_directory': '/path/to/project',  # Base directory for operations
    'docker_registry': 'your-registry.com',   # Optional Docker registry
    'build_timeout': 300,                     # Build timeout in seconds
    'keep_temp_files': False,                 # Keep temporary files for debugging
    'parallel_builds': True,                  # Allow parallel operations
}

executor = FileBuildExecutor(config)
```

### Environment Variables

```bash
# Docker configuration
export DOCKER_REGISTRY=your-registry.com
export DOCKER_USERNAME=your-username
export DOCKER_PASSWORD=your-password

# Build tool paths
export PYTHON_PATH=/usr/bin/python3
export NODE_PATH=/usr/bin/node
export CARGO_PATH=/usr/bin/cargo
export GO_PATH=/usr/bin/go
```

## Extensibility

### Adding New Project Types

```python
# Extend BuildToolExecutor
class CustomBuildExecutor(BuildToolExecutor):
    def __init__(self, base_path: str = "."):
        super().__init__(base_path)
        
        # Add custom project type
        self.build_tools['dart'] = {
            'requirements_files': ['pubspec.yaml'],
            'build_commands': ['dart pub get', 'dart compile exe'],
            'test_commands': ['dart test'],
            'lint_commands': ['dart analyze']
        }

# Use custom executor
executor = FileBuildExecutor(config)
executor.build_executor = CustomBuildExecutor(config['working_directory'])
```

### Custom File Format Support

```python
# Extend FileOperationsManager
class CustomFileManager(FileOperationsManager):
    def __init__(self, base_path: str = "."):
        super().__init__(base_path)
        
        # Add custom format
        self.supported_formats['.custom'] = self._read_custom_format
    
    def _read_custom_format(self, path: Path):
        # Custom parsing logic
        with open(path, 'r') as f:
            return self.parse_custom_format(f.read())

# Use custom manager  
executor = FileBuildExecutor(config)
executor.file_manager = CustomFileManager(config['working_directory'])
```

## Performance Considerations

### Async Operations

All operations are async and can be parallelized:

```python
# Parallel file operations
tasks = [
    executor.execute("read_file", {"file_path": f"file{i}.json"}, console, f"read_{i}")
    for i in range(10)
]

results = await asyncio.gather(*tasks)
```

### Large File Handling

- **Streaming**: Large files are processed in chunks
- **Memory Management**: Automatic cleanup of temporary files
- **Progress Tracking**: Rich progress bars for long operations

### Build Optimization

- **Dependency Caching**: Reuse dependency installations
- **Layer Caching**: Docker layer optimization
- **Parallel Builds**: Multiple projects can build simultaneously

## Security Considerations

### File Operations

- **Path Validation**: All paths are validated and sandboxed
- **Permission Checks**: Operations respect file system permissions
- **Symlink Protection**: Symlinks are resolved safely

### Docker Operations

- **Image Scanning**: Optional vulnerability scanning
- **Registry Authentication**: Secure credential handling
- **Network Isolation**: Containers run in isolated networks

### Build Security

- **Dependency Verification**: Check package signatures when available
- **Sandbox Execution**: Build operations run in controlled environment
- **Secret Management**: Environment variables are handled securely

## Monitoring and Logging

### Rich Console Output

- **Progress Bars**: Visual progress for long operations
- **Color Coding**: Success/error status with colors
- **Detailed Tables**: File listings and operation results

### Logging Integration

```python
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Operations automatically log to Saturn's logging system
executor = FileBuildExecutor(config)
```

### Metrics Collection

- **Operation Times**: Track execution duration
- **Success Rates**: Monitor operation success/failure rates
- **Resource Usage**: Memory and CPU monitoring for builds

## Troubleshooting

### Common Issues

1. **File Not Found Errors**
   ```bash
   # Check working directory
   pwd
   ls -la
   ```

2. **Docker Build Failures** 
   ```bash
   # Check Docker daemon
   docker info
   
   # Check Dockerfile syntax
   docker build --dry-run .
   ```

3. **Build Tool Missing**
   ```bash
   # Install missing tools
   pip install -r requirements.txt  # Python
   npm install                      # Node.js
   cargo build                      # Rust
   ```

4. **Permission Denied**
   ```bash
   # Fix permissions
   chmod +x script.sh
   sudo chown -R user:group directory/
   ```

### Debug Mode

```python
config = {
    'working_directory': '.',
    'debug_mode': True,
    'keep_temp_files': True,
    'verbose_logging': True
}

executor = FileBuildExecutor(config)
```

## Best Practices

### File Organization

```
project/
├── src/                    # Source code
├── tests/                  # Test files  
├── docs/                   # Documentation
├── templates/              # Template files
├── docker/                 # Docker configurations
│   ├── Dockerfile
│   └── docker-compose.yml
├── .saturn/                # Saturn configurations
│   ├── config.json
│   └── templates/
└── requirements.txt        # Dependencies
```

### Template Management

- Use descriptive variable names: `{{database_host}}` vs `{{host}}`
- Validate variables before processing
- Version control templates separately
- Document available variables

### Docker Best Practices

- Use multi-stage builds for smaller images
- Pin base image versions
- Add health checks to containers
- Use .dockerignore to exclude files

### Build Optimization

- Cache dependencies between builds
- Use parallel builds when possible
- Run tests before building Docker images
- Implement build caching strategies

## Future Enhancements

### Planned Features

- **Kubernetes Integration**: Direct K8s manifest generation and deployment
- **CI/CD Pipelines**: Built-in GitHub Actions/GitLab CI generation
- **Package Management**: Enhanced dependency management across languages
- **Cloud Storage**: Integration with S3, GCS for file operations
- **Monitoring**: Built-in application performance monitoring
- **Security Scanning**: Automated vulnerability scanning for dependencies and images

### Plugin System

```python
# Future plugin architecture
class SaturnPlugin:
    def register_operations(self) -> Dict[str, callable]:
        pass
    
    def register_file_formats(self) -> Dict[str, callable]:
        pass

# Plugin registration
executor.register_plugin(KubernetesPlugin())
executor.register_plugin(SecurityScanPlugin())
```

---

## Conclusion

The Saturn File Operations & Build Tooling System provides a comprehensive platform for managing files, building projects, and handling Docker operations. It seamlessly integrates with Saturn's existing Terraform and cloud CLI capabilities to provide end-to-end deployment automation.

Key benefits:

- **Universal**: Supports all major programming languages and build tools
- **Integrated**: Works seamlessly with existing Saturn components
- **Extensible**: Easy to add new project types and operations
- **Secure**: Built-in security and sandboxing features
- **Performant**: Async operations with parallel execution support
- **User-Friendly**: Rich console output and comprehensive error handling

This system transforms Saturn from a cloud CLI tool into a complete DevOps automation platform. 