# create-probeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/create-probe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/create-probe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/index.html#cli-aws-networkmonitor) ]

# create-probe

## Description

Create a probe within a monitor. Once you create a probe, and it begins monitoring your network traffic, youâll incur billing charges for that probe. This action requires the `monitorName` parameter. Run `ListMonitors` to get a list of monitor names. Note the name of the `monitorName` you want to create the probe for.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkmonitor-2023-08-01/CreateProbe)

## Synopsis

```
create-probe
--monitor-name <value>
--probe <value>
[--client-token <value>]
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

`--monitor-name` (string)

The name of the monitor to associated with the probe.

`--probe` (structure)

Describes the details of an individual probe for a monitor.

sourceArn -> (string)

The ARN of the subnet.

destination -> (string)

The destination IP address. This must be either `IPV4` or `IPV6` .

destinationPort -> (integer)

The port associated with the `destination` . This is required only if the `protocol` is `TCP` and must be a number between `1` and `65536` .

protocol -> (string)

The protocol used for the network traffic between the `source` and `destination` . This must be either `TCP` or `ICMP` .

packetSize -> (integer)

The size of the packets sent between the source and destination. This must be a number between `56` and `8500` .

tags -> (map)

The list of key-value pairs created and assigned to the monitor.

key -> (string)

value -> (string)

Shorthand Syntax:

```
sourceArn=string,destination=string,destinationPort=integer,protocol=string,packetSize=integer,tags={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "sourceArn": "string",
  "destination": "string",
  "destinationPort": integer,
  "protocol": "TCP"|"ICMP",
  "packetSize": integer,
  "tags": {"string": "string"
    ...}
}
```

`--client-token` (string)

Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.

`--tags` (map)

The list of key-value pairs created and assigned to the probe.

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

**Example 1: To create a probe that uses TCP and add it to a network monitor**

The following `create-probe` example creates a probe that uses the `TCP` `protocol` and adds the probe to a monitor named `Example_NetworkMonitor`. Once created, the `state` of the monitor with the probe will be `PENDING` until the monitor is `ACTIVE`. This might take several minutes, at which point the state will change to `ACTIVE`, and you can start viewing CloudWatch metrics.

```
aws networkmonitor create-probe \
    --monitor-name Example_NetworkMonitor \
    --probe sourceArn=arn:aws:ec2:region:111122223333:subnet/subnet-id,destination=10.0.0.100,destinationPort=80,protocol=TCP,packetSize=56,tags={Name=Probe1}
```

Output:

```
{
    "probeId": "probe-12345",
    "probeArn": "arn:aws:networkmonitor:region:111122223333:probe/probe-12345",
    "destination": "10.0.0.100",
    "destinationPort": 80,
    "packetSize": 56,
    "addressFamily": "IPV4",
    "vpcId": "vpc-12345",
    "state": "PENDING",
    "createdAt": "2024-03-29T12:41:57.314000-04:00",
    "modifiedAt": "2024-03-29T12:41:57.314000-04:00",
    "tags": {
        "Name": "Probe1"
    }
}
```

**Example 2: To create a probe that uses probe using ICMP and add it to a network monitor**

The following `create-probe` example creates a probe that uses the `ICMP` `protocol` and adds the probe to a monitor named `Example_NetworkMonitor`. Once created, the `state` of the monitor with the probe will be `PENDING` until the monitor is `ACTIVE`. This might take several minutes, at which point the state will change to `ACTIVE`, and you can start viewing CloudWatch metrics.

```
aws networkmonitor create-probe \
    --monitor-name Example_NetworkMonitor \
    --probe sourceArn=arn:aws:ec2:region:012345678910:subnet/subnet-id,destination=10.0.0.100,protocol=ICMP,packetSize=56,tags={Name=Probe1}
```

Output:

```
{
    "probeId": "probe-12345",
    "probeArn": "arn:aws:networkmonitor:region:111122223333:probe/probe-12345",
    "destination": "10.0.0.100",
    "packetSize": 56,
    "addressFamily": "IPV4",
    "vpcId": "vpc-12345",
    "state": "PENDING",
    "createdAt": "2024-03-29T12:44:02.452000-04:00",
    "modifiedAt": "2024-03-29T12:44:02.452000-04:00",
    "tags": {
        "Name": "Probe1"
    }
}
```

For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html) in the *Amazon CloudWatch User Guide*.

## Output

probeId -> (string)

The ID of the probe for which details are returned.

probeArn -> (string)

The ARN of the probe.

sourceArn -> (string)

The ARN of the probe.

destination -> (string)

The destination IP address for the monitor. This must be either an IPv4 or IPv6 address.

destinationPort -> (integer)

The port associated with the `destination` . This is required only if the `protocol` is `TCP` and must be a number between `1` and `65536` .

protocol -> (string)

The protocol used for the network traffic between the `source` and `destination` . This must be either `TCP` or `ICMP` .

packetSize -> (integer)

The size of the packets sent between the source and destination. This must be a number between `56` and `8500` .

addressFamily -> (string)

Indicates whether the IP address is `IPV4` or `IPV6` .

vpcId -> (string)

The ID of the source VPC or subnet.

state -> (string)

The state of the probe.

createdAt -> (timestamp)

The time and date that the probe was created.

modifiedAt -> (timestamp)

The time and date when the probe was last modified.

tags -> (map)

The list of key-value pairs assigned to the probe.

key -> (string)

value -> (string)