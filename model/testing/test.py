import json
from openai import OpenAI
import asyncio
import importlib
import os
from google.cloud import vpcaccess_v1
from google.protobuf import field_mask_pb2
from flask import Flask, request, jsonify
from flask_cors import CORS
from google.api_core.operations_v1 import OperationsAsyncClient

# Create Flask app
app = Flask(__name__)
CORS(app)

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
If no value is provided for a parameter, please assgin minimum value for that parameter.
{ "tool_calls": [ {"name": "func_name1", "arguments": {"argument1": "value1", "argument2": "value2"}}, ... (more tool calls as required) ] }
""".strip()

# OpenAI client
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

            # Build your final tool definition with the correct OpenAI format
            openai_tools.append({
                "type": "function",
                "name": method["function"]["name"],
                "description": type_info["description"],
                "parameters": parameters_copy,
            })
    return openai_tools

async def async_op_to_dict(op: OperationsAsyncClient):
    """
    Convert a google.api_core.operation_async.AsyncOperation to a dictionary.
    You can either gather the in-progress fields or wait for the final result.
    """
    # 1) If you want the in-progress fields only:
    op_dict = {
        "name": op.operation.name,    # The operation name
        "done": op.done(),            # Boolean: have we finished yet?
        "metadata": str(op.metadata), # The operation's metadata
    }

    # 2) If you actually want the completed object, wait for it to finish:
    # This will block until the operation is done, so be sure it's what you want.
    result = await op.result()

    # result itself may be a protobuf message or another complex obj
    if hasattr(result, "__dict__"):
        # Convert it to a JSON-serializable dict
        result_dict = {k: str(v) for k, v in result.__dict__.items()}
    else:
        # If all else fails, just do string or custom logic
        result_dict = str(result)

    # Return both the in-progress info and the completed result
    return {
        "operation_info": op_dict,
        "final_result": result_dict
    }

def build_prompt_system(task_instruction: str, format_instruction: str):
    prompt = f"[BEGIN OF TASK INSTRUCTION]\n{task_instruction}\n[END OF TASK INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF FORMAT INSTRUCTION]\n{format_instruction}\n[END OF FORMAT INSTRUCTION]\n\n"
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
    Dynamically call a method from the VpcAccessServiceAsyncClient.
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
        return result

    except AttributeError as e:
        print(f"Failed to find attribute: {e}")
        return {"error": f"Failed to find attribute: {str(e)}"}
    except Exception as e:
        print(f"Failed to execute request: {e}")
        return {"error": f"Failed to execute request: {str(e)}"}

def get_request_types_for_method(tools_json_path: str, method_name: str) -> list:
    """
    Returns a list of request types for the given method name.
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
    
    return sorted(all_request_types)

async def collect_pager_results(pager):
    results = []
    async for item in pager:
        results.append(item)
    return results

async def process_query(query):
    """Process query and return results"""
    # Build OpenAI tools
    tools_json_path = "vpcaccess_v1/tools.json"
    types_json_path = "vpcaccess_v1/types.json"
    openai_format_tools = build_openai_tools(tools_json_path, types_json_path)
    print(query)
    # Build prompt
    content = build_prompt_system(task_instruction, format_instruction)
    
    # Make OpenAI API call
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
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "output_text",
                        "text":  "Failed to execute request: 400 The minimum amount of instances underlying the connector must be at least 2 and The specified minimum instances value must be less than the specified maximum instances value."
                    }
                ]
               
            }
        ],
        text={
            "format": {
                "type": "text"
            }
        },
        tools=openai_format_tools,
        temperature=1,
        max_output_tokens=2048,
        top_p=1,
        store=True
    )
    
    # Process the response
    print(response.output_text)
    output_text = response.output_text
    result = {"openai_response": output_text}
    
    try:
        tools = json.loads(output_text)
        tool_results = []
        
        for call in tools.get("tool_calls", []):
            # Clean up function name if needed
            if call["name"].startswith("functions."):
                call["name"] = call["name"][len("functions."):]

            method_name = call["name"]

            # Find the corresponding request type
            request_types = get_request_types_for_method(tools_json_path, method_name)
            
            if not request_types:
                tool_results.append({
                    "method": method_name,
                    "error": "No request type found for this method"
                })
                continue
                
            # Execute the tool call
            output = await dynamic_executor(
                request_types[0],
                method_name,
                call["arguments"]
            )
            print(output)
            
            # Convert the output to a serializable format
            if hasattr(output, "__dict__"):
                output_dict = {k: str(v) for k, v in output.__dict__.items()}
            else:
                output_dict = str(output)
                
            tool_results.append({
                "method": method_name,
                "request_type": request_types[0],
                "result": output_dict
            })

            
        result["tool_results"] = tool_results
    except Exception as e:
        result["error"] = f"Error processing tool calls: {str(e)}"
    
    return result

@app.route('/process', methods=['GET'])
def process():
    """Endpoint to process a query"""
    query = request.args.get('query', '')
    
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    # Run the async processing function
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(process_query(query))
    loop.close()
    
    return jsonify(result)

@app.route("/poll_status", methods=["GET"])
def poll_status():
    """Periodically check the status of an async operation."""
    op_name = request.args.get("op_name", "")
    if not op_name:
        return jsonify({"error": "No operation name provided"}), 400

    # We'll create a short event loop for asynchronous calls:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        response = loop.run_until_complete(check_operation_status(op_name))
    finally:
        loop.close()

    return jsonify(response)

async def check_operation_status(operation_name: str):
    # 1) Create the main client
    function_client = vpcaccess_v1.VpcAccessServiceAsyncClient()

    # 2) Get the gRPC channel from that client's transport
    channel = function_client.transport.grpc_channel

    # 3) Instantiate OperationsAsyncClient with that channel
    ops_client = OperationsAsyncClient(channel=channel)

    # 4) Now you can call get_operation on ops_client
    op = await ops_client.get_operation(name=operation_name)

    # e.g., check if it's done
    is_done = op.done
    metadata = str(op.metadata)

    return {
        "operation_name": operation_name,
        "done": is_done,
        "metadata": metadata
    }

if __name__ == '__main__':
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    app.run(host='0.0.0.0', port=5600, debug=True)
