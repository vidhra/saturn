import os
import yaml
from typing import Optional, Dict, Any

DEFAULT_CONFIG_PATH = "config.yaml"

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Loads configuration from environment variables and a YAML file.
    Environment variables override file settings.
    """
    path = config_path or DEFAULT_CONFIG_PATH
    print(f"[Debug config] Attempting to load config. Path: {path}") # Debug print
    config = {}

    # Load from YAML file if it exists
    if os.path.exists(path):
        print(f"[Debug config] Found config file: {path}") # Debug print
        try:
            with open(path, 'r') as f:
                loaded_yaml = yaml.safe_load(f)
                print(f"[Debug config] YAML loaded type: {type(loaded_yaml)}, value: {loaded_yaml}") # Debug print
                config = loaded_yaml or {}
        except Exception as e:
            print(f"[Debug config] Warning: Could not read/parse config file {path}: {e}")
            config = {}
    else:
        print(f"[Debug config] Config file not found: {path}") # Debug print
        
    print(f"[Debug config] Config after YAML load: type={type(config)}, value={config}") # Debug print

    # Load from Environment Variables (and potentially override file settings)
    env_config = {
        'openai_api_key': os.getenv('OPENAI_API_KEY'),
        'gcp_project_id': os.getenv('GCP_PROJECT_ID'),
        'gcp_credentials_path': os.getenv('GOOGLE_APPLICATION_CREDENTIALS'),
    }
    print(f"[Debug config] Environment variables loaded: {env_config}") # Debug print

    # Merge environment variables, giving them precedence
    # Ensure config is a dict before merging
    if not isinstance(config, dict):
        print(f"[Debug config] Warning: Config was not a dict before env merge (type: {type(config)}). Resetting to empty dict.")
        config = {}
        
    for key, value in env_config.items():
        if value is not None:
            config[key] = value

    print(f"[Debug config] Config after env merge: type={type(config)}, value={config}") # Debug print
    return config

# Example of how to use it:
# if __name__ == '__main__':
#     settings = load_config()
#     print(f"Loaded settings: {settings}")
#     api_key = settings.get('openai_api_key')
#     if not api_key:
#         print("OpenAI API Key is missing!")
#     else:
#         print(f"OpenAI Key starts with: {api_key[:5]}...") 