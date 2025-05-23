# create-generated-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-generated-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-generated-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# create-generated-template

## Description

Creates a template from existing resources that are not already managed with CloudFormation. You can check the status of the template generation using the `DescribeGeneratedTemplate` API action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateGeneratedTemplate)

## Synopsis

```
create-generated-template
[--resources <value>]
--generated-template-name <value>
[--stack-name <value>]
[--template-configuration <value>]
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

`--resources` (list)

An optional list of resources to be included in the generated template.

If no resources are specified,the template will be created without any resources. Resources can be added to the template using the `UpdateGeneratedTemplate` API action.

(structure)

A resource included in a generated template. This data type is used with the `CreateGeneratedTemplate` and `UpdateGeneratedTemplate` API actions.

ResourceType -> (string)

The type of the resource, such as `AWS::DynamoDB::Table` . For the list of supported resources, see [Resource type support for imports and drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) in the *CloudFormation User Guide*

LogicalResourceId -> (string)

The logical resource id for this resource in the generated template.

ResourceIdentifier -> (map)

A list of up to 256 key-value pairs that identifies the scanned resource. The key is the name of one of the primary identifiers for the resource. (Primary identifiers are specified in the `primaryIdentifier` list in the resource schema.) The value is the value of that primary identifier. For example, for a `AWS::DynamoDB::Table` resource, the primary identifiers is `TableName` so the key-value pair could be `"TableName": "MyDDBTable"` . For more information, see [primaryIdentifier](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-primaryidentifier) in the *CloudFormation Command Line Interface (CLI) User Guide* .

key -> (string)

value -> (string)

Shorthand Syntax:

```
ResourceType=string,LogicalResourceId=string,ResourceIdentifier={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "string",
    "LogicalResourceId": "string",
    "ResourceIdentifier": {"string": "string"
      ...}
  }
  ...
]
```

`--generated-template-name` (string)

The name assigned to the generated template.

`--stack-name` (string)

An optional name or ARN of a stack to use as the base stack for the generated template.

`--template-configuration` (structure)

The configuration details of the generated template, including the `DeletionPolicy` and `UpdateReplacePolicy` .

DeletionPolicy -> (string)

The `DeletionPolicy` assigned to resources in the generated template. Supported values are:

- `DELETE` - delete all resources when the stack is deleted.
- `RETAIN` - retain all resources when the stack is deleted.

For more information, see [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) in the *CloudFormation User Guide* .

UpdateReplacePolicy -> (string)

The `UpdateReplacePolicy` assigned to resources in the generated template. Supported values are:

- `DELETE` - delete all resources when the resource is replaced during an update operation.
- `RETAIN` - retain all resources when the resource is replaced during an update operation.

For more information, see [UpdateReplacePolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html) in the *CloudFormation User Guide* .

Shorthand Syntax:

```
DeletionPolicy=string,UpdateReplacePolicy=string
```

JSON Syntax:

```
{
  "DeletionPolicy": "DELETE"|"RETAIN",
  "UpdateReplacePolicy": "DELETE"|"RETAIN"
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

## Output

GeneratedTemplateId -> (string)

The ID of the generated template.