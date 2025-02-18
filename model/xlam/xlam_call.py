import json
import torch 
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.random.manual_seed(0) 

model_name = "Salesforce/xLAM-1b-fc-r"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name) 

# Please use our provided instruction prompt for best performance
task_instruction = """
You are an expert in composing functions. You are given a question and a set of possible functions. 
Based on the question, you will need to make one or more function/tool calls to achieve the purpose. 
If none of the functions can be used, point it out and refuse to answer. 
If the given question lacks the parameters required by the function, also point it out.
""".strip()

format_instruction = """
The output MUST strictly adhere to the following JSON format, and NO other text MUST be included.
The example format is as follows. Please make sure the parameter type is correct. If no function call is needed, please make tool_calls an empty list '[]'.
```
{
    "tool_calls": [
    {"name": "func_name1", "arguments": {"argument1": "value1", "argument2": "value2"}},
    ... (more tool calls as required)
    ]
}
```
""".strip()

# Define the input query and available tools
query = "can you get the billing account for the project vidhra.com and list all the projects associated with it and update the billing account to a budget of 10000"



get_weather_api = {
    "name": "get_weather",
    "description": "Get the current weather for a location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, New York"
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "The unit of temperature to return"
            }
        },
        "required": ["location"]
    }
}

search_api = {
    "name": "search",
    "description": "Search for information on the internet",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query, e.g. 'latest news on AI'"
            }
        },
        "required": ["query"]
    }
}

openai_format_tools = [
  {
    "name": "get_billing_account",
    "description": "Gets information about a billing account. The current\nauthenticated user must be a `viewer of the billing\naccount <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_get_billing_account():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.GetBillingAccountRequest(\n            name=\"name_value\",\n        )\n\n        # Make the request\n        response = await client.get_billing_account(request=request)\n\n        # Handle the response\n        print(response)\n\nArgs:\n    request (Optional[Union[google.cloud.billing_v1.types.GetBillingAccountRequest, dict]]):\n        The request object. Request message for ``GetBillingAccount``.\n    name (:class:`str`):\n        Required. The resource name of the billing account to\n        retrieve. For example,\n        ``billingAccounts/012345-567890-ABCDEF``.\n\n        This corresponds to the ``name`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,\n        should be retried.\n    timeout (float): The timeout for this request.\n    metadata (Sequence[Tuple[str, str]]): Strings which should be\n        sent along with the request as metadata.\n\nReturns:\n    google.cloud.billing_v1.types.BillingAccount:\n        A billing account in the\n           [Google Cloud\n           Console](\\ https://console.cloud.google.com/). You\n           can assign a billing account to one or more projects.",
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
  },
  {
    "name": "list_billing_accounts",
    "description": "Lists the billing accounts that the current authenticated user\nhas permission to\n`view <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_list_billing_accounts():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.ListBillingAccountsRequest(\n        )\n\n        # Make the request\n        page_result = client.list_billing_accounts(request=request)\n\n        # Handle the response\n        async for response in page_result:\n            print(response)\n\nArgs:\n    request (Optional[Union[google.cloud.billing_v1.types.ListBillingAccountsRequest, dict]]):\n        The request object. Request message for ``ListBillingAccounts``.\n    parent (:class:`str`):\n        Optional. The parent resource to list billing accounts\n        from. Format:\n\n        -  ``organizations/{organization_id}``, for example,\n           ``organizations/12345678``\n        -  ``billingAccounts/{billing_account_id}``, for\n           example, ``billingAccounts/012345-567890-ABCDEF``\n\n        This corresponds to the ``parent`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,\n        should be retried.\n    timeout (float): The timeout for this request.\n    metadata (Sequence[Tuple[str, str]]): Strings which should be\n        sent along with the request as metadata.\n\nReturns:\n    google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsAsyncPager:\n        Response message for ListBillingAccounts.\n\n        Iterating over this object will yield results and\n        resolve additional pages automatically.",
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
  },
  {
    "name": "update_billing_account",
    "description": "Updates a billing account's fields. Currently the only field\nthat can be edited is ``display_name``. The current\nauthenticated user must have the ``billing.accounts.update`` IAM\npermission, which is typically given to the\n`administrator <https://cloud.google.com/billing/docs/how-to/billing-access>`__\nof the billing account.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_update_billing_account():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.UpdateBillingAccountRequest(\n            name=\"name_value\",\n        )\n\n        # Make the request\n        response = await client.update_billing_account(request=request)\n\n        # Handle the response\n        print(response)\n\nArgs:\n    request (Optional[Union[google.cloud.billing_v1.types.UpdateBillingAccountRequest, dict]]):\n        The request object. Request message for ``UpdateBillingAccount``.\n    name (:class:`str`):\n        Required. The name of the billing\n        account resource to be updated.\n\n        This corresponds to the ``name`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    account (:class:`google.cloud.billing_v1.types.BillingAccount`):\n        Required. The billing account\n        resource to replace the resource on the\n        server.\n\n        This corresponds to the ``account`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,\n        should be retried.\n    timeout (float): The timeout for this request.\n    metadata (Sequence[Tuple[str, str]]): Strings which should be\n        sent along with the request as metadata.\n\nReturns:\n    google.cloud.billing_v1.types.BillingAccount:\n        A billing account in the\n           [Google Cloud\n           Console](\\ https://console.cloud.google.com/). You\n           can assign a billing account to one or more projects.",
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
  },
  {
    "name": "create_billing_account",
    "description": "This method creates `billing\nsubaccounts <https://cloud.google.com/billing/docs/concepts#subaccounts>`__.\n\nGoogle Cloud resellers should use the Channel Services APIs,\n`accounts.customers.create <https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/create>`__\nand\n`accounts.customers.entitlements.create <https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/create>`__.\n\nWhen creating a subaccount, the current authenticated user must\nhave the ``billing.accounts.update`` IAM permission on the\nparent account, which is typically given to billing account\n`administrators <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\nThis method will return an error if the parent account has not\nbeen provisioned for subaccounts.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_create_billing_account():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.CreateBillingAccountRequest(\n        )\n\n        # Make the request\n        response = await client.create_billing_account(request=request)\n\n        # Handle the response\n        print(response)\n\nArgs:\n    request (Optional[Union[google.cloud.billing_v1.types.CreateBillingAccountRequest, dict]]):\n        The request object. Request message for ``CreateBillingAccount``.\n    billing_account (:class:`google.cloud.billing_v1.types.BillingAccount`):\n        Required. The billing account\n        resource to create. Currently\n        CreateBillingAccount only supports\n        subaccount creation, so any created\n        billing accounts must be under a\n        provided parent billing account.\n\n        This corresponds to the ``billing_account`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    parent (:class:`str`):\n        Optional. The parent to create a billing account from.\n        Format:\n\n        -  ``billingAccounts/{billing_account_id}``, for\n           example, ``billingAccounts/012345-567890-ABCDEF``\n\n        This corresponds to the ``parent`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,\n        should be retried.\n    timeout (float): The timeout for this request.\n    metadata (Sequence[Tuple[str, str]]): Strings which should be\n        sent along with the request as metadata.\n\nReturns:\n    google.cloud.billing_v1.types.BillingAccount:\n        A billing account in the\n           [Google Cloud\n           Console](\\ https://console.cloud.google.com/). You\n           can assign a billing account to one or more projects.",
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
  },
  {
    "name": "list_project_billing_info",
    "description": "Lists the projects associated with a billing account. The\ncurrent authenticated user must have the\n``billing.resourceAssociations.list`` IAM permission, which is\noften given to billing account\n`viewers <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_list_project_billing_info():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.ListProjectBillingInfoRequest(\n            name=\"name_value\",\n        )\n\n        # Make the request\n        page_result = client.list_project_billing_info(request=request)\n\n        # Handle the response\n        async for response in page_result:\n            print(response)\n\nArgs:\n    request (Optional[Union[google.cloud.billing_v1.types.ListProjectBillingInfoRequest, dict]]):\n        The request object. Request message for ``ListProjectBillingInfo``.\n    name (:class:`str`):\n        Required. The resource name of the billing account\n        associated with the projects that you want to list. For\n        example, ``billingAccounts/012345-567890-ABCDEF``.\n\n        This corresponds to the ``name`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,\n        should be retried.\n    timeout (float): The timeout for this request.\n    metadata (Sequence[Tuple[str, str]]): Strings which should be\n        sent along with the request as metadata.\n\nReturns:\n    google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoAsyncPager:\n        Request message for ListProjectBillingInfoResponse.\n\n        Iterating over this object will yield results and\n        resolve additional pages automatically.",
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
  },
  {
    "name": "get_project_billing_info",
    "description": "Gets the billing information for a project. The current\nauthenticated user must have the\n``resourcemanager.projects.get`` permission for the project,\nwhich can be granted by assigning the `Project\nViewer <https://cloud.google.com/iam/docs/understanding-roles#predefined_roles>`__\nrole.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_get_project_billing_info():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.GetProjectBillingInfoRequest(\n            name=\"name_value\",\n        )\n\n        # Make the request\n        response = await client.get_project_billing_info(request=request)\n\n        # Handle the response\n        print(response)\n\nArgs:\n    request (Optional[Union[google.cloud.billing_v1.types.GetProjectBillingInfoRequest, dict]]):\n        The request object. Request message for ``GetProjectBillingInfo``.\n    name (:class:`str`):\n        Required. The resource name of the project for which\n        billing information is retrieved. For example,\n        ``projects/tokyo-rain-123``.\n\n        This corresponds to the ``name`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,\n        should be retried.\n    timeout (float): The timeout for this request.\n    metadata (Sequence[Tuple[str, str]]): Strings which should be\n        sent along with the request as metadata.\n\nReturns:\n    google.cloud.billing_v1.types.ProjectBillingInfo:\n        Encapsulation of billing information\n        for a Google Cloud Console project. A\n        project has at most one associated\n        billing account at a time (but a billing\n        account can be assigned to multiple\n        projects).",
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
  },
  {
    "name": "update_project_billing_info",
    "description": "Sets or updates the billing account associated with a project.\nYou specify the new billing account by setting the\n``billing_account_name`` in the ``ProjectBillingInfo`` resource\nto the resource name of a billing account. Associating a project\nwith an open billing account enables billing on the project and\nallows charges for resource usage. If the project already had a\nbilling account, this method changes the billing account used\nfor resource usage charges.\n\n*Note:* Incurred charges that have not yet been reported in the\ntransaction history of the Google Cloud Console might be billed\nto the new billing account, even if the charge occurred before\nthe new billing account was assigned to the project.\n\nThe current authenticated user must have ownership privileges\nfor both the\n`project <https://cloud.google.com/docs/permissions-overview#h.bgs0oxofvnoo>`__\nand the `billing\naccount <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\nYou can disable billing on the project by setting the\n``billing_account_name`` field to empty. This action\ndisassociates the current billing account from the project. Any\nbillable activity of your in-use services will stop, and your\napplication could stop functioning as expected. Any unbilled\ncharges to date will be billed to the previously associated\naccount. The current authenticated user must be either an owner\nof the project or an owner of the billing account for the\nproject.\n\nNote that associating a project with a *closed* billing account\nwill have much the same effect as disabling billing on the\nproject: any paid resources used by the project will be shut\ndown. Thus, unless you wish to disable billing, you should\nalways call this method with the name of an *open* billing\naccount.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n\n    async def sample_update_project_billing_info():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = billing_v1.UpdateProjectBillingInfoRequest(\n            name=\"name_value\",\n        )\n\n        # Make the request\n        response = await client.update_project_billing_info(request=request)\n\n        # Handle the response\n        print(response)\n\nArgs:\n    request (Optional[Union[google.cloud.billing_v1.types.UpdateProjectBillingInfoRequest, dict]]):\n        The request object. Request message for ``UpdateProjectBillingInfo``.\n    name (:class:`str`):\n        Required. The resource name of the project associated\n        with the billing information that you want to update.\n        For example, ``projects/tokyo-rain-123``.\n\n        This corresponds to the ``name`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    project_billing_info (:class:`google.cloud.billing_v1.types.ProjectBillingInfo`):\n        The new billing information for the project. Output-only\n        fields are ignored; thus, you can leave empty all fields\n        except ``billing_account_name``.\n\n        This corresponds to the ``project_billing_info`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,\n        should be retried.\n    timeout (float): The timeout for this request.\n    metadata (Sequence[Tuple[str, str]]): Strings which should be\n        sent along with the request as metadata.\n\nReturns:\n    google.cloud.billing_v1.types.ProjectBillingInfo:\n        Encapsulation of billing information\n        for a Google Cloud Console project. A\n        project has at most one associated\n        billing account at a time (but a billing\n        account can be assigned to multiple\n        projects).",
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
  },
  {
    "name": "get_iam_policy",
    "description": "Gets the access control policy for a billing account. The caller\nmust have the ``billing.accounts.getIamPolicy`` permission on\nthe account, which is often given to billing account\n`viewers <https://cloud.google.com/billing/docs/how-to/billing-access>`__.\n\n.. code-block:: python\n\n    # This snippet has been automatically generated and should be regarded as a\n    # code template only.\n    # It will require modifications to work:\n    # - It may require correct/in-range values for request initialization.\n    # - It may require specifying regional endpoints when creating the service\n    #   client as shown in:\n    #   https://googleapis.dev/python/google-api-core/latest/client_options.html\n    from google.cloud import billing_v1\n    from google.iam.v1 import iam_policy_pb2  # type: ignore\n\n    async def sample_get_iam_policy():\n        # Create a client\n        client = billing_v1.CloudBillingAsyncClient()\n\n        # Initialize request argument(s)\n        request = iam_policy_pb2.GetIamPolicyRequest(\n            resource=\"resource_value\",\n        )\n\n        # Make the request\n        response = await client.get_iam_policy(request=request)\n\n        # Handle the response\n        print(response)\n\nArgs:\n    request (Optional[Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]]):\n        The request object. Request message for ``GetIamPolicy`` method.\n    resource (:class:`str`):\n        REQUIRED: The resource for which the\n        policy is being requested. See the\n        operation documentation for the\n        appropriate value for this field.\n\n        This corresponds to the ``resource`` field\n        on the ``request`` instance; if ``request`` is provided, this\n        should not be set.\n    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,\n        should be retried.\n    timeout (float): The timeout for this request.\n    metadata (Sequence[Tuple[str, str]]): Strings which should be\n        sent along with the request as metadata.\n\nReturns:\n    google.iam.v1.policy_pb2.Policy:\n        An Identity and Access Management (IAM) policy, which specifies access\n           controls for Google Cloud resources.\n\n           A Policy is a collection of bindings. A binding binds\n           one or more members, or principals, to a single role.\n           Principals can be user accounts, service accounts,\n           Google groups, and domains (such as G Suite). A role\n           is a named list of permissions; each role can be an\n           IAM predefined role or a user-created custom role.\n\n           For some types of Google Cloud resources, a binding\n           can also specify a condition, which is a logical\n           expression that allows access to a resource only if\n           the expression evaluates to true. A condition can add\n           constraints based on attributes of the request, the\n           resource, or both. To learn which resources support\n           conditions in their IAM policies, see the [IAM\n           documentation](\\ https://cloud.google.com/iam/help/conditions/resource-policies).\n\n           **JSON example:**\n\n           :literal:`\\`     {       \"bindings\": [         {           \"role\": \"roles/resourcemanager.organizationAdmin\",           \"members\": [             \"user:mike@example.com\",             \"group:admins@example.com\",             \"domain:google.com\",             \"serviceAccount:my-project-id@appspot.gserviceaccount.com\"           ]         },         {           \"role\": \"roles/resourcemanager.organizationViewer\",           \"members\": [             \"user:eve@example.com\"           ],           \"condition\": {             \"title\": \"expirable access\",             \"description\": \"Does not grant access after Sep 2020\",             \"expression\": \"request.time <             timestamp('2020-10-01T00:00:00.000Z')\",           }         }       ],       \"etag\": \"BwWWja0YfJA=\",       \"version\": 3     }`\\ \\`\n\n           **YAML example:**\n\n           :literal:`\\`     bindings:     - members:       - user:mike@example.com       - group:admins@example.com       - domain:google.com       - serviceAccount:my-project-id@appspot.gserviceaccount.com       role: roles/resourcemanager.organizationAdmin     - members:       - user:eve@example.com       role: roles/resourcemanager.organizationViewer       condition:         title: expirable access         description: Does not grant access after Sep 2020         expression: request.time < timestamp('2020-10-01T00:00:00.000Z')     etag: BwWWja0YfJA=     version: 3`\\ \\`\n\n           For a description of IAM and its features, see the\n           [IAM\n           documentation](\\ https://cloud.google.com/iam/docs/).",
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
 

]

# Helper function to convert openai format tools to our more concise xLAM format
def convert_to_xlam_tool(tools):
    ''''''
    if isinstance(tools, dict):
        return {
            "name": tools["name"],
            "description": tools["description"],
            "parameters": {k: v for k, v in tools["parameters"].get("properties", {}).items()}
        }
    elif isinstance(tools, list):
        return [convert_to_xlam_tool(tool) for tool in tools]
    else:
        return tools

# Helper function to build the input prompt for our model
def build_prompt(task_instruction: str, format_instruction: str, tools: list, query: str):
    prompt = f"[BEGIN OF TASK INSTRUCTION]\n{task_instruction}\n[END OF TASK INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF AVAILABLE TOOLS]\n{json.dumps(xlam_format_tools)}\n[END OF AVAILABLE TOOLS]\n\n"
    prompt += f"[BEGIN OF FORMAT INSTRUCTION]\n{format_instruction}\n[END OF FORMAT INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF QUERY]\n{query}\n[END OF QUERY]\n\n"
    return prompt
    
# Build the input and start the inference
xlam_format_tools = convert_to_xlam_tool(openai_format_tools)
print(xlam_format_tools)
content = build_prompt(task_instruction, format_instruction, xlam_format_tools, query)

messages = [{'role': 'user', 'content': content}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
)

# Check if inputs is a dictionary (as expected) or a single Tensor.
if isinstance(inputs, dict):
    # Move each tensor in the dictionary to the model's device.
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    start_len = input_ids.shape[1]
else:
    # In case the returned value is a Tensor, move it to the device.
    inputs = inputs.to(model.device)
    input_ids = inputs
    attention_mask = None
    start_len = inputs.shape[1]

pad_token_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id

outputs = model.generate(
    input_ids=input_ids,
    attention_mask=attention_mask,
    max_new_tokens=512,
    do_sample=False,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=pad_token_id
)

# Decode the generated tokens starting after the prompt length.
print(tokenizer.decode(outputs[0][start_len:], skip_special_tokens=True))
