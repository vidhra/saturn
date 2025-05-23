# create-stageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-stage.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-stage.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ivs-realtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/index.html#cli-aws-ivs-realtime) ]

# create-stage

## Description

Creates a new stage (and optionally participant tokens).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ivs-realtime-2020-07-14/CreateStage)

## Synopsis

```
create-stage
[--name <value>]
[--participant-token-configurations <value>]
[--tags <value>]
[--auto-participant-recording-configuration <value>]
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

Optional name that can be specified for the stage being created.

`--participant-token-configurations` (list)

Array of participant token configuration objects to attach to the new stage.

(structure)

Object specifying a participant token configuration in a stage.

duration -> (integer)

Duration (in minutes), after which the corresponding participant token expires. Default: 720 (12 hours).

userId -> (string)

Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customerâs own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*

attributes -> (map)

Application-provided attributes to encode into the corresponding participant token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*

key -> (string)

value -> (string)

capabilities -> (list)

Set of capabilities that the user is allowed to perform in the stage.

(string)

Shorthand Syntax:

```
duration=integer,userId=string,attributes={KeyName1=string,KeyName2=string},capabilities=string,string ...
```

JSON Syntax:

```
[
  {
    "duration": integer,
    "userId": "string",
    "attributes": {"string": "string"
      ...},
    "capabilities": ["PUBLISH"|"SUBSCRIBE", ...]
  }
  ...
]
```

`--tags` (map)

Tags attached to the resource. Array of maps, each of the form `string:string (key:value)` . See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS has no constraints on tags beyond what is documented there.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--auto-participant-recording-configuration` (structure)

Configuration object for individual participant recording, to attach to the new stage.

storageConfigurationArn -> (string)

ARN of the  StorageConfiguration resource to use for individual participant recording. Default: `""` (empty string, no storage configuration is specified). Individual participant recording cannot be started unless a storage configuration is specified, when a  Stage is created or updated. To disable individual participant recording, set this to `""` ; other fields in this object will get reset to their defaults when sending `""` .

mediaTypes -> (list)

Types of media to be recorded. Default: `AUDIO_VIDEO` .

(string)

thumbnailConfiguration -> (structure)

A complex type that allows you to enable/disable the recording of thumbnails for individual participant recording and modify the interval at which thumbnails are generated for the live session.

targetIntervalSeconds -> (integer)

The targeted thumbnail-generation interval in seconds. This is configurable only if `recordingMode` is `INTERVAL` . Default: 60.

storage -> (list)

Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails/high directory. `LATEST` saves the latest thumbnail in media/latest_thumbnail/high/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds` . You can enable both `SEQUENTIAL` and `LATEST` . Default: `SEQUENTIAL` .

(string)

recordingMode -> (string)

Thumbnail recording mode. Default: `DISABLED` .

recordingReconnectWindowSeconds -> (integer)

If a stage publisher disconnects and then reconnects within the specified interval, the multiple recordings will be considered a single recording and merged together.

The default value is 0, which disables merging.

hlsConfiguration -> (structure)

HLS configuration object for individual participant recording.

targetSegmentDurationSeconds -> (integer)

Defines the target duration for recorded segments generated when recording a stage participant. Segments may have durations longer than the specified value when needed to ensure each segment begins with a keyframe. Default: 6.

Shorthand Syntax:

```
storageConfigurationArn=string,mediaTypes=string,string,thumbnailConfiguration={targetIntervalSeconds=integer,storage=[string,string],recordingMode=string},recordingReconnectWindowSeconds=integer,hlsConfiguration={targetSegmentDurationSeconds=integer}
```

JSON Syntax:

```
{
  "storageConfigurationArn": "string",
  "mediaTypes": ["AUDIO_VIDEO"|"AUDIO_ONLY"|"NONE", ...],
  "thumbnailConfiguration": {
    "targetIntervalSeconds": integer,
    "storage": ["SEQUENTIAL"|"LATEST", ...],
    "recordingMode": "INTERVAL"|"DISABLED"
  },
  "recordingReconnectWindowSeconds": integer,
  "hlsConfiguration": {
    "targetSegmentDurationSeconds": integer
  }
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To create a stage**

The following `create-stage` example creates a stage and stage participant token for a specified user.

```
aws ivs-realtime create-stage \
    --name stage1 \
    --participant-token-configurations userId=alice
```

Output:

```
{
    "participantTokens": [
        {
            "participantId": "ABCDEfghij01234KLMN5678",
            "token": "a1b2c3d4567890ab",
            "userId": "alice"
        }
    ],
    "stage": {
        "activeSessionId": "st-a1b2c3d4e5f6g",
        "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh",
        "autoParticipantRecordingConfiguration": {
            "storageConfigurationArn": "",
            "mediaTypes": [
                "AUDIO_VIDEO"
            ],
            "thumbnailConfiguration": {
                "targetIntervalSeconds": 60,
                "storage": [
                    "SEQUENTIAL"
                ],
                "recordingMode": "DISABLED"
            },
            "recordingReconnectWindowSeconds": 0,
            "hlsConfiguration": {
                "targetSegmentDurationSeconds": 6
            }
        },
        "endpoints": {
            "events": "wss://global.events.live-video.net",
            "rtmp": "rtmp://9x0y8z7s6t5u.global-contribute-staging.live-video.net/app/",
            "rtmps": "rtmps://9x0y8z7s6t5u.global-contribute-staging.live-video.net:443/app/",
            "whip": "https://9x0y8z7s6t5u.global-bm.whip.live-video.net"
        },
        "name": "stage1",
        "tags": {}
    }
}
```

For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html) in the *Amazon IVS Low-Latency Streaming User Guide*.

**Example 2: To create a stage and configure individial participant recording**

The following `create-stage` example creates a stage and configures individual participant recording.

```
aws ivs-realtime create-stage \
    --name stage1 \
    --auto-participant-recording-configuration '{"mediaTypes": ["AUDIO_VIDEO"],"storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh", "recordingReconnectWindowSeconds": 100, \
        "hlsConfiguration": {"targetSegmentDurationSeconds": 5}}'
```

Output:

```
{
    "stage": {
        "activeSessionId": "st-a1b2c3d4e5f6g",
        "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh",
        "autoParticipantRecordingConfiguration": {
            "storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh"
            "mediaTypes": [
                "AUDIO_VIDEO"
            ],
            "thumbnailConfiguration": {
                "targetIntervalSeconds": 60,
                "storage": [
                    "SEQUENTIAL"
                ],
                "recordingMode": "DISABLED"
            },
            "recordingReconnectWindowSeconds": 100,
            "hlsConfiguration": {
                "targetSegmentDurationSeconds": 5
            }
        },
        "endpoints": {
            "events": "wss://global.events.live-video.net",
            "rtmp": "rtmp://9x0y8z7s6t5u.global-contribute-staging.live-video.net/app/",
            "rtmps": "rtmps://9x0y8z7s6t5u.global-contribute-staging.live-video.net:443/app/",
            "whip": "https://9x0y8z7s6t5u.global-bm.whip.live-video.net"
        },
        "name": "stage1",
        "tags": {}
    }
}
```

For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html) in the *Amazon IVS Low-Latency Streaming User Guide*.

**Example 3: To create a stage and configure individial participant recording with thumbnail recording enabled**

The following `create-stage` example creates a stage and configures individual participant recording with thumbnail recording enabled.

```
aws ivs-realtime create-stage \
    --name stage1 \
    --auto-participant-recording-configuration '{"mediaTypes": ["AUDIO_VIDEO"],"storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh", \
        "thumbnailConfiguration": {"recordingMode": "INTERVAL","storage": ["SEQUENTIAL"],"targetIntervalSeconds": 60}}'
```

Output:

```
{
    "stage": {
        "activeSessionId": "st-a1b2c3d4e5f6g",
        "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh",
        "autoParticipantRecordingConfiguration": {
            "storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh",
            "mediaTypes": [
                "AUDIO_VIDEO"
            ],
            "thumbnailConfiguration": {
                "targetIntervalSeconds": 60,
                "storage": [
                    "SEQUENTIAL"
                ],
                "recordingMode": "INTERVAL"
            },
            "recordingReconnectWindowSeconds": 0,
            "hlsConfiguration": {
                "targetSegmentDurationSeconds": 6
            }
        },
        "endpoints": {
            "events": "wss://global.events.live-video.net",
            "rtmp": "rtmp://9x0y8z7s6t5u.global-contribute-staging.live-video.net/app/",
            "rtmps": "rtmps://9x0y8z7s6t5u.global-contribute-staging.live-video.net:443/app/",
            "whip": "https://9x0y8z7s6t5u.global-bm.whip.live-video.net"
        },
        "name": "stage1",
        "tags": {}
    }
}
```

For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html) in the *Amazon IVS Low-Latency Streaming User Guide*.

## Output

stage -> (structure)

The stage that was created.

arn -> (string)

Stage ARN.

name -> (string)

Stage name.

activeSessionId -> (string)

ID of the active session within the stage.

tags -> (map)

Tags attached to the resource. Array of maps, each of the form `string:string (key:value)` . See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS has no constraints on tags beyond what is documented there.

key -> (string)

value -> (string)

autoParticipantRecordingConfiguration -> (structure)

Configuration object for individual participant recording, attached to the stage.

storageConfigurationArn -> (string)

ARN of the  StorageConfiguration resource to use for individual participant recording. Default: `""` (empty string, no storage configuration is specified). Individual participant recording cannot be started unless a storage configuration is specified, when a  Stage is created or updated. To disable individual participant recording, set this to `""` ; other fields in this object will get reset to their defaults when sending `""` .

mediaTypes -> (list)

Types of media to be recorded. Default: `AUDIO_VIDEO` .

(string)

thumbnailConfiguration -> (structure)

A complex type that allows you to enable/disable the recording of thumbnails for individual participant recording and modify the interval at which thumbnails are generated for the live session.

targetIntervalSeconds -> (integer)

The targeted thumbnail-generation interval in seconds. This is configurable only if `recordingMode` is `INTERVAL` . Default: 60.

storage -> (list)

Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails/high directory. `LATEST` saves the latest thumbnail in media/latest_thumbnail/high/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds` . You can enable both `SEQUENTIAL` and `LATEST` . Default: `SEQUENTIAL` .

(string)

recordingMode -> (string)

Thumbnail recording mode. Default: `DISABLED` .

recordingReconnectWindowSeconds -> (integer)

If a stage publisher disconnects and then reconnects within the specified interval, the multiple recordings will be considered a single recording and merged together.

The default value is 0, which disables merging.

hlsConfiguration -> (structure)

HLS configuration object for individual participant recording.

targetSegmentDurationSeconds -> (integer)

Defines the target duration for recorded segments generated when recording a stage participant. Segments may have durations longer than the specified value when needed to ensure each segment begins with a keyframe. Default: 6.

endpoints -> (structure)

Summary information about various endpoints for a stage.

events -> (string)

Events endpoint.

whip -> (string)

The endpoint to be used for IVS real-time streaming using the WHIP protocol.

rtmp -> (string)

The endpoint to be used for IVS real-time streaming using the RTMP protocol.

rtmps -> (string)

The endpoint to be used for IVS real-time streaming using the RTMPS protocol.

participantTokens -> (list)

Participant tokens attached to the stage. These correspond to the `participants` in the request.

(structure)

Object specifying a participant token in a stage.

**Important** : Treat tokens as opaque; i.e., do not build functionality based on token contents. The format of tokens could change in the future.

participantId -> (string)

Unique identifier for this participant token, assigned by IVS.

token -> (string)

The issued client token, encrypted.

userId -> (string)

Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customerâs own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*

attributes -> (map)

Application-provided attributes to encode into the token and attach to a stage. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*

key -> (string)

value -> (string)

duration -> (integer)

Duration (in minutes), after which the participant token expires. Default: 720 (12 hours).

capabilities -> (list)

Set of capabilities that the user is allowed to perform in the stage.

(string)

expirationTime -> (timestamp)

ISO 8601 timestamp (returned as a string) for when this token expires.