# create-stream-session-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/create-stream-session-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/create-stream-session-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gameliftstreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/index.html#cli-aws-gameliftstreams) ]

# create-stream-session-connection

## Description

Allows clients to reconnect to a recently disconnected stream session without losing any data from the last session.

A client can reconnect to a stream session thatâs in `PENDING_CLIENT_RECONNECTION` or `ACTIVE` status. In the stream session life cycle, when the client disconnects from the stream session, the stream session transitions from `CONNECTED` to `PENDING_CLIENT_RECONNECTION` status. When a client requests to reconnect by calling `CreateStreamSessionConnection` , the stream session transitions to `RECONNECTING` status. When the reconnection is successful, the stream session transitions to `ACTIVE` status. After a stream session is disconnected for longer than `ConnectionTimeoutSeconds` , the stream session transitions to the `TERMINATED` status.

To connect to an existing stream session, specify the stream group ID and stream session ID that you want to reconnect to, as well as the signal request settings to use with the stream.

`ConnectionTimeoutSeconds` defines the amount of time after the stream session disconnects that a reconnection is allowed. If a client is disconnected from the stream for longer than `ConnectionTimeoutSeconds` , the stream session ends.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gameliftstreams-2018-05-10/CreateStreamSessionConnection)

## Synopsis

```
create-stream-session-connection
[--client-token <value>]
--identifier <value>
--signal-request <value>
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

`--client-token` (string)

A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field.

`--identifier` (string)

[Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Format example: ARN-`arn:aws:gameliftstreams:us-west-2:123456789012:streamgroup/sg-1AB2C3De4` or ID-`sg-1AB2C3De4` .

The stream group that you want to run this stream session with. The stream group must be in `ACTIVE` status and have idle stream capacity.

`--signal-request` (string)

A WebRTC ICE offer string to use when initializing a WebRTC connection. The offer is a very long JSON string. Provide the string as a text value in quotes. The offer must be newly generated, not the same offer provided to `StartStreamSession` .

`--stream-session-identifier` (string)

[Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream session resource. Format example: `1AB2C3De4` . The stream session must be in `PENDING_CLIENT_RECONNECTION` or `ACTIVE` status.

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

SignalResponse -> (string)

The WebRTC answer string that the stream server generates in response to the `SignalRequest` .