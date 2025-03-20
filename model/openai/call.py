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

openai_format_tools = [{
      "type": "function",
      "name": "GetBillingAccountRequest",
      "description": "Request message for ``GetBillingAccount``.\n\nAttributes:\n    name (str):\n        Required. The resource name of the billing account to\n        retrieve. For example,\n        ``billingAccounts/012345-567890-ABCDEF``.",
      "parameters": {
        "type": "object",
        "properties": {
          "name": {
            "description": "Required. The resource name of the billing account to retrieve. For example, ``billingAccounts/012345-567890-ABCDEF``.",
            "type": "string"
          }
        },
        "required": [
          "name"
        ]
      }
    },
    {
      "type": "function",
      "name": "ListBillingAccountsRequest",
      "description": "Request message for ``ListBillingAccounts``.\n\nAttributes:\n    page_size (int):\n        Requested page size. The maximum page size is\n        100; this is also the default.\n    page_token (str):\n        A token identifying a page of results to return. This should\n        be a ``next_page_token`` value returned from a previous\n        ``ListBillingAccounts`` call. If unspecified, the first page\n        of results is returned.\n    filter (str):\n        Options for how to filter the returned billing accounts.\n        This only supports filtering for\n        `subaccounts <https://cloud.google.com/billing/docs/concepts>`__\n        under a single provided parent billing account. (for\n        example,\n        ``master_billing_account=billingAccounts/012345-678901-ABCDEF``).\n        Boolean algebra and other fields are not currently\n        supported.\n    parent (str):\n        Optional. The parent resource to list billing accounts from.\n        Format:\n\n        -  ``organizations/{organization_id}``, for example,\n    ",
      "parameters": {
        "type": "object",
        "properties": {
          "page_size": {
            "description": "Requested page size. The maximum page size is 100; this is also the default.",
            "type": "integer"
          },
          "page_token": {
            "description": "A token identifying a page of results to return. This should be a ``next_page_token`` value returned from a previous ``ListBillingAccounts`` call. If unspecified, the first page of results is returned.",
            "type": "string"
          },
          "filter": {
            "description": "Options for how to filter the returned billing accounts. This only supports filtering for `subaccounts <https://cloud.google.com/billing/docs/concepts>`__ under a single provided parent billing account. (for example, ``master_billing_account=billingAccounts/012345-678901-ABCDEF``). Boolean algebra and other fields are not currently supported.",
            "type": "string"
          },
          "parent": {
            "description": "Optional. The parent resource to list billing accounts from. Format:  -  ``organizations/{organization_id}``, for example, ``organizations/12345678`` -  ``billingAccounts/{billing_account_id}``, for example, ``billingAccounts/012345-567890-ABCDEF``",
            "type": "string"
          }
        }
      }
    },
    {
      "type": "function",
      "name": "CreateBillingAccountRequest",
      "description": "Request message for ``CreateBillingAccount``.\n\nAttributes:\n    billing_account (google.cloud.billing_v1.types.BillingAccount):\n        Required. The billing account resource to\n        create. Currently CreateBillingAccount only\n        supports subaccount creation, so any created\n        billing accounts must be under a provided parent\n        billing account.\n    parent (str):\n        Optional. The parent to create a billing account from.\n        Format:\n\n        -  ``billingAccounts/{billing_account_id}``, for example,\n           ``billingAccounts/012345-567890-ABCDEF``",
      "parameters": {
        "type": "object",
        "properties": {
          "billing_account": {
            "description": "Required. The billing account resource to create. Currently CreateBillingAccount only supports subaccount creation, so any created billing accounts must be under a provided parent billing account.",
            "type": "object",
            "properties": {
              "name": {
                "description": "Output only. Resource name of the billing account. Format: accounts/{account_id}/billingAccounts/{billing_account_id}.",
                "type": "string"
              },
              "display_name": {
                "description": "Display name of the billing account.",
                "type": "string"
              },
              "create_time": {
                "description": "Output only. The time when this billing account was created.",
                "type": "string",
                "reference": "google.protobuf.timestamp_pb2.Timestamp"
              },
              "currency_code": {
                "description": "Output only. The 3-letter currency code defined in ISO 4217.",
                "type": "string"
              },
              "region_code": {
                "description": "Output only. The CLDR region code.",
                "type": "string"
              }
            }
          },
          "parent": {
            "description": "Optional. The parent to create a billing account from. Format:  -  ``billingAccounts/{billing_account_id}``, for example, ``billingAccounts/012345-567890-ABCDEF``",
            "type": "string"
          }
        },
        "required": [
          "billing_account"
        ]
      }
    },
    {
      "type": "function",
      "name": "UpdateBillingAccountRequest",
      "description": "Request message for ``UpdateBillingAccount``.\n\nAttributes:\n    name (str):\n        Required. The name of the billing account\n        resource to be updated.\n    account (google.cloud.billing_v1.types.BillingAccount):\n        Required. The billing account resource to\n        replace the resource on the server.\n    update_mask (google.protobuf.field_mask_pb2.FieldMask):\n        The update mask applied to the resource. Only \"display_name\"\n        is currently supported.",
      "parameters": {
        "type": "object",
        "properties": {
          "name": {
            "description": "Required. The name of the billing account resource to be updated.",
            "type": "string"
          },
          "account": {
            "description": "Required. The billing account resource to replace the resource on the server.",
            "type": "object",
            "properties": {
              "name": {
                "description": "Output only. Resource name of the billing account. Format: accounts/{account_id}/billingAccounts/{billing_account_id}.",
                "type": "string"
              },
              "display_name": {
                "description": "Display name of the billing account.",
                "type": "string"
              },
              "create_time": {
                "description": "Output only. The time when this billing account was created.",
                "type": "object",
                "reference": "google.protobuf.timestamp_pb2.Timestamp"
              },
              "currency_code": {
                "description": "Output only. The 3-letter currency code defined in ISO 4217.",
                "type": "string"
              },
              "region_code": {
                "description": "Output only. The CLDR region code.",
                "type": "string"
              }
            }
          },
          "update_mask": {
            "description": "The update mask applied to the resource. Only \"display_name\" is currently supported.",
            "type": "string",
            "reference": "google.protobuf.field_mask_pb2.FieldMask"
          }
        },
        "required": [
          "name",
          "account"
        ]
      }
    },
    {
      "type": "function",
      "name": "ListProjectBillingInfoRequest",
      "description": "Request message for ``ListProjectBillingInfo``.\n\nAttributes:\n    name (str):\n        Required. The resource name of the billing account\n        associated with the projects that you want to list. For\n        example, ``billingAccounts/012345-567890-ABCDEF``.\n    page_size (int):\n        Requested page size. The maximum page size is\n        100; this is also the default.\n    page_token (str):\n        A token identifying a page of results to be returned. This\n        should be a ``next_page_token`` value returned from a\n        previous ``ListProjectBillingInfo`` call. If unspecified,\n        the first page of results is returned.",
      "parameters": {
        "type": "object",
        "properties": {
          "name": {
            "description": "Required. The resource name of the billing account associated with the projects that you want to list. For example, ``billingAccounts/012345-567890-ABCDEF``.",
            "type": "string"
          },
          "page_size": {
            "description": "Requested page size. The maximum page size is 100; this is also the default.",
            "type": "integer"
          },
          "page_token": {
            "description": "A token identifying a page of results to be returned. This should be a ``next_page_token`` value returned from a previous ``ListProjectBillingInfo`` call. If unspecified, the first page of results is returned.",
            "type": "string"
          }
        },
        "required": [
          "name"
        ]
      }
    },
    {
      "type": "function",
      "name": "GetProjectBillingInfoRequest",
      "description": "Request message for ``GetProjectBillingInfo``.\n\nAttributes:\n    name (str):\n        Required. The resource name of the project for which billing\n        information is retrieved. For example,\n        ``projects/tokyo-rain-123``.",
      "parameters": {
        "type": "object",
        "properties": {
          "name": {
            "description": "Required. The resource name of the project for which billing information is retrieved. For example, ``projects/tokyo-rain-123``.",
            "type": "string"
          }
        },
        "required": [
          "name"
        ]
      }
    },
    {
      "type": "function",
      "name": "UpdateProjectBillingInfoRequest",
      "description": "Request message for ``UpdateProjectBillingInfo``.\n\nAttributes:\n    name (str):\n        Required. The resource name of the project associated with\n        the billing information that you want to update. For\n        example, ``projects/tokyo-rain-123``.\n    project_billing_info (google.cloud.billing_v1.types.ProjectBillingInfo):\n        The new billing information for the project. Output-only\n        fields are ignored; thus, you can leave empty all fields\n        except ``billing_account_name``.",
      "parameters": {
        "type": "object",
        "properties": {
          "name": {
            "description": "Required. The resource name of the project associated with the billing information that you want to update. For example, ``projects/tokyo-rain-123``.",
            "type": "string"
          },
          "project_billing_info": {
            "description": "The new billing information for the project. Output-only fields are ignored; thus, you can leave empty all fields except ``billing_account_name``.",
            "type": "object",
            "properties": {
              "name": {
                "description": "Output only. The resource name for the ``ProjectBillingInfo``; has the form ``projects/{project_id}/billingInfo``. For example, the resource name for the billing information for project ``tokyo-rain-123`` would be ``projects/tokyo-rain-123/billingInfo``.",
                "type": "string"
              },
              "project_id": {
                "description": "Output only. The ID of the project that this ``ProjectBillingInfo`` represents, such as ``tokyo-rain-123``. This is a convenience field so that you don't need to parse the ``name`` field to obtain a project ID.",
                "type": "string"
              },
              "billing_account_name": {
                "description": "The resource name of the billing account associated with the project, if any. For example, ``billingAccounts/012345-567890-ABCDEF``.",
                "type": "string"
              },
              "billing_enabled": {
                "description": "Output only. True if the project is associated with an open billing account, to which usage on the project is charged. False if the project is associated with a closed billing account, or no billing account at all, and therefore cannot use paid services.",
                "type": "boolean"
              }
            }
          }
        },
        "required": [
          "name"
        ]
      }
    },
    {
      "type": "function",
      "name": "MoveBillingAccountRequest",
      "description": "Request message for ``MoveBillingAccount`` RPC.\n\nAttributes:\n    name (str):\n        Required. The resource name of the billing account to move.\n        Must be of the form\n        ``billingAccounts/{billing_account_id}``. The specified\n        billing account cannot be a subaccount, since a subaccount\n        always belongs to the same organization as its parent\n        account.\n    destination_parent (str):\n        Required. The resource name of the Organization to move the\n        billing account under. Must be of the form\n        ``organizations/{organization_id}``.",
      "parameters": {
        "type": "object",
        "properties": {
          "name": {
            "description": "Required. The resource name of the billing account to move. Must be of the form ``billingAccounts/{billing_account_id}``. The specified billing account cannot be a subaccount, since a subaccount always belongs to the same organization as its parent account.",
            "type": "string"
          },
          "destination_parent": {
            "description": "Required. The resource name of the Organization to move the billing account under. Must be of the form ``organizations/{organization_id}``.",
            "type": "string"
          }
        },
        "required": [
          "name",
          "destination_parent"
        ]
      }
    }]

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

async def dynamic_executor(class_name: str, method_name: str, args: dict):
    """
    Dynamically call a method from the CloudBillingAsyncClient by:
      1. Retrieving the request class using 'class_name' from billing_v1
      2. Retrieving the async method using 'method_name'
      3. Instantiating 'RequestClass' with parameter values from 'args'
         (Parsing JSON strings where appropriate)
      4. Invoking the async method.
    """
    try:
        RequestClass = getattr(billing_v1, class_name)

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
tools = json.loads(content)
for call in tools["tool_calls"]:
    print(call)
    args = extract_args(call["arguments"])
    print(args)
    asyncio.run(dynamic_executor(
        call["arguments"]["request"], 
        call["name"],
        args # Replace with your actual project ID
    ))


