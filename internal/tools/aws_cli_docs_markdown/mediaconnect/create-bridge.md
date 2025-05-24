# create-bridgeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/create-bridge.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/create-bridge.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/index.html#cli-aws-mediaconnect) ]

# create-bridge

## Description

Creates a new bridge. The request must include one source.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/CreateBridge)

## Synopsis

```
create-bridge
[--egress-gateway-bridge <value>]
[--ingress-gateway-bridge <value>]
--name <value>
[--outputs <value>]
--placement-arn <value>
[--source-failover-config <value>]
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

`--egress-gateway-bridge` (structure)

An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.

MaxBitrate -> (integer)

The maximum expected bitrate (in bps) of the egress bridge.

Shorthand Syntax:

```
MaxBitrate=integer
```

JSON Syntax:

```
{
  "MaxBitrate": integer
}
```

`--ingress-gateway-bridge` (structure)

An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.

MaxBitrate -> (integer)

The maximum expected bitrate (in bps) of the ingress bridge.

MaxOutputs -> (integer)

The maximum number of expected outputs on the ingress bridge.

Shorthand Syntax:

```
MaxBitrate=integer,MaxOutputs=integer
```

JSON Syntax:

```
{
  "MaxBitrate": integer,
  "MaxOutputs": integer
}
```

`--name` (string)

The name of the bridge. This name can not be modified after the bridge is created.

`--outputs` (list)

The outputs that you want to add to this bridge.

(structure)

Add outputs to the specified bridge.

NetworkOutput -> (structure)

The network output of the bridge. A network output is delivered to your premises.

IpAddress -> (string)

The network output IP Address.

Name -> (string)

The network output name. This name is used to reference the output and must be unique among outputs in this bridge.

NetworkName -> (string)

The network outputâs gateway network name.

Port -> (integer)

The network output port.

Protocol -> (string)

The network output protocol.

### Note

Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

Ttl -> (integer)

The network output TTL.

Shorthand Syntax:

```
NetworkOutput={IpAddress=string,Name=string,NetworkName=string,Port=integer,Protocol=string,Ttl=integer} ...
```

JSON Syntax:

```
[
  {
    "NetworkOutput": {
      "IpAddress": "string",
      "Name": "string",
      "NetworkName": "string",
      "Port": integer,
      "Protocol": "zixi-push"|"rtp-fec"|"rtp"|"zixi-pull"|"rist"|"st2110-jpegxs"|"cdi"|"srt-listener"|"srt-caller"|"fujitsu-qos"|"udp"|"ndi-speed-hq",
      "Ttl": integer
    }
  }
  ...
]
```

`--placement-arn` (string)

The bridge placement Amazon Resource Number (ARN).

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

The sources that you want to add to this bridge.

(structure)

Add an output to a bridge.

FlowSource -> (structure)

The source of the flow.

FlowArn -> (string)

The Amazon Resource Number (ARN) of the flow to use as a source of this bridge.

FlowVpcInterfaceAttachment -> (structure)

The name of the VPC interface attachment to use for this source.

VpcInterfaceName -> (string)

The name of the VPC interface to use for this resource.

Name -> (string)

The name of the flow source. This name is used to reference the source and must be unique among sources in this bridge.

NetworkSource -> (structure)

The source of the network.

MulticastIp -> (string)

The network source multicast IP.

MulticastSourceSettings -> (structure)

The settings related to the multicast source.

MulticastSourceIp -> (string)

The IP address of the source for source-specific multicast (SSM).

Name -> (string)

The name of the network source. This name is used to reference the source and must be unique among sources in this bridge.

NetworkName -> (string)

The network sourceâs gateway network name.

Port -> (integer)

The network source port.

Protocol -> (string)

The network source protocol.

### Note

Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

Shorthand Syntax:

```
FlowSource={FlowArn=string,FlowVpcInterfaceAttachment={VpcInterfaceName=string},Name=string},NetworkSource={MulticastIp=string,MulticastSourceSettings={MulticastSourceIp=string},Name=string,NetworkName=string,Port=integer,Protocol=string} ...
```

JSON Syntax:

```
[
  {
    "FlowSource": {
      "FlowArn": "string",
      "FlowVpcInterfaceAttachment": {
        "VpcInterfaceName": "string"
      },
      "Name": "string"
    },
    "NetworkSource": {
      "MulticastIp": "string",
      "MulticastSourceSettings": {
        "MulticastSourceIp": "string"
      },
      "Name": "string",
      "NetworkName": "string",
      "Port": integer,
      "Protocol": "zixi-push"|"rtp-fec"|"rtp"|"zixi-pull"|"rist"|"st2110-jpegxs"|"cdi"|"srt-listener"|"srt-caller"|"fujitsu-qos"|"udp"|"ndi-speed-hq"
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

Bridge -> (structure)

The name of the bridge that was created.

BridgeArn -> (string)

The Amazon Resource Number (ARN) of the bridge.

BridgeMessages -> (list)

Messages with details about the bridge.

(structure)

The details of an error message.

Code -> (string)

The error code.

Message -> (string)

The specific error message that MediaConnect returns to help you understand the reason that the request did not succeed.

ResourceName -> (string)

The name of the resource.

BridgeState -> (string)

The state of the bridge.

EgressGatewayBridge -> (structure)

An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.

InstanceId -> (string)

The ID of the instance running this bridge.

MaxBitrate -> (integer)

The maximum expected bitrate (in bps) of the egress bridge.

IngressGatewayBridge -> (structure)

An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.

InstanceId -> (string)

The ID of the instance running this bridge.

MaxBitrate -> (integer)

The maximum expected bitrate (in bps) of the ingress bridge.

MaxOutputs -> (integer)

The maximum number of outputs on the ingress bridge.

Name -> (string)

The name of the bridge.

Outputs -> (list)

The outputs on this bridge.

(structure)

The output of the bridge.

FlowOutput -> (structure)

The output of the associated flow.

FlowArn -> (string)

The Amazon Resource Number (ARN) of the cloud flow.

FlowSourceArn -> (string)

The Amazon Resource Number (ARN) of the flow source.

Name -> (string)

The name of the bridgeâs output.

NetworkOutput -> (structure)

The network output for the bridge.

IpAddress -> (string)

The network output IP address.

Name -> (string)

The network output name.

NetworkName -> (string)

The network outputâs gateway network name.

Port -> (integer)

The network outputâs port.

Protocol -> (string)

The network output protocol.

### Note

Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

Ttl -> (integer)

The network output TTL.

PlacementArn -> (string)

The placement Amazon Resource Number (ARN) of the bridge.

SourceFailoverConfig -> (structure)

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

Sources -> (list)

The sources on this bridge.

(structure)

The bridgeâs source.

FlowSource -> (structure)

The source of the associated flow.

FlowArn -> (string)

The ARN of the cloud flow used as a source of this bridge.

FlowVpcInterfaceAttachment -> (structure)

The name of the VPC interface attachment to use for this source.

VpcInterfaceName -> (string)

The name of the VPC interface to use for this resource.

Name -> (string)

The name of the flow source.

OutputArn -> (string)

The Amazon Resource Number (ARN) of the output.

NetworkSource -> (structure)

The network source for the bridge.

MulticastIp -> (string)

The network source multicast IP.

MulticastSourceSettings -> (structure)

The settings related to the multicast source.

MulticastSourceIp -> (string)

The IP address of the source for source-specific multicast (SSM).

Name -> (string)

The name of the network source.

NetworkName -> (string)

The network sourceâs gateway network name.

Port -> (integer)

The network source port.

Protocol -> (string)

The network source protocol.

### Note

Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.