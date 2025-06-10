import os
import yaml
from typing import Optional, Dict, Any
from rich.console import Console

console = Console()



CONFIG_FILE_NAME = "config.yaml"
USER_CONFIG_DIR = os.path.expanduser("~/.config/saturn")


ENV_VAR_MAP = {
    "openai_api_key": "OPENAI_API_KEY",
    "google_api_key": "GOOGLE_API_KEY",
    "gemini_api_key": "GEMINI_API_KEY",
    "anthropic_api_key": "ANTHROPIC_API_KEY",
    "mistral_api_key": "MISTRAL_API_KEY",
    "gcp_project_id": "GCP_PROJECT_ID",
    "gcp_credentials_path": "GOOGLE_APPLICATION_CREDENTIALS", 
    "aws_region": "AWS_REGION",
    "aws_profile": "AWS_PROFILE",
    "vector_store": "VECTOR_STORE",
    "gcp_rag_docs_path": "GCP_RAG_DOCS_PATH",
    "aws_rag_docs_path": "AWS_RAG_DOCS_PATH",
    "rag_docs_path": "GCLOUD_DOCS_PATH", 
    "rag_embedding_model": "RAG_EMBED_MODEL",
    "use_context_aware_parsing": "USE_CONTEXT_AWARE_PARSING",
    "max_chunk_size": "MAX_CHUNK_SIZE",
    "chunk_overlap": "CHUNK_OVERLAP", 
    "preserve_code_blocks": "PRESERVE_CODE_BLOCKS",
    "preserve_command_context": "PRESERVE_COMMAND_CONTEXT",
    "chroma_db_path": "CHROMA_DB_PATH",
    "gcp_chroma_collection_name": "GCP_CHROMA_COLLECTION",
    "aws_chroma_collection_name": "AWS_CHROMA_COLLECTION", 
    "chroma_collection_name": "CHROMA_COLLECTION", 
    "duckdb_path": "DUCKDB_PATH",
    "duckdb_file_name": "DUCKDB_FILE_NAME",
    "gcp_duckdb_table_name": "GCP_DUCKDB_TABLE_NAME",
    "aws_duckdb_table_name": "AWS_DUCKDB_TABLE_NAME",
    "duckdb_table_name": "DUCKDB_TABLE_NAME",
}

_config_loading = False

def load_config(config_path_override: Optional[str] = None, debug: bool = False) -> Dict[str, Any]:
    """
    Loads configuration from a YAML file, sets environment variables from YAML if not already set,
    and then merges with direct environment variable overrides.
    Precedence for YAML loading: config_path_override > ./config.yaml > ~/.config/saturn/config.yaml
    Precedence for values: Direct Environment Vars > YAML-set Env Vars (from YAML file) > YAML file values > Defaults in code.
    """
    global _config_loading
    
    if _config_loading:
        return {}
    
    _config_loading = True
    
    try:
        paths_to_check = []
        if config_path_override:
            paths_to_check.append(config_path_override)
        paths_to_check.append(os.path.join(os.getcwd(), CONFIG_FILE_NAME)) 
        paths_to_check.append(os.path.join(USER_CONFIG_DIR, CONFIG_FILE_NAME)) 
        
        yaml_config: Dict[str, Any] = {}
        loaded_config_path = None

        for path_attempt in paths_to_check:
            if debug:
                print(f"[ConfigDebug] Attempting to load config from: {path_attempt}")
            if os.path.exists(path_attempt):
                if debug:
                    print(f"[ConfigDebug] Found config file: {path_attempt}")
                try:
                    with open(path_attempt, 'r') as f:
                        loaded_data = yaml.safe_load(f)
                        if isinstance(loaded_data, dict):
                            yaml_config = loaded_data
                            loaded_config_path = path_attempt
                            if debug:
                                print(f"[ConfigDebug] Successfully loaded config from {loaded_config_path}")
                            break
                        elif debug:
                            print(f"[ConfigDebug] Warning: Config file {path_attempt} did not load as a dict. Loaded: {type(loaded_data)}")
                except Exception as e:
                    if debug:
                        print(f"[ConfigDebug] Warning: Could not read/parse config file {path_attempt}: {e}")
            elif debug:
                print(f"[ConfigDebug] Config file not found: {path_attempt}")
        
        if not loaded_config_path and debug:
            print(f"[ConfigDebug] No config file was successfully loaded from checked paths.")

        for yaml_key, env_var_name in ENV_VAR_MAP.items():
            if yaml_key in yaml_config and yaml_config[yaml_key] is not None:
                if not os.getenv(env_var_name):
                    os.environ[env_var_name] = str(yaml_config[yaml_key])

        final_config = yaml_config.copy()
        for yaml_key, env_var_name in ENV_VAR_MAP.items():
            env_value = os.getenv(env_var_name)
            if env_value is not None:
                final_config[yaml_key] = env_value

        return final_config
        
    finally:
        _config_loading = False


def vprint(*args, verbose: bool = True, **kwargs):
    """
    Verbose-aware print function that only prints when verbose is True.
    
    Args:
        *args: Arguments to pass to console.print
        verbose: Whether to print or not (default: True for backward compatibility)
        **kwargs: Keyword arguments to pass to console.print
    
    Usage:
        vprint("This will print", verbose=True)
        vprint("This won't print", verbose=False)
        vprint("Default behavior prints", verbose=True)  # default
    """
    if verbose:
        console.print(*args, **kwargs)

def vprint_debug(*args, verbose: bool = True, **kwargs):
    """
    Debug-level verbose print with [DEBUG] prefix.
    
    Args:
        *args: Arguments to pass to console.print
        verbose: Whether to print or not (default: True for backward compatibility)
        **kwargs: Keyword arguments to pass to console.print
    
    Usage:
        vprint_debug("Debug info", verbose=True)
    """
    if verbose:
        console.print(f"[blue][DEBUG][/blue]", *args, **kwargs)

def vprint_info(*args, verbose: bool = True, **kwargs):
    """
    Info-level verbose print with [INFO] prefix.
    
    Args:
        *args: Arguments to pass to console.print
        verbose: Whether to print or not (default: True for backward compatibility)
        **kwargs: Keyword arguments to pass to console.print
    
    Usage:
        vprint_info("Information message", verbose=True)
    """
    if verbose:
        console.print(f"[green][INFO][/green]", *args, **kwargs)

def vprint_warn(*args, verbose: bool = True, **kwargs):
    """
    Warning-level verbose print with [WARN] prefix.
    
    Args:
        *args: Arguments to pass to console.print
        verbose: Whether to print or not (default: True for backward compatibility)
        **kwargs: Keyword arguments to pass to console.print
    
    Usage:
        vprint_warn("Warning message", verbose=True)
    """
    if verbose:
        console.print(f"[yellow][WARN][/yellow]", *args, **kwargs)

def vprint_error(*args, verbose: bool = True, **kwargs):
    """
    Error-level verbose print with [ERROR] prefix.
    
    Args:
        *args: Arguments to pass to console.print
        verbose: Whether to print or not (default: True for backward compatibility)
        **kwargs: Keyword arguments to pass to console.print
    
    Usage:
        vprint_error("Error message", verbose=True)
    """
    if verbose:
        console.print(f"[red][ERROR][/red]", *args, **kwargs)


if __name__ == '__main__':
    print("\n=== Testing Config Loading ===")
    print(f"Current working directory: {os.getcwd()}")
    user_config_path_test = os.path.join(USER_CONFIG_DIR, CONFIG_FILE_NAME)
    print(f"Checking for user config at: {user_config_path_test}")
    print(f"Checking for CWD config at: {os.path.join(os.getcwd(), CONFIG_FILE_NAME)}")

    print("\nInitial state of GOOGLE_API_KEY in environment:", os.getenv('GOOGLE_API_KEY'))
    
    print("\nLoading config...")
    settings = load_config(debug=True)
    
    print("\nFinal state:")
    print(f"Config keys loaded: {list(settings.keys())}")
    print(f"GOOGLE_API_KEY in returned settings dict: {settings.get('google_api_key')}")
    print(f"GOOGLE_API_KEY in environment after load_config: {os.getenv('GOOGLE_API_KEY')}")
    print(f"GCP_PROJECT_ID in returned settings dict: {settings.get('gcp_project_id')}")
    print(f"GCP_PROJECT_ID in environment after load_config: {os.getenv('GCP_PROJECT_ID')}")

    print("\n=== End Config Test ===") 