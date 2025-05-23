# add-flow-sourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-sources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-sources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/index.html#cli-aws-mediaconnect) ]

# add-flow-sources

## Description

Adds sources to a flow.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/AddFlowSources)

## Synopsis

```
add-flow-sources
--flow-arn <value>
--sources <value>
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

`--flow-arn` (string)

The Amazon Resource Name (ARN) of the flow that you want to update.

`--sources` (list)

A list of sources that you want to add to the flow.

(structure)

The settings for the source of the flow.

Decryption -> (structure)

The type of encryption that is used on the content ingested from this source. Allowable encryption types: static-key.

Algorithm -> (string)

The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).

ConstantInitializationVector -> (string)

A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.

DeviceId -> (string)

The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.

KeyType -> (string)

The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).

Region -> (string)

The Amazon Web Services Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.

ResourceId -> (string)

An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

RoleArn -> (string)

The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).

SecretArn -> (string)

The ARN of the secret that you created in Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.

Url -> (string)

The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

Description -> (string)

A description for the source. This value is not used or seen outside of the current MediaConnect account.

EntitlementArn -> (string)

The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originatorâs flow.

IngestPort -> (integer)

The port that the flow will be listening on for incoming content.

MaxBitrate -> (integer)

The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.

MaxLatency -> (integer)

The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.

MaxSyncBuffer -> (integer)

The size of the buffer (in milliseconds) to use to sync incoming source data.

MediaStreamSourceConfigurations -> (list)

The media streams that are associated with the source, and the parameters for those associations.

(structure)

The media stream that you want to associate with the source, and the parameters for that association.

EncodingName -> (string)

The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.

InputConfigurations -> (list)

The media streams that you want to associate with the source.

(structure)

The transport parameters that you want to associate with an incoming media stream.

InputPort -> (integer)

The port that you want the flow to listen on for an incoming media stream.

Interface -> (structure)

The VPC interface that you want to use for the incoming media stream.

Name -> (string)

The name of the VPC interface.

MediaStreamName -> (string)

The name of the media stream.

MinLatency -> (integer)

The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the senderâs minimum latency and the receiverâs minimum latency.

Name -> (string)

The name of the source.

Protocol -> (string)

The protocol that is used by the source.

### Note

Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

SenderControlPort -> (integer)

The port that the flow uses to send outbound requests to initiate connection with the sender.

SenderIpAddress -> (string)

The IP address that the flow communicates with to initiate connection with the sender.

SourceListenerAddress -> (string)

Source IP or domain name for SRT-caller protocol.

SourceListenerPort -> (integer)

Source port for SRT-caller protocol.

StreamId -> (string)

The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.

VpcInterfaceName -> (string)

The name of the VPC interface to use for this source.

WhitelistCidr -> (string)

The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

GatewayBridgeSource -> (structure)

The source configuration for cloud flows receiving a stream from a bridge.

BridgeArn -> (string)

The ARN of the bridge feeding this flow.

VpcInterfaceAttachment -> (structure)

The name of the VPC interface attachment to use for this bridge source.

VpcInterfaceName -> (string)

The name of the VPC interface to use for this resource.

JSON Syntax:

```
[
  {
    "Decryption": {
      "Algorithm": "aes128"|"aes192"|"aes256",
      "ConstantInitializationVector": "string",
      "DeviceId": "string",
      "KeyType": "speke"|"static-key"|"srt-password",
      "Region": "string",
      "ResourceId": "string",
      "RoleArn": "string",
      "SecretArn": "string",
      "Url": "string"
    },
    "Description": "string",
    "EntitlementArn": "string",
    "IngestPort": integer,
    "MaxBitrate": integer,
    "MaxLatency": integer,
    "MaxSyncBuffer": integer,
    "MediaStreamSourceConfigurations": [
      {
        "EncodingName": "jxsv"|"raw"|"smpte291"|"pcm",
        "InputConfigurations": [
          {
            "InputPort": integer,
            "Interface": {
              "Name": "string"
            }
          }
          ...
        ],
        "MediaStreamName": "string"
      }
      ...
    ],
    "MinLatency": integer,
    "Name": "string",
    "Protocol": "zixi-push"|"rtp-fec"|"rtp"|"zixi-pull"|"rist"|"st2110-jpegxs"|"cdi"|"srt-listener"|"srt-caller"|"fujitsu-qos"|"udp"|"ndi-speed-hq",
    "SenderControlPort": integer,
    "SenderIpAddress": "string",
    "SourceListenerAddress": "string",
    "SourceListenerPort": integer,
    "StreamId": "string",
    "VpcInterfaceName": "string",
    "WhitelistCidr": "string",
    "GatewayBridgeSource": {
      "BridgeArn": "string",
      "VpcInterfaceAttachment": {
        "VpcInterfaceName": "string"
      }
    }
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

FlowArn -> (string)

The ARN of the flow that these sources were added to.

Sources -> (list)

The details of the newly added sources.

(structure)

The settings for the source of the flow.

DataTransferSubscriberFeePercent -> (integer)

Percentage from 0-100 of the data transfer cost to be billed to the subscriber.

Decryption -> (structure)

The type of encryption that is used on the content ingested from this source.

Algorithm -> (string)

The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).

ConstantInitializationVector -> (string)

A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.

DeviceId -> (string)

The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.

KeyType -> (string)

The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).

Region -> (string)

The Amazon Web Services Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.

ResourceId -> (string)

An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

RoleArn -> (string)

The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).

SecretArn -> (string)

The ARN of the secret that you created in Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.

Url -> (string)

The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

Description -> (string)

A description for the source. This value is not used or seen outside of the current MediaConnect account.

EntitlementArn -> (string)

The ARN of the entitlement that allows you to subscribe to content that comes from another Amazon Web Services account. The entitlement is set by the content originator and the ARN is generated as part of the originatorâs flow.

IngestIp -> (string)

The IP address that the flow will be listening on for incoming content.

IngestPort -> (integer)

The port that the flow will be listening on for incoming content.

MediaStreamSourceConfigurations -> (list)

The media streams that are associated with the source, and the parameters for those associations.

(structure)

The media stream that is associated with the source, and the parameters for that association.

EncodingName -> (string)

The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.

InputConfigurations -> (list)

The media streams that you want to associate with the source.

(structure)

The transport parameters that are associated with an incoming media stream.

InputIp -> (string)

The IP address that the flow listens on for incoming content for a media stream.

InputPort -> (integer)

The port that the flow listens on for an incoming media stream.

Interface -> (structure)

The VPC interface where the media stream comes in from.

Name -> (string)

The name of the VPC interface.

MediaStreamName -> (string)

A name that helps you distinguish one media stream from another.

Name -> (string)

The name of the source.

SenderControlPort -> (integer)

The IP address that the flow communicates with to initiate connection with the sender.

SenderIpAddress -> (string)

The port that the flow uses to send outbound requests to initiate connection with the sender.

SourceArn -> (string)

The ARN of the source.

Transport -> (structure)

Attributes related to the transport stream that are used in the source.

CidrAllowList -> (list)

The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16

(string)

MaxBitrate -> (integer)

The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.

MaxLatency -> (integer)

The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.

MaxSyncBuffer -> (integer)

The size of the buffer (in milliseconds) to use to sync incoming source data.

MinLatency -> (integer)

The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the senderâs minimum latency and the receiverâs minimum latency.

Protocol -> (string)

The protocol that is used by the source or output.

### Note

Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

RemoteId -> (string)

The remote ID for the Zixi-pull stream.

SenderControlPort -> (integer)

The port that the flow uses to send outbound requests to initiate connection with the sender.

SenderIpAddress -> (string)

The IP address that the flow communicates with to initiate connection with the sender.

SmoothingLatency -> (integer)

The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.

SourceListenerAddress -> (string)

Source IP or domain name for SRT-caller protocol.

SourceListenerPort -> (integer)

Source port for SRT-caller protocol.

StreamId -> (string)

The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.

NdiSpeedHqQuality -> (integer)

A quality setting for the NDI Speed HQ encoder.

NdiProgramName -> (string)

A suffix for the names of the NDI sources that the flow creates. If a custom name isnât specified, MediaConnect uses the output name.

VpcInterfaceName -> (string)

The name of the VPC interface that is used for this source.

WhitelistCidr -> (string)

The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

GatewayBridgeSource -> (structure)

The source configuration for cloud flows receiving a stream from a bridge.

BridgeArn -> (string)

The ARN of the bridge feeding this flow.

VpcInterfaceAttachment -> (structure)

The name of the VPC interface attachment to use for this bridge source.

VpcInterfaceName -> (string)

The name of the VPC interface to use for this resource.