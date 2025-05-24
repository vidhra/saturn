# update-flow-outputÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-output.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-output.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/index.html#cli-aws-mediaconnect) ]

# update-flow-output

## Description

Updates an existing flow output.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateFlowOutput)

## Synopsis

```
update-flow-output
[--cidr-allow-list <value>]
[--description <value>]
[--destination <value>]
[--encryption <value>]
--flow-arn <value>
[--max-latency <value>]
[--media-stream-output-configurations <value>]
[--min-latency <value>]
--output-arn <value>
[--port <value>]
[--protocol <value>]
[--remote-id <value>]
[--sender-control-port <value>]
[--sender-ip-address <value>]
[--smoothing-latency <value>]
[--stream-id <value>]
[--vpc-interface-attachment <value>]
[--output-status <value>]
[--ndi-program-name <value>]
[--ndi-speed-hq-quality <value>]
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

`--cidr-allow-list` (list)

The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

(string)

Syntax:

```
"string" "string" ...
```

`--description` (string)

A description of the output. This description appears only on the MediaConnect console and will not be seen by the end user.

`--destination` (string)

The IP address where you want to send the output.

`--encryption` (structure)

The type of key used for the encryption. If no `keyType` is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.

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

Shorthand Syntax:

```
Algorithm=string,ConstantInitializationVector=string,DeviceId=string,KeyType=string,Region=string,ResourceId=string,RoleArn=string,SecretArn=string,Url=string
```

JSON Syntax:

```
{
  "Algorithm": "aes128"|"aes192"|"aes256",
  "ConstantInitializationVector": "string",
  "DeviceId": "string",
  "KeyType": "speke"|"static-key"|"srt-password",
  "Region": "string",
  "ResourceId": "string",
  "RoleArn": "string",
  "SecretArn": "string",
  "Url": "string"
}
```

`--flow-arn` (string)

The Amazon Resource Name (ARN) of the flow that is associated with the output that you want to update.

`--max-latency` (integer)

The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.

`--media-stream-output-configurations` (list)

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

JSON Syntax:

```
[
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
]
```

`--min-latency` (integer)

The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the senderâs minimum latency and the receiverâs minimum latency.

`--output-arn` (string)

The ARN of the output that you want to update.

`--port` (integer)

The port to use when content is distributed to this output.

`--protocol` (string)

The protocol to use for the output.

### Note

Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

Possible values:

- `zixi-push`
- `rtp-fec`
- `rtp`
- `zixi-pull`
- `rist`
- `st2110-jpegxs`
- `cdi`
- `srt-listener`
- `srt-caller`
- `fujitsu-qos`
- `udp`
- `ndi-speed-hq`

`--remote-id` (string)

The remote ID for the Zixi-pull stream.

`--sender-control-port` (integer)

The port that the flow uses to send outbound requests to initiate connection with the sender.

`--sender-ip-address` (string)

The IP address that the flow communicates with to initiate connection with the sender.

`--smoothing-latency` (integer)

The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.

`--stream-id` (string)

The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.

`--vpc-interface-attachment` (structure)

The name of the VPC interface attachment to use for this output.

VpcInterfaceName -> (string)

The name of the VPC interface to use for this resource.

Shorthand Syntax:

```
VpcInterfaceName=string
```

JSON Syntax:

```
{
  "VpcInterfaceName": "string"
}
```

`--output-status` (string)

An indication of whether the output should transmit data or not. If you donât specify the `outputStatus` field in your request, MediaConnect leaves the value unchanged.

Possible values:

- `ENABLED`
- `DISABLED`

`--ndi-program-name` (string)

A suffix for the names of the NDI sources that the flow creates. If a custom name isnât specified, MediaConnect uses the output name.

`--ndi-speed-hq-quality` (integer)

A quality setting for the NDI Speed HQ encoder.

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

**To update an output on a flow**

The following `update-flow-output` example update an output on the specified flow.

```
aws mediaconnect update-flow-output \
    --flow-arn arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame \
    --output-arn arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYC \
    --port 3331
```

Output:

```
{
    "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame",
    "Output": {
        "Name": "NYC",
        "Port": 3331,
        "Description": "NYC stream",
        "Transport": {
            "Protocol": "rtp-fec",
            "SmoothingLatency": 100
        },
        "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYC",
        "Destination": "192.0.2.12"
    }
}
```

For more information, see [Updating Outputs on a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-update.html) in the *AWS Elemental MediaConnect User Guide*.

## Output

FlowArn -> (string)

The ARN of the flow that is associated with the updated output.

Output -> (structure)

The new settings of the output that you updated.

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