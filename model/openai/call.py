import json
from openai import ChatCompletion
from openai import OpenAI
import asyncio
import importlib
import os
from google.cloud import vpcaccess_v1,vpcaccess_v1
from google.protobuf import field_mask_pb2
import numpy as np
from sentence_transformers import SentenceTransformer
import google.api_core.exceptions
from error_agent import create_error_handled_prompt
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Any, Optional

class ToolCall(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    name: str = Field(..., description="The name of the function to call")
    arguments: Dict[str, Any] = Field(..., description="The arguments to pass to the function")

class ToolCalls(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    tool_calls: List[ToolCall] = Field(..., description="List of tool calls to make")

# Set your OpenAI API key
api_key = "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"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "vidhra-eb3e8152e0a2.json"

# Define the task instruction
task_instruction = """
You are an expert in composing functions and handling API errors. Your primary role is to:
1. Analyze and understand the user's request
2. Make appropriate function/tool calls to achieve the purpose
3. When errors occur, carefully analyze the error messages and:
   - Identify the root cause of the error
   - Check for missing or invalid parameters
   - Verify resource names and formats
   - Ensure proper permissions and access
   - Make necessary corrections to the function calls
4. If none of the functions can be used, clearly explain why
5. If the request lacks required parameters, specify which ones are missing
6. Always maintain the original intent while fixing errors
7. Learn from previous errors to prevent similar issues in subsequent attempts

Remember: Your goal is to successfully complete the task while handling any errors that arise.
""".strip()

# Define the format instruction
format_instruction = """
The output MUST strictly adhere to the following JSON format if only the parameters are understandable, and NO other text MUST be included.
The example format is as follows. Please make sure the parameter type is correct. If no function call is needed, please make tool_calls an empty list '[]'. 
Always assume the minimum default values for the parameters that are required and not provided in user query.
Please don't forget the request type in the function call. The request type is mentioned as the request_types in the function call.

""".strip()
# { "tool_calls": [ {"name": "func_name1", "arguments": {"argument1": "value1", "argument2": "value2"}}, ... (more tool calls as required) ] }
# Define the error handling instruction
error_handling_instruction = """
When an error occurs during function execution, you must:
1. Analyze the error message carefully to understand the root cause
2. Check if the error is due to:
   - Missing required parameters
   - Invalid parameter values or types
   - Resource naming issues
   - Permission or access issues
   - Resource conflicts or existence
3. Based on the error analysis:
   - If parameters are missing, add them with appropriate values
   - If values are invalid, correct them according to the API requirements
   - If resource names are malformed, fix the naming format
   - If there are permission issues, ensure proper authentication
   - If resources exist/conflict, handle accordingly
4. Modify the tool calls to address the specific error while maintaining the original intent
5. Ensure all modified tool calls still adhere to the required JSON format
6. If the error cannot be resolved, provide a clear explanation of why
""".strip()

client = OpenAI(
    api_key=api_key,  # This is the default and can be omitted
)
tools_data = {}
types_data = {}

# Initialize the embedding model once
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def filter_optional_parameters(query, tools, similarity_threshold=0.6):
    """
    Filter optional parameters based on the similarity between the query and parameter descriptions.
    
    Args:
        query (str): The user's query
        tools (list): List of tool definitions with parameters
        similarity_threshold (float): Minimum similarity score to keep a parameter (0-1)
        
    Returns:
        list: Filtered list of tools with only relevant parameters
    """
    # Embed the query
    query_embedding = embedding_model.encode(query)
    
    filtered_tools = []
    
    for tool in tools:
        # Create a deep copy of the tool to avoid modifying the original
        import copy
        tool_copy = copy.deepcopy(tool)
        
        # Skip if no parameters
        if 'parameters' not in tool_copy or 'properties' not in tool_copy['parameters']:
            filtered_tools.append(tool_copy)
            continue
        
        # Get required fields (if any)
        required_fields = tool_copy['parameters'].get('required', [])
        
        # Filter parameters
        filtered_properties = {}
        for param_name, param_info in tool_copy['parameters']['properties'].items():
            # Always keep required parameters
            if param_name in required_fields:
                filtered_properties[param_name] = param_info
                continue
                
            # Skip parameters without descriptions
            if 'description' not in param_info or not param_info['description']:
                continue
                
            # Embed the parameter description
            param_embedding = embedding_model.encode(param_info['description'])
            
            # Calculate cosine similarity
            similarity = np.dot(query_embedding, param_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(param_embedding)
            )
            
            # Keep parameter if similarity is above threshold
            if similarity > similarity_threshold:
                filtered_properties[param_name] = param_info
        
        # Update tool with filtered parameters
        tool_copy['parameters']['properties'] = filtered_properties
        filtered_tools.append(tool_copy)
    
    return filtered_tools

def format_tools_for_openai(tools):
    """
    Format tools to ensure they are properly structured for OpenAI API with consistent indentation.
    
    Args:
        tools (list): List of tool definitions
        
    Returns:
        list: Properly formatted tools
    """
    # Remove any fields that might cause validation issues
    formatted_tools = []
    for tool in tools:
        # Create a clean copy without potential problematic fields
        cleaned_tool = {
            "type": tool.get("type", "function"),
            "name": tool.get("name", ""),
            "description": tool.get("description", ""),
            "parameters": tool.get("parameters", {})
        }
        formatted_tools.append(cleaned_tool)
    
    return formatted_tools

def filter_tools_for_query(query, tools_json_path, types_json_path):
    """
    Build OpenAI tools and filter optional parameters based on query relevance.
    
    Args:
        query (str): The user's query
        tools_json_path (str): Path to tools.json file
        types_json_path (str): Path to types.json file
        
    Returns:
        list: Filtered tools with only relevant parameters
    """
    # First build the regular tools
    all_tools = build_openai_tools(tools_json_path, types_json_path)
    
    # Then filter optional parameters based on query relevance
    filtered_tools = filter_optional_parameters(query, all_tools)
    
    return filtered_tools

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
    prompt += f"[BEGIN OF ERROR HANDLING INSTRUCTION]\n{error_handling_instruction}\n[END OF ERROR HANDLING INSTRUCTION]\n\n"
    return prompt

# def build_prompt_user(query, tools_json_path, types_json_path):
#     filtered_tools = filter_tools_for_query(query, tools_json_path, types_json_path)
#     print(filtered_tools)
#     prompt = f"[BEGIN OF TASK INSTRUCTION]\n{task_instruction}\n[END OF TASK INSTRUCTION]\n\n"
#     prompt += f"[BEGIN OF AVAILABLE TOOLS]\n{json.dumps(filtered_tools)}\n[END OF AVAILABLE TOOLS]\n\n"
#     prompt += f"[BEGIN OF FORMAT INSTRUCTION]\n{format_instruction}\n[END OF FORMAT INSTRUCTION]\n\n"
#     prompt += f"[BEGIN OF QUERY]\n{query}\n[END OF QUERY]\n\n"
#     return prompt


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
    Dynamically call a method with comprehensive error handling.
    Returns a tuple of (success, result/error_message)
    """
    try:
        RequestClass = getattr(vpcaccess_v1, request_type)
        function_client = vpcaccess_v1.VpcAccessServiceAsyncClient()
        method = getattr(function_client, method_name)

        # Remove "function" from the original args before conversion
        function_value = args.pop("function", None)

        # Convert any JSON strings into Python dictionaries (or lists)
        parsed_args = convert_strings_to_json(args)

        request = RequestClass(**parsed_args)
        result = await method(request=request)
        return True, result

    except AttributeError as e:
        return False, f"Invalid request type or method: {str(e)}"
    except TypeError as e:
        return False, f"Invalid argument types: {str(e)}"
    except ValueError as e:
        return False, f"Invalid argument values: {str(e)}"
    except google.api_core.exceptions.InvalidArgument as e:
        return False, f"Invalid API arguments (400): {str(e)}"
    except google.api_core.exceptions.PermissionDenied as e:
        return False, f"Permission denied (403): {str(e)}"
    except google.api_core.exceptions.NotFound as e:
        return False, f"Resource not found (404): {str(e)}"
    except google.api_core.exceptions.AlreadyExists as e:
        return False, f"Resource already exists (409): {str(e)}"
    except google.api_core.exceptions.FailedPrecondition as e:
        return False, f"Failed precondition (412): {str(e)}"
    except google.api_core.exceptions.ResourceExhausted as e:
        return False, f"Resource exhausted (429): {str(e)}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

# Example usage




content = build_prompt_system(task_instruction, format_instruction)
# filtered_tools = filter_tools_for_query(query, tools_json_path, types_json_path)

# Format the tools properly before sending to OpenAI
formatted_tools = format_tools_for_openai(openai_format_tools)

with open("formatted_tools.json", "w") as f:
    json.dump(formatted_tools, f, indent=2)

print("Sending formatted tools to OpenAI:")
print(json.dumps(formatted_tools, indent=2))

# Helper function to build the prompt
# response = client.responses.create(
#   model="gpt-4o",
#   input=[
#     {
#       "role": "system",
#       "content": [
#         {
#           "type": "input_text",
#           "text": content
#         }
#       ]
#     },
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "input_text",
#           "text": query
#         }
#       ]
#     },
#   ],
#   text={
#     "format": {
#       "type": "text"
#     }
#   },
#   tools=formatted_tools,
# )

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
# content = response



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
# print(content.output_text)
# tools = json.loads(content.output_text)
# for call in tools["tool_calls"]:
#     # Suppose the call includes "service_name" and "method_name"
#     if call["name"].startswith("functions."):
#         call["name"] = call["name"][len("functions.") :]

#     method_name = call["name"]

#     # Find the corresponding request type
#     request_types = get_request_types_for_method(tools_json_path, method_name)  # e.g. "GetBillingAccountRequest"

#     print(f"Found request type for {method_name}: {request_types}")
#     print(request_types[0])
#     output = asyncio.run(dynamic_executor(
#         request_types[0],
#         method_name,
#         call["arguments"]
#     ))
#     print(output)
#     results = asyncio.run(collect_pager_results(output))

async def tool_call_with_feedback_loop(query, max_attempts=6):
    """
    Execute tool calls with OpenAI feedback loop for error correction.
    Sends errors back to OpenAI to get corrected tool calls until successful or max attempts reached.
    """
    attempt = 0
    previous_errors = []
    
    while attempt < max_attempts:
        try:
            # Build the conversation with error context if any
            messages = [
                {
                    "role": "system",
                    "content": [{"type": "input_text", "text": content}]
                },
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": query}]
                }
            ]
            
            # If we have previous errors, use the error handling agent to create a new prompt
            if previous_errors:
                new_prompt = create_error_handled_prompt(query, previous_errors)
                messages = [
                    {
                        "role": "system",
                        "content": [{"type": "input_text", "text": new_prompt}]
                    }
                ]
                print(new_prompt)


            # Get new tool calls from OpenAI
            response = client.responses.parse(
                model="gpt-4o",
                input=messages,
                tools=formatted_tools
            )
            print(response.output)
            
            # Parse the tool calls
            tools = ToolCalls.model_validate_json(response.output_text)
            current_errors = []

            # Execute each tool call
            for call in tools.tool_calls:
                if call["name"].startswith("functions."):
                    call["name"] = call["name"][len("functions."):]

                method_name = call["name"]
                request_types = get_request_types_for_method(tools_json_path, method_name)
                if not request_types:
                    current_errors.append({
                        "method": method_name,
                        "error": "No request type found for this method",
                        "output": call,
                    })
                    continue

                success, result = await dynamic_executor(
                    request_types[0],
                    method_name,
                    call["arguments"]
                )
                print(success, result)

                if not success:
                    # Add the error to our list with full context
                    current_errors.append({
                        "method": method_name,
                        "error": str(result),  # This now includes the HTTP status code if applicable
                        "arguments": call["arguments"]
                    })
                else:
                    print(f"Successfully executed {method_name}")
                    if hasattr(result, "__aiter__"):
                        results = await collect_pager_results(result)
                        print("Results:", results)
                    else:
                        print("Result:", result)

            # If no errors, we're done!
            if not current_errors:
                print("All operations completed successfully!")
                return

            # If we had errors, save them for the next iteration
            previous_errors = current_errors
            attempt += 1
            print(f"\nAttempt {attempt} failed with errors:")
            for error in current_errors:
                print(f"Method: {error['method']}")
                print(f"Error: {error['error']}")
                print(f"Arguments used: {json.dumps(error['arguments'], indent=2)}\n")
            print("Retrying with corrections...")

        except Exception as e:
            print(f"Unexpected error during attempt {attempt}: {e}")
            attempt += 1

    print(f"Failed after {max_attempts} attempts. Last errors:")
    print(json.dumps(previous_errors, indent=2))

# Usage
query = "Can you create a serverless vpc access connector in the project vidhra us-central1 with name 'test-vpc-access-connector' and ip address '10.8.0.0/28' in default network?"
asyncio.run(tool_call_with_feedback_loop(query))



