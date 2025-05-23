# update-probeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/update-probe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/update-probe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/index.html#cli-aws-networkmonitor) ]

# update-probe

## Description

Updates a monitor probe. This action requires both the `monitorName` and `probeId` parameters. Run `ListMonitors` to get a list of monitor names. Run `GetMonitor` to get a list of probes and probe IDs.

You can update the following para create a monitor with probes using this command. For each probe, you define the following:

- `state` âThe state of the probe.
- `destination` â The target destination IP address for the probe.
- `destinationPort` âRequired only if the protocol is `TCP` .
- `protocol` âThe communication protocol between the source and destination. This will be either `TCP` or `ICMP` .
- `packetSize` âThe size of the packets. This must be a number between `56` and `8500` .
- (Optional) `tags` âKey-value pairs created and assigned to the probe.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkmonitor-2023-08-01/UpdateProbe)

## Synopsis

```
update-probe
--monitor-name <value>
--probe-id <value>
[--state <value>]
[--destination <value>]
[--destination-port <value>]
[--protocol <value>]
[--packet-size <value>]
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

The name of the monitor that the probe was updated for.

`--probe-id` (string)

The ID of the probe to update.

`--state` (string)

The state of the probe update.

Possible values:

- `PENDING`
- `ACTIVE`
- `INACTIVE`
- `ERROR`
- `DELETING`
- `DELETED`

`--destination` (string)

The updated IP address for the probe destination. This must be either an IPv4 or IPv6 address.

`--destination-port` (integer)

The updated port for the probe destination. This is required only if the `protocol` is `TCP` and must be a number between `1` and `65536` .

`--protocol` (string)

The updated network protocol for the destination. This can be either `TCP` or `ICMP` . If the protocol is `TCP` , then `port` is also required.

Possible values:

- `TCP`
- `ICMP`

`--packet-size` (integer)

he updated packets size for network traffic between the source and destination. This must be a number between `56` and `8500` .

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

**To update a probe**

The following `update-probe` example updates a probeâs original `destination` IP address and also updates the `packetSize` to `60`.

```
aws networkmonitor update-probe \
    --monitor-name Example_NetworkMonitor \
    --probe-id probe-12345 \
    --destination 10.0.0.150 \
    --packet-size 60
```

Output:

```
{
    "probeId": "probe-12345",
    "probeArn": "arn:aws:networkmonitor:region:012345678910:probe/probe-12345",
    "sourceArn": "arn:aws:ec2:region:012345678910:subnet/subnet-12345",
    "destination": "10.0.0.150",
    "destinationPort": 80,
    "protocol": "TCP",
    "packetSize": 60,
    "addressFamily": "IPV4",
    "vpcId": "vpc-12345",
    "state": "PENDING",
    "createdAt": "2024-03-29T12:41:57.314000-04:00",
    "modifiedAt": "2024-03-29T13:52:23.115000-04:00",
    "tags": {
        "Name": "Probe1"
    }
}
```

For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html) in the *Amazon CloudWatch User Guide*.

## Output

probeId -> (string)

The updated ID of the probe.

probeArn -> (string)

The updated ARN of the probe.

sourceArn -> (string)

The updated ARN of the source subnet.

destination -> (string)

The updated destination IP address for the probe.

destinationPort -> (integer)

The updated destination port. This must be a number between `1` and `65536` .

protocol -> (string)

The updated protocol for the probe.

packetSize -> (integer)

The updated packet size for the probe.

addressFamily -> (string)

The updated IP address family. This must be either `IPV4` or `IPV6` .

vpcId -> (string)

The updated ID of the source VPC subnet ID.

state -> (string)

The state of the updated probe.

createdAt -> (timestamp)

The time and date that the probe was created.

modifiedAt -> (timestamp)

The time and date that the probe was last updated.

tags -> (map)

Update tags for a probe.

key -> (string)

value -> (string)