import json
import os
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

from rich.console import Console

console = Console()


class RunStateLogger:
    """Handles recording and saving the state of an orchestrator run."""

    def __init__(self, query: str):
        self.run_start_time = datetime.now().isoformat()
        self.query = query
        self.run_state_data = {
            "run_info": {
                "query": query,
                "start_time": self.run_start_time,
                "end_time": None,
                "final_status": "UNKNOWN",
                "attempts_made": 0,
                "final_errors": None,
            },
            "dag": {"nodes": {}, "edges": [], "execution_order": []},
            "nodes": {},
            "events": [],
        }
        console.print("[grey50][StateLogger] Initialized for query.[/grey50]")

    def set_attempts(self, attempt_count: int):
        """Sets the number of attempts made in the run."""
        self.run_state_data["run_info"]["attempts_made"] = attempt_count
        console.print(
            f"[grey50][StateLogger] Updated attempt count to {attempt_count}.[/grey50]"
        )

    def record_dag_structure(self, dag_definition: Dict[str, Any]):
        """Records the DAG structure including nodes, edges, and execution order."""
        self.run_state_data["dag"] = {
            "nodes": dag_definition["nodes"],
            "edges": dag_definition["edges"],
            "execution_order": dag_definition["execution_order"],
        }
        console.print(
            f"[grey50][StateLogger] Recorded DAG structure with {len(dag_definition['nodes'])} nodes.[/grey50]"
        )

    def record_node_initialization(
        self,
        node_id: str,
        tool_name: str,
        attempt: int,
        args: Dict[str, Any],
        initial_status: str,
    ):
        """Records the initial state of a node when planned."""
        if node_id not in self.run_state_data["nodes"]:
            self.run_state_data["nodes"][node_id] = {
                "tool_name": tool_name,
                "attempt": attempt,
                "arguments": args,
                "status_history": [(datetime.now().isoformat(), initial_status)],
                "current_status": initial_status,
                "output": None,
                "error": None,
                "dependencies": self.run_state_data["dag"]
                .get("nodes", {})
                .get(node_id, {})
                .get("dependencies", []),
            }
            console.print(
                f"[grey50][StateLogger] Node '{node_id}' initialized as {initial_status}.[/grey50]"
            )

    def record_node_status_change(self, node_id: str, new_status: str):
        """Records a change in a node's status (e.g., PENDING -> RUNNING)."""
        if node_id in self.run_state_data["nodes"]:
            timestamp = datetime.now().isoformat()
            self.run_state_data["nodes"][node_id]["status_history"].append(
                (timestamp, new_status)
            )
            self.run_state_data["nodes"][node_id]["current_status"] = new_status
            console.print(
                f"[grey50][StateLogger] Node '{node_id}' status changed to {new_status}.[/grey50]"
            )
        else:
            console.print(
                f"[bold yellow][StateLogger] Warning:[/] Tried to record status change for unknown node_id: {node_id}"
            )

    def record_node_result(
        self, node_id: str, success: bool, result_or_error: Any, final_status: str
    ):
        """Records the final outcome (success/failure) of a node."""
        if node_id in self.run_state_data["nodes"]:
            self.record_node_status_change(node_id, final_status)
            if success:
                self.run_state_data["nodes"][node_id]["output"] = result_or_error
                self.run_state_data["nodes"][node_id]["error"] = None
            else:
                self.run_state_data["nodes"][node_id]["output"] = None
                self.run_state_data["nodes"][node_id]["error"] = str(result_or_error)
            console.print(
                f"[grey50][StateLogger] Node '{node_id}' result recorded (Success: {success}).[/grey50]"
            )
        else:
            console.print(
                f"[bold yellow][StateLogger] Warning:[/] Tried to record result for unknown node_id: {node_id}"
            )

    def get_dag_summary(self) -> Dict[str, Any]:
        """Returns a summary of the DAG structure and execution state."""
        return {
            "total_nodes": len(self.run_state_data["dag"].get("nodes", {})),
            "total_edges": len(self.run_state_data["dag"].get("edges", [])),
            "execution_order": self.run_state_data["dag"].get("execution_order", []),
            "node_states": {
                node_id: node_data["current_status"]
                for node_id, node_data in self.run_state_data["nodes"].items()
            },
        }

    def set_final_run_status(
        self, status: str, errors: Optional[List[Dict[str, Any]]] = None
    ):
        """Sets the final status of the run and any errors."""
        self.run_state_data["run_info"]["final_status"] = status
        if errors:
            self.run_state_data["run_info"]["final_errors"] = errors
        else:
            self.run_state_data["run_info"]["final_errors"] = None

    def save_state(self):
        """Writes the accumulated run state to a uniquely named JSON file in a 'logs' directory."""
        self.run_state_data["run_info"]["end_time"] = datetime.now().isoformat()

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        safe_query_part = "".join(c if c.isalnum() else "_" for c in self.query)[:50]
        if not safe_query_part:
            safe_query_part = "run"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = uuid.uuid4().hex[:8]

        filename = f"{timestamp}_{unique_id}.json"
        filepath = os.path.join(log_dir, filename)

        try:
            console.print(
                f"[info]Writing final run state to [cyan]{filepath}[/cyan]...[/info]"
            )
            with open(filepath, "w") as f:
                json.dump(self.run_state_data, f, indent=2)
            console.print(
                f"[info]State file [cyan]{filename}[/cyan] written successfully to [magenta]{log_dir}/[/magenta].[/info]"
            )
        except Exception as e:
            console.print(
                f"[bold red]Error:[/] Failed to write state file {filepath}: {e}"
            )

    def record_event(self, event_type: str, event_data: Dict[str, Any]):
        event = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "data": event_data,
        }
        self.run_state_data["events"].append(event)
        console.print(f"[grey50][StateLogger] Recorded event: {event_type}[/grey50]")
