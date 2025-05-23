# create-media-capture-pipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/create-media-capture-pipeline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/create-media-capture-pipeline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-media-pipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/index.html#cli-aws-chime-sdk-media-pipelines) ]

# create-media-capture-pipeline

## Description

Creates a media pipeline.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)

## Synopsis

```
create-media-capture-pipeline
--source-type <value>
--source-arn <value>
--sink-type <value>
--sink-arn <value>
[--client-request-token <value>]
[--chime-sdk-meeting-configuration <value>]
[--sse-aws-key-management-params <value>]
[--sink-iam-role-arn <value>]
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

`--source-type` (string)

Source type from which the media artifacts are captured. A Chime SDK Meeting is the only supported source.

Possible values:

- `ChimeSdkMeeting`

`--source-arn` (string)

ARN of the source from which the media artifacts are captured.

`--sink-type` (string)

Destination type to which the media artifacts are saved. You must use an S3 bucket.

Possible values:

- `S3Bucket`

`--sink-arn` (string)

The ARN of the sink type.

`--client-request-token` (string)

The unique identifier for the client request. The token makes the API request idempotent. Use a unique token for each media pipeline request.

`--chime-sdk-meeting-configuration` (structure)

The configuration for a specified media pipeline. `SourceType` must be `ChimeSdkMeeting` .

SourceConfiguration -> (structure)

The source configuration for a specified media pipeline.

SelectedVideoStreams -> (structure)

The selected video streams for a specified media pipeline. The number of video streams canât exceed 25.

AttendeeIds -> (list)

The attendee IDs of the streams selected for a media pipeline.

(string)

ExternalUserIds -> (list)

The external user IDs of the streams selected for a media pipeline.

(string)

ArtifactsConfiguration -> (structure)

The configuration for the artifacts in an Amazon Chime SDK meeting.

Audio -> (structure)

The configuration for the audio artifacts.

MuxType -> (string)

The MUX type of the audio artifact configuration object.

Video -> (structure)

The configuration for the video artifacts.

State -> (string)

Indicates whether the video artifact is enabled or disabled.

MuxType -> (string)

The MUX type of the video artifact configuration object.

Content -> (structure)

The configuration for the content artifacts.

State -> (string)

Indicates whether the content artifact is enabled or disabled.

MuxType -> (string)

The MUX type of the artifact configuration.

CompositedVideo -> (structure)

Enables video compositing.

Layout -> (string)

The layout setting, such as `GridView` in the configuration object.

Resolution -> (string)

The video resolution setting in the configuration object. Default: HD at 1280 x 720. FHD resolution: 1920 x 1080.

GridViewConfiguration -> (structure)

The `GridView` configuration setting.

ContentShareLayout -> (string)

Defines the layout of the video tiles when content sharing is enabled.

PresenterOnlyConfiguration -> (structure)

Defines the configuration options for a presenter only video tile.

PresenterPosition -> (string)

Defines the position of the presenter video tile. Default: `TopRight` .

ActiveSpeakerOnlyConfiguration -> (structure)

The configuration settings for an `ActiveSpeakerOnly` video tile.

ActiveSpeakerPosition -> (string)

The position of the `ActiveSpeakerOnly` video tile.

HorizontalLayoutConfiguration -> (structure)

The configuration settings for a horizontal layout.

TileOrder -> (string)

Sets the automatic ordering of the video tiles.

TilePosition -> (string)

Sets the position of horizontal tiles.

TileCount -> (integer)

The maximum number of video tiles to display.

TileAspectRatio -> (string)

Specifies the aspect ratio of all video tiles.

VerticalLayoutConfiguration -> (structure)

The configuration settings for a vertical layout.

TileOrder -> (string)

Sets the automatic ordering of the video tiles.

TilePosition -> (string)

Sets the position of vertical tiles.

TileCount -> (integer)

The maximum number of tiles to display.

TileAspectRatio -> (string)

Sets the aspect ratio of the video tiles, such as 16:9.

VideoAttribute -> (structure)

The attribute settings for the video tiles.

CornerRadius -> (integer)

Sets the corner radius of all video tiles.

BorderColor -> (string)

Defines the border color of all video tiles.

HighlightColor -> (string)

Defines the highlight color for the active video tile.

BorderThickness -> (integer)

Defines the border thickness for all video tiles.

CanvasOrientation -> (string)

The orientation setting, horizontal or vertical.

JSON Syntax:

```
{
  "SourceConfiguration": {
    "SelectedVideoStreams": {
      "AttendeeIds": ["string", ...],
      "ExternalUserIds": ["string", ...]
    }
  },
  "ArtifactsConfiguration": {
    "Audio": {
      "MuxType": "AudioOnly"|"AudioWithActiveSpeakerVideo"|"AudioWithCompositedVideo"
    },
    "Video": {
      "State": "Enabled"|"Disabled",
      "MuxType": "VideoOnly"
    },
    "Content": {
      "State": "Enabled"|"Disabled",
      "MuxType": "ContentOnly"
    },
    "CompositedVideo": {
      "Layout": "GridView",
      "Resolution": "HD"|"FHD",
      "GridViewConfiguration": {
        "ContentShareLayout": "PresenterOnly"|"Horizontal"|"Vertical"|"ActiveSpeakerOnly",
        "PresenterOnlyConfiguration": {
          "PresenterPosition": "TopLeft"|"TopRight"|"BottomLeft"|"BottomRight"
        },
        "ActiveSpeakerOnlyConfiguration": {
          "ActiveSpeakerPosition": "TopLeft"|"TopRight"|"BottomLeft"|"BottomRight"
        },
        "HorizontalLayoutConfiguration": {
          "TileOrder": "JoinSequence"|"SpeakerSequence",
          "TilePosition": "Top"|"Bottom",
          "TileCount": integer,
          "TileAspectRatio": "string"
        },
        "VerticalLayoutConfiguration": {
          "TileOrder": "JoinSequence"|"SpeakerSequence",
          "TilePosition": "Left"|"Right",
          "TileCount": integer,
          "TileAspectRatio": "string"
        },
        "VideoAttribute": {
          "CornerRadius": integer,
          "BorderColor": "Black"|"Blue"|"Red"|"Green"|"White"|"Yellow",
          "HighlightColor": "Black"|"Blue"|"Red"|"Green"|"White"|"Yellow",
          "BorderThickness": integer
        },
        "CanvasOrientation": "Landscape"|"Portrait"
      }
    }
  }
}
```

`--sse-aws-key-management-params` (structure)

An object that contains server side encryption parameters to be used by media capture pipeline. The parameters can also be used by media concatenation pipeline taking media capture pipeline as a media source.

AwsKmsKeyId -> (string)

The KMS key you want to use to encrypt your media pipeline output. Decryption is required for concatenation pipeline. If using a key located in the current Amazon Web Services account, you can specify your KMS key in one of four ways:

- Use the KMS key ID itself. For example, `1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use an alias for the KMS key ID. For example, `alias/ExampleAlias` .
- Use the Amazon Resource Name (ARN) for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias` .

If using a key located in a different Amazon Web Services account than the current Amazon Web Services account, you can specify your KMS key in one of two ways:

- Use the ARN for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias` .

If you donât specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).

Note that the role specified in the `SinkIamRoleArn` request parameter must have permission to use the specified KMS key.

AwsKmsEncryptionContext -> (string)

Base64-encoded string of a UTF-8 encoded JSON, which contains the encryption context as non-secret key-value pair known as encryption context pairs, that provides an added layer of security for your data. For more information, see [KMS encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) and [Asymmetric keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Key Management Service Developer Guide* .

Shorthand Syntax:

```
AwsKmsKeyId=string,AwsKmsEncryptionContext=string
```

JSON Syntax:

```
{
  "AwsKmsKeyId": "string",
  "AwsKmsEncryptionContext": "string"
}
```

`--sink-iam-role-arn` (string)

The Amazon Resource Name (ARN) of the sink role to be used with `AwsKmsKeyId` in `SseAwsKeyManagementParams` . Can only interact with `S3Bucket` sink type. The role must belong to the callerâs account and be able to act on behalf of the caller during the API call. All minimum policy permissions requirements for the caller to perform sink-related actions are the same for `SinkIamRoleArn` .

Additionally, the role must have permission to `kms:GenerateDataKey` using KMS key supplied as `AwsKmsKeyId` in `SseAwsKeyManagementParams` . If media concatenation will be required later, the role must also have permission to `kms:Decrypt` for the same KMS key.

`--tags` (list)

The tag key-value pairs.

(structure)

A key/value pair that grants users access to meeting resources.

Key -> (string)

The key half of a tag.

Value -> (string)

The value half of a tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

MediaCapturePipeline -> (structure)

A media pipeline object, the ID, source type, source ARN, sink type, and sink ARN of a media pipeline object.

MediaPipelineId -> (string)

The ID of a media pipeline.

MediaPipelineArn -> (string)

The ARN of the media capture pipeline

SourceType -> (string)

Source type from which media artifacts are saved. You must use `ChimeMeeting` .

SourceArn -> (string)

ARN of the source from which the media artifacts are saved.

Status -> (string)

The status of the media pipeline.

SinkType -> (string)

Destination type to which the media artifacts are saved. You must use an S3 Bucket.

SinkArn -> (string)

ARN of the destination to which the media artifacts are saved.

CreatedTimestamp -> (timestamp)

The time at which the pipeline was created, in ISO 8601 format.

UpdatedTimestamp -> (timestamp)

The time at which the pipeline was updated, in ISO 8601 format.

ChimeSdkMeetingConfiguration -> (structure)

The configuration for a specified media pipeline. `SourceType` must be `ChimeSdkMeeting` .

SourceConfiguration -> (structure)

The source configuration for a specified media pipeline.

SelectedVideoStreams -> (structure)

The selected video streams for a specified media pipeline. The number of video streams canât exceed 25.

AttendeeIds -> (list)

The attendee IDs of the streams selected for a media pipeline.

(string)

ExternalUserIds -> (list)

The external user IDs of the streams selected for a media pipeline.

(string)

ArtifactsConfiguration -> (structure)

The configuration for the artifacts in an Amazon Chime SDK meeting.

Audio -> (structure)

The configuration for the audio artifacts.

MuxType -> (string)

The MUX type of the audio artifact configuration object.

Video -> (structure)

The configuration for the video artifacts.

State -> (string)

Indicates whether the video artifact is enabled or disabled.

MuxType -> (string)

The MUX type of the video artifact configuration object.

Content -> (structure)

The configuration for the content artifacts.

State -> (string)

Indicates whether the content artifact is enabled or disabled.

MuxType -> (string)

The MUX type of the artifact configuration.

CompositedVideo -> (structure)

Enables video compositing.

Layout -> (string)

The layout setting, such as `GridView` in the configuration object.

Resolution -> (string)

The video resolution setting in the configuration object. Default: HD at 1280 x 720. FHD resolution: 1920 x 1080.

GridViewConfiguration -> (structure)

The `GridView` configuration setting.

ContentShareLayout -> (string)

Defines the layout of the video tiles when content sharing is enabled.

PresenterOnlyConfiguration -> (structure)

Defines the configuration options for a presenter only video tile.

PresenterPosition -> (string)

Defines the position of the presenter video tile. Default: `TopRight` .

ActiveSpeakerOnlyConfiguration -> (structure)

The configuration settings for an `ActiveSpeakerOnly` video tile.

ActiveSpeakerPosition -> (string)

The position of the `ActiveSpeakerOnly` video tile.

HorizontalLayoutConfiguration -> (structure)

The configuration settings for a horizontal layout.

TileOrder -> (string)

Sets the automatic ordering of the video tiles.

TilePosition -> (string)

Sets the position of horizontal tiles.

TileCount -> (integer)

The maximum number of video tiles to display.

TileAspectRatio -> (string)

Specifies the aspect ratio of all video tiles.

VerticalLayoutConfiguration -> (structure)

The configuration settings for a vertical layout.

TileOrder -> (string)

Sets the automatic ordering of the video tiles.

TilePosition -> (string)

Sets the position of vertical tiles.

TileCount -> (integer)

The maximum number of tiles to display.

TileAspectRatio -> (string)

Sets the aspect ratio of the video tiles, such as 16:9.

VideoAttribute -> (structure)

The attribute settings for the video tiles.

CornerRadius -> (integer)

Sets the corner radius of all video tiles.

BorderColor -> (string)

Defines the border color of all video tiles.

HighlightColor -> (string)

Defines the highlight color for the active video tile.

BorderThickness -> (integer)

Defines the border thickness for all video tiles.

CanvasOrientation -> (string)

The orientation setting, horizontal or vertical.

SseAwsKeyManagementParams -> (structure)

An object that contains server side encryption parameters to be used by media capture pipeline. The parameters can also be used by media concatenation pipeline taking media capture pipeline as a media source.

AwsKmsKeyId -> (string)

The KMS key you want to use to encrypt your media pipeline output. Decryption is required for concatenation pipeline. If using a key located in the current Amazon Web Services account, you can specify your KMS key in one of four ways:

- Use the KMS key ID itself. For example, `1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use an alias for the KMS key ID. For example, `alias/ExampleAlias` .
- Use the Amazon Resource Name (ARN) for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias` .

If using a key located in a different Amazon Web Services account than the current Amazon Web Services account, you can specify your KMS key in one of two ways:

- Use the ARN for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias` .

If you donât specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).

Note that the role specified in the `SinkIamRoleArn` request parameter must have permission to use the specified KMS key.

AwsKmsEncryptionContext -> (string)

Base64-encoded string of a UTF-8 encoded JSON, which contains the encryption context as non-secret key-value pair known as encryption context pairs, that provides an added layer of security for your data. For more information, see [KMS encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) and [Asymmetric keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Key Management Service Developer Guide* .

SinkIamRoleArn -> (string)

The Amazon Resource Name (ARN) of the sink role to be used with `AwsKmsKeyId` in `SseAwsKeyManagementParams` .