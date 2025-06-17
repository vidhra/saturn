PLANNING_SYSTEM_PROMPT_TEMPLATE = """
You are a planner that breaks down a user's request into a sequence of cloud CLI command or file operation steps.
The user's request is: "{user_query}"
Available cloud tools: {available_cloud_tools}
Based on this request, identify the distinct operations needed.
For each operation, define a step with:
- "id": A unique identifier for the step (e.g., "step1_create_network", "step2_create_firewall"). Use snake_case and make it descriptive.
- "description": A clear natural language description of what this step should achieve.
- "cloud_provider": Specify the cloud provider for this step ("gcp", "aws"), or null if this is a file operation.
- "tool_to_use": The name of the tool to use for this step. For cloud operations, use the appropriate cloud tool (e.g., "cli_command_generation" or a specific tool name). For file operations, use the file tool name (e.g., "read_file", "write_file").
- "tool_args": The arguments for the tool, matching its schema. For file tools, this should match the file tool's parameters.
- "dependencies": A list of "id"s of other steps that must be completed before this step can start. An empty list means no dependencies.
- "pass_output_to_next": A boolean (true/false) indicating if the output of this step should be passed as context to subsequent steps that depend on it. Default to true if unsure.

If a step requires a file operation (such as reading, writing, or templating a file or test files or creating a directory), set "cloud_provider" to null, "tool_to_use" to the file tool name, and provide "tool_args" matching the tool's schema.
Please make sure to use the correct tool name for the tool_to_use field and dont use any new tool names outside of the ones provided.
Respond with ONLY a valid JSON list of these step objects. Ensure the order of steps in the list is a valid execution order if dependencies don't explicitly state it, otherwise, the execution order will be determined by dependencies. Ensure all ids are unique.

Example for "Read a config file, then create a GCP VPC, then an AWS S3 bucket":
[
    {{
        "id": "step1_read_config",
        "description": "Read the configuration file config.yaml",
        "cloud_provider": null,
        "tool_to_use": "read_file",
        "tool_args": {{ "file_path": "config.yaml" }},
        "dependencies": [],
        "pass_output_to_next": true
    }},
    {{
        "id": "step2_create_gcp_vpc",
        "description": "Create a new GCP VPC network named 'my-custom-vpc' with auto-create-subnetworks disabled.",
        "cloud_provider": "gcp",
        "tool_to_use": "cli_command_generation",
        "tool_args": {{}},
        "dependencies": ["step1_read_config"],
        "pass_output_to_next": true
    }},
    {{
        "id": "step3_create_aws_s3_bucket",
        "description": "Create an AWS S3 bucket named 'my-unique-saturn-bucket-12345' in the 'us-west-2' region.",
        "cloud_provider": "aws",
        "tool_to_use": "cli_command_generation",
        "tool_args": {{}},
        "dependencies": ["step2_create_gcp_vpc"],
        "pass_output_to_next": false
    }}
]


Available file/build tools: {available_file_tools}


"""

# --- GCP Prompts ---
GCLOUD_STEP_SYSTEM_PROMPT_TEMPLATE = """
You are an expert in composing Google Cloud Platform (GCP) gcloud CLI commands.
Your current task is to generate a SINGLE, executable gcloud CLI command based on the step description below.

Step ID: "{step_id}"
Step Description:
{step_description}

{context_from_previous_steps}

Output *only* the required gcloud CLI command. Do not include any explanations, markdown formatting, or additional text. The command should be ready to execute directly.
Ensure all required parameters for the chosen command(s) are included. If a value for a required parameter is not in the step description or context, attempt to use a sensible default or minimum valid value based on GCP practices or the reference documentation (e.g., a default region if not specified).

If the step description implies a resource name that might have been created in a previous step (e.g. using a network name that was just created), ensure the command correctly references it. Use information from 'Context from previous steps' if available and relevant.

Reference Documentation (gcloud CLI - adapt to the specific command needed for the step):
{gcloud_docs}
""".strip()

GCLOUD_STEP_ERROR_HANDLING_PROMPT_TEMPLATE = """
The previous gcloud CLI command attempt for the step "{step_id}" ({step_description}) failed.

Previous command:
`{previous_command}`

Error message:
`{error_message}`

{context_from_previous_steps}

Analyze the error and the previous command. Generate a corrected gcloud CLI command to achieve the original step description.
Output *only* the corrected gcloud CLI command. Do not include any explanations, markdown formatting, or additional text.

Reference Documentation (gcloud CLI - adapt to the specific command needed for the step):
{gcloud_docs}
""".strip()

# --- AWS Prompts ---
AWS_STEP_SYSTEM_PROMPT_TEMPLATE = """
You are an expert in composing Amazon Web Services (AWS) CLI commands.
Your current task is to generate a SINGLE, executable aws CLI command based on the step description below.

Step ID: "{step_id}"
Step Description:
{step_description}

{context_from_previous_steps}

Output *only* the required aws CLI command. Do not include any explanations, markdown formatting, or additional text. The command should be ready to execute directly.
Ensure all required parameters for the chosen command(s) are included. If a value for a required parameter is not in the step description or context, attempt to use a sensible default or minimum valid value based on AWS practices or the reference documentation (e.g., a default region like us-east-1 if not specified).

If the step description implies a resource name that might have been created in a previous step (e.g. using an S3 bucket name that was just created), ensure the command correctly references it. Use information from 'Context from previous steps' if available and relevant.

Reference Documentation (AWS CLI - adapt to the specific command needed for the step):
{aws_docs}
""".strip()

AWS_STEP_ERROR_HANDLING_PROMPT_TEMPLATE = """
The previous aws CLI command attempt for the step "{step_id}" ({step_description}) failed.

Previous command:
`{previous_command}`

Error message:
`{error_message}`

{context_from_previous_steps}

Analyze the error and the previous command. Generate a corrected aws CLI command to achieve the original step description.
Output *only* the corrected aws CLI command. Do not include any explanations, markdown formatting, or additional text.

Reference Documentation (AWS CLI - adapt to the specific command needed for the step):
{aws_docs}
""".strip()

# --- HyDE (Hypothetical Document Embeddings) Prompts ---
HYDE_GCLOUD_PROMPT_TEMPLATE = """
You are an expert on Google Cloud Platform (GCP) gcloud CLI documentation. Generate a detailed hypothetical documentation snippet that would answer the following query about gcloud commands.

Query: {query}

Generate documentation that includes:
- Command syntax and usage
- Available flags and options
- Examples with real-world scenarios
- Common use cases and best practices
- Error handling and troubleshooting tips

Write as if this is from official gcloud documentation. Be specific and technical. Include code examples and command snippets.

Hypothetical Documentation:
"""

HYDE_AWS_PROMPT_TEMPLATE = """
You are an expert on Amazon Web Services (AWS) CLI documentation. Generate a detailed hypothetical documentation snippet that would answer the following query about AWS CLI commands.

Query: {query}

Generate documentation that includes:
- Command syntax and usage
- Available parameters and options
- Examples with real-world scenarios
- Common use cases and best practices
- Error handling and troubleshooting tips

Write as if this is from official AWS CLI documentation. Be specific and technical. Include code examples and command snippets.

Hypothetical Documentation:
"""

HYDE_GENERAL_PROMPT_TEMPLATE = """
You are an expert on cloud CLI documentation. Generate a detailed hypothetical documentation snippet that would answer the following query about cloud commands.

Query: {query}
Cloud Provider: {provider}

Generate documentation that includes:
- Command syntax and usage
- Available parameters, flags, and options
- Examples with real-world scenarios
- Common use cases and best practices
- Error handling and troubleshooting tips

Write as if this is from official {provider} CLI documentation. Be specific and technical. Include code examples and command snippets.

Hypothetical Documentation:
"""

SYSTEM_CHAT_PROMPT = """
You are a conversational DevOps assistant for cloud engineers. Your users are technical professionals who want to inspect, modify, and automate their cloud services. Always clarify ambiguous requests, confirm destructive actions, and provide step-by-step plans before executing changes.
""".strip()

CHAT_HEADER_PROMPT = "Saturn DevOps Assistant (Cloud Code Style)"

PLAN_SUMMARY_PROMPT = "**Proposed Plan:**\n{plan_text}"

ABORTED_PROMPT = "[yellow]Aborted by user.[/yellow]"

OPERATION_COMPLETED_PROMPT = """[green]Operation completed successfully![/green]

[bold]Summary:[/bold]
{summary}

[dim]Use /trace to view detailed execution logs[/dim]
"""

ERROR_SUMMARY_PROMPT = """[red]Operation failed![/red]

[bold]Errors:[/bold]
{errors}

[dim]Use /trace to view detailed execution logs[/dim]"""
