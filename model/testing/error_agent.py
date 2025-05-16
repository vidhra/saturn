import json
import re
from typing import Dict, List, Optional

class ErrorAnalysisAgent:
    """Agent that analyzes errors and generates appropriate system prompts."""
    
    def __init__(self):
        self.error_patterns = {
            "validation": {
                "patterns": [
                    (r"minimum.*instances.*must be at least", "min_instances", "Set min_instances to at least 2"),
                    (r"minimum.*less than.*maximum", "min_max_instances", "Ensure min_instances is less than max_instances"),
                    (r"IP range .* is not valid", "ip_cidr_range", "Provide a valid CIDR range (e.g., '10.8.0.0/28')"),
                    (r"invalid.*format", "format", "Check the format of the provided value"),
                    (r"required.*field", "required_field", "Provide all required fields"),
                ]
            },
            "resource": {
                "patterns": [
                    (r"project .* not found", "project", "Verify project ID exists and you have access"),
                    (r"network .* not found", "network", "Verify network exists in the specified project"),
                    (r"resource .* not found", "resource", "Verify the resource exists"),
                ]
            },
            "permission": {
                "patterns": [
                    (r"Permission denied", "authorization", "Verify you have required permissions"),
                    (r"not authorized", "authorization", "Check your permissions"),
                ]
            }
        }
        
    def analyze_error(self, error_message: str) -> Dict:
        """Analyze error message and return structured error information."""
        for category, patterns in self.error_patterns.items():
            for pattern, field, fix in patterns["patterns"]:
                if re.search(pattern, error_message, re.IGNORECASE):
                    return {
                        "category": category,
                        "field": field,
                        "fix": fix,
                        "original_error": error_message
                    }
        
        return {
            "category": "unknown",
            "field": "unknown",
            "fix": "Please check all parameters and try again",
            "original_error": error_message
        }
    
    def generate_error_context(self, errors: List[Dict]) -> str:
        """Generate context from multiple errors."""
        analyzed_errors = [self.analyze_error(error["error"]) for error in errors]
        
        context = "Previous attempt failed with the following issues:\n\n"
        
        for i, error in enumerate(analyzed_errors, 1):
            context += f"Error {i}:\n"
            context += f"Category: {error['category']}\n"
            context += f"Field: {error['field']}\n"
            context += f"Fix: {error['fix']}\n"
            context += f"Original Error: {error['original_error']}\n\n"
        
        return context
    
    def generate_system_prompt(self, errors: List[Dict]) -> str:
        """Generate a focused system prompt based on the errors encountered."""
        analyzed_errors = [self.analyze_error(error["error"]) for error in errors]
        
        # Group errors by category
        error_categories = {}
        for error in analyzed_errors:
            if error["category"] not in error_categories:
                error_categories[error["category"]] = []
            error_categories[error["category"]].append(error)
        
        # Build focused instructions based on error categories
        instructions = []
        
        if "validation" in error_categories:
            instructions.append("""
            Validation Errors Detected:
            - Ensure all numeric values are within valid ranges
            - Check that minimum values are less than maximum values
            - Verify all required fields are provided
            - Ensure IP ranges are in valid CIDR format
            """)
        
        if "resource" in error_categories:
            instructions.append("""
            Resource Errors Detected:
            - Verify all resource names and IDs exist
            - Check project and network references
            - Ensure resources are in the correct region/zone
            """)
        
        if "permission" in error_categories:
            instructions.append("""
            Permission Errors Detected:
            - Verify you have the necessary permissions
            - Check service account roles and permissions
            - Ensure proper authentication is configured
            """)
        
        # Build the final system prompt
        system_prompt = """
        You are an expert in composing functions with a focus on error correction.
        Based on the previous errors, please make the following adjustments:
        
        {instructions}
        
        Additional Guidelines:
        - Double-check all parameter values before making the call
        - Ensure all required fields are provided
        - Verify resource names and IDs are correct
        - Check that numeric values are within valid ranges
        - Ensure proper formatting of all values
        
        The output MUST strictly adhere to the following JSON format:
        { "tool_calls": [ {"name": "func_name1", "arguments": {"argument1": "value1", "argument2": "value2"}} ] }
        """.format(instructions="\n".join(instructions))
        
        return system_prompt.strip()

def create_error_handled_prompt(original_prompt: str, errors: List[Dict]) -> str:
    """Create a new prompt that incorporates error handling."""
    agent = ErrorAnalysisAgent()
    
    # Generate error context
    error_context = agent.generate_error_context(errors)
    
    # Generate focused system prompt
    system_prompt = agent.generate_system_prompt(errors)
    
    # Combine everything
    new_prompt = f"""
    {system_prompt}
    
    Error Context:
    {error_context}
    
    Original Query:
    {original_prompt}
    """
    
    return new_prompt.strip() 