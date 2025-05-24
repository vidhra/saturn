# list-stream-sessions-by-accountÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/list-stream-sessions-by-account.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/list-stream-sessions-by-account.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gameliftstreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/index.html#cli-aws-gameliftstreams) ]

# list-stream-sessions-by-account

## Description

Retrieves a list of Amazon GameLift Streams stream sessions that this user account has access to.

In the returned list of stream sessions, the `ExportFilesMetadata` property only shows the `Status` value. To get the `OutpurUri` and `StatusReason` values, use [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) .

We donât recommend using this operation to regularly check stream session statuses because itâs costly. Instead, to check status updates for a specific stream session, use [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)

`list-stream-sessions-by-account` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Items`

## Synopsis

```
list-stream-sessions-by-account
[--export-files-status <value>]
[--status <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--export-files-status` (string)

Filter by the exported files status. You can specify one status in each request to retrieve only sessions that currently have that exported files status.

Possible values:

- `SUCCEEDED`
- `FAILED`
- `PENDING`

`--status` (string)

Filter by the stream session status. You can specify one status in each request to retrieve only sessions that are currently in that status.

Possible values:

- `ACTIVATING`
- `ACTIVE`
- `CONNECTED`
- `PENDING_CLIENT_RECONNECTION`
- `RECONNECTING`
- `TERMINATING`
- `TERMINATED`
- `ERROR`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

Items -> (list)

A collection of Amazon GameLift Streams stream sessions that are associated with a stream group and returned in response to a list request. Each item includes stream session metadata and status.

(structure)

Describes a Amazon GameLift Streams stream session. To retrieve additional details for the stream session, call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) .

ApplicationArn -> (string)

An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the application resource. Format example: ARN-`arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6` or ID-`a-9ZY8X7Wv6` .

Arn -> (string)

An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream session resource. Format example: `1AB2C3De4` . .

CreatedAt -> (timestamp)

A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).

ExportFilesMetadata -> (structure)

Provides details about the stream sessionâs exported files.

OutputUri -> (string)

The S3 bucket URI where Amazon GameLift Streams uploaded the set of compressed exported files for a stream session. Amazon GameLift Streams generates a ZIP file name based on the stream session metadata. Alternatively, you can provide a custom file name with a `.zip` file extension.

Example 1: If you provide an S3 URI called `s3://MyBucket/MyGame_Session1.zip` , then Amazon GameLift Streams will save the files at that location.

Example 2: If you provide an S3 URI called `s3://MyBucket/MyGameSessions_ExportedFiles/` , then Amazon GameLift Streams will save the files at `s3://MyBucket/MyGameSessions_ExportedFiles/YYYYMMDD-HHMMSS-appId-sg-Id-sessionId.zip` or another similar name.

Status -> (string)

The result of the [ExportStreamSessionFiles](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ExportStreamSessionFiles.html) operation.

StatusReason -> (string)

A short description of the reason the export is in `FAILED` status.

LastUpdatedAt -> (timestamp)

A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).

Location -> (string)

The location where Amazon GameLift Streams is hosting the stream session.

A locationâs name. For example, `us-east-1` . For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions and quotas](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide* .

Protocol -> (string)

The data transfer protocol in use with the stream session.

Status -> (string)

The current status of the stream session resource. Possible statuses include the following:

- `ACTIVATING` : The stream session is starting and preparing to stream.
- `ACTIVE` : The stream session is ready to accept client connections.
- `CONNECTED` : The stream session has a connected client.
- `PENDING_CLIENT_RECONNECTION` : A client has recently disconnected, and the stream session is waiting for the client to reconnect. After a short time, if the client doesnât reconnect, the stream session status transitions to `TERMINATED` .
- `TERMINATING` : The stream session is ending.
- `TERMINATED` : The stream session has ended.
- `ERROR` : The stream session failed to activate.

UserId -> (string)

An opaque, unique identifier for an end-user, defined by the developer.

NextToken -> (string)

A token that marks the start of the next sequential page of results. If an operation doesnât return a token, youâve reached the end of the list.