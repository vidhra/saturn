import asyncio
import sys
from typing import Tuple, Type

from .base_state import BaseState, StateMachineContext

class ReasoningState(BaseState):
    """
    Reasoning state that analyzes the query and shows thinking process.
    Displays dynamic thinking messages that overwrite themselves.
    """

    def __repr__(self):
        return "ReasoningState"

    async def run(
        self, context: StateMachineContext
    ) -> Tuple[Type[BaseState], StateMachineContext]:
        """
        Analyze the query using LLM reasoning and show reasoning process with dynamic display.
        """
        from .planning_state import PlanningState


        reasoning_result = await self._perform_llm_reasoning(context)
        context.reasoning_analysis = reasoning_result
        context.state_recorder.record_event(
            "reasoning_completed",
            {
                "query": context.original_query,
                "query_length": len(context.original_query),
                "complexity_indicators": self._analyze_query_complexity(
                    context.original_query
                ),
                "reasoning_result": reasoning_result,
            },
        )

        print("\n🧠 Reasoning complete. Moving to planning...")
        return PlanningState, context

    async def _perform_llm_reasoning(self, context: StateMachineContext) -> dict:
        """Actually perform LLM-based reasoning while showing visual progress."""

        display_task = asyncio.create_task(self._show_reasoning_process(context))

        try:
            reasoning_prompt = f"""
                You are analyzing a user query to understand its intent and requirements before creating an execution plan.

                Query: "{context.original_query}"

                Please analyze this query and provide a structured reasoning in the following format:

                1. INTENT ANALYSIS: What is the user trying to accomplish?
                2. SCOPE & COMPLEXITY: How complex is this request? (simple/moderate/complex)
                3. KEY COMPONENTS: What are the main technical components involved?
                4. DEPENDENCIES: What prerequisites or dependencies might be needed?
                5. APPROACH: What's the best high-level approach to tackle this?

                Provide a concise but thorough analysis. Be specific about cloud services, tools, or technologies mentioned.
                """

            response = await context.llm_interface.agenerate(
                [
                    {
                        "role": "system",
                        "content": "You are a cloud infrastructure expert analyzing user requests for execution planning.",
                    },
                    {"role": "user", "content": reasoning_prompt},
                ]
            )

            reasoning_text = response.choices[0].message.content.strip()

            # Parse the reasoning into structured format
            reasoning_result = {
                "raw_analysis": reasoning_text,
                "intent": self._extract_section(reasoning_text, "INTENT ANALYSIS"),
                "complexity": self._extract_section(
                    reasoning_text, "SCOPE & COMPLEXITY"
                ),
                "components": self._extract_section(reasoning_text, "KEY COMPONENTS"),
                "dependencies": self._extract_section(reasoning_text, "DEPENDENCIES"),
                "approach": self._extract_section(reasoning_text, "APPROACH"),
                "timestamp": context.state_recorder.run_start_time,
            }

        except Exception as e:
            reasoning_result = {
                "raw_analysis": f"LLM reasoning failed: {e}",
                "intent": "Parse user query for cloud operations",
                "complexity": "moderate",
                "components": ["cloud services", "infrastructure"],
                "dependencies": ["cloud authentication", "permissions"],
                "approach": "Standard step-by-step execution",
                "timestamp": context.state_recorder.run_start_time,
                "error": str(e),
            }

        finally:
            # Stop the visual display
            display_task.cancel()
            try:
                await display_task
            except asyncio.CancelledError:
                pass

        return reasoning_result

    def _extract_section(self, text: str, section_name: str) -> str:
        """Extract a specific section from the reasoning text."""
        lines = text.split("\n")
        section_lines = []
        in_section = False

        for line in lines:
            if section_name.upper() in line.upper():
                in_section = True
                # Get the content after the colon if it exists
                if ":" in line:
                    section_lines.append(line.split(":", 1)[1].strip())
                continue
            elif (
                in_section
                and line.strip()
                and any(
                    keyword in line.upper()
                    for keyword in [
                        "ANALYSIS",
                        "SCOPE",
                        "COMPONENTS",
                        "DEPENDENCIES",
                        "APPROACH",
                    ]
                )
            ):
                # Hit the next section
                break
            elif in_section and line.strip():
                section_lines.append(line.strip())

        return " ".join(section_lines).strip() if section_lines else "Not specified"

    async def _show_reasoning_process(self, context: StateMachineContext):
        """Show dynamic reasoning process that overwrites itself."""

        has_console = context.console is not None

        thinking_lines = [
            ["Analyzing your request..."],
        ]

        if has_console:

            for i, lines in enumerate(thinking_lines):

                for line in lines:
                    if line.strip():
                        context.console.print(line)
                    else:
                        context.console.print("")

                if i < len(thinking_lines) - 1:
                    await asyncio.sleep(1.2)
                else:
                    await asyncio.sleep(0.5)
        else:
            for i, lines in enumerate(thinking_lines):

                for line in lines:
                    if line.strip():
                        print(line)
                    else:
                        print("")

                sys.stdout.flush()

                if i < len(thinking_lines) - 1:
                    await asyncio.sleep(1.2)
                else:
                    await asyncio.sleep(0.5)

    def _analyze_query_complexity(self, query: str) -> dict:
        """Analyze query to understand complexity."""
        query_lower = query.lower()

        complexity_indicators = {
            "is_multi_step": any(
                word in query_lower for word in ["and", "then", "after", "next", "also"]
            ),
            "mentions_cloud_services": any(
                service in query_lower
                for service in [
                    "gcp",
                    "aws",
                    "azure",
                    "compute",
                    "storage",
                    "database",
                    "vpc",
                    "ec2",
                    "s3",
                ]
            ),
            "has_terraform_keywords": any(
                word in query_lower
                for word in ["terraform", "infrastructure", "iac", "provision"]
            ),
            "mentions_security": any(
                word in query_lower
                for word in [
                    "security",
                    "firewall",
                    "iam",
                    "policy",
                    "access",
                    "permissions",
                ]
            ),
            "query_word_count": len(query.split()),
            "estimated_complexity": (
                "simple"
                if len(query.split()) < 10
                else "moderate" if len(query.split()) < 25 else "complex"
            ),
        }

        return complexity_indicators
