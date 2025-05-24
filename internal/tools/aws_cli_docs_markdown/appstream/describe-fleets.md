# describe-fleetsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-fleets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-fleets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appstream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/index.html#cli-aws-appstream) ]

# describe-fleets

## Description

Retrieves a list that describes one or more specified fleets, if the fleet names are provided. Otherwise, all fleets in the account are described.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeFleets)

`describe-fleets` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Fleets`

## Synopsis

```
describe-fleets
[--names <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--max-items <value>]
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

The names of the fleets to describe.

(string)

Syntax:

```
"string" "string" ...
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

Fleets -> (list)

Information about the fleets.

(structure)

Describes a fleet.

Arn -> (string)

The Amazon Resource Name (ARN) for the fleet.

Name -> (string)

The name of the fleet.

DisplayName -> (string)

The fleet name to display.

Description -> (string)

The description to display.

ImageName -> (string)

The name of the image used to create the fleet.

ImageArn -> (string)

The ARN for the public, private, or shared image.

InstanceType -> (string)

The instance type to use when launching fleet instances. The following instance types are available:

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

FleetType -> (string)

The fleet type.

ALWAYS_ON

Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.

ON_DEMAND

Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.

ComputeCapacityStatus -> (structure)

The capacity status for the fleet.

Desired -> (integer)

The desired number of streaming instances.

Running -> (integer)

The total number of simultaneous streaming instances that are running.

InUse -> (integer)

The number of instances in use for streaming.

Available -> (integer)

The number of currently available instances that can be used to stream sessions.

DesiredUserSessions -> (integer)

The total number of sessions slots that are either running or pending. This represents the total number of concurrent streaming sessions your fleet can support in a steady state.

DesiredUserSessionCapacity = ActualUserSessionCapacity + PendingUserSessionCapacity

This only applies to multi-session fleets.

AvailableUserSessions -> (integer)

The number of idle session slots currently available for user sessions.

AvailableUserSessionCapacity = ActualUserSessionCapacity - ActiveUserSessions

This only applies to multi-session fleets.

ActiveUserSessions -> (integer)

The number of user sessions currently being used for streaming sessions. This only applies to multi-session fleets.

ActualUserSessions -> (integer)

The total number of session slots that are available for streaming or are currently streaming.

ActualUserSessionCapacity = AvailableUserSessionCapacity + ActiveUserSessions

This only applies to multi-session fleets.

MaxUserDurationInSeconds -> (integer)

The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.

Specify a value between 600 and 360000.

DisconnectTimeoutInSeconds -> (integer)

The amount of time that a streaming session remains active after users disconnect. If they try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.

Specify a value between 60 and 36000.

State -> (string)

The current state for the fleet.

VpcConfig -> (structure)

The VPC configuration for the fleet.

SubnetIds -> (list)

The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string)

SecurityGroupIds -> (list)

The identifiers of the security groups for the fleet or image builder.

(string)

CreatedTime -> (timestamp)

The time the fleet was created.

FleetErrors -> (list)

The fleet errors.

(structure)

Describes a fleet error.

ErrorCode -> (string)

The error code.

ErrorMessage -> (string)

The error message.

EnableDefaultInternetAccess -> (boolean)

Indicates whether default internet access is enabled for the fleet.

DomainJoinInfo -> (structure)

The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.

DirectoryName -> (string)

The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName -> (string)

The distinguished name of the organizational unit for computer accounts.

IdleDisconnectTimeoutInSeconds -> (integer)

The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the `DisconnectTimeoutInSeconds` time interval begins. Users are notified before they are disconnected due to inactivity. If users try to reconnect to the streaming session before the time interval specified in `DisconnectTimeoutInSeconds` elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in `IdleDisconnectTimeoutInSeconds` elapses, they are disconnected.

To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 36000. The default value is 0.

### Note

If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you donât do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.

IamRoleArn -> (string)

The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance calls the AWS Security Token Service (STS) `AssumeRole` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the **appstream_machine_role** credential profile on the instance.

For more information, see [Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html) in the *Amazon AppStream 2.0 Administration Guide* .

StreamView -> (string)

The AppStream 2.0 view that is displayed to your users when they stream from the fleet. When `APP` is specified, only the windows of applications opened by users display. When `DESKTOP` is specified, the standard desktop that is provided by the operating system displays.

The default value is `APP` .

Platform -> (string)

The platform of the fleet.

MaxConcurrentSessions -> (integer)

The maximum number of concurrent sessions for the fleet.

UsbDeviceFilterStrings -> (list)

The USB device filter strings associated with the fleet.

(string)

SessionScriptS3Location -> (structure)

The S3 location of the session scripts configuration zip file. This only applies to Elastic fleets.

S3Bucket -> (string)

The S3 bucket of the S3 object.

S3Key -> (string)

The S3 key of the S3 object.

This is required when used for the following:

- IconS3Location (Actions: CreateApplication and UpdateApplication)
- SessionScriptS3Location (Actions: CreateFleet and UpdateFleet)
- ScriptDetails (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `CUSTOM` PackagingType (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `APPSTREAM2` PackagingType, and using an existing application package (VHD file). In this case, `S3Key` refers to the VHD file. If a new application package is required, then `S3Key` is not required. (Actions: CreateAppBlock)

MaxSessionsPerInstance -> (integer)

The maximum number of user sessions on an instance. This only applies to multi-session fleets.

NextToken -> (string)

The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.