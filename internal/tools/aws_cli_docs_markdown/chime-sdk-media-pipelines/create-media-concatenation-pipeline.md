# create-media-concatenation-pipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/create-media-concatenation-pipeline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/create-media-concatenation-pipeline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-media-pipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/index.html#cli-aws-chime-sdk-media-pipelines) ]

# create-media-concatenation-pipeline

## Description

Creates a media concatenation pipeline.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)

## Synopsis

```
create-media-concatenation-pipeline
--sources <value>
--sinks <value>
[--client-request-token <value>]
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

`--sources` (list)

An object that specifies the sources for the media concatenation pipeline.

(structure)

The source type and media pipeline configuration settings in a configuration object.

Type -> (string)

The type of concatenation source in a configuration object.

MediaCapturePipelineSourceConfiguration -> (structure)

The concatenation settings for the media pipeline in a configuration object.

MediaPipelineArn -> (string)

The media pipeline ARN in the configuration object of a media capture pipeline.

ChimeSdkMeetingConfiguration -> (structure)

The meeting configuration settings in a media capture pipeline configuration object.

ArtifactsConfiguration -> (structure)

The configuration for the artifacts in an Amazon Chime SDK meeting concatenation.

Audio -> (structure)

The configuration for the audio artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

Video -> (structure)

The configuration for the video artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

Content -> (structure)

The configuration for the content artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

DataChannel -> (structure)

The configuration for the data channel artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

TranscriptionMessages -> (structure)

The configuration for the transcription messages artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

MeetingEvents -> (structure)

The configuration for the meeting events artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

CompositedVideo -> (structure)

The configuration for the composited video artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

JSON Syntax:

```
[
  {
    "Type": "MediaCapturePipeline",
    "MediaCapturePipelineSourceConfiguration": {
      "MediaPipelineArn": "string",
      "ChimeSdkMeetingConfiguration": {
        "ArtifactsConfiguration": {
          "Audio": {
            "State": "Enabled"
          },
          "Video": {
            "State": "Enabled"|"Disabled"
          },
          "Content": {
            "State": "Enabled"|"Disabled"
          },
          "DataChannel": {
            "State": "Enabled"|"Disabled"
          },
          "TranscriptionMessages": {
            "State": "Enabled"|"Disabled"
          },
          "MeetingEvents": {
            "State": "Enabled"|"Disabled"
          },
          "CompositedVideo": {
            "State": "Enabled"|"Disabled"
          }
        }
      }
    }
  }
  ...
]
```

`--sinks` (list)

An object that specifies the data sinks for the media concatenation pipeline.

(structure)

The data sink of the configuration object.

Type -> (string)

The type of data sink in the configuration object.

S3BucketSinkConfiguration -> (structure)

The configuration settings for an Amazon S3 bucket sink.

Destination -> (string)

The destination URL of the S3 bucket.

Shorthand Syntax:

```
Type=string,S3BucketSinkConfiguration={Destination=string} ...
```

JSON Syntax:

```
[
  {
    "Type": "S3Bucket",
    "S3BucketSinkConfiguration": {
      "Destination": "string"
    }
  }
  ...
]
```

`--client-request-token` (string)

The unique identifier for the client request. The token makes the API request idempotent. Use a unique token for each media concatenation pipeline request.

`--tags` (list)

The tags associated with the media concatenation pipeline.

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

MediaConcatenationPipeline -> (structure)

A media concatenation pipeline object, the ID, source type, `MediaPipelineARN` , and sink of a media concatenation pipeline object.

MediaPipelineId -> (string)

The ID of the media pipeline being concatenated.

MediaPipelineArn -> (string)

The ARN of the media pipeline that you specify in the `SourceConfiguration` object.

Sources -> (list)

The data sources being concatenated.

(structure)

The source type and media pipeline configuration settings in a configuration object.

Type -> (string)

The type of concatenation source in a configuration object.

MediaCapturePipelineSourceConfiguration -> (structure)

The concatenation settings for the media pipeline in a configuration object.

MediaPipelineArn -> (string)

The media pipeline ARN in the configuration object of a media capture pipeline.

ChimeSdkMeetingConfiguration -> (structure)

The meeting configuration settings in a media capture pipeline configuration object.

ArtifactsConfiguration -> (structure)

The configuration for the artifacts in an Amazon Chime SDK meeting concatenation.

Audio -> (structure)

The configuration for the audio artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

Video -> (structure)

The configuration for the video artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

Content -> (structure)

The configuration for the content artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

DataChannel -> (structure)

The configuration for the data channel artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

TranscriptionMessages -> (structure)

The configuration for the transcription messages artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

MeetingEvents -> (structure)

The configuration for the meeting events artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

CompositedVideo -> (structure)

The configuration for the composited video artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

Sinks -> (list)

The data sinks of the concatenation pipeline.

(structure)

The data sink of the configuration object.

Type -> (string)

The type of data sink in the configuration object.

S3BucketSinkConfiguration -> (structure)

The configuration settings for an Amazon S3 bucket sink.

Destination -> (string)

The destination URL of the S3 bucket.

Status -> (string)

The status of the concatenation pipeline.

CreatedTimestamp -> (timestamp)

The time at which the concatenation pipeline was created.

UpdatedTimestamp -> (timestamp)

The time at which the concatenation pipeline was last updated.