# batch-describe-type-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/batch-describe-type-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/batch-describe-type-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# batch-describe-type-configurations

## Description

Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry for the account and Region.

For more information, see [Edit configuration data for extensions in your account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-set-configuration.html) in the *CloudFormation User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/BatchDescribeTypeConfigurations)

## Synopsis

```
batch-describe-type-configurations
--type-configuration-identifiers <value>
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

`--type-configuration-identifiers` (list)

The list of identifiers for the desired extension configurations.

(structure)

Identifying information for the configuration of a CloudFormation extension.

TypeArn -> (string)

The Amazon Resource Name (ARN) for the extension, in this account and Region.

For public extensions, this will be the ARN assigned when you call the [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) API operation in this account and Region. For private extensions, this will be the ARN assigned when you call the [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) API operation in this account and Region.

TypeConfigurationAlias -> (string)

The alias specified for this configuration, if one was specified when the configuration was set.

TypeConfigurationArn -> (string)

The Amazon Resource Name (ARN) for the configuration, in this account and Region.

Type -> (string)

The type of extension.

TypeName -> (string)

The name of the extension type to which this configuration applies.

Shorthand Syntax:

```
TypeArn=string,TypeConfigurationAlias=string,TypeConfigurationArn=string,Type=string,TypeName=string ...
```

JSON Syntax:

```
[
  {
    "TypeArn": "string",
    "TypeConfigurationAlias": "string",
    "TypeConfigurationArn": "string",
    "Type": "RESOURCE"|"MODULE"|"HOOK",
    "TypeName": "string"
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

**To batch describe a type configuration**

The following `batch-describe-type-configurations` example configures the data for the type.

```
aws cloudformation batch-describe-type-configurations \
    --region us-west-2 \
    --type-configuration-identifiers TypeArn="arn:aws:cloudformation:us-west-2:123456789012:type/resource/Example-Test-Type,TypeConfigurationAlias=MyConfiguration"
```

Output:

```
{
    "Errors": [],
    "UnprocessedTypeConfigurations": [],
    "TypeConfigurations": [
        {
            "Arn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/Example-Test-Type",
            "Alias": "MyConfiguration",
            "Configuration": "{\n        \"Example\": {\n            \"ApiKey\": \"examplekey\",\n            \"ApplicationKey\": \"examplekey1\",\n            \"ApiURL\": \"exampleurl\"\n            }\n}",
            "LastUpdated": "2021-10-01T15:25:46.210000+00:00",
            "TypeArn": "arn:aws:cloudformation:us-east-1:123456789012:type/resource/Example-Test-Type"
        }
    ]
}
```

For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *AWS CloudFormation User Guide*.

## Output

Errors -> (list)

A list of information concerning any errors generated during the setting of the specified configurations.

(structure)

Detailed information concerning an error generated during the setting of configuration data for a CloudFormation extension.

ErrorCode -> (string)

The error code.

ErrorMessage -> (string)

The error message.

TypeConfigurationIdentifier -> (structure)

Identifying information for the configuration of a CloudFormation extension.

TypeArn -> (string)

The Amazon Resource Name (ARN) for the extension, in this account and Region.

For public extensions, this will be the ARN assigned when you call the [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) API operation in this account and Region. For private extensions, this will be the ARN assigned when you call the [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) API operation in this account and Region.

TypeConfigurationAlias -> (string)

The alias specified for this configuration, if one was specified when the configuration was set.

TypeConfigurationArn -> (string)

The Amazon Resource Name (ARN) for the configuration, in this account and Region.

Type -> (string)

The type of extension.

TypeName -> (string)

The name of the extension type to which this configuration applies.

UnprocessedTypeConfigurations -> (list)

A list of any of the specified extension configurations that CloudFormation could not process for any reason.

(structure)

Identifying information for the configuration of a CloudFormation extension.

TypeArn -> (string)

The Amazon Resource Name (ARN) for the extension, in this account and Region.

For public extensions, this will be the ARN assigned when you call the [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) API operation in this account and Region. For private extensions, this will be the ARN assigned when you call the [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) API operation in this account and Region.

TypeConfigurationAlias -> (string)

The alias specified for this configuration, if one was specified when the configuration was set.

TypeConfigurationArn -> (string)

The Amazon Resource Name (ARN) for the configuration, in this account and Region.

Type -> (string)

The type of extension.

TypeName -> (string)

The name of the extension type to which this configuration applies.

TypeConfigurations -> (list)

A list of any of the specified extension configurations from the CloudFormation registry.

(structure)

Detailed information concerning the specification of a CloudFormation extension in a given account and Region.

For more information, see [Edit configuration data for extensions in your account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-set-configuration.html) in the *CloudFormation User Guide* .

Arn -> (string)

The Amazon Resource Name (ARN) for the configuration data, in this account and Region.

Alias -> (string)

The alias specified for this configuration, if one was specified when the configuration was set.

Configuration -> (string)

A JSON string specifying the configuration data for the extension, in this account and Region.

If a configuration hasnât been set for a specified extension, CloudFormation returns `{}` .

LastUpdated -> (timestamp)

When the configuration data was last updated for this extension.

If a configuration hasnât been set for a specified extension, CloudFormation returns `null` .

TypeArn -> (string)

The Amazon Resource Name (ARN) for the extension, in this account and Region.

For public extensions, this will be the ARN assigned when you call the [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) API operation in this account and Region. For private extensions, this will be the ARN assigned when you call the [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) API operation in this account and Region.

TypeName -> (string)

The name of the extension.

IsDefaultConfiguration -> (boolean)

Whether this configuration data is the default configuration for the extension.