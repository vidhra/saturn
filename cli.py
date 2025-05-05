import typer
import os
import asyncio
from typing import Optional, Dict, Any
from rich.console import Console
from rich.panel import Panel
import argparse
from dotenv import load_dotenv

# Import actual components from the package (using the new name 'saturn')
from saturn.config import load_config
# Import the main feedback loop function from the new orchestrator module
# from saturn.orchestrator import run_query_with_state_machine 
from saturn.orchestrator import run_query_with_feedback # Corrected import
from saturn.knowledge_base import KnowledgeBase
from saturn.gcp_executor import GcpExecutor

# Remove Temporary stubs
# async def run_query_with_feedback(...): ...
# def load_config(...): ...

# --- Load Config Once at Module Level ---
# Configuration is loaded when the script starts, using env vars or default config.yaml
# The --config-file option per command is removed for this approach.
APP_CONFIG = load_config() 

# --- CLI Application ---
app = typer.Typer()
console = Console()

# Load environment variables from .env file
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Run Saturn GCP agent with a query.")
    parser.add_argument("query", type=str, help="The natural language query for the GCP agent.")
    parser.add_argument("--provider", type=str, default=os.getenv("LLM_PROVIDER", "openai"), help="LLM provider (e.g., openai, gemini, claude, mistral)")
    parser.add_argument("--model", type=str, default=os.getenv("OPENAI_MODEL"), help="Specific LLM model name (e.g., gpt-4o)") # Optional, specific to provider
    parser.add_argument("--project-id", type=str, default=os.getenv("GCP_PROJECT_ID"), help="Google Cloud Project ID")
    parser.add_argument("--creds-path", type=str, default=os.getenv("GCP_CREDENTIALS_PATH"), help="Path to GCP service account key file (uses ADC if not provided)")
    parser.add_argument("--max-retries", type=int, default=int(os.getenv("MAX_RETRIES", "3")), help="Max retry attempts for the state machine")
    parser.add_argument("--kb-path", type=str, default=os.getenv("KB_PATH", APP_CONFIG.get('kb_path', "api_defs")), help="Path to the knowledge base API definitions")

    args = parser.parse_args()

    # --- Use APP_CONFIG as the base and update with CLI args --- 
    config = APP_CONFIG.copy() # Start with the globally loaded config

    # Update config with values from args IF they differ from the argparse default 
    # (or simply override, prioritizing CLI args/env vars used by argparse)
    config['llm_provider'] = args.provider 
    if args.model: # Only override if model arg is provided
        config[f'{args.provider}_model'] = args.model
    if args.project_id: # Check if arg was provided (might need better check depending on argparse setup)
         config['gcp_project_id'] = args.project_id
    if args.creds_path:
         config['gcp_credentials_path'] = args.creds_path
    config['max_retries'] = args.max_retries
    # KB path is handled by argparse default, no need to update here unless logic changes

    # Check the final merged config dictionary
    if not config.get('gcp_project_id'):
        print("Error: GCP Project ID not found. Set GCP_PROJECT_ID environment variable, use --project-id argument, or add to config file.")
        return

    # Validate API key presence for the selected provider
    # Use the merged config for validation
    required_api_key_name = f'{config["llm_provider"]}_api_key'
    if not config.get(required_api_key_name):
         print(f"Error: {required_api_key_name.upper()} environment variable or config value not set for provider '{config['llm_provider']}'.")
         return

    print("--- Initializing Saturn Agent ---")
    print(f"Using LLM Provider: {args.provider}")
    if args.model:
        print(f"Using Model: {args.model}")
    print(f"Target GCP Project: {args.project_id}")
    print(f"Knowledge Base Path: {args.kb_path}")
    
    try:
        print(f"Loading API definitions from: {args.kb_path}")
        kb = KnowledgeBase(args.kb_path)
        executor = GcpExecutor(config)
        print("Components initialized.")

        # Run the query using the state machine orchestrator
        print("--- Starting Query Processing ---")
        # asyncio.run(run_query_with_state_machine(args.query, config, kb, executor))
        # Corrected function call:
        asyncio.run(run_query_with_feedback(args.query, config, kb, executor, args.max_retries))

    except FileNotFoundError:
         print(f"ERROR: Knowledge Base directory '{args.kb_path}' not found.")
    except Exception as e:
        print(f"\n--- An unexpected error occurred --- ")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 