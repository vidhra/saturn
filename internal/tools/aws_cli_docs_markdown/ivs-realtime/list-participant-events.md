# list-participant-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-participant-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-participant-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ivs-realtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/index.html#cli-aws-ivs-realtime) ]

# list-participant-events

## Description

Lists events for a specified participant that occurred during a specified stage session.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ivs-realtime-2020-07-14/ListParticipantEvents)

## Synopsis

```
list-participant-events
--stage-arn <value>
--session-id <value>
--participant-id <value>
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

`--stage-arn` (string)

Stage ARN.

`--session-id` (string)

ID of a session within the stage.

`--participant-id` (string)

Unique identifier for this participant. This is assigned by IVS and returned by  CreateParticipantToken .

`--next-token` (string)

The first participant event to retrieve. This is used for pagination; see the `nextToken` response field.

`--max-results` (integer)

Maximum number of results to return. Default: 50.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To get a list of stage participant events**

The following `list-participant-events` example lists all participant events for a specified participant ID and session ID of a specified stage ARN (Amazon Resource Name).

```
aws ivs-realtime list-participant-events \
    --stage-arn arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh \
    --session-id st-a1b2c3d4e5f6g \
    --participant-id abCDEf12GHIj
```

Output:

```
{
    "events": [
        {
            "eventTime": "2023-04-26T20:36:28+00:00",
            "name": "LEFT",
            "participantId": "abCDEf12GHIj"
        },
        {
            "eventTime": "2023-04-26T20:36:28+00:00",
            "name": "PUBLISH_STOPPED",
            "participantId": "abCDEf12GHIj"
        },
        {
            "eventTime": "2023-04-26T20:30:34+00:00",
            "name": "JOINED",
            "participantId": "abCDEf12GHIj"
        },
        {
            "eventTime": "2023-04-26T20:30:34+00:00",
            "name": "PUBLISH_STARTED",
            "participantId": "abCDEf12GHIj"
        }
    ]
}
```

For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/userguide/multiple-hosts.html) in the *Amazon Interactive Video Service User Guide*.

## Output

events -> (list)

List of the matching events.

(structure)

An occurrence during a stage session.

name -> (string)

The name of the event.

participantId -> (string)

Unique identifier for the participant who triggered the event. This is assigned by IVS.

eventTime -> (timestamp)

ISO 8601 timestamp (returned as a string) for when the event occurred.

remoteParticipantId -> (string)

Unique identifier for the remote participant. For a subscribe event, this is the publisher. For a publish or join event, this is null. This is assigned by IVS.

errorCode -> (string)

If the event is an error event, the error code is provided to give insight into the specific error that occurred. If the event is not an error event, this field is null.

- `B_FRAME_PRESENT` â The participantâs stream includes B-frames. For details, see [IVS RTMP Publishing](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html) .
- `BITRATE_EXCEEDED` â The participant exceeded the maximum supported bitrate. For details, see [Service Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html) .
- `INSUFFICIENT_CAPABILITIES` â The participant tried to take an action that the participantâs token is not allowed to do. For details on participant capabilities, see the `capabilities` field in  CreateParticipantToken .
- `INTERNAL_SERVER_EXCEPTION` â The participant failed to publish to the stage due to an internal server error.
- `INVALID_AUDIO_CODEC` â The participant is using an invalid audio codec. For details, see [Stream Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html) .
- `INVALID_INPUT` â The participant is using an invalid input stream.
- `INVALID_PROTOCOL` â The participantâs IngestConfiguration resource is configured for RTMPS but they tried streaming with RTMP. For details, see [IVS RTMP Publishing](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html) .
- `INVALID_STREAM_KEY` â The participant is using an invalid stream key. For details, see [IVS RTMP Publishing](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html) .
- `INVALID_VIDEO_CODEC` â The participant is using an invalid video codec. For details, see [Stream Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html) .
- `PUBLISHER_NOT_FOUND` â The participant tried to subscribe to a publisher that doesnât exist.
- `QUOTA_EXCEEDED` â The number of participants who want to publish/subscribe to a stage exceeds the quota. For details, see [Service Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html) .
- `RESOLUTION_EXCEEDED` â The participant exceeded the maximum supported resolution. For details, see [Service Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html) .
- `REUSE_OF_STREAM_KEY` â The participant tried to use a stream key that is associated with another active stage session.
- `STREAM_DURATION_EXCEEDED` â The participant exceeded the maximum allowed stream duration. For details, see [Service Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html) .

nextToken -> (string)

If there are more events than `maxResults` , use `nextToken` in the request to get the next set.