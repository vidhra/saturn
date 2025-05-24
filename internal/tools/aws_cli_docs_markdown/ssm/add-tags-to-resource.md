# add-tags-to-resourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/add-tags-to-resource.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/add-tags-to-resource.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# add-tags-to-resource

## Description

Adds or overwrites one or more tags for the specified resource. *Tags* are metadata that you can assign to your automations, documents, managed nodes, maintenance windows, Parameter Store parameters, and patch baselines. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your accountâs managed nodes that helps you track each nodeâs owner and stack level. For example:

- `Key=Owner,Value=DbAdmin`
- `Key=Owner,Value=SysAdmin`
- `Key=Owner,Value=Dev`
- `Key=Stack,Value=Production`
- `Key=Stack,Value=Pre-Production`
- `Key=Stack,Value=Test`

Most resources can have a maximum of 50 tags. Automations can have a maximum of 5 tags.

We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. Tags donât have any semantic meaning to and are interpreted strictly as a string of characters.

For more information about using tags with Amazon Elastic Compute Cloud (Amazon EC2) instances, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/AddTagsToResource)

## Synopsis

```
add-tags-to-resource
--resource-type <value>
--resource-id <value>
--tags <value>
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

`--resource-type` (string)

Specifies the type of resource you are tagging.

### Note

The `ManagedInstance` type for this API operation is for on-premises managed nodes. You must specify the name of the managed node in the following format: `mi-*ID_number* `` . For example, ``mi-1a2b3c4d5e6f` .

Possible values:

- `Document`
- `ManagedInstance`
- `MaintenanceWindow`
- `Parameter`
- `PatchBaseline`
- `OpsItem`
- `OpsMetadata`
- `Automation`
- `Association`

`--resource-id` (string)

The resource ID you want to tag.

Use the ID of the resource. Here are some examples:

`MaintenanceWindow` : `mw-012345abcde`

`PatchBaseline` : `pb-012345abcde`

`Automation` : `example-c160-4567-8519-012345abcde`

`OpsMetadata` object: `ResourceID` for tagging is created from the Amazon Resource Name (ARN) for the object. Specifically, `ResourceID` is created from the strings that come after the word `opsmetadata` in the ARN. For example, an OpsMetadata object with an ARN of `arn:aws:ssm:us-east-2:1234567890:opsmetadata/aws/ssm/MyGroup/appmanager` has a `ResourceID` of either `aws/ssm/MyGroup/appmanager` or `/aws/ssm/MyGroup/appmanager` .

For the `Document` and `Parameter` values, use the name of the resource. If youâre tagging a shared document, you must use the full ARN of the document.

`ManagedInstance` : `mi-012345abcde`

### Note

The `ManagedInstance` type for this API operation is only for on-premises managed nodes. You must specify the name of the managed node in the following format: `mi-*ID_number* `` . For example, ``mi-1a2b3c4d5e6f` .

`--tags` (list)

One or more tags. The value parameter is required.

### Warning

Donât enter personally identifiable information in this field.

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

**Example 1: To add tags to a maintenance window**

The following `add-tags-to-resource` example adds a tag to the specified maintenance window.

```
aws ssm add-tags-to-resource \
    --resource-type "MaintenanceWindow" \
    --resource-id "mw-03eb9db428EXAMPLE" \
    --tags "Key=Stack,Value=Production"
```

This command produces no output.

**Example 2: To add tags to a parameter**

The following `add-tags-to-resource` example adds two tags to to the specified parameter.

```
aws ssm add-tags-to-resource \
    --resource-type "Parameter" \
    --resource-id "My-Parameter" \
    --tags '[{"Key":"Region","Value":"East"},{"Key":"Environment", "Value":"Production"}]'
```

This command produces no output.

**Example 3: To add tags to an SSM document**

The following `add-tags-to-resource` example adds a tag to to the specified document.

```
aws ssm add-tags-to-resource \
    --resource-type "Document" \
    --resource-id "My-Document" \
    --tags "Key=Quarter,Value=Q322"
```

This command produces no output.

For more information, see [Tagging Systems Manager resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/tagging-resources.html) in the *AWS Systems Manager User Guide*.

## Output

None