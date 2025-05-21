PLANNING_SYSTEM_PROMPT_TEMPLATE = """
You are a planner that breaks down a user's request into a sequence of gcloud CLI command steps.
The user's request is: "{user_query}"

Based on this request, identify the distinct gcloud operations needed.
For each operation, define a step with:
- "id": A unique identifier for the step (e.g., "step1_create_network", "step2_create_firewall"). Use snake_case and make it descriptive.
- "description": A clear natural language description of what this gcloud command should achieve. This description will be given to another AI to generate the exact gcloud command.
- "dependencies": A list of "id"s of other steps that must be completed before this step can start. An empty list means no dependencies.
- "tool_to_use": For now, always set this to "gcloud_command_generation".
- "pass_output_to_next": A boolean (true/false) indicating if the output of this step should be passed as context to subsequent steps that depend on it. Default to true if unsure.

Respond with ONLY a valid JSON list of these step objects. Ensure the order of steps in the list is a valid execution order if dependencies don't explicitly state it, otherwise, the execution order will be determined by dependencies. Ensure all ids are unique.

Example for "Create a VPC, then a subnet in it, then a firewall rule for the VPC":
[
    {{
        "id": "step1_create_vpc",
        "description": "Create a new VPC network named 'my-custom-vpc' with auto-create-subnetworks disabled and enable Private Google Access.",
        "dependencies": [],
        "tool_to_use": "gcloud_command_generation",
        "pass_output_to_next": true
    }},
    {{
        "id": "step2_create_subnet",
        "description": "Create a subnet named 'my-custom-subnet' in the 'my-custom-vpc' network in region 'us-central1' with IP range '10.1.0.0/24'.",
        "dependencies": ["step1_create_vpc"],
        "tool_to_use": "gcloud_command_generation",
        "pass_output_to_next": false
    }},
    {{
        "id": "step3_create_firewall_rule",
        "description": "Create a firewall rule named 'allow-ssh-my-custom-vpc' for the 'my-custom-vpc' network, allowing TCP ingress on port 22 from any source ('0.0.0.0/0') with a priority of 1000.",
        "dependencies": ["step1_create_vpc"],
        "tool_to_use": "gcloud_command_generation",
        "pass_output_to_next": false
    }}
]
"""

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

Reference Documentation (gcloud compute instances create - this is a general example, adapt to the specific command needed for the step):
{gcloud_docs}
""".strip()

GCLOUD_STEP_ERROR_HANDLING_PROMPT_TEMPLATE = """
The previous gcloud command attempt for the step "{step_id}" ({step_description}) failed.

Previous command:
`{previous_command}`

Error message:
`{error_message}`

{context_from_previous_steps}

Analyze the error and the previous command. Generate a corrected gcloud CLI command to achieve the original step description.
Output *only* the corrected gcloud CLI command. Do not include any explanations, markdown formatting, or additional text.

Reference Documentation (gcloud compute instances create - this is a general example, adapt to the specific command needed for the step):
{gcloud_docs}
""".strip() 