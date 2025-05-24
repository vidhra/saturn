# activate-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/activate-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/activate-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# activate-type

## Description

Activates a public third-party extension, making it available for use in stack templates. Once you have activated a public third-party extension in your account and Region, use [SetTypeConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html) to specify configuration properties for the extension. For more information, see [Using public extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html) in the *CloudFormation User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ActivateType)

## Synopsis

```
activate-type
[--type <value>]
[--public-type-arn <value>]
[--publisher-id <value>]
[--type-name <value>]
[--type-name-alias <value>]
[--auto-update | --no-auto-update]
[--logging-config <value>]
[--execution-role-arn <value>]
[--version-bump <value>]
[--major-version <value>]
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

`--type` (string)

The extension type.

Conditional: You must specify `PublicTypeArn` , or `TypeName` , `Type` , and `PublisherId` .

Possible values:

- `RESOURCE`
- `MODULE`
- `HOOK`

`--public-type-arn` (string)

The Amazon Resource Name (ARN) of the public extension.

Conditional: You must specify `PublicTypeArn` , or `TypeName` , `Type` , and `PublisherId` .

`--publisher-id` (string)

The ID of the extension publisher.

Conditional: You must specify `PublicTypeArn` , or `TypeName` , `Type` , and `PublisherId` .

`--type-name` (string)

The name of the extension.

Conditional: You must specify `PublicTypeArn` , or `TypeName` , `Type` , and `PublisherId` .

`--type-name-alias` (string)

An alias to assign to the public extension, in this account and Region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.

An extension alias must be unique within a given account and Region. You can activate the same public resource multiple times in the same account and Region, using different type name aliases.

`--auto-update` | `--no-auto-update` (boolean)

Whether to automatically update the extension in this account and Region when a new *minor* version is published by the extension publisher. Major versions released by the publisher must be manually updated.

The default is `true` .

`--logging-config` (structure)

Contains logging configuration information for an extension.

LogRoleArn -> (string)

The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.

LogGroupName -> (string)

The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extensionâs handlers.

Shorthand Syntax:

```
LogRoleArn=string,LogGroupName=string
```

JSON Syntax:

```
{
  "LogRoleArn": "string",
  "LogGroupName": "string"
}
```

`--execution-role-arn` (string)

The name of the IAM execution role to use to activate the extension.

`--version-bump` (string)

Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of `AutoUpdate` .

- `MAJOR` : CloudFormation updates the extension to the newest major version, if one is available.
- `MINOR` : CloudFormation updates the extension to the newest minor version, if one is available.

Possible values:

- `MAJOR`
- `MINOR`

`--major-version` (long)

The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available *minor* version of the major version selected.

You can specify `MajorVersion` or `VersionBump` , but not both.

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

**To activate a type**

The following `activate-type` example activates a public third-party extension, making it available for use in stack templates.

```
aws cloudformation activate-type \
    --region us-west-2 \
    --type RESOURCE \
    --type-name Example::Test::1234567890abcdef0 \
    --type-name-alias Example::Test::Alias
```

Output:

```
{
    "Arn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/Example-Test-Alias"
}
```

For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *AWS CloudFormation User Guide*.

## Output

Arn -> (string)

The Amazon Resource Name (ARN) of the activated extension, in this account and Region.