# create-attendeeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-meetings/create-attendee.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-meetings/create-attendee.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-meetings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-meetings/index.html#cli-aws-chime-sdk-meetings) ]

# create-attendee

## Description

Creates a new attendee for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see [Using the Amazon Chime SDK](https://docs.aws.amazon.com/chime/latest/dg/meetings-sdk.html) in the *Amazon Chime Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-meetings-2021-07-15/CreateAttendee)

## Synopsis

```
create-attendee
--meeting-id <value>
--external-user-id <value>
[--capabilities <value>]
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

`--meeting-id` (string)

The unique ID of the meeting.

`--external-user-id` (string)

The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.

Pattern: `[-_&@+=,(){}\[\]\/Â«Â».:|'"#a-zA-Z0-9Ã-Ã¿\s]*`

Values that begin with `aws:` are reserved. You canât configure a value that uses this prefix.

`--capabilities` (structure)

The capabilities (`audio` , `video` , or `content` ) that you want to grant an attendee. If you donât specify capabilities, all users have send and receive capabilities on all media channels by default.

### Note

You use the capabilities with a set of values that control what the capabilities can do, such as `SendReceive` data. For more information about those values, see .

When using capabilities, be aware of these corner cases:

- If you specify `MeetingFeatures:Video:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive` , `Send` , or `Receive` for `AttendeeCapabilities:Video` will be rejected with `ValidationError 400` .
- If you specify `MeetingFeatures:Content:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive` , `Send` , or `Receive` for `AttendeeCapabilities:Content` will be rejected with `ValidationError 400` .
- You canât set `content` capabilities to `SendReceive` or `Receive` unless you also set `video` capabilities to `SendReceive` or `Receive` . If you donât set the `video` capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your `video` capability to receive and you set your `content` capability to not receive.
- When you change an `audio` capability from `None` or `Receive` to `Send` or `SendReceive` , and if the attendee left their microphone unmuted, audio will flow from the attendee to the other meeting participants.
- When you change a `video` or `content` capability from `None` or `Receive` to `Send` or `SendReceive` , and if the attendee turned on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.

Audio -> (string)

The audio capability assigned to an attendee.

Video -> (string)

The video capability assigned to an attendee.

Content -> (string)

The content capability assigned to an attendee.

Shorthand Syntax:

```
Audio=string,Video=string,Content=string
```

JSON Syntax:

```
{
  "Audio": "SendReceive"|"Send"|"Receive"|"None",
  "Video": "SendReceive"|"Send"|"Receive"|"None",
  "Content": "SendReceive"|"Send"|"Receive"|"None"
}
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

Attendee -> (structure)

The attendee information, including attendee ID and join token.

ExternalUserId -> (string)

The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.

Pattern: `[-_&@+=,(){}\[\]\/Â«Â».:|'"#a-zA-Z0-9Ã-Ã¿\s]*`

Values that begin with `aws:` are reserved. You canât configure a value that uses this prefix. Case insensitive.

AttendeeId -> (string)

The Amazon Chime SDK attendee ID.

JoinToken -> (string)

The join token used by the Amazon Chime SDK attendee.

Capabilities -> (structure)

The capabilities assigned to an attendee: audio, video, or content.

### Note

You use the capabilities with a set of values that control what the capabilities can do, such as `SendReceive` data. For more information about those values, see .

When using capabilities, be aware of these corner cases:

- If you specify `MeetingFeatures:Video:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive` , `Send` , or `Receive` for `AttendeeCapabilities:Video` will be rejected with `ValidationError 400` .
- If you specify `MeetingFeatures:Content:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive` , `Send` , or `Receive` for `AttendeeCapabilities:Content` will be rejected with `ValidationError 400` .
- You canât set `content` capabilities to `SendReceive` or `Receive` unless you also set `video` capabilities to `SendReceive` or `Receive` . If you donât set the `video` capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your `video` capability to receive and you set your `content` capability to not receive.
- When you change an `audio` capability from `None` or `Receive` to `Send` or `SendReceive` , and if the attendee left their microphone unmuted, audio will flow from the attendee to the other meeting participants.
- When you change a `video` or `content` capability from `None` or `Receive` to `Send` or `SendReceive` , and if the attendee turned on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.

Audio -> (string)

The audio capability assigned to an attendee.

Video -> (string)

The video capability assigned to an attendee.

Content -> (string)

The content capability assigned to an attendee.