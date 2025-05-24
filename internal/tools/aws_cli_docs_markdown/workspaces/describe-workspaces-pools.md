# describe-workspaces-poolsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces-pools.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces-pools.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/index.html#cli-aws-workspaces) ]

# describe-workspaces-pools

## Description

Describes the specified WorkSpaces Pools.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspacesPools)

## Synopsis

```
describe-workspaces-pools
[--pool-ids <value>]
[--filters <value>]
[--limit <value>]
[--next-token <value>]
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

`--pool-ids` (list)

The identifier of the WorkSpaces Pools.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

The filter conditions for the WorkSpaces Pool to return.

(structure)

Describes the filter conditions for WorkSpaces Pools to return.

Name -> (string)

The name of the pool to filter.

Values -> (list)

The values for filtering WorkSpaces Pools.

(string)

Operator -> (string)

The operator values for filtering WorkSpaces Pools.

Shorthand Syntax:

```
Name=string,Values=string,string,Operator=string ...
```

JSON Syntax:

```
[
  {
    "Name": "PoolName",
    "Values": ["string", ...],
    "Operator": "EQUALS"|"NOTEQUALS"|"CONTAINS"|"NOTCONTAINS"
  }
  ...
]
```

`--limit` (integer)

The maximum number of items to return.

`--next-token` (string)

If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.

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

WorkspacesPools -> (list)

Information about the WorkSpaces Pools.

(structure)

Describes a pool of WorkSpaces.

PoolId -> (string)

The identifier of a pool.

PoolArn -> (string)

The Amazon Resource Name (ARN) for the pool.

CapacityStatus -> (structure)

The capacity status for the pool

AvailableUserSessions -> (integer)

The number of user sessions currently available for streaming from your pool.

AvailableUserSessions = ActualUserSessions - ActiveUserSessions

DesiredUserSessions -> (integer)

The total number of sessions slots that are either running or pending. This represents the total number of concurrent streaming sessions your pool can support in a steady state.

ActualUserSessions -> (integer)

The total number of user sessions that are available for streaming or are currently streaming in your pool.

ActualUserSessions = AvailableUserSessions + ActiveUserSessions

ActiveUserSessions -> (integer)

The number of user sessions currently being used for your pool.

PoolName -> (string)

The name of the pool.

Description -> (string)

The description of the pool.

State -> (string)

The current state of the pool.

CreatedAt -> (timestamp)

The time the pool was created.

BundleId -> (string)

The identifier of the bundle used by the pool.

DirectoryId -> (string)

The identifier of the directory used by the pool.

Errors -> (list)

The pool errors.

(structure)

Describes a pool error.

ErrorCode -> (string)

The error code.

ErrorMessage -> (string)

The error message.

ApplicationSettings -> (structure)

The persistent application settings for users of the pool.

Status -> (string)

Specifies whether persistent application settings are enabled for users during their pool sessions.

SettingsGroup -> (string)

The path prefix for the S3 bucket where usersâ persistent application settings are stored.

S3BucketName -> (string)

The S3 bucket where usersâ persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an Amazon Web Services Region, an S3 bucket is created. The bucket is unique to the Amazon Web Services account and the Region.

TimeoutSettings -> (structure)

The amount of time that a pool session remains active after users disconnect. If they try to reconnect to the pool session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new pool instance.

DisconnectTimeoutInSeconds -> (integer)

Specifies the amount of time, in seconds, that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within the time set, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.

IdleDisconnectTimeoutInSeconds -> (integer)

The amount of time in seconds a connection will stay active while idle.

MaxUserDurationInSeconds -> (integer)

Specifies the maximum amount of time, in seconds, that a streaming session can remain active. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.

RunningMode -> (string)

The running mode of the pool.

NextToken -> (string)

If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.