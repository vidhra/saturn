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
query = "can you update the billing info of the project vidhra to vidhra-ai"



client = OpenAI(
    api_key=api_key,  # This is the default and can be omitted
)

openai_format_tools = [    {
        "type": "function",
        
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
                "description": "Required. The resource name of the billing account to retrieve. For example, ``billingAccounts/012345-567890-ABCDEF``.  This corresponds to the ``name`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.cloud.billing_v1.types.BillingAccount: A billing account in the [Google Cloud Console](\\ https://console.cloud.google.com/). You can assign a billing account to one or more projects."
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
          },
          "request_types": [
            "GetBillingAccountRequest"
          ]
        
      },
      {
        "type": "function",
       
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
                "description": "Optional. The parent resource to list billing accounts from. Format:  -  ``organizations/{organization_id}``, for example, ``organizations/12345678`` -  ``billingAccounts/{billing_account_id}``, for example, ``billingAccounts/012345-567890-ABCDEF``  This corresponds to the ``parent`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsAsyncPager: Response message for ListBillingAccounts.  Iterating over this object will yield results and resolve additional pages automatically."
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
          },
          "request_types": [
            "ListBillingAccountsRequest"
          ]
        
      },
      {
        "type": "function",
       
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
                "description": "Required. The name of the billing account resource to be updated.  This corresponds to the ``name`` field on the ``request`` instance; if ``request`` is provided, this should not be set."
              },
              "account": {
                "type": "string",
                "description": "Required. The billing account resource to replace the resource on the server.  This corresponds to the ``account`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.cloud.billing_v1.types.BillingAccount: A billing account in the [Google Cloud Console](\\ https://console.cloud.google.com/). You can assign a billing account to one or more projects."
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
          },
          "request_types": [
            "UpdateBillingAccountRequest"
          ]
        
      },
      {
        "type": "function",
        
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
                "description": "Required. The billing account resource to create. Currently CreateBillingAccount only supports subaccount creation, so any created billing accounts must be under a provided parent billing account.  This corresponds to the ``billing_account`` field on the ``request`` instance; if ``request`` is provided, this should not be set."
              },
              "parent": {
                "type": "string",
                "description": "Optional. The parent to create a billing account from. Format:  -  ``billingAccounts/{billing_account_id}``, for example, ``billingAccounts/012345-567890-ABCDEF``  This corresponds to the ``parent`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.cloud.billing_v1.types.BillingAccount: A billing account in the [Google Cloud Console](\\ https://console.cloud.google.com/). You can assign a billing account to one or more projects."
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
          },
          "request_types": [
            "CreateBillingAccountRequest"
          ]
        
      },
      {
        "type": "function",
       
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
                "description": "Required. The resource name of the billing account associated with the projects that you want to list. For example, ``billingAccounts/012345-567890-ABCDEF``.  This corresponds to the ``name`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoAsyncPager: Request message for ListProjectBillingInfoResponse.  Iterating over this object will yield results and resolve additional pages automatically."
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
          },
          "request_types": [
            "ListProjectBillingInfoRequest"
          ]
        
      },
      {
        "type": "function",
        
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
                "description": "Required. The resource name of the project for which billing information is retrieved. For example, ``projects/tokyo-rain-123``.  This corresponds to the ``name`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.cloud.billing_v1.types.ProjectBillingInfo: Encapsulation of billing information for a Google Cloud Console project. A project has at most one associated billing account at a time (but a billing account can be assigned to multiple projects)."
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
          },
          "request_types": [
            "GetProjectBillingInfoRequest"
          ]
        
      },
      {
        "type": "function",
        
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
                "description": "Required. The resource name of the project associated with the billing information that you want to update. For example, ``projects/tokyo-rain-123``.  This corresponds to the ``name`` field on the ``request`` instance; if ``request`` is provided, this should not be set."
              },
              "project_billing_info": {
                "type": "string",
                "description": "The new billing information for the project. Output-only fields are ignored; thus, you can leave empty all fields except ``billing_account_name``.  This corresponds to the ``project_billing_info`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.cloud.billing_v1.types.ProjectBillingInfo: Encapsulation of billing information for a Google Cloud Console project. A project has at most one associated billing account at a time (but a billing account can be assigned to multiple projects)."
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
          },
          "request_types": [
            "UpdateProjectBillingInfoRequest"
          ]
        
      },
      {
        "type": "function",
        
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
                "description": "REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  This corresponds to the ``resource`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.iam.v1.policy_pb2.Policy: An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources.  A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role.  For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](\\ https://cloud.google.com/iam/help/conditions/resource-policies).  **JSON example:**  :literal:`\\`     {       \"bindings\": [         {           \"role\": \"roles/resourcemanager.organizationAdmin\",           \"members\": [             \"user:mike@example.com\",             \"group:admins@example.com\",             \"domain:google.com\",             \"serviceAccount:my-project-id@appspot.gserviceaccount.com\"           ]         },         {           \"role\": \"roles/resourcemanager.organizationViewer\",           \"members\": [             \"user:eve@example.com\"           ],           \"condition\": {             \"title\": \"expirable access\",             \"description\": \"Does not grant access after Sep 2020\",             \"expression\": \"request.time <             timestamp('2020-10-01T00:00:00.000Z')\",           }         }       ],       \"etag\": \"BwWWja0YfJA=\",       \"version\": 3     }`\\ \\`  **YAML example:**  :literal:`\\`     bindings:     - members:       - user:mike@example.com       - group:admins@example.com       - domain:google.com       - serviceAccount:my-project-id@appspot.gserviceaccount.com       role: roles/resourcemanager.organizationAdmin     - members:       - user:eve@example.com       role: roles/resourcemanager.organizationViewer       condition:         title: expirable access         description: Does not grant access after Sep 2020         expression: request.time < timestamp('2020-10-01T00:00:00.000Z')     etag: BwWWja0YfJA=     version: 3`\\ \\`  For a description of IAM and its features, see the [IAM documentation](\\ https://cloud.google.com/iam/docs/)."
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
          },
          "request_types": [
            "GetIamPolicyRequest"
          ]
        
      },
      {
        "type": "function",
        
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
                "description": "REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  This corresponds to the ``resource`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.iam.v1.policy_pb2.Policy: An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources.  A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role.  For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](\\ https://cloud.google.com/iam/help/conditions/resource-policies).  **JSON example:**  :literal:`\\`     {       \"bindings\": [         {           \"role\": \"roles/resourcemanager.organizationAdmin\",           \"members\": [             \"user:mike@example.com\",             \"group:admins@example.com\",             \"domain:google.com\",             \"serviceAccount:my-project-id@appspot.gserviceaccount.com\"           ]         },         {           \"role\": \"roles/resourcemanager.organizationViewer\",           \"members\": [             \"user:eve@example.com\"           ],           \"condition\": {             \"title\": \"expirable access\",             \"description\": \"Does not grant access after Sep 2020\",             \"expression\": \"request.time <             timestamp('2020-10-01T00:00:00.000Z')\",           }         }       ],       \"etag\": \"BwWWja0YfJA=\",       \"version\": 3     }`\\ \\`  **YAML example:**  :literal:`\\`     bindings:     - members:       - user:mike@example.com       - group:admins@example.com       - domain:google.com       - serviceAccount:my-project-id@appspot.gserviceaccount.com       role: roles/resourcemanager.organizationAdmin     - members:       - user:eve@example.com       role: roles/resourcemanager.organizationViewer       condition:         title: expirable access         description: Does not grant access after Sep 2020         expression: request.time < timestamp('2020-10-01T00:00:00.000Z')     etag: BwWWja0YfJA=     version: 3`\\ \\`  For a description of IAM and its features, see the [IAM documentation](\\ https://cloud.google.com/iam/docs/)."
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
          },
          "request_types": [
            "SetIamPolicyRequest"
          ]
        
      },
      {
        "type": "function",
        
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
                "description": "REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  This corresponds to the ``resource`` field on the ``request`` instance; if ``request`` is provided, this should not be set."
              },
              "permissions": {
                "type": "string",
                "description": "The set of permissions to check for the ``resource``. Permissions with wildcards (such as '*' or 'storage.*') are not allowed. For more information see `IAM Overview <https://cloud.google.com/iam/docs/overview#permissions>`__.  This corresponds to the ``permissions`` field on the ``request`` instance; if ``request`` is provided, this should not be set. retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any, should be retried. timeout (float): The timeout for this request. metadata (Sequence[Tuple[str, str]]): Strings which should be sent along with the request as metadata.  Returns: google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse: Response message for TestIamPermissions method."
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
          },
          "request_types": [
            "TestIamPermissionsRequest"
          ]
        
      },
      {
        "type": "function",
        
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
          },
          "request_types": [
            "MoveBillingAccountRequest"
          ]
        
      }
      ]
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


