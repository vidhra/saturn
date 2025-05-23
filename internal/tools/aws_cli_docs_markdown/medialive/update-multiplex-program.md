# update-multiplex-programÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex-program.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex-program.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# update-multiplex-program

## Description

Update a program in a multiplex.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/UpdateMultiplexProgram)

## Synopsis

```
update-multiplex-program
--multiplex-id <value>
[--multiplex-program-settings <value>]
--program-name <value>
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

`--multiplex-id` (string)
The ID of the multiplex of the program to update.

`--multiplex-program-settings` (structure)
The new settings for a multiplex program.PreferredChannelPipeline -> (string)

Indicates which pipeline is preferred by the multiplex for program ingest.

ProgramNumber -> (integer)

Unique program number.

ServiceDescriptor -> (structure)

Transport stream service descriptor configuration for the Multiplex program.

ProviderName -> (string)

Name of the provider.

ServiceName -> (string)

Name of the service.

VideoSettings -> (structure)

Program video settings configuration.

ConstantBitrate -> (integer)

The constant bitrate configuration for the video encode. When this field is defined, StatmuxSettings must be undefined.

StatmuxSettings -> (structure)

Statmux rate control settings. When this field is defined, ConstantBitrate must be undefined.

MaximumBitrate -> (integer)

Maximum statmux bitrate.

MinimumBitrate -> (integer)

Minimum statmux bitrate.

Priority -> (integer)

The purpose of the priority is to use a combination of thenmultiplex rate control algorithm and the QVBR capability of thenencoder to prioritize the video quality of some channels in anmultiplex over others. Channels that have a higher priority willnget higher video quality at the expense of the video quality ofnother channels in the multiplex with lower priority.

Shorthand Syntax:

```
PreferredChannelPipeline=string,ProgramNumber=integer,ServiceDescriptor={ProviderName=string,ServiceName=string},VideoSettings={ConstantBitrate=integer,StatmuxSettings={MaximumBitrate=integer,MinimumBitrate=integer,Priority=integer}}
```

JSON Syntax:

```
{
  "PreferredChannelPipeline": "CURRENTLY_ACTIVE"|"PIPELINE_0"|"PIPELINE_1",
  "ProgramNumber": integer,
  "ServiceDescriptor": {
    "ProviderName": "string",
    "ServiceName": "string"
  },
  "VideoSettings": {
    "ConstantBitrate": integer,
    "StatmuxSettings": {
      "MaximumBitrate": integer,
      "MinimumBitrate": integer,
      "Priority": integer
    }
  }
}
```

`--program-name` (string)
The name of the program to update.

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

MultiplexProgram -> (structure)

The updated multiplex program.

ChannelId -> (string)

The MediaLive channel associated with the program.

MultiplexProgramSettings -> (structure)

The settings for this multiplex program.

PreferredChannelPipeline -> (string)

Indicates which pipeline is preferred by the multiplex for program ingest.

ProgramNumber -> (integer)

Unique program number.

ServiceDescriptor -> (structure)

Transport stream service descriptor configuration for the Multiplex program.

ProviderName -> (string)

Name of the provider.

ServiceName -> (string)

Name of the service.

VideoSettings -> (structure)

Program video settings configuration.

ConstantBitrate -> (integer)

The constant bitrate configuration for the video encode. When this field is defined, StatmuxSettings must be undefined.

StatmuxSettings -> (structure)

Statmux rate control settings. When this field is defined, ConstantBitrate must be undefined.

MaximumBitrate -> (integer)

Maximum statmux bitrate.

MinimumBitrate -> (integer)

Minimum statmux bitrate.

Priority -> (integer)

The purpose of the priority is to use a combination of thenmultiplex rate control algorithm and the QVBR capability of thenencoder to prioritize the video quality of some channels in anmultiplex over others. Channels that have a higher priority willnget higher video quality at the expense of the video quality ofnother channels in the multiplex with lower priority.

PacketIdentifiersMap -> (structure)

The packet identifier map for this multiplex program.

AudioPids -> (list)

Placeholder documentation for __listOf__integer

(integer)

Placeholder documentation for __integer

DvbSubPids -> (list)

Placeholder documentation for __listOf__integer

(integer)

Placeholder documentation for __integer

DvbTeletextPid -> (integer)

Placeholder documentation for __integer

EtvPlatformPid -> (integer)

Placeholder documentation for __integer

EtvSignalPid -> (integer)

Placeholder documentation for __integer

KlvDataPids -> (list)

Placeholder documentation for __listOf__integer

(integer)

Placeholder documentation for __integer

PcrPid -> (integer)

Placeholder documentation for __integer

PmtPid -> (integer)

Placeholder documentation for __integer

PrivateMetadataPid -> (integer)

Placeholder documentation for __integer

Scte27Pids -> (list)

Placeholder documentation for __listOf__integer

(integer)

Placeholder documentation for __integer

Scte35Pid -> (integer)

Placeholder documentation for __integer

TimedMetadataPid -> (integer)

Placeholder documentation for __integer

VideoPid -> (integer)

Placeholder documentation for __integer

AribCaptionsPid -> (integer)

Placeholder documentation for __integer

DvbTeletextPids -> (list)

Placeholder documentation for __listOf__integer

(integer)

Placeholder documentation for __integer

EcmPid -> (integer)

Placeholder documentation for __integer

Smpte2038Pid -> (integer)

Placeholder documentation for __integer

PipelineDetails -> (list)

Contains information about the current sources for the specified program in the specified multiplex. Keep in mind that each multiplex pipeline connects to both pipelines in a given source channel (the channel identified by the program). But only one of those channel pipelines is ever active at one time.

(structure)

The current source for one of the pipelines in the multiplex.

ActiveChannelPipeline -> (string)

Identifies the channel pipeline that is currently active for the pipeline (identified by PipelineId) in the multiplex.

PipelineId -> (string)

Identifies a specific pipeline in the multiplex.

ProgramName -> (string)

The name of the multiplex program.