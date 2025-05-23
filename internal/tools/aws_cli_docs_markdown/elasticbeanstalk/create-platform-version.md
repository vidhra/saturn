# create-platform-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-platform-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-platform-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# create-platform-version

## Description

Create a new version of your custom platform.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CreatePlatformVersion)

## Synopsis

```
create-platform-version
--platform-name <value>
--platform-version <value>
--platform-definition-bundle <value>
[--environment-name <value>]
[--option-settings <value>]
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

`--platform-name` (string)

The name of your custom platform.

`--platform-version` (string)

The number, such as 1.0.2, for the new platform version.

`--platform-definition-bundle` (structure)

The location of the platform definition archive in Amazon S3.

S3Bucket -> (string)

The Amazon S3 bucket where the data is located.

S3Key -> (string)

The Amazon S3 key where the data is located.

Shorthand Syntax:

```
S3Bucket=string,S3Key=string
```

JSON Syntax:

```
{
  "S3Bucket": "string",
  "S3Key": "string"
}
```

`--environment-name` (string)

The name of the builder environment.

`--option-settings` (list)

The configuration option settings to apply to the builder environment.

(structure)

A specification identifying an individual configuration option along with its current value. For a list of possible namespaces and option values, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the *AWS Elastic Beanstalk Developer Guide* .

ResourceName -> (string)

A unique resource name for the option setting. Use it for a timeâbased scaling configuration option.

Namespace -> (string)

A unique namespace that identifies the optionâs associated AWS resource.

OptionName -> (string)

The name of the configuration option.

Value -> (string)

The current value for the configuration option.

Shorthand Syntax:

```
ResourceName=string,Namespace=string,OptionName=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "ResourceName": "string",
    "Namespace": "string",
    "OptionName": "string",
    "Value": "string"
  }
  ...
]
```

`--tags` (list)

Specifies the tags applied to the new platform version.

Elastic Beanstalk applies these tags only to the platform version. Environments that you create using the platform version donât inherit the tags.

(structure)

Describes a tag applied to a resource in an environment.

Key -> (string)

The key of the tag.

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

## Output

PlatformSummary -> (structure)

Detailed information about the new version of the custom platform.

PlatformArn -> (string)

The ARN of the platform version.

PlatformOwner -> (string)

The AWS account ID of the person who created the platform version.

PlatformStatus -> (string)

The status of the platform version. You can create an environment from the platform version once it is ready.

PlatformCategory -> (string)

The category of platform version.

OperatingSystemName -> (string)

The operating system used by the platform version.

OperatingSystemVersion -> (string)

The version of the operating system used by the platform version.

SupportedTierList -> (list)

The tiers in which the platform version runs.

(string)

SupportedAddonList -> (list)

The additions associated with the platform version.

(string)

PlatformLifecycleState -> (string)

The state of the platform version in its lifecycle.

Possible values: `recommended` | empty

If an empty value is returned, the platform version is supported but isnât the recommended one for its branch.

PlatformVersion -> (string)

The version string of the platform version.

PlatformBranchName -> (string)

The platform branch to which the platform version belongs.

PlatformBranchLifecycleState -> (string)

The state of the platform versionâs branch in its lifecycle.

Possible values: `beta` | `supported` | `deprecated` | `retired`

Builder -> (structure)

The builder used to create the custom platform.

ARN -> (string)

The ARN of the builder.