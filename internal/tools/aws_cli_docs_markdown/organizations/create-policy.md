# create-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [organizations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/index.html#cli-aws-organizations) ]

# create-policy

## Description

Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual Amazon Web Services account.

For more information about policies and their use, see [Managing Organizations policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html) .

If the request includes tags, then the requester must have the `organizations:TagResource` permission.

This operation can be called only from the organizationâs management account or by a member account that is a delegated administrator for an Amazon Web Services service.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/CreatePolicy)

## Synopsis

```
create-policy
--content <value>
--description <value>
--name <value>
--type <value>
[--tags <value>]
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

`--content` (string)

The policy text content to add to the new policy. The text that you supply must adhere to the rules of the policy type you specify in the `Type` parameter.

The maximum size of a policy document depends on the policyâs type. For more information, see [Maximum and minimum values](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html#min-max-values) in the *Organizations User Guide* .

`--description` (string)

An optional description to assign to the policy.

`--name` (string)

The friendly name to assign to the policy.

The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of any of the characters in the ASCII character range.

`--type` (string)

The type of policy to create. You can specify one of the following values:

- [SERVICE_CONTROL_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html)
- [RESOURCE_CONTROL_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html)
- [DECLARATIVE_POLICY_EC2](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html)
- [BACKUP_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html)
- [TAG_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)
- [CHATBOT_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html)
- [AISERVICES_OPT_OUT_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html)

Possible values:

- `SERVICE_CONTROL_POLICY`
- `RESOURCE_CONTROL_POLICY`
- `TAG_POLICY`
- `BACKUP_POLICY`
- `AISERVICES_OPT_OUT_POLICY`
- `CHATBOT_POLICY`
- `DECLARATIVE_POLICY_EC2`

`--tags` (list)

A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you canât set it to `null` . For more information about tagging, see [Tagging Organizations resources](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html) in the Organizations User Guide.

### Note

If any one of the tags is not valid or if you exceed the allowed number of tags for a policy, then the entire request fails and the policy is not created.

(structure)

A custom key-value pair associated with a resource within your organization.

You can attach tags to any of the following organization resources.

- Amazon Web Services account
- Organizational unit (OU)
- Organization root
- Policy

Key -> (string)

The key identifier, or name, of the tag.

Value -> (string)

The string value thatâs associated with the key of the tag. You can set the value of a tag to an empty string, but you canât set the value of a tag to null.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

**Example 1: To create a policy with a text source file for the JSON policy**

The following example shows you how to create an service control policy (SCP) named `AllowAllS3Actions`. The policy contents are taken from a file on the local computer called `policy.json`.

```
aws organizations create-policy --content file://policy.json --name AllowAllS3Actions, --type SERVICE_CONTROL_POLICY --description "Allows delegation of all S3 actions"
```

The output includes a policy object with details about the new policy:

```
{
        "Policy": {
                "Content": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"s3:*\"],\"Resource\":[\"*\"]}]}",
                "PolicySummary": {
                        "Arn": "arn:aws:organizations::o-exampleorgid:policy/service_control_policy/p-examplepolicyid111",
                        "Description": "Allows delegation of all S3 actions",
                        "Name": "AllowAllS3Actions",
                        "Type":"SERVICE_CONTROL_POLICY"
                }
        }
}
```

**Example 2: To create a policy with a JSON policy as a parameter**

The following example shows you how to create the same SCP, this time by embedding the policy contents as a JSON string in the parameter. The string must be escaped with backslashes before the double quotes to ensure that they are treated as literals in the parameter, which itself is surrounded by double quotes:

```
aws organizations create-policy --content "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"s3:*\"],\"Resource\":[\"*\"]}]}" --name AllowAllS3Actions --type SERVICE_CONTROL_POLICY --description "Allows delegation of all S3 actions"
```

For more information about creating and using policies in your organization, see [Managing Organization Policies](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html) in the *AWS Organizations User Guide*.

## Output

Policy -> (structure)

A structure that contains details about the newly created policy.

PolicySummary -> (structure)

A structure that contains additional details about the policy.

Id -> (string)

The unique identifier (ID) of the policy.

The [regex pattern](http://wikipedia.org/wiki/regex) for a policy ID string requires âp-â followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).

Arn -> (string)

The Amazon Resource Name (ARN) of the policy.

For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the *Amazon Web Services Service Authorization Reference* .

Name -> (string)

The friendly name of the policy.

The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Description -> (string)

The description of the policy.

Type -> (string)

The type of policy.

AwsManaged -> (boolean)

A boolean value that indicates whether the specified policy is an Amazon Web Services managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

Content -> (string)

The text content of the policy.