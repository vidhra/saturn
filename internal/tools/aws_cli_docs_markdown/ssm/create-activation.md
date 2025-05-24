# create-activationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-activation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-activation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# create-activation

## Description

Generates an activation code and activation ID you can use to register your on-premises servers, edge devices, or virtual machine (VM) with Amazon Web Services Systems Manager. Registering these machines with Systems Manager makes it possible to manage them using Systems Manager tools. You use the activation code and ID when installing SSM Agent on machines in your hybrid environment. For more information about requirements for managing on-premises machines using Systems Manager, see [Using Amazon Web Services Systems Manager in hybrid and multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html) in the *Amazon Web Services Systems Manager User Guide* .

### Note

Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, and on-premises servers and VMs that are configured for Systems Manager are all called *managed nodes* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateActivation)

## Synopsis

```
create-activation
[--description <value>]
[--default-instance-name <value>]
--iam-role <value>
[--registration-limit <value>]
[--expiration-date <value>]
[--tags <value>]
[--registration-metadata <value>]
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

`--description` (string)

A user-defined description of the resource that you want to register with Systems Manager.

### Warning

Donât enter personally identifiable information in this field.

`--default-instance-name` (string)

The name of the registered, managed node as it will appear in the Amazon Web Services Systems Manager console or when you use the Amazon Web Services command line tools to list Systems Manager resources.

### Warning

Donât enter personally identifiable information in this field.

`--iam-role` (string)

The name of the Identity and Access Management (IAM) role that you want to assign to the managed node. This IAM role must provide AssumeRole permissions for the Amazon Web Services Systems Manager service principal `ssm.amazonaws.com` . For more information, see [Create the IAM service role required for Systems Manager in a hybrid and multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-service-role.html) in the *Amazon Web Services Systems Manager User Guide* .

### Note

You canât specify an IAM service-linked role for this parameter. You must create a unique role.

`--registration-limit` (integer)

Specify the maximum number of managed nodes you want to register. The default value is `1` .

`--expiration-date` (timestamp)

The date by which this activation request should expire, in timestamp format, such as â2024-07-07T00:00:00â. You can specify a date up to 30 days in advance. If you donât provide an expiration date, the activation code expires in 24 hours.

`--tags` (list)

Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an activation to identify which servers or virtual machines (VMs) in your on-premises environment you intend to activate. In this case, you could specify the following key-value pairs:

- `Key=OS,Value=Windows`
- `Key=Environment,Value=Production`

### Warning

When you install SSM Agent on your on-premises servers and VMs, you specify an activation ID and code. When you specify the activation ID and code, tags assigned to the activation are automatically applied to the on-premises servers or VMs.

You canât add tags to or delete tags from an existing activation. You can tag your on-premises servers, edge devices, and VMs after they connect to Systems Manager for the first time and are assigned a managed node ID. This means they are listed in the Amazon Web Services Systems Manager console with an ID that is prefixed with âmi-â. For information about how to add tags to your managed nodes, see  AddTagsToResource . For information about how to remove tags from your managed nodes, see  RemoveTagsFromResource .

(structure)

Metadata that you assign to your Amazon Web Services resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Amazon Web Services Systems Manager, you can apply tags to Systems Manager documents (SSM documents), managed nodes, maintenance windows, parameters, patch baselines, OpsItems, and OpsMetadata.

Key -> (string)

The name of the tag.

Value -> (string)

The value of the tag.

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

`--registration-metadata` (list)

Reserved for internal use.

(structure)

Reserved for internal use.

Key -> (string)

Reserved for internal use.

Value -> (string)

Reserved for internal use.

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

**To create a managed instance activation**

The following `create-activation` example creates a managed instance activation.

```
aws ssm create-activation \
    --default-instance-name "HybridWebServers" \
    --iam-role "HybridWebServersRole" \
    --registration-limit 5
```

Output:

```
{
    "ActivationId": "5743558d-563b-4457-8682-d16c3EXAMPLE",
    "ActivationCode": "dRmgnYaFv567vEXAMPLE"
}
```

For more information, see [Step 4: Create a Managed-Instance Activation for a Hybrid Environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-managed-instance-activation.html) in the *AWS Systems Manager User Guide*.

## Output

ActivationId -> (string)

The ID number generated by the system when it processed the activation. The activation ID functions like a user name.

ActivationCode -> (string)

The code the system generates when it processes the activation. The activation code functions like a password to validate the activation ID.