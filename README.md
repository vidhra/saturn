# GCP Natural Language CLI

This project aims to provide a command-line interface (CLI) for interacting with Google Cloud Platform (GCP) APIs using natural language queries. It leverages OpenAI's function calling capabilities to translate user requests into specific GCP API calls and includes an error-handling feedback loop to improve reliability.

## Features (Planned)

*   **Natural Language Input:** Control GCP resources using commands like "create a firewall rule", "list storage buckets", etc.
*   **Multi-Service Support:** Designed to work with various GCP services (Compute Engine, VPC Access, Cloud Storage, etc.).
*   **Error Correction:** Automatically attempts to correct failed API calls by analyzing errors and adjusting parameters.
*   **Extensible Knowledge Base:** Uses API definitions (initially JSON files) to inform the LLM about available GCP functions.
*   **(Future) State Management:** Track created resources.
*   **(Future) DAG Planning:** Model dependencies between operations for complex workflows.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd gcp-natural-language-cli
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration:**
    *   **Environment Variables:** Set the following environment variables:
        *   `OPENAI_API_KEY`: Your OpenAI API key.
        *   `GCP_PROJECT_ID`: Your Google Cloud project ID.
        *   `GOOGLE_APPLICATION_CREDENTIALS`: (Optional) Path to your GCP service account key file. If not set, the tool relies on Application Default Credentials (ADC).
    *   **Alternatively, use `config.yaml`:** Create a `config.yaml` file in the root directory with the following structure:
        ```yaml
        openai_api_key: "sk-..."
        gcp_project_id: "your-gcp-project-id"
        gcp_credentials_path: "/path/to/your/keyfile.json" # Optional
        ```

5.  **API Definitions:** Place the `tools.json` and `types.json` files for each required GCP service into subdirectories within the `api_defs/` directory. The subdirectory name should correspond to the service name used in the code (e.g., `api_defs/vpcaccess_v1/`, `api_defs/compute_v1/`).

## Usage

```bash
python cli.py "Your natural language query here" [OPTIONS]
```

**Example:**

```bash
python cli.py "Create a serverless VPC access connector named 'my-connector' in us-central1 with IP range 10.8.0.0/28 in the default network."
```

**Options:**

*   `--config-file TEXT`: Path to configuration file (default: `config.yaml`).
*   `--state-file TEXT`: Path to state file (default: `gcp_state.json`).
*   `--api-defs-dir TEXT`: Directory containing GCP API definitions (default: `api_defs`).
*   `--max-attempts INTEGER`: Maximum retry attempts for API calls (default: 5).
*   `--verbose, -v`: Enable verbose output.
*   `--help`: Show help message.

## Development

(Add notes on running tests, contributing, etc. later)
