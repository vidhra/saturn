# start-compositionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/start-composition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/start-composition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ivs-realtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/index.html#cli-aws-ivs-realtime) ]

# start-composition

## Description

Starts a Composition from a stage based on the configuration provided in the request.

A Composition is an ephemeral resource that exists after this operation returns successfully. Composition stops and the resource is deleted:

- When  StopComposition is called.
- After a 1-minute timeout, when all participants are disconnected from the stage.
- After a 1-minute timeout, if there are no participants in the stage when StartComposition is called.
- When broadcasting to the IVS channel fails and all retries are exhausted.
- When broadcasting is disconnected and all attempts to reconnect are exhausted.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ivs-realtime-2020-07-14/StartComposition)

## Synopsis

```
start-composition
--stage-arn <value>
[--idempotency-token <value>]
[--layout <value>]
--destinations <value>
[--tags <value>]
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

ARN of the stage to be used for compositing.

`--idempotency-token` (string)

Idempotency token.

`--layout` (structure)

Layout object to configure composition parameters.

grid -> (structure)

Configuration related to grid layout. Default: Grid layout.

featuredParticipantAttribute -> (string)

This attribute name identifies the featured slot. A participant with this attribute set to `"true"` (as a string value) in  ParticipantTokenConfiguration is placed in the featured slot. Default: `""` (no featured participant).

omitStoppedVideo -> (boolean)

Determines whether to omit participants with stopped video in the composition. Default: `false` .

videoAspectRatio -> (string)

Sets the non-featured participant display mode, to control the aspect ratio of video tiles. `VIDEO` is 16:9, `SQUARE` is 1:1, and `PORTRAIT` is 3:4. Default: `VIDEO` .

videoFillMode -> (string)

Defines how video content fits within the participant tile: `FILL` (stretched), `COVER` (cropped), or `CONTAIN` (letterboxed). When not set, `videoFillMode` defaults to `COVER` fill mode for participants in the grid and to `CONTAIN` fill mode for featured participants.

gridGap -> (integer)

Specifies the spacing between participant tiles in pixels. Default: `2` .

pip -> (structure)

Configuration related to PiP layout.

featuredParticipantAttribute -> (string)

This attribute name identifies the featured slot. A participant with this attribute set to `"true"` (as a string value) in  ParticipantTokenConfiguration is placed in the featured slot. Default: `""` (no featured participant).

omitStoppedVideo -> (boolean)

Determines whether to omit participants with stopped video in the composition. Default: `false` .

videoFillMode -> (string)

Defines how video content fits within the participant tile: `FILL` (stretched), `COVER` (cropped), or `CONTAIN` (letterboxed). Default: `COVER` .

gridGap -> (integer)

Specifies the spacing between participant tiles in pixels. Default: `0` .

pipParticipantAttribute -> (string)

Specifies the participant for the PiP window. A participant with this attribute set to `"true"` (as a string value) in  ParticipantTokenConfiguration is placed in the PiP slot. Default: `""` (no PiP participant).

pipBehavior -> (string)

Defines PiP behavior when all participants have left: `STATIC` (maintains original position/size) or `DYNAMIC` (expands to full composition). Default: `STATIC` .

pipOffset -> (integer)

Sets the PiP windowâs offset position in pixels from the closest edges determined by `PipPosition` . Default: `0` .

pipPosition -> (string)

Determines the corner position of the PiP window. Default: `BOTTOM_RIGHT` .

pipWidth -> (integer)

Specifies the width of the PiP window in pixels. When this is not set explicitly, `pipWidth` âs value will be based on the size of the composition and the aspect ratio of the participantâs video.

pipHeight -> (integer)

Specifies the height of the PiP window in pixels. When this is not set explicitly, `pipHeight` âs value will be based on the size of the composition and the aspect ratio of the participantâs video.

Shorthand Syntax:

```
grid={featuredParticipantAttribute=string,omitStoppedVideo=boolean,videoAspectRatio=string,videoFillMode=string,gridGap=integer},pip={featuredParticipantAttribute=string,omitStoppedVideo=boolean,videoFillMode=string,gridGap=integer,pipParticipantAttribute=string,pipBehavior=string,pipOffset=integer,pipPosition=string,pipWidth=integer,pipHeight=integer}
```

JSON Syntax:

```
{
  "grid": {
    "featuredParticipantAttribute": "string",
    "omitStoppedVideo": true|false,
    "videoAspectRatio": "AUTO"|"VIDEO"|"SQUARE"|"PORTRAIT",
    "videoFillMode": "FILL"|"COVER"|"CONTAIN",
    "gridGap": integer
  },
  "pip": {
    "featuredParticipantAttribute": "string",
    "omitStoppedVideo": true|false,
    "videoFillMode": "FILL"|"COVER"|"CONTAIN",
    "gridGap": integer,
    "pipParticipantAttribute": "string",
    "pipBehavior": "STATIC"|"DYNAMIC",
    "pipOffset": integer,
    "pipPosition": "TOP_LEFT"|"TOP_RIGHT"|"BOTTOM_LEFT"|"BOTTOM_RIGHT",
    "pipWidth": integer,
    "pipHeight": integer
  }
}
```

`--destinations` (list)

Array of destination configuration.

(structure)

Complex data type that defines destination-configuration objects.

name -> (string)

Name that can be specified to help identify the destination.

channel -> (structure)

An IVS channel to be used for broadcasting, for server-side composition. Either a `channel` or an `s3` must be specified.

channelArn -> (string)

ARN of the channel to use for broadcasting. The channel and stage resources must be in the same AWS account and region. The channel must be offline (not broadcasting).

encoderConfigurationArn -> (string)

ARN of the  EncoderConfiguration resource. The encoder configuration and stage resources must be in the same AWS account and region.

s3 -> (structure)

An S3 storage configuration to be used for recording video data. Either a `channel` or an `s3` must be specified.

storageConfigurationArn -> (string)

ARN of the  StorageConfiguration where recorded videos will be stored.

encoderConfigurationArns -> (list)

ARNs of the  EncoderConfiguration resource. The encoder configuration and stage resources must be in the same AWS account and region.

(string)

recordingConfiguration -> (structure)

Array of maps, each of the form `string:string (key:value)` . This is an optional customer specification, currently used only to specify the recording format for storing a recording in Amazon S3.

hlsConfiguration -> (structure)

An HLS configuration object to return information about how the recording will be configured.

targetSegmentDurationSeconds -> (integer)

Defines the target duration for recorded segments generated when using composite recording. Segments may have durations shorter than the specified value when needed to ensure each segment begins with a keyframe. Default: 2.

format -> (string)

The recording format for storing a recording in Amazon S3.

thumbnailConfigurations -> (list)

A complex type that allows you to enable/disable the recording of thumbnails for a  Composition and modify the interval at which thumbnails are generated for the live session.

(structure)

An object representing a configuration of thumbnails for recorded video for a  Composition .

targetIntervalSeconds -> (integer)

The targeted thumbnail-generation interval in seconds. Default: 60.

storage -> (list)

Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails/(width)x(height) directory, where (width) and (height) are the width and height of the thumbnail. `LATEST` saves the latest thumbnail in media/latest_thumbnail/(width)x(height)/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds` . You can enable both `SEQUENTIAL` and `LATEST` . Default: `SEQUENTIAL` .

(string)

JSON Syntax:

```
[
  {
    "name": "string",
    "channel": {
      "channelArn": "string",
      "encoderConfigurationArn": "string"
    },
    "s3": {
      "storageConfigurationArn": "string",
      "encoderConfigurationArns": ["string", ...],
      "recordingConfiguration": {
        "hlsConfiguration": {
          "targetSegmentDurationSeconds": integer
        },
        "format": "HLS"
      },
      "thumbnailConfigurations": [
        {
          "targetIntervalSeconds": integer,
          "storage": ["SEQUENTIAL"|"LATEST", ...]
        }
        ...
      ]
    }
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

**Example 1: To start a composition with default layout settings**

The following `start-composition` example starts a composition for the specified stage to be streamed to the specified locations.

```
aws ivs-realtime start-composition \
    --stage-arn arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd \
    --destinations '[{"channel": {"channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", \
        "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"}}, \
        {"s3":{"encoderConfigurationArns":["arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"], \
        "recordingConfiguration": {"hlsConfiguration": {"targetSegmentDurationSeconds": 5}}, \
        "storageConfigurationArn":"arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE"}}]'
```

Output:

```
{
    "composition": {
        "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh",
        "destinations": [
            {
                "configuration": {
                    "channel": {
                        "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg",
                        "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"
                    },
                    "name": ""
                },
                "id": "AabBCcdDEefF",
                "state": "STARTING"
            },
            {
                "configuration": {
                    "name": "",
                    "s3": {
                        "encoderConfigurationArns": [
                            "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"
                        ],
                        "recordingConfiguration": {
                            "format": "HLS",
                            "hlsConfiguration": {
                                "targetSegmentDurationSeconds": 5
                            }
                        },
                        "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE"
                    }
                },
                "detail": {
                    "s3": {
                        "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite"
                    }
                },
                "id": "GHFabcgefABC",
                "state": "STARTING"
            }
        ],
        "layout": {
            "grid": {
                "featuredParticipantAttribute": ""
                "gridGap": 2,
                "omitStoppedVideo": false,
                "videoAspectRatio": "VIDEO",
                "videoFillMode": ""
            }
        },
        "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd",
        "startTime": "2023-10-16T23:24:00+00:00",
        "state": "STARTING",
        "tags": {}
    }
}
```

For more information, see [IVS Composite Recording | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html) in the *Amazon IVS Real-Time Streaming User Guide*.

**Example 2: To start a composition with PiP layout**

The following `start-composition` example starts a composition for the specified stage to be streamed to the specified locations using PiP layout.

```
aws ivs-realtime start-composition \
    --stage-arn arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd \
    --destinations '[{"channel": {"channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", \
        "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"}}, \
        {"s3":{"encoderConfigurationArns":["arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"], \
        "storageConfigurationArn":"arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE"}}]' \
    --layout pip='{featuredParticipantAttribute="abcdefg"}'
```

Output:

```
{
    "composition": {
        "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/wxyzWXYZpqrs",
        "destinations": [
            {
                "configuration": {
                    "channel": {
                        "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg",
                        "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"
                    },
                    "name": ""
                },
                "id": "AabBCcdDEefF",
                "state": "STARTING"
            },
            {
                "configuration": {
                    "name": "",
                    "s3": {
                        "encoderConfigurationArns": [
                            "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"
                        ],
                        "recordingConfiguration": {
                            "format": "HLS",
                            "hlsConfiguration": {
                                "targetSegmentDurationSeconds": 2
                            }
                        },
                        "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE"
                    }
                },
                "detail": {
                    "s3": {
                        "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite"
                    }
                },
                "id": "GHFabcgefABC",
                "state": "STARTING"
            }
        ],
        "layout": {
            "pip": {
                "featuredParticipantAttribute": "abcdefg",
                "gridGap": 0,
                "omitStoppedVideo": false,
                "pipBehavior": "STATIC",
                "pipOffset": 0,
                "pipParticipantAttribute": "",
                "pipPosition": "BOTTOM_RIGHT",
                "videoFillMode": "COVER"
            }
        },
        "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd",
        "startTime": "2023-10-16T23:24:00+00:00",
        "state": "STARTING",
        "tags": {}
    }
}
```

For more information, see [IVS Composite Recording | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html) in the *Amazon IVS Real-Time Streaming User Guide*.

**Example 3: To start a composition with thumbnail recording enabled**

The following `start-composition` example starts a composition for the specified stage to be streamed to the specified locations with thumbnail recording enabled.

```
aws ivs-realtime start-composition \
    --stage-arn arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd \
    --destinations '[{"channel": {"channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", \
        "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"}}, \
        {"s3": {"encoderConfigurationArns": ["arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"], \
        "storageConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE", \
        "thumbnailConfigurations": [{"storage": ["SEQUENTIAL"],"targetIntervalSeconds": 60}]}}]'
```

Output:

```
{
    "composition": {
        "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh",
        "destinations": [
            {
                "configuration": {
                    "channel": {
                        "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg",
                        "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"
                    },
                    "name": ""
                },
                "id": "AabBCcdDEefF",
                "state": "STARTING"
            },
            {
                "configuration": {
                    "name": "",
                    "s3": {
                        "encoderConfigurationArns": [
                            "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"
                        ],
                        "recordingConfiguration": {
                            "format": "HLS",
                            "hlsConfiguration": {
                                "targetSegmentDurationSeconds": 2
                            }
                        },
                        "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE",
                        "thumbnailConfigurations": [
                           {
                              "targetIntervalSeconds": 60,
                              "storage": [
                                  "SEQUENTIAL"
                              ]
                           }
                        ]
                    }
                },
                "detail": {
                    "s3": {
                        "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite"
                    }
                },
                "id": "GHFabcgefABC",
                "state": "STARTING"
            }
        ],
        "layout": {
            "grid": {
                "featuredParticipantAttribute": ""
                "gridGap": 2,
                "omitStoppedVideo": false,
                "videoAspectRatio": "VIDEO",
                "videoFillMode": ""
            }
        },
        "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd",
        "startTime": "2023-10-16T23:24:00+00:00",
        "state": "STARTING",
        "tags": {}
    }
}
```

For more information, see [IVS Composite Recording | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html) in the *Amazon IVS Real-Time Streaming User Guide*.

## Output

composition -> (structure)

The Composition that was created.

arn -> (string)

ARN of the Composition resource.

stageArn -> (string)

ARN of the stage used as input

state -> (string)

State of the Composition.

layout -> (structure)

Layout object to configure composition parameters.

grid -> (structure)

Configuration related to grid layout. Default: Grid layout.

featuredParticipantAttribute -> (string)

This attribute name identifies the featured slot. A participant with this attribute set to `"true"` (as a string value) in  ParticipantTokenConfiguration is placed in the featured slot. Default: `""` (no featured participant).

omitStoppedVideo -> (boolean)

Determines whether to omit participants with stopped video in the composition. Default: `false` .

videoAspectRatio -> (string)

Sets the non-featured participant display mode, to control the aspect ratio of video tiles. `VIDEO` is 16:9, `SQUARE` is 1:1, and `PORTRAIT` is 3:4. Default: `VIDEO` .

videoFillMode -> (string)

Defines how video content fits within the participant tile: `FILL` (stretched), `COVER` (cropped), or `CONTAIN` (letterboxed). When not set, `videoFillMode` defaults to `COVER` fill mode for participants in the grid and to `CONTAIN` fill mode for featured participants.

gridGap -> (integer)

Specifies the spacing between participant tiles in pixels. Default: `2` .

pip -> (structure)

Configuration related to PiP layout.

featuredParticipantAttribute -> (string)

This attribute name identifies the featured slot. A participant with this attribute set to `"true"` (as a string value) in  ParticipantTokenConfiguration is placed in the featured slot. Default: `""` (no featured participant).

omitStoppedVideo -> (boolean)

Determines whether to omit participants with stopped video in the composition. Default: `false` .

videoFillMode -> (string)

Defines how video content fits within the participant tile: `FILL` (stretched), `COVER` (cropped), or `CONTAIN` (letterboxed). Default: `COVER` .

gridGap -> (integer)

Specifies the spacing between participant tiles in pixels. Default: `0` .

pipParticipantAttribute -> (string)

Specifies the participant for the PiP window. A participant with this attribute set to `"true"` (as a string value) in  ParticipantTokenConfiguration is placed in the PiP slot. Default: `""` (no PiP participant).

pipBehavior -> (string)

Defines PiP behavior when all participants have left: `STATIC` (maintains original position/size) or `DYNAMIC` (expands to full composition). Default: `STATIC` .

pipOffset -> (integer)

Sets the PiP windowâs offset position in pixels from the closest edges determined by `PipPosition` . Default: `0` .

pipPosition -> (string)

Determines the corner position of the PiP window. Default: `BOTTOM_RIGHT` .

pipWidth -> (integer)

Specifies the width of the PiP window in pixels. When this is not set explicitly, `pipWidth` âs value will be based on the size of the composition and the aspect ratio of the participantâs video.

pipHeight -> (integer)

Specifies the height of the PiP window in pixels. When this is not set explicitly, `pipHeight` âs value will be based on the size of the composition and the aspect ratio of the participantâs video.

destinations -> (list)

Array of Destination objects. A Composition can contain either one destination (`channel` or `s3` ) or two (one `channel` and one `s3` ).

(structure)

Object specifying the status of a Destination.

id -> (string)

Unique identifier for this destination, assigned by IVS.

state -> (string)

State of the Composition Destination.

startTime -> (timestamp)

UTC time of the destination start. This is an ISO 8601 timestamp; *note that this is returned as a string* .

endTime -> (timestamp)

UTC time of the destination end. This is an ISO 8601 timestamp; *note that this is returned as a string* .

configuration -> (structure)

Configuration used to create this destination.

name -> (string)

Name that can be specified to help identify the destination.

channel -> (structure)

An IVS channel to be used for broadcasting, for server-side composition. Either a `channel` or an `s3` must be specified.

channelArn -> (string)

ARN of the channel to use for broadcasting. The channel and stage resources must be in the same AWS account and region. The channel must be offline (not broadcasting).

encoderConfigurationArn -> (string)

ARN of the  EncoderConfiguration resource. The encoder configuration and stage resources must be in the same AWS account and region.

s3 -> (structure)

An S3 storage configuration to be used for recording video data. Either a `channel` or an `s3` must be specified.

storageConfigurationArn -> (string)

ARN of the  StorageConfiguration where recorded videos will be stored.

encoderConfigurationArns -> (list)

ARNs of the  EncoderConfiguration resource. The encoder configuration and stage resources must be in the same AWS account and region.

(string)

recordingConfiguration -> (structure)

Array of maps, each of the form `string:string (key:value)` . This is an optional customer specification, currently used only to specify the recording format for storing a recording in Amazon S3.

hlsConfiguration -> (structure)

An HLS configuration object to return information about how the recording will be configured.

targetSegmentDurationSeconds -> (integer)

Defines the target duration for recorded segments generated when using composite recording. Segments may have durations shorter than the specified value when needed to ensure each segment begins with a keyframe. Default: 2.

format -> (string)

The recording format for storing a recording in Amazon S3.

thumbnailConfigurations -> (list)

A complex type that allows you to enable/disable the recording of thumbnails for a  Composition and modify the interval at which thumbnails are generated for the live session.

(structure)

An object representing a configuration of thumbnails for recorded video for a  Composition .

targetIntervalSeconds -> (integer)

The targeted thumbnail-generation interval in seconds. Default: 60.

storage -> (list)

Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails/(width)x(height) directory, where (width) and (height) are the width and height of the thumbnail. `LATEST` saves the latest thumbnail in media/latest_thumbnail/(width)x(height)/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds` . You can enable both `SEQUENTIAL` and `LATEST` . Default: `SEQUENTIAL` .

(string)

detail -> (structure)

Optional details regarding the status of the destination.

s3 -> (structure)

An S3 detail object to return information about the S3 destination.

recordingPrefix -> (string)

The S3 bucket prefix under which the recording is stored.

tags -> (map)

Tags attached to the resource. Array of maps, each of the form `string:string (key:value)` . See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS has no constraints on tags beyond what is documented there.

key -> (string)

value -> (string)

startTime -> (timestamp)

UTC time of the Composition start. This is an ISO 8601 timestamp; *note that this is returned as a string* .

endTime -> (timestamp)

UTC time of the Composition end. This is an ISO 8601 timestamp; *note that this is returned as a string* .