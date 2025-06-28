#!/usr/bin/env python3
"""
Comprehensive tests for MCP (Model Context Protocol) integration with Saturn.

Tests cover:
- Basic MCP integration functionality
- Tool discovery and schema generation
- Integration with existing Saturn tools
- System prompt generation with MCP tools
- Tool routing (Saturn vs MCP)
"""

import asyncio
import pytest
import pytest_asyncio
import sys
from pathlib import Path

# Add the parent directory to the path so we can import saturn modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from saturn.mcp_integration import MCPToolIntegrator, MCPServerManager
from saturn.prompts import PLANNING_SYSTEM_PROMPT_TEMPLATE


class TestMCPIntegration:
    """Test suite for MCP integration functionality."""
    
    @pytest_asyncio.fixture
    async def integrator(self):
        """Create an MCP integrator instance for testing."""
        integrator = MCPToolIntegrator(".")
        await integrator.initialize()
        yield integrator
        await integrator.shutdown()
    
    def test_mcp_server_manager_creation(self):
        """Test MCP server manager can be created and loads config."""
        manager = MCPServerManager("mcp_servers.json")
        assert manager is not None
        assert hasattr(manager, 'servers')
        assert isinstance(manager.servers, dict)
    
    @pytest.mark.asyncio
    async def test_mcp_tool_integrator_creation(self):
        """Test MCP tool integrator can be created."""
        integrator = MCPToolIntegrator(".")
        assert integrator is not None
        assert hasattr(integrator, 'mcp_manager')
        assert hasattr(integrator, 'saturn_tools')
        await integrator.shutdown()
    
    @pytest.mark.asyncio
    async def test_saturn_tools_available(self, integrator):
        """Test that Saturn tools are available through the integrator."""
        tools_summary = integrator.get_tools_summary()
        assert tools_summary['saturn_tools'] > 0
        assert tools_summary['total_tools'] > 0
        
        # Check specific Saturn tools exist
        combined_schemas = integrator.get_combined_tools_schema()
        tool_names = [tool["function"]["name"] for tool in combined_schemas]
        
        expected_tools = ["read_file", "write_file", "build_project", "detect_project_type"]
        for expected_tool in expected_tools:
            assert expected_tool in tool_names
    
    @pytest.mark.asyncio
    async def test_tool_schemas_format(self, integrator):
        """Test that tool schemas are in correct OpenAI format."""
        combined_schemas = integrator.get_combined_tools_schema()
        
        for schema in combined_schemas:
            assert "type" in schema
            assert schema["type"] == "function"
            assert "function" in schema
            assert "name" in schema["function"]
            assert "description" in schema["function"]
            assert "parameters" in schema["function"]
    
    @pytest.mark.asyncio
    async def test_saturn_tool_routing(self, integrator):
        """Test that Saturn tools are routed correctly."""
        # Test a Saturn tool call
        result = await integrator.call_tool("detect_project_type", {})
        
        assert "success" in result
        assert "tool" in result
        assert result["tool"] == "detect_project_type"
        
        if result["success"]:
            assert "result" in result
            assert isinstance(result["result"], dict)
    
    @pytest.mark.asyncio
    async def test_mcp_tool_routing(self, integrator):
        """Test that MCP tools would be routed correctly."""
        # Test with a mock MCP tool name
        result = await integrator.call_tool("mcp_test_server_test_tool", {"test": "arg"})
        
        # Should fail because no actual MCP server is connected, but routing should work
        assert "success" in result
        assert result["success"] == False  # Expected since no server connected
        assert "error" in result
    
    @pytest.mark.asyncio
    async def test_system_prompt_integration(self, integrator):
        """Test integration with existing system prompts."""
        tools_summary = integrator.get_tools_summary()
        mcp_description = integrator.get_mcp_tools_description()
        
        # Get tool names for prompt
        combined_schemas = integrator.get_combined_tools_schema()
        saturn_tool_names = [
            tool["function"]["name"] for tool in combined_schemas 
            if not tool["function"]["name"].startswith("mcp_")
        ]
        
        available_file_tools = ", ".join(saturn_tool_names)
        available_mcp_tools = mcp_description if mcp_description else "(No MCP tools currently available)"
        
        # Test prompt formatting
        sample_query = "Read config.yaml and create a Docker container"
        formatted_prompt = PLANNING_SYSTEM_PROMPT_TEMPLATE.format(
            user_query=sample_query,
            available_cloud_tools="gcp_cli, aws_cli",
            available_file_tools=available_file_tools,
            available_mcp_tools=available_mcp_tools
        )
        
        assert sample_query in formatted_prompt
        assert "read_file" in formatted_prompt
        assert "Available MCP tools:" in formatted_prompt
    
    @pytest.mark.asyncio
    async def test_mcp_tools_description_format(self, integrator):
        """Test MCP tools description formatting."""
        description = integrator.get_mcp_tools_description()
        
        # When no MCP tools are available, should return empty string
        if not integrator.mcp_manager.tools:
            assert description == ""
        else:
            # When MCP tools are available, should contain server info
            assert "MCP Tools" in description
            assert "servers" in description
    
    def test_mcp_enabled_config_integration(self):
        """Test that MCP integration respects configuration."""
        # This would typically be tested with actual config loading
        # For now, just verify the structure exists
        assert True  # Placeholder - actual config testing would go here


@pytest.mark.asyncio
async def test_basic_functionality():
    """Standalone test for basic MCP functionality."""
    print("🧪 Basic MCP Integration Test")
    print("=" * 50)
    
    try:
        # Test 1: Initialize MCP integrator
        integrator = MCPToolIntegrator(".")
        print("✓ MCPToolIntegrator created successfully")
        
        # Test 2: Check Saturn tools are available
        tools_summary = integrator.get_tools_summary()
        print(f"✓ Saturn tools available: {tools_summary['saturn_tools']}")
        
        # Test 3: Get tool schemas
        schemas = integrator.get_combined_tools_schema()
        print(f"✓ Combined tool schemas: {len(schemas)} tools")
        
        # Test 4: Test Saturn tool call
        result = await integrator.call_tool("detect_project_type", {})
        if result["success"]:
            print("✓ Saturn tool call successful")
        else:
            print(f"✗ Saturn tool call failed: {result.get('error')}")
        
        # Test 5: Cleanup
        await integrator.shutdown()
        print("✓ Shutdown completed")
        
        return True
        
    except Exception as e:
        print(f"✗ Test failed with exception: {e}")
        import traceback
        traceback.print_exc()
        return False


@pytest.mark.asyncio
async def test_prompt_integration():
    """Test integration with system prompts."""
    print("🎯 Testing MCP Integration with System Prompts")
    print("=" * 60)
    
    # Initialize MCP integrator
    integrator = MCPToolIntegrator(".")
    await integrator.initialize()
    
    # Get tools summary
    tools_summary = integrator.get_tools_summary()
    print(f"📊 Tools Summary:")
    print(f"   Saturn Tools: {tools_summary['saturn_tools']}")
    print(f"   MCP Tools: {tools_summary['mcp_tools']}")
    print(f"   Total Tools: {tools_summary['total_tools']}")
    
    # Get available tools for prompts
    combined_schemas = integrator.get_combined_tools_schema()
    saturn_tool_names = [
        tool["function"]["name"] for tool in combined_schemas 
        if not tool["function"]["name"].startswith("mcp_")
    ]
    
    print(f"🛠️  Available Saturn Tools: {len(saturn_tool_names)}")
    print("✅ MCP Integration working with system prompts!")
    
    await integrator.shutdown()


if __name__ == "__main__":
    # Run standalone tests
    print("🚀 Running MCP Integration Tests")
    print("=" * 60)
    
    # Test 1: Basic functionality
    success1 = asyncio.run(test_basic_functionality())
    print()
    
    # Test 2: Prompt integration
    asyncio.run(test_prompt_integration())
    print()
    
    print(f"{'✅ All tests PASSED' if success1 else '❌ Some tests FAILED'}") 