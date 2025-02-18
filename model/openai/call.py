import json
from openai import ChatCompletion
from openai import OpenAI
# Set your OpenAI API key
api_key = "sk-proj-MJmVD8pfcaf7GesMW4gOT3BlbkFJNUioNOsSm7kMom161U9D"

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
{ "tool_calls": [ {"name": "func_name1", "arguments": {"argument1": "value1", "argument2": "value2"}}, ... (more tool calls as required) ] }
""".strip()

# Define the user query
query = "can you get the billing account for the project vidhra.com and list all the projects associated with it and update the billing account to a budget of 10000"


client = OpenAI(
    api_key=api_key,  # This is the default and can be omitted
)

openai_format_tools = [
  {
    "type": "function",
    "function": {
      "name": "get_billing_account",
      "description": "Gets information about a billing account. The current\nauthenticated user must be a `viewer of the billing\naccount <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_get_billing_account():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.GetBillingAccountRequest(\n            name=\"name_value\",\n        )\n\n        # Make the request\n        response = await client.get_billing_account(request=request)\n\n    ",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "name": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "name",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "list_billing_accounts",
      "description": "Lists the billing accounts that the current authenticated user\nhas permission to\n`view <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_list_billing_accounts():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.ListBillingAccountsRequest(\n        )\n\n        # Make the request\n        page_result = client.list_billing_accounts(request=request)\n\n        # Handle the response\n        async for response in",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "parent": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "parent",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "update_billing_account",
      "description": "Updates a billing account's fields. Currently the only field\nthat can be edited is ``display_name``. The current\nauthenticated user must have the ``billing.accounts.update`` IAM\npermission, which is typically given to the\n`administrator <https://cloud.google.com/billing/docs/how-to/billing-access>`__\nof the billing account.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_update_billing_account():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.UpdateBillingAccount",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "name": {
            "type": "string",
            "description": ""
          },
          "account": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "name",
          "account",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "create_billing_account",
      "description": "This method creates `billing\nsubaccounts <https://cloud.google.com/billing/docs/concepts#subaccounts>`__.\n\nGoogle Cloud resellers should use the Channel Services APIs,\n`accounts.customers.create <https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/create>`__\nand\n`accounts.customers.entitlements.create <https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/create>`__.\n\nWhen creating a subaccount, the current authenticated user must\nhave the ``billing.accounts.update`` IAM permission on the\nparent account, which is typically given to billing account\n`administrators <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\nThis method will return an error if the parent account has not\nbeen provisioned for subaccounts.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "billing_account": {
            "type": "string",
            "description": ""
          },
          "parent": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "billing_account",
          "parent",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "list_project_billing_info",
      "description": "Lists the projects associated with a billing account. The\ncurrent authenticated user must have the\n``billing.resourceAssociations.list`` IAM permission, which is\noften given to billing account\n`viewers <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_list_project_billing_info():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.ListProjectBillingInfoRequest(\n            name=\"name_value\",\n        )\n\n  ",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "name": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "name",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_project_billing_info",
      "description": "Gets the billing information for a project. The current\nauthenticated user must have the\n``resourcemanager.projects.get`` permission for the project,\nwhich can be granted by assigning the `Project\nViewer <https://cloud.google.com/iam/docs/understanding-roles#predefined_roles>`__\nrole.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_get_project_billing_info():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.GetProjectBillingInfoRequest(\n            name=\"name_value",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "name": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "name",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "update_project_billing_info",
      "description": "Sets or updates the billing account associated with a project.\nYou specify the new billing account by setting the\n``billing_account_name`` in the ``ProjectBillingInfo`` resource\nto the resource name of a billing account. Associating a project\nwith an open billing account enables billing on the project and\nallows charges for resource usage. If the project already had a\nbilling account, this method changes the billing account used\nfor resource usage charges.\n\n*Note:* Incurred charges that have not yet been reported in the\ntransaction history of the Google Cloud Console might be billed\nto the new billing account, even if the charge occurred before\nthe new billing account was assigned to the project.\n\nThe current authenticated user must have ownership privileges\nfor both the\n`project <https://cloud.google.com/docs/permissions-overview#h.bgs0oxofvnoo>`__\nand the `billing\naccount <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\nYou can disable billing on the project by setting the\n``billing_accoun",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "name": {
            "type": "string",
            "description": ""
          },
          "project_billing_info": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "name",
          "project_billing_info",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_iam_policy",
      "description": "Gets the access control policy for a billing account. The caller\nmust have the ``billing.accounts.getIamPolicy`` permission on\nthe account, which is often given to billing account\n`viewers <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n    from google.iam.v1 import iam_policy_pb2  # type: ignore\n\n    async def sample_get_iam_policy():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = iam_policy_pb2.GetIamPolicyRequest(\n            r",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "resource": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "resource",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "set_iam_policy",
      "description": "Sets the access control policy for a billing account. Replaces\nany existing policy. The caller must have the\n``billing.accounts.setIamPolicy`` permission on the account,\nwhich is often given to billing account\n`administrators <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n    from google.iam.v1 import iam_policy_pb2  # type: ignore\n\n    async def sample_set_iam_policy():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = iam_policy_p",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "resource": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "resource",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "test_iam_permissions",
      "description": "Tests the access control policy for a billing\naccount. This method takes the resource and a set of\npermissions as input and returns the subset of the input\npermissions that the caller is allowed for that\nresource.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n    from google.iam.v1 import iam_policy_pb2  # type: ignore\n\n    async def sample_test_iam_permissions():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = iam_policy_pb2.TestIamPermissionsRequest(\n            resource=\"resource_value\",\n   ",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "resource": {
            "type": "string",
            "description": ""
          },
          "permissions": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "resource",
          "permissions",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "move_billing_account",
      "description": "Changes which parent organization a billing account\nbelongs to.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_move_billing_account():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.MoveBillingAccountRequest(\n            name=\"name_value\",\n            destination_parent=\"destination_parent_value\",\n        )\n\n        # Make the request\n        response = await client.move_billing_account(request=request)\n\n        # Handle the response\n        print(response)\n\nArg",
      "parameters": {
        "type": "object",
        "properties": {
          "request": {
            "type": "string",
            "description": ""
          },
          "retry": {
            "type": "string",
            "description": ""
          },
          "timeout": {
            "type": "string",
            "description": ""
          },
          "metadata": {
            "type": "string",
            "description": ""
          }
        },
        "required": [
          "request",
          "retry",
          "timeout",
          "metadata"
        ]
      }
    }
  }
]


# Helper function to build the prompt
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": query
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "billingAccounts/0123456"
        }
      ]
    },
  ],
  tools=openai_format_tools,
  max_completion_tokens=5000
)
# Call the API to get the response


# Print the response content
print(response.choices[0].message.tool_calls)
