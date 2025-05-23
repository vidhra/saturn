# describe-platform-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-platform-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-platform-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# describe-platform-version

## Description

Describes a platform version. Provides full details. Compare to  ListPlatformVersions , which provides summary information about a list of platform versions.

For definitions of platform version and other platform-related terms, see [AWS Elastic Beanstalk Platforms Glossary](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribePlatformVersion)

## Synopsis

```
describe-platform-version
[--platform-arn <value>]
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

`--platform-arn` (string)

The ARN of the platform version.

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

PlatformDescription -> (structure)

Detailed information about the platform version.

PlatformArn -> (string)

The ARN of the platform version.

PlatformOwner -> (string)

The AWS account ID of the person who created the platform version.

PlatformName -> (string)

The name of the platform version.

PlatformVersion -> (string)

The version of the platform version.

SolutionStackName -> (string)

The name of the solution stack used by the platform version.

PlatformStatus -> (string)

The status of the platform version.

DateCreated -> (timestamp)

The date when the platform version was created.

DateUpdated -> (timestamp)

The date when the platform version was last updated.

PlatformCategory -> (string)

The category of the platform version.

Description -> (string)

The description of the platform version.

Maintainer -> (string)

Information about the maintainer of the platform version.

OperatingSystemName -> (string)

The operating system used by the platform version.

OperatingSystemVersion -> (string)

The version of the operating system used by the platform version.

ProgrammingLanguages -> (list)

The programming languages supported by the platform version.

(structure)

A programming language supported by the platform.

Name -> (string)

The name of the programming language.

Version -> (string)

The version of the programming language.

Frameworks -> (list)

The frameworks supported by the platform version.

(structure)

A framework supported by the platform.

Name -> (string)

The name of the framework.

Version -> (string)

The version of the framework.

CustomAmiList -> (list)

The custom AMIs supported by the platform version.

(structure)

A custom AMI available to platforms.

VirtualizationType -> (string)

The type of virtualization used to create the custom AMI.

ImageId -> (string)

THe ID of the image used to create the custom AMI.

SupportedTierList -> (list)

The tiers supported by the platform version.

(string)

SupportedAddonList -> (list)

The additions supported by the platform version.

(string)

PlatformLifecycleState -> (string)

The state of the platform version in its lifecycle.

Possible values: `Recommended` | `null`

If a null value is returned, the platform version isnât the recommended one for its branch. Each platform branch has a single recommended platform version, typically the most recent one.

PlatformBranchName -> (string)

The platform branch to which the platform version belongs.

PlatformBranchLifecycleState -> (string)

The state of the platform versionâs branch in its lifecycle.

Possible values: `Beta` | `Supported` | `Deprecated` | `Retired`