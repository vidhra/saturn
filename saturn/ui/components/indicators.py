"""
Status and progress indicators for the Saturn TUI application.
"""

from textual.widgets import Static


class ThinkingIndicator(Static):
    """Real-time thinking display with state tracking like ResponseStatus"""

    def __init__(self, **kwargs):
        super().__init__("", **kwargs)
        self.visible = False
        self.current_state = ""
        self.current_step = ""
        self.operation_count = 0

        # State descriptions for better UX
        self.state_descriptions = {
            "StartState": "Initializing Saturn AI Assistant...",
            "ReasoningState": "Analyzing your request and understanding intent...",
            "PlanningState": "Creating execution plan and selecting tools...",
            "ExecutingState": "Executing operations on cloud infrastructure...",
            "ProcessingResultsState": "Processing results and validating operations...",
            "TerraformState": "Managing infrastructure with Terraform...",
            "TerraformPlanningState": "Planning Terraform resource configurations...",
            "CompletedState": "Operations completed successfully!",
            "FailedState": "Operations failed - reviewing errors...",
        }

        # Dynamic sub-operations for each state
        self.sub_operations = {
            "ReasoningState": [
                "Parsing natural language query",
                "Identifying cloud services mentioned",
                "Analyzing complexity and scope",
                "Determining execution approach",
            ],
            "PlanningState": [
                "Discovering available tools",
                "Building dependency graph",
                "Optimizing execution order",
                "Validating tool parameters",
            ],
            "ExecutingState": [
                "Authenticating with cloud providers",
                "Executing infrastructure operations",
                "Monitoring operation progress",
                "Collecting execution results",
            ],
            "ProcessingResultsState": [
                "Validating operation results",
                "Checking for errors or warnings",
                "Updating state tracking",
                "Preparing next steps",
            ],
        }

    def start_thinking(self, message: str = ""):
        """Start the thinking animation"""
        self.visible = True
        self.display = True
        # Force immediate refresh
        self.refresh()
        if message:
            self.update(f"[bold yellow]▶[/bold yellow] {message}")
        else:
            self._show_current_state()

    def update_state(self, state_name: str, step: str = ""):
        """Update current state and step information"""
        if state_name != self.current_state:
            self.current_state = state_name
            self.current_step = step
            self.operation_count = 0
            self._show_current_state()
        elif step and step != self.current_step:
            self.current_step = step
            self._show_current_state()

    def _show_current_state(self):
        """Show current state with description and sub-operations"""
        if not self.visible:
            return

        # Main state description
        main_desc = self.state_descriptions.get(
            self.current_state, f"Processing {self.current_state}..."
        )

        # Show sub-operation if available
        sub_ops = self.sub_operations.get(self.current_state, [])
        if sub_ops and self.operation_count < len(sub_ops):
            current_sub_op = sub_ops[self.operation_count % len(sub_ops)]
            display_text = f"[bold yellow]▶[/bold yellow] {main_desc}\n[dim]  └─ {current_sub_op}...[/dim]"
            self.operation_count += 1
        elif self.current_step:
            display_text = f"[bold yellow]▶[/bold yellow] {main_desc}\n[dim]  └─ {self.current_step}[/dim]"
        else:
            display_text = f"[bold yellow]▶[/bold yellow] {main_desc}"

        self.update(display_text)

        # Auto-advance sub-operations for active states
        if sub_ops and self.current_state in [
            "ReasoningState",
            "PlanningState",
            "ExecutingState",
        ]:
            self.set_timer(1.5, self._advance_sub_operation)

    def _advance_sub_operation(self):
        """Advance to next sub-operation for visual progress"""
        if self.visible and self.current_state in self.sub_operations:
            self._show_current_state()

    def stop_thinking(self):
        """Stop thinking and hide"""
        self.visible = False
        self.display = False
        self.update("")
        self.current_state = ""
        self.current_step = ""
        self.operation_count = 0 