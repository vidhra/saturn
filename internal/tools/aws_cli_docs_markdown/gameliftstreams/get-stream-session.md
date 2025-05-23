# get-stream-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/get-stream-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/get-stream-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gameliftstreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/index.html#cli-aws-gameliftstreams) ]

# get-stream-session

## Description

Retrieves properties for a Amazon GameLift Streams stream session resource. Specify the Amazon Resource Name (ARN) of the stream session that you want to retrieve and its stream group ARN. If the operation is successful, it returns properties for the requested resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gameliftstreams-2018-05-10/GetStreamSession)

## Synopsis

```
get-stream-session
--identifier <value>
--stream-session-identifier <value>
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

`--identifier` (string)

The stream group that runs this stream session.

This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Format example: ARN-`arn:aws:gameliftstreams:us-west-2:123456789012:streamgroup/sg-1AB2C3De4` or ID-`sg-1AB2C3De4` .

`--stream-session-identifier` (string)

An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream session resource. Format example: `1AB2C3De4` .

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

AdditionalEnvironmentVariables -> (map)

A set of options that you can use to control the stream session runtime environment, expressed as a set of key-value pairs. You can use this to configure the application or stream session details. You can also provide custom environment variables that Amazon GameLift Streams passes to your game client.

### Note

If you want to debug your application with environment variables, we recommend that you do so in a local environment outside of Amazon GameLift Streams. For more information, refer to the Compatibility Guidance in the troubleshooting section of the Developer Guide.

`AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.

key -> (string)

value -> (string)

AdditionalLaunchArgs -> (list)

A list of CLI arguments that are sent to the streaming server when a stream session launches. You can use this to configure the application or stream session details. You can also provide custom arguments that Amazon GameLift Streams passes to your game client.

`AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.

(string)

ApplicationArn -> (string)

The application streaming in this session.

This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Format example: `arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6` .

Arn -> (string)

The Amazon Resource Name (ARN) assigned to the stream session resource. When combined with the stream group ARN, this value uniquely identifies it across all Amazon Web Services Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamsession/[resource ID]` .

ConnectionTimeoutSeconds -> (integer)

The maximum length of time (in seconds) that Amazon GameLift Streams keeps the stream session open. At this point, Amazon GameLift Streams ends the stream session regardless of any existing client connections.

CreatedAt -> (timestamp)

A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).

Description -> (string)

A human-readable label for the stream session. You can update this value at any time.

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

LogFileLocationUri -> (string)

Access location for log files that your content generates during a stream session. These log files are uploaded to cloud storage location at the end of a stream session. The Amazon GameLift Streams application resource defines which log files to upload.

Protocol -> (string)

The data transfer protocol in use with the stream session.

SessionLengthSeconds -> (integer)

The length of time that Amazon GameLift Streams keeps the game session open.

SignalRequest -> (string)

The WebRTC ICE offer string that a client generates to initiate a connection to the stream session.

SignalResponse -> (string)

The WebRTC answer string that the stream server generates in response to the `SignalRequest` .

Status -> (string)

The current status of the stream session. A stream session can host clients when in `ACTIVE` status.

StatusReason -> (string)

A short description of the reason the stream session is in `ERROR` status.

StreamGroupId -> (string)

The unique identifier for the Amazon GameLift Streams stream group that is hosting the stream session.

UserId -> (string)

An opaque, unique identifier for an end-user, defined by the developer.

WebSdkProtocolUrl -> (string)

The URL of an S3 bucket that stores Amazon GameLift Streams WebSDK files. The URL is used to establish connection with the client.