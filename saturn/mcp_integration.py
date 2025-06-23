# MCP (Model Context Protocol) Integration for Saturn
import json
import asyncio
import logging
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
from dataclasses import dataclass, asdict
from enum import Enum

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# MCP SDK imports
try:
    from mcp import ClientSession, StdioServerParameters, types
    from mcp.client.stdio import stdio_client
    from mcp.client.streamable_http import streamablehttp_client
    MCP_AVAILABLE = True
    
    # Fallback for get_display_name if not available
    def get_display_name(tool):
        """Get display name for a tool, handling both dict and object formats."""
        try:
            if isinstance(tool, dict):
                # Handle dictionary-based tools (from Docker direct JSON-RPC)
                annotations = tool.get('annotations', {})
                return annotations.get('title', tool.get('name', 'Unknown Tool'))
            else:
                # Handle object-based tools (from MCP SDK)
                return getattr(tool, 'display_name', None) or getattr(tool, 'name', 'Unknown Tool')
        except (AttributeError, TypeError):
            return 'Unknown Tool'
        
except ImportError:
    MCP_AVAILABLE = False
    ClientSession = None
    StdioServerParameters = None
    types = None
    get_display_name = None


class MCPTransportType(Enum):
    """Supported MCP transport types."""
    STDIO = "stdio"
    HTTP = "http"
    STREAMABLE_HTTP = "streamable_http"


@dataclass
class MCPServerConfig:
    """Configuration for an MCP server."""
    name: str
    transport: MCPTransportType
    enabled: bool = True
    
    # STDIO transport parameters
    command: Optional[str] = None
    args: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    
    # HTTP transport parameters
    url: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    
    # Server metadata
    description: Optional[str] = None
    capabilities: Optional[List[str]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MCPServerConfig':
        """Create from dictionary representation."""
        # Convert transport string to enum
        if isinstance(data.get('transport'), str):
            data['transport'] = MCPTransportType(data['transport'])
        return cls(**data)


@dataclass
class MCPTool:
    """Represents a tool from an MCP server."""
    name: str
    description: str
    parameters: Dict[str, Any]
    server_name: str
    display_name: Optional[str] = None
    
    def to_openai_schema(self) -> Dict[str, Any]:
        """Convert to OpenAI-compatible tool schema."""
        return {
            "type": "function",
            "function": {
                "name": f"mcp_{self.server_name}_{self.name}",
                "description": f"[MCP:{self.server_name}] {self.description}",
                "parameters": self.parameters
            }
        }


class MCPServerManager:
    """Manages connections to multiple MCP servers."""
    
    def __init__(self, config_file: str = "mcp_servers.json"):
        self.config_file = Path(config_file)
        self.servers: Dict[str, MCPServerConfig] = {}
        self.sessions: Dict[str, ClientSession] = {}
        self.tools: Dict[str, List[MCPTool]] = {}
        self.console = Console()
        self.logger = logging.getLogger(__name__)
        
        # Load server configurations
        self._load_server_configs()
    
    def _load_server_configs(self):
        """Load MCP server configurations from file."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    self.servers = {
                        name: MCPServerConfig.from_dict(config)
                        for name, config in data.get('servers', {}).items()
                    }
                self.console.print(f"[green]✓ Loaded {len(self.servers)} MCP server configurations[/green]")
            except Exception as e:
                self.console.print(f"[red]✗ Error loading MCP configs: {e}[/red]")
                self.servers = {}
        else:
            # Create default configuration file
            self._create_default_config()
    
    def _create_default_config(self):
        """Create a default MCP server configuration file."""
        default_config = {
            "servers": {
                "filesystem": {
                    "name": "filesystem",
                    "transport": "stdio",
                    "command": "mcp-server-filesystem",
                    "args": ["--root", "."],
                    "description": "File system operations server",
                    "enabled": False
                },
                "git": {
                    "name": "git",
                    "transport": "stdio", 
                    "command": "mcp-server-git",
                    "args": ["--repository", "."],
                    "description": "Git operations server",
                    "enabled": False
                },
                "web_search": {
                    "name": "web_search",
                    "transport": "stdio",
                    "command": "mcp-server-brave-search",
                    "description": "Web search capabilities",
                    "enabled": False
                },
                "database": {
                    "name": "database",
                    "transport": "stdio",
                    "command": "mcp-server-sqlite",
                    "args": ["--db-path", "database.db"],
                    "description": "SQLite database operations",
                    "enabled": False
                }
            }
        }
        
        try:
            with open(self.config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            self.console.print(f"[yellow]📄 Created default MCP config: {self.config_file}[/yellow]")
            self.console.print("[dim]Edit the file to enable and configure MCP servers[/dim]")
        except Exception as e:
            self.console.print(f"[red]✗ Error creating default config: {e}[/red]")
    
    def add_server(self, config: MCPServerConfig):
        """Add a new MCP server configuration."""
        self.servers[config.name] = config
        self._save_configs()
    
    def remove_server(self, name: str):
        """Remove an MCP server configuration."""
        if name in self.servers:
            del self.servers[name]
            self._save_configs()
    
    def enable_server(self, name: str, enabled: bool = True):
        """Enable or disable an MCP server."""
        if name in self.servers:
            self.servers[name].enabled = enabled
            self._save_configs()
    
    def _save_configs(self):
        """Save server configurations to file."""
        try:
            config_data = {
                "servers": {
                    name: server.to_dict()
                    for name, server in self.servers.items()
                }
            }
            with open(self.config_file, 'w') as f:
                json.dump(config_data, f, indent=2)
        except Exception as e:
            self.console.print(f"[red]✗ Error saving configs: {e}[/red]")
    
    async def connect_to_servers(self) -> Dict[str, bool]:
        """Connect to all enabled MCP servers."""
        if not MCP_AVAILABLE:
            self.console.print("[red]✗ MCP SDK not available. Install with: pip install mcp[/red]")
            return {}
        
        connection_results = {}
        enabled_servers = {name: config for name, config in self.servers.items() if config.enabled}
        
        if not enabled_servers:
            self.console.print("[yellow]⚠️  No MCP servers enabled[/yellow]")
            return {}
        
        self.console.print(f"[bold blue]🔌 Connecting to {len(enabled_servers)} MCP servers...[/bold blue]")
        
        for name, config in enabled_servers.items():
            try:
                success = await self._connect_to_server(name, config)
                connection_results[name] = success
                
                if success:
                    self.console.print(f"[green]✓ Connected to {name}[/green]")
                else:
                    self.console.print(f"[red]✗ Failed to connect to {name}[/red]")
                    
            except Exception as e:
                self.console.print(f"[red]✗ Error connecting to {name}: {e}[/red]")
                connection_results[name] = False
        
        return connection_results
    
    async def _connect_to_server(self, name: str, config: MCPServerConfig) -> bool:
        """Connect to a single MCP server with timeout."""
        try:
            if config.transport == MCPTransportType.STDIO:
                # Use asyncio.wait_for to prevent hanging
                # Docker containers need more time
                timeout = 20.0 if config.command == "docker" else 10.0
                return await asyncio.wait_for(
                    self._connect_stdio_server(name, config),
                    timeout=timeout
                )
                
            elif config.transport == MCPTransportType.STREAMABLE_HTTP:
                if not config.url:
                    self.logger.error(f"No URL provided for HTTP server {name}")
                    return False
                
                return await asyncio.wait_for(
                    self._connect_http_server(name, config),
                    timeout=10.0
                )
                
            else:
                self.logger.error(f"Unsupported transport type: {config.transport}")
                return False
                
        except asyncio.TimeoutError:
            self.console.print(f"[yellow]⏰ Connection to {name} timed out[/yellow]")
            return False
        except Exception as e:
            self.logger.error(f"Failed to connect to {name}: {e}")
            return False

    async def _connect_stdio_server(self, name: str, config: MCPServerConfig) -> bool:
        """Connect to stdio MCP server with enhanced Docker support."""
        try:
            # For Docker-based servers, use direct JSON-RPC communication
            if config.command == "docker":
                return await self._connect_docker_server(name, config)
            
            # Merge environment variables properly for all servers
            import os
            merged_env = dict(os.environ)  # Start with current environment
            if config.env:
                merged_env.update(config.env)  # Add/override with config env vars
                self.console.print(f"[dim]Environment variables for {name}: {list(config.env.keys())}[/dim]")
            
            server_params = StdioServerParameters(
                command=config.command,
                args=config.args or [],
                env=merged_env  # Always pass merged environment
            )
            
            # Create stdio client connection
            client_context = stdio_client(server_params)
            read_stream, write_stream = await client_context.__aenter__()
            
            # Store the context for proper cleanup
            self._client_contexts = getattr(self, '_client_contexts', {})
            self._client_contexts[name] = client_context
            
            # Create session with longer timeout for Docker containers
            session = ClientSession(read_stream, write_stream)
            
            # Docker containers may need more time to initialize
            if config.command == "docker":
                # Give Docker-based servers more time to start up
                self.console.print(f"[blue]🐳 Docker container started for {name}, waiting for MCP protocol...[/blue]")
                await asyncio.sleep(3.0)  # Increased sleep time
                self.console.print(f"[blue]📡 Initializing MCP session for {name}...[/blue]")
                await asyncio.wait_for(session.initialize(), timeout=20.0)  # Increased timeout
            else:
                await asyncio.wait_for(session.initialize(), timeout=8.0)
            
            self.sessions[name] = session
            self.console.print(f"[green]✓ Successfully connected to {name}[/green]")
            return True
            
        except asyncio.TimeoutError:
            self.console.print(f"[yellow]⏰ {name} connection timed out during session initialization[/yellow]")
            return False
        except Exception as e:
            self.logger.error(f"STDIO connection error for {name}: {e}")
            return False

    async def _connect_docker_server(self, name: str, config: MCPServerConfig) -> bool:
        """Connect to Docker-based MCP server using direct JSON-RPC communication."""
        try:
            import asyncio
            import json
            import os
            
            # Prepare environment variables
            env = dict(os.environ)
            if config.env:
                env.update(config.env)
                self.console.print(f"[dim]Environment variables for {name}: {list(config.env.keys())}[/dim]")
            
            # Start Docker container
            cmd = [config.command] + (config.args or [])
            self.console.print(f"[blue]🐳 Starting Docker container: {' '.join(cmd)}[/blue]")
            
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env
            )
            
            # Wait for server to start
            self.console.print(f"[blue]📡 Waiting for Docker container to initialize...[/blue]")
            await asyncio.sleep(3.0)
            
            # Send MCP initialize message
            init_msg = {
                "jsonrpc": "2.0",
                "method": "initialize",
                "id": 1,
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {"name": "saturn-mcp", "version": "1.0.0"}
                }
            }
            
            # Send initialization
            init_json = json.dumps(init_msg) + "\n"
            process.stdin.write(init_json.encode())
            await process.stdin.drain()
            
            # Read response with timeout
            try:
                response_data = await asyncio.wait_for(
                    process.stdout.readline(), 
                    timeout=10.0
                )
                response = json.loads(response_data.decode().strip())
                
                if response.get("result") and response["result"].get("protocolVersion"):
                    self.console.print(f"[green]✓ Docker MCP server {name} initialized[/green]")
                    
                    # Get tools list
                    tools_msg = {
                        "jsonrpc": "2.0",
                        "method": "tools/list",
                        "id": 2,
                        "params": {}
                    }
                    
                    tools_json = json.dumps(tools_msg) + "\n"
                    process.stdin.write(tools_json.encode())
                    await process.stdin.drain()
                    
                    tools_response_data = await asyncio.wait_for(
                        process.stdout.readline(),
                        timeout=5.0
                    )
                    tools_response = json.loads(tools_response_data.decode().strip())
                    
                    if tools_response.get("result") and tools_response["result"].get("tools"):
                        tools = tools_response["result"]["tools"]
                        self.console.print(f"[green]✓ Retrieved {len(tools)} tools from {name}[/green]")
                        
                        # Store tools in a simple format for now
                        # We'll create a custom session wrapper for Docker servers
                        self.docker_processes = getattr(self, 'docker_processes', {})
                        self.docker_processes[name] = {
                            'process': process,
                            'tools': tools
                        }
                        
                        # Create mock session object for compatibility
                        class MockDockerSession:
                            def __init__(self, name, tools, process):
                                self.name = name
                                self.tools = tools
                                self.process = process
                            
                            async def list_tools(self):
                                return type('MockResult', (), {'tools': self.tools})()
                            
                            async def call_tool(self, tool_name: str, arguments: Dict[str, Any]):
                                """Call a tool via direct Docker JSON-RPC communication."""
                                try:
                                    # Send tool call message
                                    call_msg = {
                                        "jsonrpc": "2.0",
                                        "method": "tools/call",
                                        "id": 3,
                                        "params": {
                                            "name": tool_name,
                                            "arguments": arguments
                                        }
                                    }
                                    
                                    call_json = json.dumps(call_msg) + "\n"
                                    self.process.stdin.write(call_json.encode())
                                    await self.process.stdin.drain()
                                    
                                    # Read response with timeout
                                    response_data = await asyncio.wait_for(
                                        self.process.stdout.readline(),
                                        timeout=30.0  # GitHub API calls can take longer
                                    )
                                    response = json.loads(response_data.decode().strip())
                                    
                                    if response.get("result"):
                                        return response["result"]
                                    elif response.get("error"):
                                        raise Exception(f"MCP tool error: {response['error']}")
                                    else:
                                        raise Exception(f"Invalid response from MCP server: {response}")
                                        
                                except asyncio.TimeoutError:
                                    raise Exception(f"Timeout calling tool {tool_name}")
                                except Exception as e:
                                    raise Exception(f"Error calling tool {tool_name}: {e}")
                            
                            async def close(self):
                                if self.process and self.process.returncode is None:
                                    try:
                                        self.process.terminate()
                                        await asyncio.wait_for(self.process.wait(), timeout=2.0)
                                    except:
                                        pass
                        
                        self.sessions[name] = MockDockerSession(name, tools, process)
                        return True
                    else:
                        self.console.print(f"[yellow]⚠️  No tools received from {name}[/yellow]")
                        return False
                else:
                    self.console.print(f"[red]✗ Invalid initialize response from {name}[/red]")
                    return False
                    
            except asyncio.TimeoutError:
                self.console.print(f"[yellow]⏰ Docker server {name} initialization timed out[/yellow]")
                return False
                
        except Exception as e:
            self.console.print(f"[red]✗ Error connecting to Docker server {name}: {e}[/red]")
            return False

    async def _connect_http_server(self, name: str, config: MCPServerConfig) -> bool:
        """Connect to HTTP MCP server."""
        try:
            # Create HTTP client connection
            client_context = streamablehttp_client(config.url)
            read_stream, write_stream, _ = await client_context.__aenter__()
            
            # Store the context for proper cleanup
            self._client_contexts = getattr(self, '_client_contexts', {})
            self._client_contexts[name] = client_context
            
            # Create session
            session = ClientSession(read_stream, write_stream)
            await session.initialize()
            
            self.sessions[name] = session
            return True
            
        except Exception as e:
            self.logger.error(f"HTTP connection error for {name}: {e}")
            return False
    
    async def fetch_all_tools(self) -> Dict[str, List[MCPTool]]:
        """Fetch tools from all connected MCP servers."""
        all_tools = {}
        
        for server_name, session in self.sessions.items():
            try:
                tools = await self._fetch_server_tools(server_name, session)
                all_tools[server_name] = tools
                self.console.print(f"[green]📦 Fetched {len(tools)} tools from {server_name}[/green]")
                
            except Exception as e:
                self.console.print(f"[red]✗ Error fetching tools from {server_name}: {e}[/red]")
                all_tools[server_name] = []
        
        self.tools = all_tools
        return all_tools
    
    async def _fetch_server_tools(self, server_name: str, session: ClientSession) -> List[MCPTool]:
        """Fetch tools from a specific MCP server."""
        try:
            # Handle Docker servers with pre-fetched tools
            if hasattr(session, 'tools') and isinstance(session.tools, list):
                # Docker server with raw tool dictionaries
                mcp_tools = []
                for tool in session.tools:
                    if isinstance(tool, dict):
                        display_name = get_display_name(tool)
                        
                        mcp_tool = MCPTool(
                            name=tool.get('name', ''),
                            description=tool.get('description', ''),
                            parameters=tool.get('inputSchema', {}),
                            server_name=server_name,
                            display_name=display_name
                        )
                        mcp_tools.append(mcp_tool)
                    else:
                        # Regular MCP SDK tool object
                        display_name = get_display_name(tool)
                        
                        mcp_tool = MCPTool(
                            name=tool.name,
                            description=tool.description or "",
                            parameters=tool.inputSchema or {},
                            server_name=server_name,
                            display_name=display_name
                        )
                        mcp_tools.append(mcp_tool)
                
                return mcp_tools
            else:
                # Regular MCP SDK session
                tools_response = await session.list_tools()
                
                mcp_tools = []
                for tool in tools_response.tools:
                    display_name = get_display_name(tool)
                    
                    mcp_tool = MCPTool(
                        name=tool.name,
                        description=tool.description or "",
                        parameters=tool.inputSchema or {},
                        server_name=server_name,
                        display_name=display_name
                    )
                    mcp_tools.append(mcp_tool)
                
                return mcp_tools
            
        except Exception as e:
            self.logger.error(f"Error fetching tools from {server_name}: {e}")
            return []
    
    async def call_tool(self, server_name: str, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Call a tool on a specific MCP server."""
        if server_name not in self.sessions:
            return {
                "success": False,
                "error": f"No active session for server: {server_name}",
                "tool": tool_name
            }
        
        try:
            session = self.sessions[server_name]
            result = await session.call_tool(tool_name, arguments)
            
            return {
                "success": True,
                "result": result,
                "server": server_name,
                "tool": tool_name
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Tool call failed: {str(e)}",
                "server": server_name,
                "tool": tool_name
            }
    
    def get_all_tools_schemas(self) -> List[Dict[str, Any]]:
        """Get OpenAI-compatible schemas for all MCP tools."""
        schemas = []
        
        for server_name, tools in self.tools.items():
            for tool in tools:
                schemas.append(tool.to_openai_schema())
        
        return schemas
    
    def display_server_status(self):
        """Display status of all MCP servers."""
        table = Table(title="MCP Server Status")
        table.add_column("Server", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Transport", style="dim")
        table.add_column("Tools", justify="right")
        table.add_column("Description", style="dim")
        
        for name, config in self.servers.items():
            if config.enabled:
                if name in self.sessions:
                    status = "[green]Connected[/green]"
                    tool_count = len(self.tools.get(name, []))
                else:
                    status = "[red]Disconnected[/red]"
                    tool_count = 0
            else:
                status = "[dim]Disabled[/dim]"
                tool_count = "-"
            
            table.add_row(
                name,
                status,
                config.transport.value,
                str(tool_count),
                config.description or ""
            )
        
        self.console.print(table)
    
    async def disconnect_all(self):
        """Disconnect from all MCP servers."""
        # Close sessions first
        for name, session in self.sessions.items():
            try:
                await asyncio.wait_for(session.close(), timeout=2.0)
                self.console.print(f"[green]✓ Disconnected from {name}[/green]")
            except asyncio.TimeoutError:
                self.console.print(f"[yellow]⏰ Timeout disconnecting from {name}[/yellow]")
            except Exception as e:
                self.console.print(f"[yellow]⚠️  Error disconnecting from {name}: {e}[/yellow]")
        
        # Clean up client contexts with better error handling
        if hasattr(self, '_client_contexts'):
            for name, context in self._client_contexts.items():
                try:
                    # Skip cleanup if context was never properly initialized
                    if hasattr(context, '__aexit__'):
                        await asyncio.wait_for(context.__aexit__(None, None, None), timeout=1.0)
                except (asyncio.TimeoutError, RuntimeError, asyncio.CancelledError):
                    # Silently ignore context cleanup errors - these are often SDK-related
                    pass
                except Exception:
                    # Also ignore other context cleanup errors
                    pass
            self._client_contexts.clear()
        
        self.sessions.clear()


class MCPToolIntegrator:
    """Integrates MCP tools with Saturn's existing file build tools."""
    
    def __init__(self, working_directory: str = "."):
        self.working_directory = working_directory
        self.mcp_manager = MCPServerManager()
        self.console = Console()
        
        # Import Saturn's existing file build tools
        try:
            from saturn.file_build_tools import create_file_build_tools_for_llm
            self.saturn_tools = create_file_build_tools_for_llm(working_directory)
        except ImportError:
            self.saturn_tools = {"tools_schema": [], "handler": None, "available_tools": []}
        
    async def initialize(self) -> bool:
        """Initialize MCP integration with timeout."""
        self.console.print("[bold blue]🚀 Initializing MCP Integration[/bold blue]")
        
        try:
            # Connect to MCP servers with timeout
            connections = await asyncio.wait_for(
                self.mcp_manager.connect_to_servers(),
                timeout=30.0  # 30 second total timeout for Docker containers
            )
            
            if connections:
                # Fetch tools from all connected servers
                await asyncio.wait_for(
                    self.mcp_manager.fetch_all_tools(),
                    timeout=10.0
                )
                self.mcp_manager.display_server_status()
                return True
            else:
                self.console.print("[yellow]⚠️  No MCP servers connected[/yellow]")
                return False
                
        except asyncio.TimeoutError:
            self.console.print("[yellow]⏰ MCP initialization timed out[/yellow]")
            # Try to cleanup any partial connections
            try:
                await asyncio.wait_for(self.mcp_manager.disconnect_all(), timeout=5.0)
            except:
                pass
            return False
        except Exception as e:
            self.console.print(f"[red]❌ MCP initialization error: {e}[/red]")
            return False
    
    def get_combined_tools_schema(self) -> List[Dict[str, Any]]:
        """Get combined schemas for Saturn and MCP tools."""
        # Start with Saturn's existing tools
        combined_schemas = self.saturn_tools.get("tools_schema", []).copy()
        
        # Add MCP tools
        mcp_schemas = self.mcp_manager.get_all_tools_schemas()
        combined_schemas.extend(mcp_schemas)
        
        return combined_schemas
    
    def get_tools_summary(self) -> Dict[str, Any]:
        """Get summary of all available tools."""
        saturn_count = len(self.saturn_tools.get("tools_schema", []))
        mcp_count = sum(len(tools) for tools in self.mcp_manager.tools.values())
        
        return {
            "saturn_tools": saturn_count,
            "mcp_tools": mcp_count,
            "total_tools": saturn_count + mcp_count,
            "mcp_servers": len(self.mcp_manager.sessions),
            "available_servers": len([s for s in self.mcp_manager.servers.values() if s.enabled])
        }
    
    def get_mcp_tools_description(self) -> str:
        """Get a description of MCP tools for inclusion in existing system prompts."""
        tools_summary = self.get_tools_summary()
        
        if tools_summary['mcp_tools'] == 0:
            return ""
        
        description_parts = [f"MCP Tools ({tools_summary['mcp_tools']} tools from {tools_summary['mcp_servers']} servers):"]
        
        # Add MCP tool descriptions by server
        for server_name, tools in self.mcp_manager.tools.items():
            if tools:
                description_parts.append(f"- {server_name.title()} Server: {', '.join([tool.display_name or tool.name for tool in tools[:3]])}")
                if len(tools) > 3:
                    description_parts.append(f"  ... and {len(tools) - 3} more tools")
        
        description_parts.append("Note: MCP tools are prefixed with 'mcp_{server}_{tool_name}'")
        
        return "\n".join(description_parts)
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Route tool calls to appropriate handlers (Saturn or MCP)."""
        
        # Check if it's an MCP tool (prefixed with mcp_)
        if tool_name.startswith("mcp_"):
            return await self._call_mcp_tool(tool_name, arguments)
        else:
            return await self._call_saturn_tool(tool_name, arguments)
    
    async def _call_mcp_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Call an MCP tool."""
        try:
            # Parse MCP tool name: mcp_{server}_{tool}
            # Handle cases where tool names include the server name
            if not tool_name.startswith("mcp_"):
                return {
                    "success": False,
                    "error": f"Invalid MCP tool name format: {tool_name}",
                    "tool": tool_name
                }
            
            # Remove mcp_ prefix
            remaining = tool_name[4:]  # Remove "mcp_"
            
            # Find matching server name from registered servers
            server_name = None
            actual_tool_name = None
            
            for registered_server in self.mcp_manager.sessions.keys():
                # Check if the remaining part starts with the server name
                if remaining.startswith(registered_server + "_"):
                    server_name = registered_server
                    actual_tool_name = remaining[len(registered_server) + 1:]  # +1 for underscore
                    break
                # Also check case-insensitive match
                elif remaining.lower().startswith(registered_server.lower() + "_"):
                    server_name = registered_server
                    actual_tool_name = remaining[len(registered_server) + 1:]
                    break
            
            # If no direct match, check if tool name contains server name elements
            if not server_name:
                for registered_server in self.mcp_manager.sessions.keys():
                    # For github server, also check for "Github_Server" pattern
                    if registered_server == "github" and ("Github_Server_" in remaining or "github_" in remaining.lower()):
                        server_name = registered_server
                        # Extract actual tool name by removing Github_Server_ or github_ prefix
                        if "Github_Server_" in remaining:
                            actual_tool_name = remaining.split("Github_Server_", 1)[1]
                        else:
                            actual_tool_name = remaining.split("github_", 1)[1]
                        break
            
            if not server_name or not actual_tool_name:
                return {
                    "success": False,
                    "error": f"Could not parse server name from tool: {tool_name}. Available servers: {list(self.mcp_manager.sessions.keys())}",
                    "tool": tool_name
                }
            
            return await self.mcp_manager.call_tool(server_name, actual_tool_name, arguments)
            
        except Exception as e:
            return {
                "success": False,
                "error": f"MCP tool call error: {str(e)}",
                "tool": tool_name
            }
    
    async def _call_saturn_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Call a Saturn file build tool."""
        try:
            handler = self.saturn_tools.get("handler")
            if not handler:
                return {
                    "success": False,
                    "error": "Saturn tools handler not available",
                    "tool": tool_name
                }
            
            # Create tool call in expected format
            tool_call = {
                "type": "function",
                "function": {
                    "name": tool_name,
                    "arguments": arguments
                }
            }
            
            return await handler.handle_tool_call(tool_call)
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Saturn tool call error: {str(e)}",
                "tool": tool_name
            }
    
    async def shutdown(self):
        """Shutdown MCP integration."""
        await self.mcp_manager.disconnect_all()
        self.console.print("[green]✓ MCP integration shutdown complete[/green]")


# Convenience functions for easy integration

async def initialize_mcp_integration(working_directory: str = ".") -> MCPToolIntegrator:
    """Initialize MCP integration with Saturn tools."""
    integrator = MCPToolIntegrator(working_directory)
    await integrator.initialize()
    return integrator


if __name__ == "__main__":
    pass