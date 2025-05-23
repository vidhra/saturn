# create-flowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/create-flow.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/create-flow.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/index.html#cli-aws-mediaconnect) ]

# create-flow

## Description

Creates a new flow. The request must include one source. The request optionally can include outputs (up to 50) and entitlements (up to 50).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/CreateFlow)

## Synopsis

```
create-flow
[--availability-zone <value>]
[--entitlements <value>]
[--media-streams <value>]
--name <value>
[--outputs <value>]
[--source <value>]
[--source-failover-config <value>]
[--sources <value>]
[--vpc-interfaces <value>]
[--maintenance <value>]
[--source-monitoring-config <value>]
[--flow-size <value>]
[--ndi-config <value>]
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

`--availability-zone` (string)

The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current Amazon Web Services Region.

`--entitlements` (list)

The entitlements that you want to grant on a flow.

(structure)

The entitlements that you want to grant on a flow.

DataTransferSubscriberFeePercent -> (integer)

Percentage from 0-100 of the data transfer cost to be billed to the subscriber.

Description -> (string)

A description of the entitlement. This description appears only on the MediaConnect console and will not be seen by the subscriber or end user.

Encryption -> (structure)

The type of encryption that will be used on the output that is associated with this entitlement. Allowable encryption types: static-key, speke.

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

EntitlementStatus -> (string)

An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you donât specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.

Name -> (string)

The name of the entitlement. This value must be unique within the current flow.

Subscribers -> (list)

The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.

(string)

Shorthand Syntax:

```
DataTransferSubscriberFeePercent=integer,Description=string,Encryption={Algorithm=string,ConstantInitializationVector=string,DeviceId=string,KeyType=string,Region=string,ResourceId=string,RoleArn=string,SecretArn=string,Url=string},EntitlementStatus=string,Name=string,Subscribers=string,string ...
```

JSON Syntax:

```
[
  {
    "DataTransferSubscriberFeePercent": integer,
    "Description": "string",
    "Encryption": {
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
    "EntitlementStatus": "ENABLED"|"DISABLED",
    "Name": "string",
    "Subscribers": ["string", ...]
  }
  ...
]
```

`--media-streams` (list)

The media streams that you want to add to the flow. You can associate these media streams with sources and outputs on the flow.

(structure)

The media stream that you want to add to the flow.

Attributes -> (structure)

The attributes that you want to assign to the new media stream.

Fmtp -> (structure)

The settings that you want to use to define the media stream.

ChannelOrder -> (string)

The format of the audio channel.

Colorimetry -> (string)

The format that is used for the representation of color.

ExactFramerate -> (string)

The frame rate for the video stream, in frames/second. For example: 60000/1001. If you specify a whole number, MediaConnect uses a ratio of N/1. For example, if you specify 60, MediaConnect uses 60/1 as the `exactFramerate` .

Par -> (string)

The pixel aspect ratio (PAR) of the video.

Range -> (string)

The encoding range of the video.

ScanMode -> (string)

The type of compression that was used to smooth the videoâs appearance.

Tcs -> (string)

The transfer characteristic system (TCS) that is used in the video.

Lang -> (string)

The audio language, in a format that is recognized by the receiver.

ClockRate -> (integer)

The sample rate (in Hz) for the stream. If the media stream type is video or ancillary data, set this value to 90000. If the media stream type is audio, set this value to either 48000 or 96000.

Description -> (string)

A description that can help you quickly identify what your media stream is used for.

MediaStreamId -> (integer)

A unique identifier for the media stream.

MediaStreamName -> (string)

A name that helps you distinguish one media stream from another.

MediaStreamType -> (string)

The type of media stream.

VideoFormat -> (string)

The resolution of the video.

Shorthand Syntax:

```
Attributes={Fmtp={ChannelOrder=string,Colorimetry=string,ExactFramerate=string,Par=string,Range=string,ScanMode=string,Tcs=string},Lang=string},ClockRate=integer,Description=string,MediaStreamId=integer,MediaStreamName=string,MediaStreamType=string,VideoFormat=string ...
```

JSON Syntax:

```
[
  {
    "Attributes": {
      "Fmtp": {
        "ChannelOrder": "string",
        "Colorimetry": "BT601"|"BT709"|"BT2020"|"BT2100"|"ST2065-1"|"ST2065-3"|"XYZ",
        "ExactFramerate": "string",
        "Par": "string",
        "Range": "NARROW"|"FULL"|"FULLPROTECT",
        "ScanMode": "progressive"|"interlace"|"progressive-segmented-frame",
        "Tcs": "SDR"|"PQ"|"HLG"|"LINEAR"|"BT2100LINPQ"|"BT2100LINHLG"|"ST2065-1"|"ST428-1"|"DENSITY"
      },
      "Lang": "string"
    },
    "ClockRate": integer,
    "Description": "string",
    "MediaStreamId": integer,
    "MediaStreamName": "string",
    "MediaStreamType": "video"|"audio"|"ancillary-data",
    "VideoFormat": "string"
  }
  ...
]
```

`--name` (string)

The name of the flow.

`--outputs` (list)

The outputs that you want to add to this flow.

(structure)

A request to add an output to a flow.

CidrAllowList -> (list)

The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

(string)

Description -> (string)

A description of the output. This description appears only on the Audit Manager console and will not be seen by the end user.

Destination -> (string)

The IP address from which video will be sent to output destinations.

Encryption -> (structure)

The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.

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

MaxLatency -> (integer)

The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.

MediaStreamOutputConfigurations -> (list)

The media streams that are associated with the output, and the parameters for those associations.

(structure)

The media stream that you want to associate with the output, and the parameters for that association.

DestinationConfigurations -> (list)

The media streams that you want to associate with the output.

(structure)

The definition of a media stream that you want to associate with the output.

DestinationIp -> (string)

The IP address where you want MediaConnect to send contents of the media stream.

DestinationPort -> (integer)

The port that you want MediaConnect to use when it distributes the media stream to the output.

Interface -> (structure)

The VPC interface that you want to use for the media stream associated with the output.

Name -> (string)

The name of the VPC interface.

EncodingName -> (string)

The format that will be used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.

EncodingParameters -> (structure)

A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source.

CompressionFactor -> (double)

A value that is used to calculate compression for an output. The bitrate of the output is calculated as follows: Output bitrate = (1 / compressionFactor) * (source bitrate) This property only applies to outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol. Valid values are floating point numbers in the range of 3.0 to 10.0, inclusive.

EncoderProfile -> (string)

A setting on the encoder that drives compression settings. This property only applies to video media streams associated with outputs that use the ST 2110 JPEG XS protocol, if at least one source on the flow uses the CDI protocol.

MediaStreamName -> (string)

The name of the media stream that is associated with the output.

MinLatency -> (integer)

The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the senderâs minimum latency and the receiverâs minimum latency.

Name -> (string)

The name of the output. This value must be unique within the current flow.

Port -> (integer)

The port to use when content is distributed to this output.

Protocol -> (string)

The protocol to use for the output.

### Note

Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

RemoteId -> (string)

The remote ID for the Zixi-pull output stream.

SenderControlPort -> (integer)

The port that the flow uses to send outbound requests to initiate connection with the sender.

SmoothingLatency -> (integer)

The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.

StreamId -> (string)

The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.

VpcInterfaceAttachment -> (structure)

The name of the VPC interface attachment to use for this output.

VpcInterfaceName -> (string)

The name of the VPC interface to use for this resource.

OutputStatus -> (string)

An indication of whether the new output should be enabled or disabled as soon as it is created. If you donât specify the outputStatus field in your request, MediaConnect sets it to ENABLED.

NdiSpeedHqQuality -> (integer)

A quality setting for the NDI Speed HQ encoder.

NdiProgramName -> (string)

A suffix for the names of the NDI sources that the flow creates. If a custom name isnât specified, MediaConnect uses the output name.

JSON Syntax:

```
[
  {
    "CidrAllowList": ["string", ...],
    "Description": "string",
    "Destination": "string",
    "Encryption": {
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
    "MaxLatency": integer,
    "MediaStreamOutputConfigurations": [
      {
        "DestinationConfigurations": [
          {
            "DestinationIp": "string",
            "DestinationPort": integer,
            "Interface": {
              "Name": "string"
            }
          }
          ...
        ],
        "EncodingName": "jxsv"|"raw"|"smpte291"|"pcm",
        "EncodingParameters": {
          "CompressionFactor": double,
          "EncoderProfile": "main"|"high"
        },
        "MediaStreamName": "string"
      }
      ...
    ],
    "MinLatency": integer,
    "Name": "string",
    "Port": integer,
    "Protocol": "zixi-push"|"rtp-fec"|"rtp"|"zixi-pull"|"rist"|"st2110-jpegxs"|"cdi"|"srt-listener"|"srt-caller"|"fujitsu-qos"|"udp"|"ndi-speed-hq",
    "RemoteId": "string",
    "SenderControlPort": integer,
    "SmoothingLatency": integer,
    "StreamId": "string",
    "VpcInterfaceAttachment": {
      "VpcInterfaceName": "string"
    },
    "OutputStatus": "ENABLED"|"DISABLED",
    "NdiSpeedHqQuality": integer,
    "NdiProgramName": "string"
  }
  ...
]
```

`--source` (structure)

The settings for the source that you want to use for the new flow.

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
```

`--source-failover-config` (structure)

The settings for source failover.

FailoverMode -> (string)

The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.

RecoveryWindow -> (integer)

Search window time to look for dash-7 packets.

SourcePriority -> (structure)

The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.

PrimarySource -> (string)

The name of the source you choose as the primary source for this flow.

State -> (string)

The state of source failover on the flow. If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

Shorthand Syntax:

```
FailoverMode=string,RecoveryWindow=integer,SourcePriority={PrimarySource=string},State=string
```

JSON Syntax:

```
{
  "FailoverMode": "MERGE"|"FAILOVER",
  "RecoveryWindow": integer,
  "SourcePriority": {
    "PrimarySource": "string"
  },
  "State": "ENABLED"|"DISABLED"
}
```

`--sources` (list)

The sources that are assigned to the flow.

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

`--vpc-interfaces` (list)

The VPC interfaces you want on the flow.

(structure)

The details of the VPC interfaces that you want to add to the flow.

Name -> (string)

The name for the VPC interface. This name must be unique within the flow.

NetworkInterfaceType -> (string)

The type of network interface.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.

SecurityGroupIds -> (list)

A virtual firewall to control inbound and outbound traffic.

(string)

SubnetId -> (string)

The subnet IDs that you want to use for your VPC interface. A range of IP addresses in your VPC. When you create your VPC, you specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. When you create a subnet for your VPC, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block. The subnets that you use across all VPC interfaces on the flow must be in the same Availability Zone as the flow.

Shorthand Syntax:

```
Name=string,NetworkInterfaceType=string,RoleArn=string,SecurityGroupIds=string,string,SubnetId=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "NetworkInterfaceType": "ena"|"efa",
    "RoleArn": "string",
    "SecurityGroupIds": ["string", ...],
    "SubnetId": "string"
  }
  ...
]
```

`--maintenance` (structure)

The maintenance settings you want to use for the flow.

MaintenanceDay -> (string)

A day of a week when the maintenance will happen.

MaintenanceStartHour -> (string)

UTC time when the maintenance will happen.

Use 24-hour HH:MM format.

Minutes must be 00.

Example: 13:00.

The default value is 02:00.

Shorthand Syntax:

```
MaintenanceDay=string,MaintenanceStartHour=string
```

JSON Syntax:

```
{
  "MaintenanceDay": "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday"|"Saturday"|"Sunday",
  "MaintenanceStartHour": "string"
}
```

`--source-monitoring-config` (structure)

The settings for source monitoring.

ThumbnailState -> (string)

Indicates whether thumbnails are enabled or disabled.

AudioMonitoringSettings -> (list)

Contains the settings for audio stream metrics monitoring.

(structure)

Specifies the configuration for audio stream metrics monitoring.

SilentAudio -> (structure)

Detects periods of silence.

State -> (string)

Indicates whether the `SilentAudio` metric is enabled or disabled.

ThresholdSeconds -> (integer)

Specifies the number of consecutive seconds of silence that triggers an event or alert.

ContentQualityAnalysisState -> (string)

Indicates whether content quality analysis is enabled or disabled.

VideoMonitoringSettings -> (list)

Contains the settings for video stream metrics monitoring.

(structure)

Specifies the configuration for video stream metrics monitoring.

BlackFrames -> (structure)

Detects video frames that are black.

State -> (string)

Indicates whether the `BlackFrames` metric is enabled or disabled..

ThresholdSeconds -> (integer)

Specifies the number of consecutive seconds of black frames that triggers an event or alert.

FrozenFrames -> (structure)

Detects video frames that have not changed.

State -> (string)

Indicates whether the `FrozenFrames` metric is enabled or disabled.

ThresholdSeconds -> (integer)

Specifies the number of consecutive seconds of a static image that triggers an event or alert.

JSON Syntax:

```
{
  "ThumbnailState": "ENABLED"|"DISABLED",
  "AudioMonitoringSettings": [
    {
      "SilentAudio": {
        "State": "ENABLED"|"DISABLED",
        "ThresholdSeconds": integer
      }
    }
    ...
  ],
  "ContentQualityAnalysisState": "ENABLED"|"DISABLED",
  "VideoMonitoringSettings": [
    {
      "BlackFrames": {
        "State": "ENABLED"|"DISABLED",
        "ThresholdSeconds": integer
      },
      "FrozenFrames": {
        "State": "ENABLED"|"DISABLED",
        "ThresholdSeconds": integer
      }
    }
    ...
  ]
}
```

`--flow-size` (string)

Determines the processing capacity and feature set of the flow. Set this optional parameter to `LARGE` if you want to enable NDI outputs on the flow.

Possible values:

- `MEDIUM`
- `LARGE`

`--ndi-config` (structure)

Specifies the configuration settings for NDI outputs. Required when the flow includes NDI outputs.

NdiState -> (string)

A setting that controls whether NDI outputs can be used in the flow. Must be ENABLED to add NDI outputs. Default is DISABLED.

MachineName -> (string)

A prefix for the names of the NDI sources that the flow creates. If a custom name isnât specified, MediaConnect generates a unique 12-character ID as the prefix.

NdiDiscoveryServers -> (list)

A list of up to three NDI discovery server configurations. While not required by the API, this configuration is necessary for NDI functionality to work properly.

(structure)

Specifies the configuration settings for individual NDI discovery servers. A maximum of 3 servers is allowed.

DiscoveryServerAddress -> (string)

The unique network address of the NDI discovery server.

DiscoveryServerPort -> (integer)

The port for the NDI discovery server. Defaults to 5959 if a custom port isnât specified.

VpcInterfaceAdapter -> (string)

The identifier for the Virtual Private Cloud (VPC) network interface used by the flow.

Shorthand Syntax:

```
NdiState=string,MachineName=string,NdiDiscoveryServers=[{DiscoveryServerAddress=string,DiscoveryServerPort=integer,VpcInterfaceAdapter=string},{DiscoveryServerAddress=string,DiscoveryServerPort=integer,VpcInterfaceAdapter=string}]
```

JSON Syntax:

```
{
  "NdiState": "ENABLED"|"DISABLED",
  "MachineName": "string",
  "NdiDiscoveryServers": [
    {
      "DiscoveryServerAddress": "string",
      "DiscoveryServerPort": integer,
      "VpcInterfaceAdapter": "string"
    }
    ...
  ]
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

**To create a flow**

The following `create-flow` example creates a flow with the specified configuration.

```
aws mediaconnect create-flow \
    --availability-zone us-west-2c \
    --name ExampleFlow \
    --source Description='Example source, backup',IngestPort=1055,Name=BackupSource,Protocol=rtp,WhitelistCidr=10.24.34.0/23
```

Output:

```
{
    "Flow": {
        "FlowArn": "arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:ExampleFlow",
        "AvailabilityZone": "us-west-2c",
        "EgressIp": "54.245.71.21",
        "Source": {
            "IngestPort": 1055,
            "SourceArn": "arn:aws:mediaconnect:us-east-1:123456789012:source:2-3aBC45dEF67hiJ89-c34de5fG678h:BackupSource",
            "Transport": {
                "Protocol": "rtp",
                "MaxBitrate": 80000000
            },
            "Description": "Example source, backup",
            "IngestIp": "54.245.71.21",
            "WhitelistCidr": "10.24.34.0/23",
            "Name": "mySource"
        },
        "Entitlements": [],
        "Name": "ExampleFlow",
        "Outputs": [],
        "Status": "STANDBY",
        "Description": "Example source, backup"
    }
}
```

For more information, see [Creating a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-create.html) in the *AWS Elemental MediaConnect User Guide*.

## Output

Flow -> (structure)

The flow that you created.

AvailabilityZone -> (string)

The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current Amazon Web Services Region.

Description -> (string)

A description of the flow. This value is not used or seen outside of the current MediaConnect account.

EgressIp -> (string)

The IP address from which video will be sent to output destinations.

Entitlements -> (list)

The entitlements in this flow.

(structure)

The settings for a flow entitlement.

DataTransferSubscriberFeePercent -> (integer)

Percentage from 0-100 of the data transfer cost to be billed to the subscriber.

Description -> (string)

A description of the entitlement.

Encryption -> (structure)

The type of encryption that will be used on the output that is associated with this entitlement.

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

EntitlementArn -> (string)

The ARN of the entitlement.

EntitlementStatus -> (string)

An indication of whether the entitlement is enabled.

Name -> (string)

The name of the entitlement.

Subscribers -> (list)

The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.

(string)

FlowArn -> (string)

The Amazon Resource Name (ARN) of the flow.

MediaStreams -> (list)

The media streams that are associated with the flow. After you associate a media stream with a source, you can also associate it with outputs on the flow.

(structure)

A media stream represents one component of your content, such as video, audio, or ancillary data. After you add a media stream to your flow, you can associate it with sources and outputs that use the ST 2110 JPEG XS or CDI protocol.

Attributes -> (structure)

Attributes that are related to the media stream.

Fmtp -> (structure)

The settings that you want to use to define the media stream.

ChannelOrder -> (string)

The format of the audio channel.

Colorimetry -> (string)

The format used for the representation of color.

ExactFramerate -> (string)

The frame rate for the video stream, in frames/second. For example: 60000/1001.

Par -> (string)

The pixel aspect ratio (PAR) of the video.

Range -> (string)

The encoding range of the video.

ScanMode -> (string)

The type of compression that was used to smooth the videoâs appearance.

Tcs -> (string)

The transfer characteristic system (TCS) that is used in the video.

Lang -> (string)

The audio language, in a format that is recognized by the receiver.

ClockRate -> (integer)

The sample rate for the stream. This value is measured in Hz.

Description -> (string)

A description that can help you quickly identify what your media stream is used for.

Fmt -> (integer)

The format type number (sometimes referred to as RTP payload type) of the media stream. MediaConnect assigns this value to the media stream. For ST 2110 JPEG XS outputs, you need to provide this value to the receiver.

MediaStreamId -> (integer)

A unique identifier for the media stream.

MediaStreamName -> (string)

A name that helps you distinguish one media stream from another.

MediaStreamType -> (string)

The type of media stream.

VideoFormat -> (string)

The resolution of the video.

Name -> (string)

The name of the flow.

Outputs -> (list)

The outputs in this flow.

(structure)

The settings for an output.

DataTransferSubscriberFeePercent -> (integer)

Percentage from 0-100 of the data transfer cost to be billed to the subscriber.

Description -> (string)

A description of the output.

Destination -> (string)

The address where you want to send the output.

Encryption -> (structure)

The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).

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

EntitlementArn -> (string)

The ARN of the entitlement on the originatorââs flow. This value is relevant only on entitled flows.

ListenerAddress -> (string)

The IP address that the receiver requires in order to establish a connection with the flow. For public networking, the ListenerAddress is represented by the elastic IP address of the flow. For private networking, the ListenerAddress is represented by the elastic network interface IP address of the VPC. This field applies only to outputs that use the Zixi pull or SRT listener protocol.

MediaLiveInputArn -> (string)

The input ARN of the MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.

MediaStreamOutputConfigurations -> (list)

The configuration for each media stream that is associated with the output.

(structure)

The media stream that is associated with the output, and the parameters for that association.

DestinationConfigurations -> (list)

The transport parameters that are associated with each outbound media stream.

(structure)

The transport parameters that you want to associate with an outbound media stream.

DestinationIp -> (string)

The IP address where you want MediaConnect to send contents of the media stream.

DestinationPort -> (integer)

The port that you want MediaConnect to use when it distributes the media stream to the output.

Interface -> (structure)

The VPC interface that you want to use for the media stream associated with the output.

Name -> (string)

The name of the VPC interface.

OutboundIp -> (string)

The IP address that the receiver requires in order to establish a connection with the flow. This value is represented by the elastic network interface IP address of the VPC. This field applies only to outputs that use the CDI or ST 2110 JPEG XS or protocol.

EncodingName -> (string)

The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.

EncodingParameters -> (structure)

A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source.

CompressionFactor -> (double)

A value that is used to calculate compression for an output. The bitrate of the output is calculated as follows: Output bitrate = (1 / compressionFactor) * (source bitrate) This property only applies to outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol. Valid values are floating point numbers in the range of 3.0 to 10.0, inclusive.

EncoderProfile -> (string)

A setting on the encoder that drives compression settings. This property only applies to video media streams associated with outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol.

MediaStreamName -> (string)

The name of the media stream.

Name -> (string)

The name of the output. This value must be unique within the current flow.

OutputArn -> (string)

The ARN of the output.

Port -> (integer)

The port to use when content is distributed to this output.

Transport -> (structure)

Attributes related to the transport stream that are used in the output.

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

VpcInterfaceAttachment -> (structure)

The name of the VPC interface attachment to use for this output.

VpcInterfaceName -> (string)

The name of the VPC interface to use for this resource.

BridgeArn -> (string)

The ARN of the bridge added to this output.

BridgePorts -> (list)

The bridge output ports currently in use.

(integer)

OutputStatus -> (string)

An indication of whether the output is transmitting data or not.

Source -> (structure)

The source for the flow.

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

SourceFailoverConfig -> (structure)

The settings for the source failover.

FailoverMode -> (string)

The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.

RecoveryWindow -> (integer)

Search window time to look for dash-7 packets.

SourcePriority -> (structure)

The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.

PrimarySource -> (string)

The name of the source you choose as the primary source for this flow.

State -> (string)

The state of source failover on the flow. If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

Sources -> (list)

The settings for the sources that are assigned to the flow.

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

Status -> (string)

The current status of the flow.

VpcInterfaces -> (list)

The VPC Interfaces for this flow.

(structure)

The settings for a VPC source.

Name -> (string)

Immutable and has to be a unique against other VpcInterfaces in this Flow.

NetworkInterfaceIds -> (list)

IDs of the network interfaces created in customerâs account by MediaConnect.

(string)

NetworkInterfaceType -> (string)

The type of network interface.

RoleArn -> (string)

A role Arn MediaConnect can assume to create ENIs in your account.

SecurityGroupIds -> (list)

Security Group IDs to be used on ENI.

(string)

SubnetId -> (string)

Subnet must be in the AZ of the Flow.

Maintenance -> (structure)

The maintenance settings for the flow.

MaintenanceDay -> (string)

A day of a week when the maintenance will happen. Use Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday.

MaintenanceDeadline -> (string)

The Maintenance has to be performed before this deadline in ISO UTC format. Example: 2021-01-30T08:30:00Z.

MaintenanceScheduledDate -> (string)

A scheduled date in ISO UTC format when the maintenance will happen. Use YYYY-MM-DD format. Example: 2021-01-30.

MaintenanceStartHour -> (string)

UTC time when the maintenance will happen. Use 24-hour HH:MM format. Minutes must be 00. Example: 13:00. The default value is 02:00.

SourceMonitoringConfig -> (structure)

The settings for source monitoring.

ThumbnailState -> (string)

Indicates whether thumbnails are enabled or disabled.

AudioMonitoringSettings -> (list)

Contains the settings for audio stream metrics monitoring.

(structure)

Specifies the configuration for audio stream metrics monitoring.

SilentAudio -> (structure)

Detects periods of silence.

State -> (string)

Indicates whether the `SilentAudio` metric is enabled or disabled.

ThresholdSeconds -> (integer)

Specifies the number of consecutive seconds of silence that triggers an event or alert.

ContentQualityAnalysisState -> (string)

Indicates whether content quality analysis is enabled or disabled.

VideoMonitoringSettings -> (list)

Contains the settings for video stream metrics monitoring.

(structure)

Specifies the configuration for video stream metrics monitoring.

BlackFrames -> (structure)

Detects video frames that are black.

State -> (string)

Indicates whether the `BlackFrames` metric is enabled or disabled..

ThresholdSeconds -> (integer)

Specifies the number of consecutive seconds of black frames that triggers an event or alert.

FrozenFrames -> (structure)

Detects video frames that have not changed.

State -> (string)

Indicates whether the `FrozenFrames` metric is enabled or disabled.

ThresholdSeconds -> (integer)

Specifies the number of consecutive seconds of a static image that triggers an event or alert.

FlowSize -> (string)

Determines the processing capacity and feature set of the flow. Set this optional parameter to LARGE if you want to enable NDI outputs on the flow.

NdiConfig -> (structure)

Specifies the configuration settings for NDI outputs. Required when the flow includes NDI outputs.

NdiState -> (string)

A setting that controls whether NDI outputs can be used in the flow. Must be ENABLED to add NDI outputs. Default is DISABLED.

MachineName -> (string)

A prefix for the names of the NDI sources that the flow creates. If a custom name isnât specified, MediaConnect generates a unique 12-character ID as the prefix.

NdiDiscoveryServers -> (list)

A list of up to three NDI discovery server configurations. While not required by the API, this configuration is necessary for NDI functionality to work properly.

(structure)

Specifies the configuration settings for individual NDI discovery servers. A maximum of 3 servers is allowed.

DiscoveryServerAddress -> (string)

The unique network address of the NDI discovery server.

DiscoveryServerPort -> (integer)

The port for the NDI discovery server. Defaults to 5959 if a custom port isnât specified.

VpcInterfaceAdapter -> (string)

The identifier for the Virtual Private Cloud (VPC) network interface used by the flow.