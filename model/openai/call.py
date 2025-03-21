import json
from openai import ChatCompletion
from openai import OpenAI
import asyncio
import importlib
import os
from google.cloud import billing_v1
# Set your OpenAI API key
api_key = "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"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "vidhra-eb3e8152e0a2.json"

# Define the task instruction
task_instruction = """
You are an expert in composing functions. You are given a question and a set of possible functions. 
Based on the question, you will need to make one or more function/tool calls to achieve the purpose. 
If none of the functions can be used, point it out and refuse to answer. 
If the given question lacks the parameters required by the function, also point it out.
""".strip()

# Define the format instruction
format_instruction = """
The output MUST strictly adhere to the following JSON format, and NO other text MUST be included.
The example format is as follows. Please make sure the parameter type is correct. If no function call is needed, please make tool_calls an empty list '[]'. 
Please don't forget the request type in the function call. The request type is mentioned as the request_types in the function call.
{ "tool_calls": [ {"name": "func_name1", "arguments": {"argument1": "value1", "argument2": "value2"}}, ... (more tool calls as required) ] }
""".strip()

# Define the user query
query = "can you update the billing account info of the project vidhra to vidhra-ai"



client = OpenAI(
    api_key=api_key,  # This is the default and can be omitted
)
tools_data = {}
types_data = {}

def build_openai_tools(tools_json_path, types_json_path):
    """
    Builds OpenAI function definitions by combining tools.json and types.json information.
    """
    with open(tools_json_path, 'r') as f:
        tools_data = json.load(f)
    
    with open(types_json_path, 'r') as f:
        types_data = json.load(f)

    # Extract all request types from types.json for quick lookup
    request_types_map = {}
    for file_types in types_data.values():
        for type_info in file_types:
            if type_info["type"] == "function":
                request_types_map[type_info["name"]] = type_info

    openai_tools = []
    
    # Process each service in tools.json
    for service_name, service_data in tools_data.items():
        for method in service_data["methods"]:
            # Get the request type from the method
            request_types = method["function"].get("request_types", [])
            if not request_types:
                continue
                
            # Use the first request type to build the function definition
            request_type = request_types[0]
            type_info = request_types_map.get(request_type)
            
            if not type_info:
                continue

            # Build the OpenAI function definition
            print(method["function"]["name"])
            tool = {
                "type": "function",
                "name": method["function"]["name"],
                "description": type_info["description"],
                "parameters": type_info["parameters"]
            }
            openai_tools.append(tool)

    return openai_tools

# Use the function to build tools dynamically
tools_json_path = "billing_v1/tools.json"
types_json_path = "billing_v1/types.json"
openai_format_tools = build_openai_tools(tools_json_path, types_json_path)


def build_prompt(task_instruction: str, format_instruction: str, tools: list, query: str):
    prompt = f"[BEGIN OF TASK INSTRUCTION]\n{task_instruction}\n[END OF TASK INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF AVAILABLE TOOLS]\n{json.dumps(openai_format_tools)}\n[END OF AVAILABLE TOOLS]\n\n"
    prompt += f"[BEGIN OF FORMAT INSTRUCTION]\n{format_instruction}\n[END OF FORMAT INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF QUERY]\n{query}\n[END OF QUERY]\n\n"
    return prompt

def convert_strings_to_json(data: dict) -> dict:
    """Recursively attempt to parse any string fields as JSON objects."""
    new_data = {}
    for k, v in data.items():
        if isinstance(v, str):
            try:
                parsed_value = json.loads(v)
                # If it's valid JSON, store the parsed structure (dict, list, etc.)
                new_data[k] = parsed_value
            except json.JSONDecodeError:
                # If it's not valid JSON, leave it as-is
                new_data[k] = v
        elif isinstance(v, dict):
            # Recurse into nested dictionaries
            new_data[k] = convert_strings_to_json(v)
        elif isinstance(v, list):
            # Check if there's a nested dictionary inside the list
            new_list = []
            for item in v:
                if isinstance(item, dict):
                    new_list.append(convert_strings_to_json(item))
                else:
                    new_list.append(item)
            new_data[k] = new_list
        else:
            # For all other types, just pass them along
            new_data[k] = v
    return new_data

async def dynamic_executor(request_type: str, method_name: str, args: dict):
    """
    Dynamically call a method from the CloudBillingAsyncClient by:
      1. Retrieving the request class using 'class_name' from billing_v1
      2. Retrieving the async method using 'method_name'
      3. Instantiating 'RequestClass' with parameter values from 'args'
         (Parsing JSON strings where appropriate)
      4. Invoking the async method.
    """
    try:
        RequestClass = getattr(billing_v1, request_type)

        billing_client = billing_v1.CloudBillingAsyncClient()
        method = getattr(billing_client, method_name)

        # Convert any JSON strings into Python dictionaries (or lists)
        parsed_args = convert_strings_to_json(args)

        # Instantiate request object with the parsed arguments
        print(parsed_args)
        request = RequestClass(**parsed_args)

        billing_info = await method(request=request)
        print(billing_info)
        return billing_info

    except AttributeError as e:
        print(f"Failed to find attribute: {e}")
    except Exception as e:
        print(f"Failed to execute request: {e}")

# Example usage




content = build_prompt(task_instruction, format_instruction, openai_format_tools, query)

#Helper function to build the prompt
response = client.responses.create(
  model="gpt-4.5-preview",
  input=[
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": content
        }
      ]
    },
  ],
  text={
    "format": {
      "type": "json_object"
    }
  },
  tools=openai_format_tools,
)

def extract_args(arguments: dict,start_key='request',end_key='retry'):
    keys = list(arguments.keys())
    try:
        # Get start and end indexes
        start_index = keys.index(start_key)
        end_index = keys.index(end_key)
        
        # Return a new dictionary with keys/values in the desired range
        return {key: arguments[key] for key in keys[start_index+1:end_index]}
    except ValueError as e:
        # if keys don't exist
        print(f"Key error: {e}")
        return {}

# asyncio.run(get_billing_info())
#Call the API to get the response
# tool_calls = response.choices[0].message.tool_calls
# content = response.choices[0].message.content
content = response.output_text
print(content)


def get_request_types_for_method(tools_json_path: str, method_name: str) -> list:
    """
    Returns a list of request types for the given *method name* (e.g. 'update_project_billing_info').
    Gathers them from all services in tools.json.
    """
    import json

    with open(tools_json_path, "r", encoding="utf-8") as f:
        tools_data = json.load(f)

    # We’ll search across all services for this method
    all_request_types = set()

    for service_name, service_data in tools_data.items():
        for method_def in service_data.get("methods", []):
            fn_info = method_def.get("function", {})
            if fn_info.get("name") == method_name:
                # method_name matches, gather any request_types
                req_types = fn_info.get("request_types", [])
                for rt in req_types:
                    all_request_types.add(rt)

    return sorted(all_request_types)


# Example usage:
tools_json_path = "billing_v1/tools.json"


# Then in your dynamic_executor or wherever you need it:
tools = json.loads(content)
for call in tools["tool_calls"]:
    # Suppose the call includes "service_name" and "method_name"
    method_name = call["name"]

    # Find the corresponding request type
    request_types = get_request_types_for_method(tools_json_path, method_name)  # e.g. "GetBillingAccountRequest"

    print(f"Found request type for {method_name}: {request_types}")
    print(request_types[0])
    asyncio.run(dynamic_executor(
        request_types[0],
        method_name,
        call["arguments"]
    ))


