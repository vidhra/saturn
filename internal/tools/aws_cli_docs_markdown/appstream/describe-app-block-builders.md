# describe-app-block-buildersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-app-block-builders.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-app-block-builders.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appstream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/index.html#cli-aws-appstream) ]

# describe-app-block-builders

## Description

Retrieves a list that describes one or more app block builders.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeAppBlockBuilders)

## Synopsis

```
describe-app-block-builders
[--names <value>]
[--next-token <value>]
[--max-results <value>]
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

`--names` (list)

The names of the app block builders.

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The pagination token used to retrieve the next page of results for this operation.

`--max-results` (integer)

The maximum size of each page of results. The maximum value is 25.

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

AppBlockBuilders -> (list)

The list that describes one or more app block builders.

(structure)

Describes an app block builder.

Arn -> (string)

The ARN of the app block builder.

Name -> (string)

The name of the app block builder.

DisplayName -> (string)

The display name of the app block builder.

Description -> (string)

The description of the app block builder.

Platform -> (string)

The platform of the app block builder.

`WINDOWS_SERVER_2019` is the only valid value.

InstanceType -> (string)

The instance type of the app block builder.

EnableDefaultInternetAccess -> (boolean)

Indicates whether default internet access is enabled for the app block builder.

IamRoleArn -> (string)

The ARN of the IAM role that is applied to the app block builder.

VpcConfig -> (structure)

The VPC configuration for the app block builder.

SubnetIds -> (list)

The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string)

SecurityGroupIds -> (list)

The identifiers of the security groups for the fleet or image builder.

(string)

State -> (string)

The state of the app block builder.

CreatedTime -> (timestamp)

The creation time of the app block builder.

AppBlockBuilderErrors -> (list)

The app block builder errors.

(structure)

Describes a resource error.

ErrorCode -> (string)

The error code.

ErrorMessage -> (string)

The error message.

ErrorTimestamp -> (timestamp)

The time the error occurred.

StateChangeReason -> (structure)

The state change reason.

Code -> (string)

The state change reason code.

Message -> (string)

The state change reason message.

AccessEndpoints -> (list)

The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints.

(structure)

Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType -> (string)

The type of interface endpoint.

VpceId -> (string)

The identifier (ID) of the VPC in which the interface endpoint is used.

NextToken -> (string)

The pagination token used to retrieve the next page of results for this operation.