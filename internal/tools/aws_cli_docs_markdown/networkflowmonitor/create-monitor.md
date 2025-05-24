# create-monitorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/create-monitor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/create-monitor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkflowmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/index.html#cli-aws-networkflowmonitor) ]

# create-monitor

## Description

Create a monitor for specific network flows between local and remote resources, so that you can monitor network performance for one or several of your workloads. For each monitor, Network Flow Monitor publishes detailed end-to-end performance metrics and a network health indicators (NHI) that informs you whether there were Amazon Web Services network issues for one or more of the network flows tracked by a monitor, during a time period that you choose.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkflowmonitor-2023-04-19/CreateMonitor)

## Synopsis

```
create-monitor
--monitor-name <value>
--local-resources <value>
[--remote-resources <value>]
--scope-arn <value>
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

The name of the monitor.

`--local-resources` (list)

The local resources to monitor. A local resource, in a bi-directional flow of a workload, is the host where the agent is installed. For example, if a workload consists of an interaction between a web service and a backend database (for example, Amazon Relational Database Service (RDS)), the EC2 instance hosting the web service, which also runs the agent, is the local resource.

(structure)

A local resource is the host where the agent is installed. Local resources can be a a subnet, a VPC, or an Availability Zone.

type -> (string)

The type of the local resource. Valid values are `AWS::EC2::VPC` `AWS::AvailabilityZone` or `AWS::EC2::Subnet` .

identifier -> (string)

The identifier of the local resource, such as an ARN.

Shorthand Syntax:

```
type=string,identifier=string ...
```

JSON Syntax:

```
[
  {
    "type": "AWS::EC2::VPC"|"AWS::AvailabilityZone"|"AWS::EC2::Subnet",
    "identifier": "string"
  }
  ...
]
```

`--remote-resources` (list)

The remote resources to monitor. A remote resource is the other endpoint in the bi-directional flow of a workload, with a local resource. For example, Amazon Relational Database Service (RDS) can be a remote resource.

(structure)

A remote resource is the other endpoint in a network flow. That is, one endpoint is the local resource and the other is the remote resource. Remote resources can be a a subnet, a VPC, an Availability Zone, or an Amazon Web Services service.

type -> (string)

The type of the remote resource. Valid values are `AWS::EC2::VPC` `AWS::AvailabilityZone` , `AWS::EC2::Subnet` , or `AWS::AWSService` .

identifier -> (string)

The identifier of the remote resource, such as an ARN.

Shorthand Syntax:

```
type=string,identifier=string ...
```

JSON Syntax:

```
[
  {
    "type": "AWS::EC2::VPC"|"AWS::AvailabilityZone"|"AWS::EC2::Subnet"|"AWS::AWSService",
    "identifier": "string"
  }
  ...
]
```

`--scope-arn` (string)

The Amazon Resource Name (ARN) of the scope for the monitor.

`--client-token` (string)

A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Donât reuse the same client token for other API requests.

`--tags` (map)

The tags for a monitor. You can add a maximum of 200 tags.

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

**To create a monitor**

The following `create-monitor` example creates a monitor named `demo` in the specified account.

```
aws networkflowmonitor create-monitor \
    --monitor-name demo \
    --local-resources type="AWS::EC2::VPC",identifier="arn:aws:ec2:us-east-1:123456789012:vpc/vpc-03ea55eeda25adbb0"  \
    --scope-arn arn:aws:networkflowmonitor:us-east-1:123456789012:scope/e21cda79-30a0-4c12-9299-d8629d76d8cf
```

Output:

```
{
    "monitorArn": "arn:aws:networkflowmonitor:us-east-1:123456789012:monitor/demo",
    "monitorName": "demo",
    "monitorStatus": "ACTIVE",
    "tags": {}
}
```

For more information, see [Create a monitor in Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-monitors-create.html) in the *Amazon CloudWatch User Guide*.

## Output

monitorArn -> (string)

The Amazon Resource Name (ARN) of the monitor.

monitorName -> (string)

The name of the monitor.

monitorStatus -> (string)

The status of a monitor. The status can be one of the following

- `PENDING` : The monitor is in the process of being created.
- `ACTIVE` : The monitor is active.
- `INACTIVE` : The monitor is inactive.
- `ERROR` : Monitor creation failed due to an error.
- `DELETING` : The monitor is in the process of being deleted.

localResources -> (list)

The local resources to monitor. A local resource, in a bi-directional flow of a workload, is the host where the agent is installed.

(structure)

A local resource is the host where the agent is installed. Local resources can be a a subnet, a VPC, or an Availability Zone.

type -> (string)

The type of the local resource. Valid values are `AWS::EC2::VPC` `AWS::AvailabilityZone` or `AWS::EC2::Subnet` .

identifier -> (string)

The identifier of the local resource, such as an ARN.

remoteResources -> (list)

The remote resources to monitor. A remote resource is the other endpoint in the bi-directional flow of a workload, with a local resource. For example, Amazon Relational Database Service (RDS) can be a remote resource. The remote resource is identified by its ARN or an identifier.

(structure)

A remote resource is the other endpoint in a network flow. That is, one endpoint is the local resource and the other is the remote resource. Remote resources can be a a subnet, a VPC, an Availability Zone, or an Amazon Web Services service.

type -> (string)

The type of the remote resource. Valid values are `AWS::EC2::VPC` `AWS::AvailabilityZone` , `AWS::EC2::Subnet` , or `AWS::AWSService` .

identifier -> (string)

The identifier of the remote resource, such as an ARN.

createdAt -> (timestamp)

The date and time when the monitor was created.

modifiedAt -> (timestamp)

The last date and time that the monitor was modified.

tags -> (map)

The tags for a monitor.

key -> (string)

value -> (string)