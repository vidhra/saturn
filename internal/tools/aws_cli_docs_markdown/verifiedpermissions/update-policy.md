# update-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [verifiedpermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/index.html#cli-aws-verifiedpermissions) ]

# update-policy

## Description

Modifies a Cedar static policy in the specified policy store. You can change only certain elements of the [UpdatePolicyDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyInput.html#amazonverifiedpermissions-UpdatePolicy-request-UpdatePolicyDefinition) parameter. You can directly update only static policies. To change a template-linked policy, you must update the template instead, using [UpdatePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html) .

### Note

- If policy validation is enabled in the policy store, then updating a static policy causes Verified Permissions to validate the policy against the schema in the policy store. If the updated static policy doesnât pass validation, the operation fails and the update isnât stored.
- When you edit a static policy, you can change only certain elements of a static policy:
- The action referenced by the policy.
- A condition clause, such as when and unless.

You canât change these elements of a static policy:

- Changing a policy from a static policy to a template-linked policy.
- Changing the effect of a static policy from permit or forbid.
- The principal referenced by a static policy.
- The resource referenced by a static policy.

- To update a template-linked policy, you must update the template instead.

### Note

Verified Permissions is * [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency) * . It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/verifiedpermissions-2021-12-01/UpdatePolicy)

## Synopsis

```
update-policy
--policy-store-id <value>
--policy-id <value>
--definition <value>
[--cli-input-json | --cli-input-yaml]
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

Specifies the ID of the policy store that contains the policy that you want to update.

`--policy-id` (string)

Specifies the ID of the policy that you want to update. To find this value, you can use [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html) .

`--definition` (tagged union structure)

Specifies the updated policy content that you want to replace on the specified policy. The content must be valid Cedar policy language text.

You can change only the following elements from the policy definition:

- The `action` referenced by the policy.
- Any conditional clauses, such as `when` or `unless` clauses.

You **canât** change the following elements:

- Changing from `static` to `templateLinked` .
- Changing the effect of the policy from `permit` or `forbid` .
- The `principal` referenced by the policy.
- The `resource` referenced by the policy.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `static`.

static -> (structure)

Contains details about the updates to be applied to a static policy.

description -> (string)

Specifies the description to be added to or replaced on the static policy.

statement -> (string)

Specifies the Cedar policy language text to be added to or replaced on the static policy.

### Warning

You can change only the following elements from the original content:

- The `action` referenced by the policy.
- Any conditional clauses, such as `when` or `unless` clauses.

You **canât** change the following elements:

- Changing from `StaticPolicy` to `TemplateLinkedPolicy` .
- The effect (`permit` or `forbid` ) of the policy.
- The `principal` referenced by the policy.
- The `resource` referenced by the policy.

Shorthand Syntax:

```
static={description=string,statement=string}
```

JSON Syntax:

```
{
  "static": {
    "description": "string",
    "statement": "string"
  }
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

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

**Example 1: To create a static policy**

The following `create-policy` example creates a static policy with a policy scope that specifies both a principal and a resource.

```
aws verifiedpermissions create-policy \
    --definition file://definition.txt \
    --policy-store-id PSEXAMPLEabcdefg111111
```

The `statement` parameter takes a string representation of a JSON object. It contains embedded quotation marks (â) within the outermost quotation mark pair. This requires you to convert the JSON to a string by preceding all embedded quotation marks with a backslash character ( " ) and combining all lines into a single text line with no line breaks.

Example strings can be displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

Contents of file `definition.txt`:

```
{
    "static": {
        "description":  "Grant everyone of janeFriends UserGroup access to the vacationFolder Album",
        "statement": "permit(principal in UserGroup::\"janeFriends\", action, resource in Album::\"vacationFolder\" );"
    }
}
```

Output:

```
{
    "createdDate": "2023-06-12T20:33:37.382907+00:00",
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
}
```

**Example 2: To create a static policy that grants access to a resource to everyone**

The following `create-policy` example creates a static policy with a policy scope that specifies only a resource.

```
aws verifiedpermissions create-policy \
    --definition file://definition2.txt \
    --policy-store-id PSEXAMPLEabcdefg111111
```

Contents of file `definition2.txt`:

```
{
    "static": {
        "description":  "Grant everyone access to the publicFolder Album",
        "statement": "permit(principal, action, resource in Album::\"publicFolder\");"
    }
}
```

Output:

```
{
    "createdDate": "2023-06-12T20:39:44.975897+00:00",
    "lastUpdatedDate": "2023-06-12T20:39:44.975897+00:00",
    "policyId": "PbfR73F8oh5MMfr9uRtFDB",
    "policyStoreId": "PSEXAMPLEabcdefg222222",
    "policyType": "STATIC",
    "resource": {
        "entityId": "publicFolder",
        "entityType": "Album"
    }
}
```

**Example 3: To create a template-linked policy that is associated with the specified template**

The following `create-policy` example creates a template-linked policy using the specified policy template and associates the specified principal to use with the new template-linked policy.

```
aws verifiedpermissions create-policy \
    --definition file://definition2.txt \
    --policy-store-id PSEXAMPLEabcdefg111111
```

Contents of definition3.txt:

```
{
    "templateLinked": {
        "policyTemplateId": "PTEXAMPLEabcdefg111111",
        "principal": {
            "entityType": "User",
            "entityId": "alice"
        }
    }
}
```

Output:

```
{
    "createdDate": "2023-06-12T20:49:51.490211+00:00",
    "lastUpdatedDate": "2023-06-12T20:49:51.490211+00:00",
    "policyId": "TPEXAMPLEabcdefg111111",
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
```

For more information about policies, see [Amazon Verified Permissions policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies.html) in the *Amazon Verified Permissions User Guide*.

## Output

policyStoreId -> (string)

The ID of the policy store that contains the policy that was updated.

policyId -> (string)

The ID of the policy that was updated.

policyType -> (string)

The type of the policy that was updated.

principal -> (structure)

The principal specified in the policyâs scope. This element isnât included in the response when `Principal` isnât present in the policy content.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

resource -> (structure)

The resource specified in the policyâs scope. This element isnât included in the response when `Resource` isnât present in the policy content.

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

createdDate -> (timestamp)

The date and time that the policy was originally created.

lastUpdatedDate -> (timestamp)

The date and time that the policy was most recently updated.

effect -> (string)

The effect of the decision that a policy returns to an authorization request. For example, `"effect": "Permit"` .