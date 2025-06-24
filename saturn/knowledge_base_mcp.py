# Knowledge Base MCP Integration Utilities
from typing import Any, Dict, List, Optional

from .knowledge_base import KnowledgeBase
from .mcp_integration import MCPToolIntegrator


class MCPEnhancedKnowledgeBase:
    """Extends the existing KnowledgeBase with MCP tools integration."""

    def __init__(
        self,
        knowledge_base: KnowledgeBase,
        mcp_integrator: Optional[MCPToolIntegrator] = None,
    ):
        self.knowledge_base = knowledge_base
        self.mcp_integrator = mcp_integrator

    def get_enhanced_tool_counts(self) -> Dict[str, Any]:
        """Get tool counts including MCP tools."""
        base_counts = self.knowledge_base.get_tool_counts()

        if self.mcp_integrator:
            mcp_summary = self.mcp_integrator.get_tools_summary()
            return {
                **base_counts,
                "mcp_tools": mcp_summary["mcp_tools"],
                "mcp_servers": mcp_summary["mcp_servers"],
                "total_tools_with_mcp": base_counts["total_tools"]
                + mcp_summary["mcp_tools"],
            }

        return {
            **base_counts,
            "mcp_tools": 0,
            "mcp_servers": 0,
            "total_tools_with_mcp": base_counts["total_tools"],
        }

    def get_available_cloud_tools_description(self) -> str:
        """Get description of available cloud tools."""
        return self.knowledge_base.get_available_cloud_tools()

    def get_available_file_tools_description(self) -> str:
        """Get description of available file tools."""
        return self.knowledge_base.get_available_file_tools()

    def get_available_mcp_tools_description(self) -> str:
        """Get description of available MCP tools."""
        if self.mcp_integrator:
            return self.mcp_integrator.get_mcp_tools_description()
        return "No MCP tools available."

    def get_combined_tools_schema(self) -> List[Dict[str, Any]]:
        """Get combined tool schemas for LLM tool calling."""
        if self.mcp_integrator:
            return self.mcp_integrator.get_combined_tools_schema()

        from saturn.file_build_tools import create_file_build_tools_for_llm

        saturn_tools = create_file_build_tools_for_llm()
        return saturn_tools.get("tools_schema", [])

    async def call_tool(
        self, tool_name: str, arguments: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Route tool calls to appropriate handlers."""
        if self.mcp_integrator and tool_name.startswith("mcp_"):
            return await self.mcp_integrator.call_tool(tool_name, arguments)

        from saturn.file_build_tools import create_file_build_tools_for_llm

        saturn_tools = create_file_build_tools_for_llm()
        handler = saturn_tools.get("handler")

        if handler:
            tool_call = {
                "type": "function",
                "function": {"name": tool_name, "arguments": arguments},
            }
            return await handler.handle_tool_call(tool_call)

        return {
            "success": False,
            "error": f"No handler available for tool: {tool_name}",
            "tool": tool_name,
        }


def create_enhanced_knowledge_base(
    config: Dict[str, Any], mcp_integrator: Optional[MCPToolIntegrator] = None
) -> MCPEnhancedKnowledgeBase:
    """Create an enhanced knowledge base with MCP integration."""

    knowledge_base = KnowledgeBase(
        api_defs_dir=config.get("api_defs_dir", "./internal/knowledge_base"),
        working_directory=config.get("working_directory", "."),
    )

    return MCPEnhancedKnowledgeBase(knowledge_base, mcp_integrator)
