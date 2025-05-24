# create-monitorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/create-monitor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/create-monitor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/index.html#cli-aws-networkmonitor) ]

# create-monitor

## Description

Creates a monitor between a source subnet and destination IP address. Within a monitor youâll create one or more probes that monitor network traffic between your source Amazon Web Services VPC subnets and your destination IP addresses. Each probe then aggregates and sends metrics to Amazon CloudWatch.

You can also create a monitor with probes using this command. For each probe, you define the following:

- `source` âThe subnet IDs where the probes will be created.
- `destination` â The target destination IP address for the probe.
- `destinationPort` âRequired only if the protocol is `TCP` .
- `protocol` âThe communication protocol between the source and destination. This will be either `TCP` or `ICMP` .
- `packetSize` âThe size of the packets. This must be a number between `56` and `8500` .
- (Optional) `tags` âKey-value pairs created and assigned to the probe.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkmonitor-2023-08-01/CreateMonitor)

## Synopsis

```
create-monitor
--monitor-name <value>
[--probes <value>]
[--aggregation-period <value>]
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

The name identifying the monitor. It can contain only letters, underscores (_), or dashes (-), and can be up to 200 characters.

`--probes` (list)

Displays a list of all of the probes created for a monitor.

(structure)

Creates a monitor probe.

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

probeTags -> (map)

The list of key-value pairs created and assigned to the monitor.

key -> (string)

value -> (string)

Shorthand Syntax:

```
sourceArn=string,destination=string,destinationPort=integer,protocol=string,packetSize=integer,probeTags={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "sourceArn": "string",
    "destination": "string",
    "destinationPort": integer,
    "protocol": "TCP"|"ICMP",
    "packetSize": integer,
    "probeTags": {"string": "string"
      ...}
  }
  ...
]
```

`--aggregation-period` (long)

The time, in seconds, that metrics are aggregated and sent to Amazon CloudWatch. Valid values are either `30` or `60` . `60` is the default if no period is chosen.

`--client-token` (string)

Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.

`--tags` (map)

The list of key-value pairs created and assigned to the monitor.

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

**Example 1: To create a network monitor with an aggregation period**

The following `create-monitor` example creates a monitor named `Example_NetworkMonitor` with an `aggregationPeriod` set to `30` seconds. The initial `state` of the monitor will be `INACTIVE` because there are no probes associated with it. The state changes to `ACTIVE` only when probes are added. You can use the [update-monitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/update-monitor.html) or [create-probe](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/create-probe.html) commands to add probes to this monitor.

```
aws networkmonitor create-monitor \
     --monitor-name Example_NetworkMonitor \
     --aggregation-period 30
```

Output:

```
{
    "monitorArn": "arn:aws:networkmonitor:region:111122223333:monitor/Example_NetworkMonitor",
    "monitorName": "Example_NetworkMonitor",
    "state": "INACTIVE",
    "aggregationPeriod": 30,
    "tags": {}
}
```

For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html) in the *Amazon CloudWatch User Guide*.

**Example 2: To create a network monitor with a probe using TCP and also includes tags**

The following `create-monitor` example creates a monitor named `Example_NetworkMonitor`. The command also creates one probe that uses the `ICMP` protocol and includes tags. Since no `aggregationPeriod` is passed in the request, `60` seconds is set as the default. The `state` of the monitor with the probe will be `PENDING` until the monitor is `ACTIVE`. This might take several minutes, at which point the `state` will change to `ACTIVE`, and you can start viewing CloudWatch metrics.

```
aws networkmonitor create-monitor \
    --monitor-name Example_NetworkMonitor \
    --probes sourceArn=arn:aws:ec2:region:111122223333:subnet/subnet-id,destination=10.0.0.100,destinationPort=80,protocol=TCP,packetSize=56,probeTags={Name=Probe1} \
    --tags Monitor=Monitor1
```

Output:

```
{
    "monitorArn": "arn:aws:networkmonitor:region111122223333:monitor/Example_NetworkMonitor",
    "monitorName": "Example_NetworkMonitor",
    "state": "PENDING",
    "aggregationPeriod": 60,
    "tags": {
        "Monitor": "Monitor1"
    }
}
```

For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html) in the *Amazon CloudWatch User Guide*.

**Example 3: To create a network monitor with a probe using ICMP and also includes tags**

The following `create-monitor` example creates a monitor named `Example_NetworkMonitor` with an `aggregationPeriod` of `30` seconds. The command also creates one probe that uses the `ICMP` protocol and includes tags. Since no `aggregationPeriod` is passed in the request, `60` seconds is set as the default. The `state` of the monitor with the probe will be `PENDING` until the monitor is `ACTIVE`. This might take several minutes, at which point the `state` will change to `ACTIVE`, and you can start viewing CloudWatch metrics.

```
aws networkmonitor create-monitor \
     --monitor-name Example_NetworkMonitor \
     --aggregation-period 30 \
     --probes sourceArn=arn:aws:ec2:region111122223333:subnet/subnet-id,destination=10.0.0.100,protocol=ICMP,packetSize=56,probeTags={Name=Probe1} \
     --tags Monitor=Monitor1
```

Output:

```
{
    "monitorArn": "arn:aws:networkmonitor:region:111122223333:monitor/Example_NetworkMonitor",
    "monitorName": "Example_NetworkMonitor",
    "state": "PENDING",
    "aggregationPeriod": 30,
    "tags": {
        "Monitor": "Monitor1"
    }
}
```

For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html) in the *Amazon CloudWatch User Guide*.

## Output

monitorArn -> (string)

The ARN of the monitor.

monitorName -> (string)

The name of the monitor.

state -> (string)

The state of the monitor.

aggregationPeriod -> (long)

The number of seconds that metrics are aggregated by and sent to Amazon CloudWatch. This will be either `30` or `60` .

tags -> (map)

The list of key-value pairs assigned to the monitor.

key -> (string)

value -> (string)