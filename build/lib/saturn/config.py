import os
import yaml
from typing import Optional, Dict, Any

# Standard config locations - will be checked in order
CONFIG_FILE_NAME = "config.yaml"
USER_CONFIG_DIR = os.path.expanduser("~/.config/saturn")

# Map of config.yaml keys to their corresponding environment variable names
ENV_VAR_MAP = {
    "openai_api_key": "OPENAI_API_KEY",
    "google_api_key": "GOOGLE_API_KEY",
    "gemini_api_key": "GEMINI_API_KEY",
    "anthropic_api_key": "ANTHROPIC_API_KEY",
    "mistral_api_key": "MISTRAL_API_KEY",
    "gcp_project_id": "GCP_PROJECT_ID",
    "gcp_credentials_path": "GOOGLE_APPLICATION_CREDENTIALS", # Note: GOOGLE_APPLICATION_CREDENTIALS is standard for ADC
    "aws_region": "AWS_REGION",
    "aws_profile": "AWS_PROFILE",
    "vector_store": "VECTOR_STORE",
    "rag_docs_path": "GCLOUD_DOCS_PATH", # Consider renaming to RAG_DOCS_PATH for clarity
    "rag_embedding_model": "RAG_EMBED_MODEL",
    "chroma_db_path": "CHROMA_DB_PATH",
    "chroma_collection_name": "CHROMA_COLLECTION",
    "duckdb_path": "DUCKDB_PATH",
    "duckdb_file_name": "DUCKDB_FILE_NAME",
    "duckdb_table_name": "DUCKDB_TABLE_NAME",
}

def load_config(config_path_override: Optional[str] = None) -> Dict[str, Any]:
    """
    Loads configuration from a YAML file, sets environment variables from YAML if not already set,
    and then merges with direct environment variable overrides.
    Precedence for YAML loading: config_path_override > ./config.yaml > ~/.config/saturn/config.yaml
    Precedence for values: Direct Environment Vars > YAML-set Env Vars (from YAML file) > YAML file values > Defaults in code.
    """
    paths_to_check = []
    if config_path_override:
        paths_to_check.append(config_path_override)
    paths_to_check.append(os.path.join(os.getcwd(), CONFIG_FILE_NAME)) # Current working directory
    paths_to_check.append(os.path.join(USER_CONFIG_DIR, CONFIG_FILE_NAME)) # User config directory
    
    yaml_config: Dict[str, Any] = {}
    loaded_config_path = None

    for path_attempt in paths_to_check:
        print(f"[ConfigDebug] Attempting to load config from: {path_attempt}")
        if os.path.exists(path_attempt):
            print(f"[ConfigDebug] Found config file: {path_attempt}")
            try:
                with open(path_attempt, 'r') as f:
                    loaded_data = yaml.safe_load(f)
                    if isinstance(loaded_data, dict):
                        yaml_config = loaded_data
                        loaded_config_path = path_attempt
                        print(f"[ConfigDebug] Successfully loaded config from {loaded_config_path} with keys: {list(loaded_data.keys())}")
                        break # Stop searching once a config is successfully loaded
                    else:
                        print(f"[ConfigDebug] Warning: Config file {path_attempt} did not load as a dict. Loaded: {type(loaded_data)}")
            except Exception as e:
                print(f"[ConfigDebug] Warning: Could not read/parse config file {path_attempt}: {e}")
        else:
            print(f"[ConfigDebug] Config file not found: {path_attempt}")
    
    if not loaded_config_path:
        print(f"[ConfigDebug] No config file was successfully loaded from checked paths.")

    # Set environment variables from YAML config if they are not already set in the environment
    for yaml_key, env_var_name in ENV_VAR_MAP.items():
        if yaml_key in yaml_config and yaml_config[yaml_key] is not None:
            if not os.getenv(env_var_name):
                os.environ[env_var_name] = str(yaml_config[yaml_key])
                # print(f"[ConfigDebug] Set env var '{env_var_name}' from config.yaml value.") # Less verbose
            # else:
                # print(f"[ConfigDebug] Env var '{env_var_name}' already set, not overwriting from yaml.")

    # Debug print for GOOGLE_API_KEY after potential setting from YAML
    current_google_api_key_in_env = os.getenv("GOOGLE_API_KEY")
    if current_google_api_key_in_env:
        print(f"[ConfigDebug] After potential YAML->env setting: os.getenv('GOOGLE_API_KEY') is set.")
    else:
        print("[ConfigDebug] After potential YAML->env setting: os.getenv('GOOGLE_API_KEY') is None.")

    final_config = yaml_config.copy()
    for yaml_key_for_final_config, env_var_name_for_final_config in ENV_VAR_MAP.items():
        env_value = os.getenv(env_var_name_for_final_config)
        if env_value is not None:
            final_config[yaml_key_for_final_config] = env_value
            # print(f"[ConfigDebug] Final config for '{yaml_key_for_final_config}' set from env var '{env_var_name_for_final_config}'.")
    
    # Ensure USER_CONFIG_DIR exists if we decide to write a default config later
    # For now, just create it if we loaded a config from there or if it's a standard path.
    # if not os.path.exists(USER_CONFIG_DIR):
    #     try:
    #         os.makedirs(USER_CONFIG_DIR)
    #         print(f"[ConfigDebug] Created user config directory: {USER_CONFIG_DIR}")
    #     except Exception as e:
    #         print(f"[ConfigDebug] Could not create user config directory {USER_CONFIG_DIR}: {e}")

    return final_config

# Example of how to use it:
if __name__ == '__main__':
    print("\n=== Testing Config Loading ===")
    # Simulate running from a project directory where config.yaml might exist
    # To test, create a dummy config.yaml in your CWD or ~/.config/saturn/
    print(f"Current working directory: {os.getcwd()}")
    user_config_path_test = os.path.join(USER_CONFIG_DIR, CONFIG_FILE_NAME)
    print(f"Checking for user config at: {user_config_path_test}")
    print(f"Checking for CWD config at: {os.path.join(os.getcwd(), CONFIG_FILE_NAME)}")

    # Test initial state
    print("\nInitial state of GOOGLE_API_KEY in environment:", os.getenv('GOOGLE_API_KEY'))
    
    print("\nLoading config...")
    # Pass no override to test default search paths
    settings = load_config()
    
    print("\nFinal state:")
    print(f"Config keys loaded: {list(settings.keys())}")
    print(f"GOOGLE_API_KEY in returned settings dict: {settings.get('google_api_key')}")
    print(f"GOOGLE_API_KEY in environment after load_config: {os.getenv('GOOGLE_API_KEY')}")
    
    # Example: Check GCP_PROJECT_ID
    print(f"GCP_PROJECT_ID in returned settings dict: {settings.get('gcp_project_id')}")
    print(f"GCP_PROJECT_ID in environment after load_config: {os.getenv('GCP_PROJECT_ID')}")

    print("\n=== End Config Test ===") 