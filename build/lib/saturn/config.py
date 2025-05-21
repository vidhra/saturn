import os
import yaml
from typing import Optional, Dict, Any

# Update path to look in root directory
DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yaml")

# Map of config.yaml keys to their corresponding environment variable names
# This helps in setting environment variables from yaml if not already present
ENV_VAR_MAP = {
    "openai_api_key": "OPENAI_API_KEY",
    "google_api_key": "GOOGLE_API_KEY", # For Gemini/Google AI Studio embeddings
    "gemini_api_key": "GEMINI_API_KEY", # If you have a separate one for Gemini LLM
    "anthropic_api_key": "ANTHROPIC_API_KEY",
    "mistral_api_key": "MISTRAL_API_KEY",
    "gcp_project_id": "GCP_PROJECT_ID",
    "gcp_credentials_path": "GOOGLE_APPLICATION_CREDENTIALS",
    # Add other keys from config.yaml you want to expose as env vars if not set
    "vector_store": "VECTOR_STORE",
    "rag_docs_path": "GCLOUD_DOCS_PATH",
    "rag_embedding_model": "RAG_EMBED_MODEL",
    "chroma_db_path": "CHROMA_DB_PATH",
    "chroma_collection_name": "CHROMA_COLLECTION",
    "duckdb_path": "DUCKDB_PATH",
    "duckdb_file_name": "DUCKDB_FILE_NAME",
    "duckdb_table_name": "DUCKDB_TABLE_NAME",
}

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Loads configuration from a YAML file, sets environment variables from YAML if not already set,
    and then merges with direct environment variable overrides.
    Precedence: Direct Environment Vars > YAML-set Env Vars (from YAML file) > YAML file values > Defaults in code.
    """
    path = config_path or DEFAULT_CONFIG_PATH
    print(f"[ConfigDebug] Attempting to load config from: {path}")
    yaml_config: Dict[str, Any] = {}

    if os.path.exists(path):
        print(f"[ConfigDebug] Found config file: {path}")
        try:
            with open(path, 'r') as f:
                loaded_data = yaml.safe_load(f)
                if isinstance(loaded_data, dict):
                    yaml_config = loaded_data
                    print(f"[ConfigDebug] Successfully loaded config with keys: {list(loaded_data.keys())}")
                else:
                    print(f"[ConfigDebug] Warning: Config file {path} did not load as a dict. Loaded: {type(loaded_data)}")
        except Exception as e:
            print(f"[ConfigDebug] Warning: Could not read/parse config file {path}: {e}")
    else:
        print(f"[ConfigDebug] Config file not found: {path}")

    # Set environment variables from YAML config if they are not already set in the environment
    # This makes keys from config.yaml available to libraries that only read from os.environ
    for yaml_key, env_var_name in ENV_VAR_MAP.items():
        if yaml_key in yaml_config and yaml_config[yaml_key] is not None:
            if not os.getenv(env_var_name): # Only set if not already present in environment
                os.environ[env_var_name] = str(yaml_config[yaml_key])
                print(f"[ConfigDebug] Set env var '{env_var_name}' from config.yaml value.")
            else:
                print(f"[ConfigDebug] Env var '{env_var_name}' already set, not overwriting from yaml.")

    # ---- ADDED DEBUG PRINT ----
    # This will show what os.getenv sees *after* the above loop tried to set it from YAML.
    current_google_api_key_in_env = os.getenv("GOOGLE_API_KEY")
    if current_google_api_key_in_env:
        print(f"[ConfigDebug] After env var setting: os.getenv('GOOGLE_API_KEY') is: {current_google_api_key_in_env[:5]}...{current_google_api_key_in_env[-4:]}")
    else:
        print("[ConfigDebug] After env var setting: os.getenv('GOOGLE_API_KEY') is None.")
    # ---- END DEBUG PRINT ----

    # Initialize final config with a copy of yaml_config (or empty if yaml failed)
    # This ensures that if an env var isn't explicitly checked below but was in yaml, it's still in the returned config dict.
    final_config = yaml_config.copy() 

    # Now, explicitly load/override with direct environment variables for known keys.
    # This gives direct environment settings the highest precedence for these specific keys.
    # For other keys, if they were set in os.environ by the loop above, libraries will pick them up.
    # And they are also in final_config if they were in the yaml.
    for yaml_key_for_final_config, env_var_name_for_final_config in ENV_VAR_MAP.items():
        env_value = os.getenv(env_var_name_for_final_config)
        if env_value is not None:
            final_config[yaml_key_for_final_config] = env_value # Override yaml_config if env var is explicitly set
    
    return final_config

# Example of how to use it:
if __name__ == '__main__':
    print("\n=== Testing Config Loading ===")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Looking for config at: {DEFAULT_CONFIG_PATH}")
    
    # Test initial state
    print("\nInitial state:")
    print(f"GOOGLE_API_KEY in environment: {os.getenv('GOOGLE_API_KEY') is not None}")
    
    # Load config
    print("\nLoading config...")
    settings = load_config()
    
    # Test final state
    print("\nFinal state:")
    print(f"Config keys found: {list(settings.keys())}")
    print(f"GOOGLE_API_KEY in settings: {settings.get('google_api_key') is not None}")
    print(f"GOOGLE_API_KEY in environment: {os.getenv('GOOGLE_API_KEY') is not None}")
    
    if os.getenv('GOOGLE_API_KEY'):
        key = os.getenv('GOOGLE_API_KEY')
        print(f"GOOGLE_API_KEY value: {key[:5]}...{key[-4:]}")
    else:
        print("GOOGLE_API_KEY not found in environment!")
    
    print("\n=== End Config Test ===") 