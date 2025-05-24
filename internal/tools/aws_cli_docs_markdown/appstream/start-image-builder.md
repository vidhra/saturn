# start-image-builderÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/start-image-builder.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/start-image-builder.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appstream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/index.html#cli-aws-appstream) ]

# start-image-builder

## Description

Starts the specified image builder.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/StartImageBuilder)

## Synopsis

```
start-image-builder
--name <value>
[--appstream-agent-version <value>]
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

`--name` (string)

The name of the image builder.

`--appstream-agent-version` (string)

The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].

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

ImageBuilder -> (structure)

Information about the image builder.

Name -> (string)

The name of the image builder.

Arn -> (string)

The ARN for the image builder.

ImageArn -> (string)

The ARN of the image from which this builder was created.

Description -> (string)

The description to display.

DisplayName -> (string)

The image builder name to display.

VpcConfig -> (structure)

The VPC configuration of the image builder.

SubnetIds -> (list)

The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string)

SecurityGroupIds -> (list)

The identifiers of the security groups for the fleet or image builder.

(string)

InstanceType -> (string)

The instance type for the image builder. The following instance types are available:

- stream.standard.small
- stream.standard.medium
- stream.standard.large
- stream.compute.large
- stream.compute.xlarge
- stream.compute.2xlarge
- stream.compute.4xlarge
- stream.compute.8xlarge
- stream.memory.large
- stream.memory.xlarge
- stream.memory.2xlarge
- stream.memory.4xlarge
- stream.memory.8xlarge
- stream.memory.z1d.large
- stream.memory.z1d.xlarge
- stream.memory.z1d.2xlarge
- stream.memory.z1d.3xlarge
- stream.memory.z1d.6xlarge
- stream.memory.z1d.12xlarge
- stream.graphics-design.large
- stream.graphics-design.xlarge
- stream.graphics-design.2xlarge
- stream.graphics-design.4xlarge
- stream.graphics-desktop.2xlarge
- stream.graphics.g4dn.xlarge
- stream.graphics.g4dn.2xlarge
- stream.graphics.g4dn.4xlarge
- stream.graphics.g4dn.8xlarge
- stream.graphics.g4dn.12xlarge
- stream.graphics.g4dn.16xlarge
- stream.graphics-pro.4xlarge
- stream.graphics-pro.8xlarge
- stream.graphics-pro.16xlarge

Platform -> (string)

The operating system platform of the image builder.

IamRoleArn -> (string)

The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) `AssumeRole` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the **appstream_machine_role** credential profile on the instance.

For more information, see [Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html) in the *Amazon AppStream 2.0 Administration Guide* .

State -> (string)

The state of the image builder.

StateChangeReason -> (structure)

The reason why the last state change occurred.

Code -> (string)

The state change reason code.

Message -> (string)

The state change reason message.

CreatedTime -> (timestamp)

The time stamp when the image builder was created.

EnableDefaultInternetAccess -> (boolean)

Enables or disables default internet access for the image builder.

DomainJoinInfo -> (structure)

The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.

DirectoryName -> (string)

The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName -> (string)

The distinguished name of the organizational unit for computer accounts.

NetworkAccessConfiguration -> (structure)

Describes the network details of the fleet or image builder instance.

EniPrivateIpAddress -> (string)

The private IP address of the elastic network interface that is attached to instances in your VPC.

EniId -> (string)

The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

ImageBuilderErrors -> (list)

The image builder errors.

(structure)

Describes a resource error.

ErrorCode -> (string)

The error code.

ErrorMessage -> (string)

The error message.

ErrorTimestamp -> (timestamp)

The time the error occurred.

AppstreamAgentVersion -> (string)

The version of the AppStream 2.0 agent that is currently being used by the image builder.

AccessEndpoints -> (list)

The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.

(structure)

Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType -> (string)

The type of interface endpoint.

VpceId -> (string)

The identifier (ID) of the VPC in which the interface endpoint is used.

LatestAppstreamAgentVersion -> (string)

Indicates whether the image builder is using the latest AppStream 2.0 agent version or not.