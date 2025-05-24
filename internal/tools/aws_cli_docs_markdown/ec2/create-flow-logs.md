# create-flow-logsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-flow-logs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-flow-logs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# create-flow-logs

## Description

Creates one or more flow logs to capture information about IP traffic for a specific network interface, subnet, or VPC.

Flow log data for a monitored network interface is recorded as flow log records, which are log events consisting of fields that describe the traffic flow. For more information, see [Flow log records](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html) in the *Amazon VPC User Guide* .

When publishing to CloudWatch Logs, flow log records are published to a log group, and each network interface has a unique log stream in the log group. When publishing to Amazon S3, flow log records for all of the monitored network interfaces are published to a single log file object that is stored in the specified bucket.

For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateFlowLogs)

## Synopsis

```
create-flow-logs
[--dry-run | --no-dry-run]
[--client-token <value>]
[--deliver-logs-permission-arn <value>]
[--deliver-cross-account-role <value>]
[--log-group-name <value>]
--resource-ids <value>
--resource-type <value>
[--traffic-type <value>]
[--log-destination-type <value>]
[--log-destination <value>]
[--log-format <value>]
[--tag-specifications <value>]
[--max-aggregation-interval <value>]
[--destination-options <value>]
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--client-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [How to ensure idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

`--deliver-logs-permission-arn` (string)

The ARN of the IAM role that allows Amazon EC2 to publish flow logs to the log destination.

This parameter is required if the destination type is `cloud-watch-logs` , or if the destination type is `kinesis-data-firehose` and the delivery stream and the resources to monitor are in different accounts.

`--deliver-cross-account-role` (string)

The ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.

`--log-group-name` (string)

The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs.

This parameter is valid only if the destination type is `cloud-watch-logs` .

`--resource-ids` (list)

The IDs of the resources to monitor. For example, if the resource type is `VPC` , specify the IDs of the VPCs.

Constraints: Maximum of 25 for transit gateway resource types. Maximum of 1000 for the other resource types.

(string)

Syntax:

```
"string" "string" ...
```

`--resource-type` (string)

The type of resource to monitor.

Possible values:

- `VPC`
- `Subnet`
- `NetworkInterface`
- `TransitGateway`
- `TransitGatewayAttachment`

`--traffic-type` (string)

The type of traffic to monitor (accepted traffic, rejected traffic, or all traffic). This parameter is not supported for transit gateway resource types. It is required for the other resource types.

Possible values:

- `ACCEPT`
- `REJECT`
- `ALL`

`--log-destination-type` (string)

The type of destination for the flow log data.

Default: `cloud-watch-logs`

Possible values:

- `cloud-watch-logs`
- `s3`
- `kinesis-data-firehose`

`--log-destination` (string)

The destination for the flow log data. The meaning of this parameter depends on the destination type.

- If the destination type is `cloud-watch-logs` , specify the ARN of a CloudWatch Logs log group. For example: arn:aws:logs:*region* :*account_id* :log-group:*my_group*   Alternatively, use the `LogGroupName` parameter.
- If the destination type is `s3` , specify the ARN of an S3 bucket. For example: arn:aws:s3:::*my_bucket* /*my_subfolder* / The subfolder is optional. Note that you canât use `AWSLogs` as a subfolder name.
- If the destination type is `kinesis-data-firehose` , specify the ARN of a Kinesis Data Firehose delivery stream. For example: arn:aws:firehose:*region* :*account_id* :deliverystream:*my_stream*

`--log-format` (string)

The fields to include in the flow log record. List the fields in the order in which they should appear. If you omit this parameter, the flow log is created using the default format. If you specify this parameter, you must include at least one field. For more information about the available fields, see [Flow log records](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html) in the *Amazon VPC User Guide* or [Transit Gateway Flow Log records](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html#flow-log-records) in the *Amazon Web Services Transit Gateway Guide* .

Specify the fields using the `${field-id}` format, separated by spaces.

`--tag-specifications` (list)

The tags to apply to the flow logs.

(structure)

The tags to apply to a resource when the resource is being created. When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.

### Note

The `Valid Values` lists all the resource types that can be tagged. However, the action youâre using might not support tagging all of these resource types. If you try to tag a resource type that is unsupported for the action youâre using, youâll get an error.

ResourceType -> (string)

The type of resource to tag on creation.

Tags -> (list)

The tags to apply to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

Shorthand Syntax:

```
ResourceType=string,Tags=[{Key=string,Value=string},{Key=string,Value=string}] ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "capacity-reservation"|"client-vpn-endpoint"|"customer-gateway"|"carrier-gateway"|"coip-pool"|"declarative-policies-report"|"dedicated-host"|"dhcp-options"|"egress-only-internet-gateway"|"elastic-ip"|"elastic-gpu"|"export-image-task"|"export-instance-task"|"fleet"|"fpga-image"|"host-reservation"|"image"|"import-image-task"|"import-snapshot-task"|"instance"|"instance-event-window"|"internet-gateway"|"ipam"|"ipam-pool"|"ipam-scope"|"ipv4pool-ec2"|"ipv6pool-ec2"|"key-pair"|"launch-template"|"local-gateway"|"local-gateway-route-table"|"local-gateway-virtual-interface"|"local-gateway-virtual-interface-group"|"local-gateway-route-table-vpc-association"|"local-gateway-route-table-virtual-interface-group-association"|"natgateway"|"network-acl"|"network-interface"|"network-insights-analysis"|"network-insights-path"|"network-insights-access-scope"|"network-insights-access-scope-analysis"|"outpost-lag"|"placement-group"|"prefix-list"|"replace-root-volume-task"|"reserved-instances"|"route-table"|"security-group"|"security-group-rule"|"service-link-virtual-interface"|"snapshot"|"spot-fleet-request"|"spot-instances-request"|"subnet"|"subnet-cidr-reservation"|"traffic-mirror-filter"|"traffic-mirror-session"|"traffic-mirror-target"|"transit-gateway"|"transit-gateway-attachment"|"transit-gateway-connect-peer"|"transit-gateway-multicast-domain"|"transit-gateway-policy-table"|"transit-gateway-route-table"|"transit-gateway-route-table-announcement"|"volume"|"vpc"|"vpc-endpoint"|"vpc-endpoint-connection"|"vpc-endpoint-service"|"vpc-endpoint-service-permission"|"vpc-peering-connection"|"vpn-connection"|"vpn-gateway"|"vpc-flow-log"|"capacity-reservation-fleet"|"traffic-mirror-filter-rule"|"vpc-endpoint-connection-device-type"|"verified-access-instance"|"verified-access-group"|"verified-access-endpoint"|"verified-access-policy"|"verified-access-trust-provider"|"vpn-connection-device-type"|"vpc-block-public-access-exclusion"|"route-server"|"route-server-endpoint"|"route-server-peer"|"ipam-resource-discovery"|"ipam-resource-discovery-association"|"instance-connect-endpoint"|"verified-access-endpoint-target"|"ipam-external-resource-verification-token"|"mac-modification-task",
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  }
  ...
]
```

`--max-aggregation-interval` (integer)

The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. The possible values are 60 seconds (1 minute) or 600 seconds (10 minutes). This parameter must be 60 seconds for transit gateway resource types.

When a network interface is attached to a [Nitro-based instance](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) , the aggregation interval is always 60 seconds or less, regardless of the value that you specify.

Default: 600

`--destination-options` (structure)

The destination options.

FileFormat -> (string)

The format for the flow log. The default is `plain-text` .

HiveCompatiblePartitions -> (boolean)

Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3. The default is `false` .

PerHourPartition -> (boolean)

Indicates whether to partition the flow log per hour. This reduces the cost and response time for queries. The default is `false` .

Shorthand Syntax:

```
FileFormat=string,HiveCompatiblePartitions=boolean,PerHourPartition=boolean
```

JSON Syntax:

```
{
  "FileFormat": "plain-text"|"parquet",
  "HiveCompatiblePartitions": true|false,
  "PerHourPartition": true|false
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

**Example 1: To create a flow log**

The following `create-flow-logs` example creates a flow log that captures all rejected traffic for the specified network interface. The flow logs are delivered to a log group in CloudWatch Logs using the permissions in the specified IAM role.

```
aws ec2 create-flow-logs \
    --resource-type NetworkInterface \
    --resource-ids eni-11223344556677889 \
    --traffic-type REJECT \
    --log-group-name my-flow-logs \
    --deliver-logs-permission-arn arn:aws:iam::123456789101:role/publishFlowLogs
```

Output:

```
{
    "ClientToken": "so0eNA2uSHUNlHI0S2cJ305GuIX1CezaRdGtexample",
    "FlowLogIds": [
        "fl-12345678901234567"
    ],
    "Unsuccessful": []
}
```

For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide*.

**Example 2: To create a flow log with a custom format**

The following `create-flow-logs` example creates a flow log that captures all traffic for the specified VPC and delivers the flow logs to an Amazon S3 bucket. The `--log-format` parameter specifies a custom format for the flow log records. To run this command on Windows, change the single quotes (â) to double quotes (â).

```
aws ec2 create-flow-logs \
    --resource-type VPC \
    --resource-ids vpc-00112233344556677 \
    --traffic-type ALL \
    --log-destination-type s3 \
    --log-destination arn:aws:s3:::flow-log-bucket/my-custom-flow-logs/ \
    --log-format '${version} ${vpc-id} ${subnet-id} ${instance-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${tcp-flags} ${type} ${pkt-srcaddr} ${pkt-dstaddr}'
```

For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide*.

**Example 3: To create a flow log with a one-minute maximum aggregation interval**

The following `create-flow-logs` example creates a flow log that captures all traffic for the specified VPC and delivers the flow logs to an Amazon S3 bucket. The `--max-aggregation-interval` parameter specifies a maximum aggregation interval of 60 seconds (1 minute).

```
aws ec2 create-flow-logs \
    --resource-type VPC \
    --resource-ids vpc-00112233344556677 \
    --traffic-type ALL \
    --log-destination-type s3 \
    --log-destination arn:aws:s3:::flow-log-bucket/my-custom-flow-logs/ \
    --max-aggregation-interval 60
```

For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide*.

## Output

ClientToken -> (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

FlowLogIds -> (list)

The IDs of the flow logs.

(string)

Unsuccessful -> (list)

Information about the flow logs that could not be created successfully.

(structure)

Information about items that were not successfully processed in a batch call.

Error -> (structure)

Information about the error.

Code -> (string)

The error code.

Message -> (string)

The error message accompanying the error code.

ResourceId -> (string)

The ID of the resource.