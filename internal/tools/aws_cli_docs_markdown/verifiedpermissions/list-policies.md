# list-policiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-policies.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-policies.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [verifiedpermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/index.html#cli-aws-verifiedpermissions) ]

# list-policies

## Description

Returns a paginated list of all policies stored in the specified policy store.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/verifiedpermissions-2021-12-01/ListPolicies)

`list-policies` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `policies`

## Synopsis

```
list-policies
--policy-store-id <value>
[--filter <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--policy-store-id` (string)

Specifies the ID of the policy store you want to list policies from.

`--filter` (structure)

Specifies a filter that limits the response to only policies that match the specified criteria. For example, you list only the policies that reference a specified principal.

principal -> (tagged union structure)

Filters the output to only policies that reference the specified principal.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `unspecified`, `identifier`.

unspecified -> (boolean)

Used to indicate that a principal or resource is not specified. This can be used to search for policies that are not associated with a specific principal or resource.

identifier -> (structure)

The identifier of the entity. It can consist of either an EntityType and EntityId, a principal, or a resource.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

resource -> (tagged union structure)

Filters the output to only policies that reference the specified resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `unspecified`, `identifier`.

unspecified -> (boolean)

Used to indicate that a principal or resource is not specified. This can be used to search for policies that are not associated with a specific principal or resource.

identifier -> (structure)

The identifier of the entity. It can consist of either an EntityType and EntityId, a principal, or a resource.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

policyType -> (string)

Filters the output to only policies of the specified type.

policyTemplateId -> (string)

Filters the output to only template-linked policies that were instantiated from the specified policy template.

Shorthand Syntax:

```
principal={unspecified=boolean,identifier={entityType=string,entityId=string}},resource={unspecified=boolean,identifier={entityType=string,entityId=string}},policyType=string,policyTemplateId=string
```

JSON Syntax:

```
{
  "principal": {
    "unspecified": true|false,
    "identifier": {
      "entityType": "string",
      "entityId": "string"
    }
  },
  "resource": {
    "unspecified": true|false,
    "identifier": {
      "entityType": "string",
      "entityId": "string"
    }
  },
  "policyType": "STATIC"|"TEMPLATE_LINKED",
  "policyTemplateId": "string"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list the available policies**

The following `list-policies` example lists all policies in the specified policy store.

```
aws verifiedpermissions list-policies \
    --policy-store-id PSEXAMPLEabcdefg111111
```

Output:

```
{
    "policies": [
        {
            "createdDate": "2023-06-12T20:33:37.382907+00:00",
            "definition": {
                "static": {
                    "description": "Grant everyone of janeFriends UserGroup access to the vacationFolder Album"
                }
            },
            "lastUpdatedDate": "2023-06-12T20:33:37.382907+00:00",
            "policyId": "SPEXAMPLEabcdefg111111",
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "policyType": "STATIC",
            "principal": {
                "entityId": "janeFriends",
                "entityType": "UserGroup"
            },
            "resource": {
                "entityId": "vacationFolder",
                "entityType": "Album"
            }
        },
        {
            "createdDate": "2023-06-12T20:39:44.975897+00:00",
            "definition": {
                "static": {
                    "description": "Grant everyone access to the publicFolder Album"
                }
            },
            "lastUpdatedDate": "2023-06-12T20:39:44.975897+00:00",
            "policyId": "SPEXAMPLEabcdefg222222",
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "policyType": "STATIC",
            "resource": {
                "entityId": "publicFolder",
                "entityType": "Album"
            }
        },
        {
            "createdDate": "2023-06-12T20:49:51.490211+00:00",
            "definition": {
                "templateLinked": {
                    "policyTemplateId": "PTEXAMPLEabcdefg111111"
                }
            },
            "lastUpdatedDate": "2023-06-12T20:49:51.490211+00:00",
            "policyId": "SPEXAMPLEabcdefg333333",
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "policyType": "TEMPLATE_LINKED",
            "principal": {
                "entityId": "alice",
                "entityType": "User"
            },
            "resource": {
                "entityId": "VacationPhoto94.jpg",
                "entityType": "Photo"
            }
        }
    ]
}
```

For more information about policies, see [Amazon Verified Permissions policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies.html) in the *Amazon Verified Permissions User Guide*.

## Output

nextToken -> (string)

If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null` . This indicates that this is the last page of results.

policies -> (list)

Lists all policies that are available in the specified policy store.

(structure)

Contains information about a policy.

This data type is used as a response parameter for the [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html) operation.

policyStoreId -> (string)

The identifier of the policy store where the policy you want information about is stored.

policyId -> (string)

The identifier of the policy you want information about.

policyType -> (string)

The type of the policy. This is one of the following values:

- `STATIC`
- `TEMPLATE_LINKED`

principal -> (structure)

The principal associated with the policy.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

resource -> (structure)

The resource associated with the policy.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

actions -> (list)

The action that a policy permits or forbids. For example, `{"actions": [{"actionId": "ViewPhoto", "actionType": "PhotoFlash::Action"}, {"entityID": "SharePhoto", "entityType": "PhotoFlash::Action"}]}` .

(structure)

Contains information about an action for a request for which an authorization decision is made.

This data type is used as a request parameter to the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

Example: `{ "actionId": "<action name>", "actionType": "Action" }`

actionType -> (string)

The type of an action.

actionId -> (string)

The ID of an action.

definition -> (tagged union structure)

The policy definition of an item in the list of policies returned.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `static`, `templateLinked`.

static -> (structure)

Information about a static policy that wasnât created with a policy template.

description -> (string)

A description of the static policy.

templateLinked -> (structure)

Information about a template-linked policy that was created by instantiating a policy template.

policyTemplateId -> (string)

The unique identifier of the policy template used to create this policy.

principal -> (structure)

The principal associated with this template-linked policy. Verified Permissions substitutes this principal for the `?principal` placeholder in the policy template when it evaluates an authorization request.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

resource -> (structure)

The resource associated with this template-linked policy. Verified Permissions substitutes this resource for the `?resource` placeholder in the policy template when it evaluates an authorization request.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

createdDate -> (timestamp)

The date and time the policy was created.

lastUpdatedDate -> (timestamp)

The date and time the policy was most recently updated.

effect -> (string)

The effect of the decision that a policy returns to an authorization request. For example, `"effect": "Permit"` .