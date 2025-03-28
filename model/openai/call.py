import json
from openai import ChatCompletion
from openai import OpenAI
import asyncio
import importlib
import os
from google.cloud import functions_v1,vpcaccess_v1
from google.protobuf import field_mask_pb2
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
The output MUST strictly adhere to the following JSON format if only the parameters are understandable, and NO other text MUST be included.
The example format is as follows. Please make sure the parameter type is correct. If no function call is needed, please make tool_calls an empty list '[]'. 
Please don't forget the request type in the function call. The request type is mentioned as the request_types in the function call.
{ "tool_calls": [ {"name": "func_name1", "arguments": {"argument1": "value1", "argument2": "value2"}}, ... (more tool calls as required) ] }
""".strip()

# Define the user query
query = " Can you create vpc access connectors in the project vidhra us-central1?"



client = OpenAI(
    api_key=api_key,  # This is the default and can be omitted
)
tools_data = {}
types_data = {}

def build_openai_tools(tools_json_path, types_json_path):
    """
    Builds OpenAI function definitions by combining tools.json and types.json.
    Any 'enum' definitions like:
      {
        "type": "enum",
        "values": {
          "SECURE_ALWAYS": {"value": 1},
          "SECURE_OPTIONAL": {"value": 2}
        }
      }
    will be turned into:
      {
        "type": "string",
        "enum": ["SECURE_ALWAYS", "SECURE_OPTIONAL"]
      }
    and your final list of tools will now each have "type": "function".
    """
    import json

    with open(tools_json_path, "r", encoding="utf-8") as f:
        tools_data = json.load(f)

    with open(types_json_path, "r", encoding="utf-8") as f:
        types_data = json.load(f)

    # A map { "CreateFunctionRequest": { ... }, ... } from types.json
    request_types_map = {}
    for file_types in types_data.values():
        for type_info in file_types:
            if type_info["type"] == "function":
                request_types_map[type_info["name"]] = type_info

    def transform_fields(schema_fragment):
        """
        Recursively walks the schema, and:
          1. Converts any enum references into { "type": "string", "enum": [...] }.
          2. If 'resolved_schema' is present, merges its properties into the parent object.
        """
        if not isinstance(schema_fragment, dict):
            return schema_fragment

        # Merge properties from resolved_schema into schema_fragment
        if "resolved_schema" in schema_fragment and isinstance(schema_fragment["resolved_schema"], dict):
            resolved = schema_fragment.pop("resolved_schema")

            # Merge 'properties' from resolved_schema into the parent
            if "properties" in resolved and isinstance(resolved["properties"], dict):
                if "properties" not in schema_fragment:
                    schema_fragment["properties"] = {}
                for prop_name, prop_value in resolved["properties"].items():
                    schema_fragment["properties"][prop_name] = prop_value

            # Merge any other top-level fields from resolved_schema
            for key, val in resolved.items():
                if key != "properties":
                    schema_fragment[key] = val
        print(schema_fragment)

        # Convert enumerations
        if schema_fragment.get("type") == "enum" and "values" in schema_fragment:
            enum_vals = schema_fragment.pop("values")
            schema_fragment["type"] = "string"
            schema_fragment["enum"] = list(enum_vals.keys())

        # Recurse into 'properties'
        if "properties" in schema_fragment and isinstance(schema_fragment["properties"], dict):
            for prop_name, prop_value in schema_fragment["properties"].items():
                schema_fragment["properties"][prop_name] = transform_fields(prop_value)

        # Recurse into 'items'
        if "items" in schema_fragment:
            if isinstance(schema_fragment["items"], dict):
                schema_fragment["items"] = transform_fields(schema_fragment["items"])
            elif isinstance(schema_fragment["items"], list):
                schema_fragment["items"] = [transform_fields(x) for x in schema_fragment["items"]]

        # Recurse into 'additionalProperties'
        if "additionalProperties" in schema_fragment and isinstance(schema_fragment["additionalProperties"], dict):
            schema_fragment["additionalProperties"] = transform_fields(schema_fragment["additionalProperties"])

        return schema_fragment

    openai_tools = []

    # For each function method found in tools.json, look up the corresponding type schema
    for service_name, service_data in tools_data.items():
        for method in service_data["methods"]:
            request_types = method["function"].get("request_types", [])
            if not request_types:
                continue
            request_type_name = request_types[0]
            if request_type_name not in request_types_map:
                continue

            import copy
            type_info = request_types_map[request_type_name]
            parameters_copy = copy.deepcopy(type_info["parameters"])

            # Transform any enums -> { type: "string", enum: [...] }
            parameters_copy = transform_fields(parameters_copy)

            # Build your final tool definition (note the "type": "function" fix)
            print(method["function"]["name"])
            openai_tools.append({
                "type": "function",
                "name": method["function"]["name"],
                "description": type_info["description"],
                "parameters": parameters_copy,
            })

    return openai_tools

# Use the function to build tools dynamically
tools_json_path = "vpcaccess_v1/tools.json"
types_json_path = "vpcaccess_v1/types.json"
openai_format_tools = build_openai_tools(tools_json_path, types_json_path)

def build_prompt_system(task_instruction: str, format_instruction: str):
    prompt = f"[BEGIN OF TASK INSTRUCTION]\n{task_instruction}\n[END OF TASK INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF FORMAT INSTRUCTION]\n{format_instruction}\n[END OF FORMAT INSTRUCTION]\n\n"
    return prompt

def build_prompt_user(tools: list, query: str):
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
        RequestClass = getattr(vpcaccess_v1, request_type)
        # RequestClassFunctionAccount = getattr(vpcaccess_v1, "VpcAccess")

        function_client = vpcaccess_v1.VpcAccessServiceAsyncClient()
        method = getattr(function_client, method_name)

        # Remove "account" from the original args before conversion
        function_value = args.pop("function", None)

        # Convert any JSON strings into Python dictionaries (or lists)
        parsed_args = convert_strings_to_json(args)


        request = None

        # # Attach the "account" field to a BillingAccount object if present
        # if function_value is not None:
        #     parsed_args_function = convert_strings_to_json(function_value)
        #     request = RequestClass(**parsed_args,function=RequestClassFunctionAccount(**parsed_args_function))
        # else:
        request = RequestClass(**parsed_args)



        billing_info = await method(request=request)
        print(billing_info)
        return billing_info

    except AttributeError as e:
        print(f"Failed to find attribute: {e}")
    except Exception as e:
        print(f"Failed to execute request: {e}")

# Example usage




content = build_prompt_system(task_instruction, format_instruction)

#Helper function to build the prompt
response = client.responses.create(
  model="gpt-4.5-preview",
  input=[
    {
      "role": "system",
      "content": [
        {
          "type": "input_text",
          "text": content
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": query
        }
      ]
    },
  ],
  text={
    "format": {
      "type": "text"
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
content = response



def get_request_types_for_method(tools_json_path: str, method_name: str) -> list:
    """
    Returns a list of request types for the given *method name* (e.g. 'update_project_billing_info').
    Gathers them from all services in tools.json.
    """
    import json

    with open(tools_json_path, "r", encoding="utf-8") as f:
        tools_data = json.load(f)

    # We'll search across all services for this method
    all_request_types = set()

    for service_name, service_data in tools_data.items():
        for method_def in service_data.get("methods", []):
            fn_info = method_def.get("function", {})
            if fn_info.get("name") == method_name:
                # method_name matches, gather any request_types
                req_types = fn_info.get("request_types", [])
                for rt in req_types:
                    all_request_types.add(rt)
    print(all_request_types)
    return sorted(all_request_types)


# Example usage:
tools_json_path = "vpcaccess_v1/tools.json"

async def collect_pager_results(pager):
    results = []
    async for item in pager:
        results.append(item)
    return results


# Then in your dynamic_executor or wherever you need it:
print(content.output_text)
tools = json.loads(content.output_text)
for call in tools["tool_calls"]:
    # Suppose the call includes "service_name" and "method_name"
    if call["name"].startswith("functions."):
        call["name"] = call["name"][len("functions.") :]

    method_name = call["name"]

    # Find the corresponding request type
    request_types = get_request_types_for_method(tools_json_path, method_name)  # e.g. "GetBillingAccountRequest"

    print(f"Found request type for {method_name}: {request_types}")
    print(request_types[0])
    output = asyncio.run(dynamic_executor(
        request_types[0],
        method_name,
        call["arguments"]
    ))
    print(output)
    results = asyncio.run(collect_pager_results(output))

