# update-inputÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-input.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-input.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# update-input

## Description

Updates an input.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/UpdateInput)

## Synopsis

```
update-input
[--destinations <value>]
[--input-devices <value>]
--input-id <value>
[--input-security-groups <value>]
[--media-connect-flows <value>]
[--name <value>]
[--role-arn <value>]
[--sources <value>]
[--srt-settings <value>]
[--multicast-settings <value>]
[--smpte2110-receiver-group-settings <value>]
[--sdi-sources <value>]
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

`--destinations` (list)
Destination settings for PUSH type inputs.(structure)

Endpoint settings for a PUSH type input.

StreamName -> (string)

A unique name for the location the RTMP stream is being pushed to.

Network -> (string)

If the push input has an input location of ON-PREM, ID the ID of the attached network.

NetworkRoutes -> (list)

If the push input has an input location of ON-PREM itâs a requirement to specify what the route of the input is going to be on the customer local network.

(structure)

A network route configuration.

Cidr -> (string)

The CIDR of the route.

Gateway -> (string)

An optional gateway for the route.

StaticIpAddress -> (string)

If the push input has an input location of ON-PREM itâs optional to specify what the ip address of the input is going to be on the customer local network.

Shorthand Syntax:

```
StreamName=string,Network=string,NetworkRoutes=[{Cidr=string,Gateway=string},{Cidr=string,Gateway=string}],StaticIpAddress=string ...
```

JSON Syntax:

```
[
  {
    "StreamName": "string",
    "Network": "string",
    "NetworkRoutes": [
      {
        "Cidr": "string",
        "Gateway": "string"
      }
      ...
    ],
    "StaticIpAddress": "string"
  }
  ...
]
```

`--input-devices` (list)
Settings for the devices.(structure)

Settings for an input device.

Id -> (string)

The unique ID for the device.

Shorthand Syntax:

```
Id=string ...
```

JSON Syntax:

```
[
  {
    "Id": "string"
  }
  ...
]
```

`--input-id` (string)
Unique ID of the input.

`--input-security-groups` (list)
A list of security groups referenced by IDs to attach to the input.(string)

Placeholder documentation for __string

Syntax:

```
"string" "string" ...
```

`--media-connect-flows` (list)
A list of the MediaConnect Flow ARNs that you want to use as the source of the input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.(structure)

The settings for a MediaConnect Flow.

FlowArn -> (string)

The ARN of the MediaConnect Flow that you want to use as a source.

Shorthand Syntax:

```
FlowArn=string ...
```

JSON Syntax:

```
[
  {
    "FlowArn": "string"
  }
  ...
]
```

`--name` (string)
Name of the input.

`--role-arn` (string)
The Amazon Resource Name (ARN) of the role this input assumes during and after creation.

`--sources` (list)
The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.(structure)

Settings for for a PULL type input.

PasswordParam -> (string)

The key used to extract the password from EC2 Parameter store.

Url -> (string)

This represents the customerâs source URL where stream is pulled from.

Username -> (string)

The username for the input source.

Shorthand Syntax:

```
PasswordParam=string,Url=string,Username=string ...
```

JSON Syntax:

```
[
  {
    "PasswordParam": "string",
    "Url": "string",
    "Username": "string"
  }
  ...
]
```

`--srt-settings` (structure)
The settings associated with an SRT input.SrtCallerSources -> (list)

Placeholder documentation for __listOfSrtCallerSourceRequest

(structure)

Configures the connection for a source that uses SRT as the connection protocol. In terms of establishing the connection, MediaLive is always the caller and the upstream system is always the listener. In terms of transmission of the source content, MediaLive is always the receiver and the upstream system is always the sender.

Decryption -> (structure)

Complete these parameters only if the content is encrypted.

Algorithm -> (string)

The algorithm used to encrypt content.

PassphraseSecretArn -> (string)

The ARN for the secret in Secrets Manager. Someone in your organization must create a secret and provide you with its ARN. This secret holds the passphrase that MediaLive will use to decrypt the source content.

MinimumLatency -> (integer)

The preferred latency (in milliseconds) for implementing packet loss and recovery. Packet recovery is a key feature of SRT. Obtain this value from the operator at the upstream system.

SrtListenerAddress -> (string)

The IP address at the upstream system (the listener) that MediaLive (the caller) will connect to.

SrtListenerPort -> (string)

The port at the upstream system (the listener) that MediaLive (the caller) will connect to.

StreamId -> (string)

This value is required if the upstream system uses this identifier because without it, the SRT handshake between MediaLive (the caller) and the upstream system (the listener) might fail.

JSON Syntax:

```
{
  "SrtCallerSources": [
    {
      "Decryption": {
        "Algorithm": "AES128"|"AES192"|"AES256",
        "PassphraseSecretArn": "string"
      },
      "MinimumLatency": integer,
      "SrtListenerAddress": "string",
      "SrtListenerPort": "string",
      "StreamId": "string"
    }
    ...
  ]
}
```

`--multicast-settings` (structure)
Multicast Input settings.Sources -> (list)

Placeholder documentation for __listOfMulticastSourceUpdateRequest

(structure)

Pair of multicast url and source ip address (optional) that make up a multicast source.

SourceIp -> (string)

This represents the ip address of the device sending the multicast stream.

Url -> (string)

This represents the customerâs source URL where multicast stream is pulled from.

Shorthand Syntax:

```
Sources=[{SourceIp=string,Url=string},{SourceIp=string,Url=string}]
```

JSON Syntax:

```
{
  "Sources": [
    {
      "SourceIp": "string",
      "Url": "string"
    }
    ...
  ]
}
```

`--smpte2110-receiver-group-settings` (structure)
Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input.Smpte2110ReceiverGroups -> (list)

Placeholder documentation for __listOfSmpte2110ReceiverGroup

(structure)

A receiver group is a collection of video, audio, and ancillary streams that you want to group together and attach to one input.

SdpSettings -> (structure)

The single Smpte2110ReceiverGroupSdpSettings that identify the video, audio, and ancillary streams for this receiver group.

AncillarySdps -> (list)

A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one ancillary SMPTE 2110 stream. Each stream encapsulates one captions stream (out of any number you can include) or the single SCTE 35 stream that you can include.

(structure)

The location of the SDP file for one of the SMPTE 2110 streams in a receiver group.

MediaIndex -> (integer)

The index of the media stream in the SDP file for one SMPTE 2110 stream.

SdpUrl -> (string)

The URL of the SDP file for one SMPTE 2110 stream.

AudioSdps -> (list)

A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one audio SMPTE 2110 stream.

(structure)

The location of the SDP file for one of the SMPTE 2110 streams in a receiver group.

MediaIndex -> (integer)

The index of the media stream in the SDP file for one SMPTE 2110 stream.

SdpUrl -> (string)

The URL of the SDP file for one SMPTE 2110 stream.

VideoSdp -> (structure)

The InputSdpLocation that specifies the SDP file and index for the single video SMPTE 2110 stream for this 2110 input.

MediaIndex -> (integer)

The index of the media stream in the SDP file for one SMPTE 2110 stream.

SdpUrl -> (string)

The URL of the SDP file for one SMPTE 2110 stream.

JSON Syntax:

```
{
  "Smpte2110ReceiverGroups": [
    {
      "SdpSettings": {
        "AncillarySdps": [
          {
            "MediaIndex": integer,
            "SdpUrl": "string"
          }
          ...
        ],
        "AudioSdps": [
          {
            "MediaIndex": integer,
            "SdpUrl": "string"
          }
          ...
        ],
        "VideoSdp": {
          "MediaIndex": integer,
          "SdpUrl": "string"
        }
      }
    }
    ...
  ]
}
```

`--sdi-sources` (list)
SDI Sources for this Input.(string)

Placeholder documentation for __string

Syntax:

```
"string" "string" ...
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

Input -> (structure)

Placeholder documentation for Input

Arn -> (string)

The Unique ARN of the input (generated, immutable).

AttachedChannels -> (list)

A list of channel IDs that that input is attached to (currently an input can only be attached to one channel).

(string)

Placeholder documentation for __string

Destinations -> (list)

A list of the destinations of the input (PUSH-type).

(structure)

The settings for a PUSH type input.

Ip -> (string)

The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input.

Port -> (string)

The port number for the input.

Url -> (string)

This represents the endpoint that the customer stream will be pushed to.

Vpc -> (structure)

The properties for a VPC type input destination.

AvailabilityZone -> (string)

The availability zone of the Input destination.

NetworkInterfaceId -> (string)

The network interface ID of the Input destination in the VPC.

Network -> (string)

The ID of the attached network.

NetworkRoutes -> (list)

If the push input has an input location of ON-PREM itâs a requirement to specify what the route of the input is going to be on the customer local network.

(structure)

A network route configuration.

Cidr -> (string)

The CIDR of the route.

Gateway -> (string)

An optional gateway for the route.

Id -> (string)

The generated ID of the input (unique for user account, immutable).

InputClass -> (string)

STANDARD - MediaLive expects two sources to be connected to this input. If the channel is also STANDARD, both sources will be ingested. If the channel is SINGLE_PIPELINE, only the first source will be ingested; the second source will always be ignored, even if the first source fails. SINGLE_PIPELINE - You can connect only one source to this input. If the ChannelClass is also SINGLE_PIPELINE, this value is valid. If the ChannelClass is STANDARD, this value is not valid because the channel requires two sources in the input.

InputDevices -> (list)

Settings for the input devices.

(structure)

Settings for an input device.

Id -> (string)

The unique ID for the device.

InputPartnerIds -> (list)

A list of IDs for all Inputs which are partners of this one.

(string)

Placeholder documentation for __string

InputSourceType -> (string)

Certain pull input sources can be dynamic, meaning that they can have their URLâs dynamically changes during input switch actions. Presently, this functionality only works with MP4_FILE and TS_FILE inputs.

MediaConnectFlows -> (list)

A list of MediaConnect Flows for this input.

(structure)

The settings for a MediaConnect Flow.

FlowArn -> (string)

The unique ARN of the MediaConnect Flow being used as a source.

Name -> (string)

The user-assigned name (This is a mutable value).

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role this input assumes during and after creation.

SecurityGroups -> (list)

A list of IDs for all the Input Security Groups attached to the input.

(string)

Placeholder documentation for __string

Sources -> (list)

A list of the sources of the input (PULL-type).

(structure)

The settings for a PULL type input.

PasswordParam -> (string)

The key used to extract the password from EC2 Parameter store.

Url -> (string)

This represents the customerâs source URL where stream is pulled from.

Username -> (string)

The username for the input source.

State -> (string)

Placeholder documentation for InputState

Tags -> (map)

A collection of key-value pairs.

key -> (string)

Placeholder documentation for __string

value -> (string)

Placeholder documentation for __string

Type -> (string)

The different types of inputs that AWS Elemental MediaLive supports.

SrtSettings -> (structure)

The settings associated with an SRT input.

SrtCallerSources -> (list)

Placeholder documentation for __listOfSrtCallerSource

(structure)

The configuration for a source that uses SRT as the connection protocol. In terms of establishing the connection, MediaLive is always caller and the upstream system is always the listener. In terms of transmission of the source content, MediaLive is always the receiver and the upstream system is always the sender.

Decryption -> (structure)

The decryption settings for the SRT caller source. Present only if the source has decryption enabled.

Algorithm -> (string)

The algorithm used to encrypt content.

PassphraseSecretArn -> (string)

The ARN for the secret in Secrets Manager. Someone in your organization must create a secret and provide you with its ARN. The secret holds the passphrase that MediaLive uses to decrypt the source content.

MinimumLatency -> (integer)

The preferred latency (in milliseconds) for implementing packet loss and recovery. Packet recovery is a key feature of SRT.

SrtListenerAddress -> (string)

The IP address at the upstream system (the listener) that MediaLive (the caller) connects to.

SrtListenerPort -> (string)

The port at the upstream system (the listener) that MediaLive (the caller) connects to.

StreamId -> (string)

The stream ID, if the upstream system uses this identifier.

InputNetworkLocation -> (string)

The location of this input. AWS, for an input existing in the AWS Cloud, On-Prem for an input in a customer network.

MulticastSettings -> (structure)

Multicast Input settings.

Sources -> (list)

Placeholder documentation for __listOfMulticastSource

(structure)

Pair of multicast url and source ip address (optional) that make up a multicast source.

SourceIp -> (string)

This represents the ip address of the device sending the multicast stream.

Url -> (string)

This represents the customerâs source URL where multicast stream is pulled from.

Smpte2110ReceiverGroupSettings -> (structure)

Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input.

Smpte2110ReceiverGroups -> (list)

Placeholder documentation for __listOfSmpte2110ReceiverGroup

(structure)

A receiver group is a collection of video, audio, and ancillary streams that you want to group together and attach to one input.

SdpSettings -> (structure)

The single Smpte2110ReceiverGroupSdpSettings that identify the video, audio, and ancillary streams for this receiver group.

AncillarySdps -> (list)

A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one ancillary SMPTE 2110 stream. Each stream encapsulates one captions stream (out of any number you can include) or the single SCTE 35 stream that you can include.

(structure)

The location of the SDP file for one of the SMPTE 2110 streams in a receiver group.

MediaIndex -> (integer)

The index of the media stream in the SDP file for one SMPTE 2110 stream.

SdpUrl -> (string)

The URL of the SDP file for one SMPTE 2110 stream.

AudioSdps -> (list)

A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one audio SMPTE 2110 stream.

(structure)

The location of the SDP file for one of the SMPTE 2110 streams in a receiver group.

MediaIndex -> (integer)

The index of the media stream in the SDP file for one SMPTE 2110 stream.

SdpUrl -> (string)

The URL of the SDP file for one SMPTE 2110 stream.

VideoSdp -> (structure)

The InputSdpLocation that specifies the SDP file and index for the single video SMPTE 2110 stream for this 2110 input.

MediaIndex -> (integer)

The index of the media stream in the SDP file for one SMPTE 2110 stream.

SdpUrl -> (string)

The URL of the SDP file for one SMPTE 2110 stream.

SdiSources -> (list)

SDI Sources for this Input.

(string)

Placeholder documentation for __string