# get-ec2-instance-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-ec2-instance-recommendations

## Description

Returns Amazon EC2 instance recommendations.

Compute Optimizer generates recommendations for Amazon Elastic Compute Cloud (Amazon EC2) instances that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetEC2InstanceRecommendations)

## Synopsis

```
get-ec2-instance-recommendations
[--instance-arns <value>]
[--next-token <value>]
[--max-results <value>]
[--filters <value>]
[--account-ids <value>]
[--recommendation-preferences <value>]
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

`--instance-arns` (list)

The Amazon Resource Name (ARN) of the instances for which to return recommendations.

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token to advance to the next page of instance recommendations.

`--max-results` (integer)

The maximum number of instance recommendations to return with a single request.

To retrieve the remaining results, make another request with the returned `nextToken` value.

`--filters` (list)

An array of objects to specify a filter that returns a more specific list of instance recommendations.

(structure)

Describes a filter that returns a more specific list of recommendations. Use this filter with the  GetAutoScalingGroupRecommendations and  GetEC2InstanceRecommendations actions.

You can use `EBSFilter` with the  GetEBSVolumeRecommendations action, `LambdaFunctionRecommendationFilter` with the  GetLambdaFunctionRecommendations action, and `JobFilter` with the  DescribeRecommendationExportJobs action.

name -> (string)

The name of the filter.

Specify `Finding` to return recommendations with a specific finding classification. For example, `Underprovisioned` .

Specify `RecommendationSourceType` to return recommendations of a specific resource type. For example, `Ec2Instance` .

Specify `FindingReasonCodes` to return recommendations with a specific finding reason code. For example, `CPUUnderprovisioned` .

Specify `InferredWorkloadTypes` to return recommendations of a specific inferred workload. For example, `Redis` .

You can filter your EC2 instance recommendations by `tag:key` and `tag-key` tags.

A `tag:key` is a key and value combination of a tag assigned to your recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all recommendations that have a tag with the key of `Owner` and the value of `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

A `tag-key` is the key of a tag assigned to your recommendations. Use this filter to find all of your recommendations that have a tag with a specific key. This doesnât consider the tag value. For example, you can find your recommendations with a tag key value of `Owner` or without any tag keys assigned.

values -> (list)

The value of the filter.

The valid values for this parameter are as follows, depending on what you specify for the `name` parameter and the resource type that you wish to filter results for:

- Specify `Optimized` or `NotOptimized` if you specify the `name` parameter as `Finding` and you want to filter results for Auto Scaling groups.
- Specify `Underprovisioned` , `Overprovisioned` , or `Optimized` if you specify the `name` parameter as `Finding` and you want to filter results for EC2 instances.
- Specify `Ec2Instance` or `AutoScalingGroup` if you specify the `name` parameter as `RecommendationSourceType` .
- Specify one of the following options if you specify the `name` parameter as `FindingReasonCodes` :
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id1)`CPUOverprovisioned` ** â The instanceâs CPU configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id3)`CPUUnderprovisioned` ** â The instanceâs CPU configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better CPU performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id5)`MemoryOverprovisioned` ** â The instanceâs memory configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id7)`MemoryUnderprovisioned` ** â The instanceâs memory configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better memory performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id9)`EBSThroughputOverprovisioned` ** â The instanceâs EBS throughput configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id11)`EBSThroughputUnderprovisioned` ** â The instanceâs EBS throughput configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id13)`EBSIOPSOverprovisioned` ** â The instanceâs EBS IOPS configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id15)`EBSIOPSUnderprovisioned` ** â The instanceâs EBS IOPS configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better EBS IOPS performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id17)`NetworkBandwidthOverprovisioned` ** â The instanceâs network bandwidth configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id19)`NetworkBandwidthUnderprovisioned` ** â The instanceâs network bandwidth configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better network bandwidth performance. This finding reason happens when the `NetworkIn` or `NetworkOut` performance of an instance is impacted.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id21)`NetworkPPSOverprovisioned` ** â The instanceâs network PPS (packets per second) configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id23)`NetworkPPSUnderprovisioned` ** â The instanceâs network PPS (packets per second) configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better network PPS performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id25)`DiskIOPSOverprovisioned` ** â The instanceâs disk IOPS configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id27)`DiskIOPSUnderprovisioned` ** â The instanceâs disk IOPS configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better disk IOPS performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id29)`DiskThroughputOverprovisioned` ** â The instanceâs disk throughput configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id31)`DiskThroughputUnderprovisioned` ** â The instanceâs disk throughput configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better disk throughput performance.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "Finding"|"FindingReasonCodes"|"RecommendationSourceType"|"InferredWorkloadTypes",
    "values": ["string", ...]
  }
  ...
]
```

`--account-ids` (list)

The ID of the Amazon Web Services account for which to return instance recommendations.

If your account is the management account of an organization, use this parameter to specify the member account for which you want to return instance recommendations.

Only one account ID can be specified per request.

(string)

Syntax:

```
"string" "string" ...
```

`--recommendation-preferences` (structure)

An object to specify the preferences for the Amazon EC2 instance recommendations to return in the response.

cpuVendorArchitectures -> (list)

Specifies the CPU vendor and architecture for Amazon EC2 instance and Auto Scaling group recommendations.

For example, when you specify `AWS_ARM64` with:

- A  GetEC2InstanceRecommendations or  GetAutoScalingGroupRecommendations request, Compute Optimizer returns recommendations that consist of Graviton instance types only.
- A  GetEC2RecommendationProjectedMetrics request, Compute Optimizer returns projected utilization metrics for Graviton instance type recommendations only.
- A  ExportEC2InstanceRecommendations or  ExportAutoScalingGroupRecommendations request, Compute Optimizer exports recommendations that consist of Graviton instance types only.

(string)

Shorthand Syntax:

```
cpuVendorArchitectures=string,string
```

JSON Syntax:

```
{
  "cpuVendorArchitectures": ["AWS_ARM64"|"CURRENT", ...]
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

## Output

nextToken -> (string)

The token to use to advance to the next page of instance recommendations.

This value is null when there are no more pages of instance recommendations to return.

instanceRecommendations -> (list)

An array of objects that describe instance recommendations.

(structure)

Describes an Amazon EC2 instance recommendation.

instanceArn -> (string)

The Amazon Resource Name (ARN) of the current instance.

accountId -> (string)

The Amazon Web Services account ID of the instance.

instanceName -> (string)

The name of the current instance.

currentInstanceType -> (string)

The instance type of the current instance.

finding -> (string)

The finding classification of the instance.

Findings for instances include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id33)`Underprovisioned` ** âAn instance is considered under-provisioned when at least one specification of your instance, such as CPU, memory, or network, does not meet the performance requirements of your workload. Under-provisioned instances may lead to poor application performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id35)`Overprovisioned` ** âAn instance is considered over-provisioned when at least one specification of your instance, such as CPU, memory, or network, can be sized down while still meeting the performance requirements of your workload, and no specification is under-provisioned. Over-provisioned instances may lead to unnecessary infrastructure cost.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id37)`Optimized` ** âAn instance is considered optimized when all specifications of your instance, such as CPU, memory, and network, meet the performance requirements of your workload and is not over provisioned. For optimized resources, Compute Optimizer might recommend a new generation instance type.

### Note

The valid values in your API responses appear as OVER_PROVISIONED, UNDER_PROVISIONED, or OPTIMIZED.

findingReasonCodes -> (list)

The reason for the finding classification of the instance.

Finding reason codes for instances include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id39)`CPUOverprovisioned` ** â The instanceâs CPU configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `CPUUtilization` metric of the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id41)`CPUUnderprovisioned` ** â The instanceâs CPU configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better CPU performance. This is identified by analyzing the `CPUUtilization` metric of the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id43)`MemoryOverprovisioned` ** â The instanceâs memory configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the memory utilization metric of the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id45)`MemoryUnderprovisioned` ** â The instanceâs memory configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better memory performance. This is identified by analyzing the memory utilization metric of the current instance during the look-back period.

### Note

Memory utilization is analyzed only for resources that have the unified CloudWatch agent installed on them. For more information, see [Enabling memory utilization with the Amazon CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent) in the *Compute Optimizer User Guide* . On Linux instances, Compute Optimizer analyses the `mem_used_percent` metric in the `CWAgent` namespace, or the legacy `MemoryUtilization` metric in the `System/Linux` namespace. On Windows instances, Compute Optimizer analyses the `Memory % Committed Bytes In Use` metric in the `CWAgent` namespace.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id47)`EBSThroughputOverprovisioned` ** â The instanceâs EBS throughput configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metrics of EBS volumes attached to the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id49)`EBSThroughputUnderprovisioned` ** â The instanceâs EBS throughput configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metrics of EBS volumes attached to the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id51)`EBSIOPSOverprovisioned` ** â The instanceâs EBS IOPS configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metric of EBS volumes attached to the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id53)`EBSIOPSUnderprovisioned` ** â The instanceâs EBS IOPS configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better EBS IOPS performance. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metric of EBS volumes attached to the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id55)`NetworkBandwidthOverprovisioned` ** â The instanceâs network bandwidth configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `NetworkIn` and `NetworkOut` metrics of the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id57)`NetworkBandwidthUnderprovisioned` ** â The instanceâs network bandwidth configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better network bandwidth performance. This is identified by analyzing the `NetworkIn` and `NetworkOut` metrics of the current instance during the look-back period. This finding reason happens when the `NetworkIn` or `NetworkOut` performance of an instance is impacted.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id59)`NetworkPPSOverprovisioned` ** â The instanceâs network PPS (packets per second) configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `NetworkPacketsIn` and `NetworkPacketsIn` metrics of the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id61)`NetworkPPSUnderprovisioned` ** â The instanceâs network PPS (packets per second) configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better network PPS performance. This is identified by analyzing the `NetworkPacketsIn` and `NetworkPacketsIn` metrics of the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id63)`DiskIOPSOverprovisioned` ** â The instanceâs disk IOPS configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `DiskReadOps` and `DiskWriteOps` metrics of the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id65)`DiskIOPSUnderprovisioned` ** â The instanceâs disk IOPS configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better disk IOPS performance. This is identified by analyzing the `DiskReadOps` and `DiskWriteOps` metrics of the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id67)`DiskThroughputOverprovisioned` ** â The instanceâs disk throughput configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `DiskReadBytes` and `DiskWriteBytes` metrics of the current instance during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id69)`DiskThroughputUnderprovisioned` ** â The instanceâs disk throughput configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better disk throughput performance. This is identified by analyzing the `DiskReadBytes` and `DiskWriteBytes` metrics of the current instance during the look-back period.

### Note

For more information about instance metrics, see [List the available CloudWatch metrics for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html) in the *Amazon Elastic Compute Cloud User Guide* . For more information about EBS volume metrics, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) in the *Amazon Elastic Compute Cloud User Guide* .

(string)

utilizationMetrics -> (list)

An array of objects that describe the utilization metrics of the instance.

(structure)

Describes a utilization metric of a resource, such as an Amazon EC2 instance.

Compare the utilization metric data of your resource against its projected utilization metric data to determine the performance difference between your current resource and the recommended option.

name -> (string)

The name of the utilization metric.

The following utilization metrics are available:

- `Cpu` - The percentage of allocated EC2 compute units that are currently in use on the instance. This metric identifies the processing power required to run an application on the instance. Depending on the instance type, tools in your operating system can show a lower percentage than CloudWatch when the instance is not allocated a full processor core. Units: Percent
- `Memory` - The percentage of memory that is currently in use on the instance. This metric identifies the amount of memory required to run an application on the instance. Units: Percent

### Note

The `Memory` metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see [Enabling Memory Utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent) .

- `GPU` - The percentage of allocated GPUs that currently run on the instance.
- `GPU_MEMORY` - The percentage of total GPU memory that currently runs on the instance.

### Note

The `GPU` and `GPU_MEMORY` metrics are only returned for resources with the unified CloudWatch Agent installed on them. For more information, see [Enabling NVIDIA GPU utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#nvidia-cw-agent) .

- `EBS_READ_OPS_PER_SECOND` - The completed read operations from all EBS volumes attached to the instance in a specified period of time. Unit: Count
- `EBS_WRITE_OPS_PER_SECOND` - The completed write operations to all EBS volumes attached to the instance in a specified period of time. Unit: Count
- `EBS_READ_BYTES_PER_SECOND` - The bytes read from all EBS volumes attached to the instance in a specified period of time. Unit: Bytes
- `EBS_WRITE_BYTES_PER_SECOND` - The bytes written to all EBS volumes attached to the instance in a specified period of time. Unit: Bytes
- `DISK_READ_OPS_PER_SECOND` - The completed read operations from all instance store volumes available to the instance in a specified period of time. If there are no instance store volumes, either the value is `0` or the metric is not reported.
- `DISK_WRITE_OPS_PER_SECOND` - The completed write operations from all instance store volumes available to the instance in a specified period of time. If there are no instance store volumes, either the value is `0` or the metric is not reported.
- `DISK_READ_BYTES_PER_SECOND` - The bytes read from all instance store volumes available to the instance. This metric is used to determine the volume of the data the application reads from the disk of the instance. This can be used to determine the speed of the application. If there are no instance store volumes, either the value is `0` or the metric is not reported.
- `DISK_WRITE_BYTES_PER_SECOND` - The bytes written to all instance store volumes available to the instance. This metric is used to determine the volume of the data the application writes onto the disk of the instance. This can be used to determine the speed of the application. If there are no instance store volumes, either the value is `0` or the metric is not reported.
- `NETWORK_IN_BYTES_PER_SECOND` - The number of bytes received by the instance on all network interfaces. This metric identifies the volume of incoming network traffic to a single instance.
- `NETWORK_OUT_BYTES_PER_SECOND` - The number of bytes sent out by the instance on all network interfaces. This metric identifies the volume of outgoing network traffic from a single instance.
- `NETWORK_PACKETS_IN_PER_SECOND` - The number of packets received by the instance on all network interfaces. This metric identifies the volume of incoming traffic in terms of the number of packets on a single instance.
- `NETWORK_PACKETS_OUT_PER_SECOND` - The number of packets sent out by the instance on all network interfaces. This metric identifies the volume of outgoing traffic in terms of the number of packets on a single instance.

statistic -> (string)

The statistic of the utilization metric.

The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.

The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the *Compute Optimizer User Guide* . You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

value -> (double)

The value of the utilization metric.

lookBackPeriodInDays -> (double)

The number of days for which utilization metrics were analyzed for the instance.

recommendationOptions -> (list)

An array of objects that describe the recommendation options for the instance.

(structure)

Describes a recommendation option for an Amazon EC2 instance.

instanceType -> (string)

The instance type of the instance recommendation.

instanceGpuInfo -> (structure)

Describes the GPU accelerator settings for the recommended instance type.

gpus -> (list)

Describes the GPU accelerators for the instance type.

(structure)

Describes the GPU accelerators for the instance type.

gpuCount -> (integer)

The number of GPUs for the instance type.

gpuMemorySizeInMiB -> (integer)

The total size of the memory for the GPU accelerators for the instance type, in MiB.

projectedUtilizationMetrics -> (list)

An array of objects that describe the projected utilization metrics of the instance recommendation option.

### Note

The `Cpu` and `Memory` metrics are the only projected utilization metrics returned. Additionally, the `Memory` metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see [Enabling Memory Utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent) .

(structure)

Describes a utilization metric of a resource, such as an Amazon EC2 instance.

Compare the utilization metric data of your resource against its projected utilization metric data to determine the performance difference between your current resource and the recommended option.

name -> (string)

The name of the utilization metric.

The following utilization metrics are available:

- `Cpu` - The percentage of allocated EC2 compute units that are currently in use on the instance. This metric identifies the processing power required to run an application on the instance. Depending on the instance type, tools in your operating system can show a lower percentage than CloudWatch when the instance is not allocated a full processor core. Units: Percent
- `Memory` - The percentage of memory that is currently in use on the instance. This metric identifies the amount of memory required to run an application on the instance. Units: Percent

### Note

The `Memory` metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see [Enabling Memory Utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent) .

- `GPU` - The percentage of allocated GPUs that currently run on the instance.
- `GPU_MEMORY` - The percentage of total GPU memory that currently runs on the instance.

### Note

The `GPU` and `GPU_MEMORY` metrics are only returned for resources with the unified CloudWatch Agent installed on them. For more information, see [Enabling NVIDIA GPU utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#nvidia-cw-agent) .

- `EBS_READ_OPS_PER_SECOND` - The completed read operations from all EBS volumes attached to the instance in a specified period of time. Unit: Count
- `EBS_WRITE_OPS_PER_SECOND` - The completed write operations to all EBS volumes attached to the instance in a specified period of time. Unit: Count
- `EBS_READ_BYTES_PER_SECOND` - The bytes read from all EBS volumes attached to the instance in a specified period of time. Unit: Bytes
- `EBS_WRITE_BYTES_PER_SECOND` - The bytes written to all EBS volumes attached to the instance in a specified period of time. Unit: Bytes
- `DISK_READ_OPS_PER_SECOND` - The completed read operations from all instance store volumes available to the instance in a specified period of time. If there are no instance store volumes, either the value is `0` or the metric is not reported.
- `DISK_WRITE_OPS_PER_SECOND` - The completed write operations from all instance store volumes available to the instance in a specified period of time. If there are no instance store volumes, either the value is `0` or the metric is not reported.
- `DISK_READ_BYTES_PER_SECOND` - The bytes read from all instance store volumes available to the instance. This metric is used to determine the volume of the data the application reads from the disk of the instance. This can be used to determine the speed of the application. If there are no instance store volumes, either the value is `0` or the metric is not reported.
- `DISK_WRITE_BYTES_PER_SECOND` - The bytes written to all instance store volumes available to the instance. This metric is used to determine the volume of the data the application writes onto the disk of the instance. This can be used to determine the speed of the application. If there are no instance store volumes, either the value is `0` or the metric is not reported.
- `NETWORK_IN_BYTES_PER_SECOND` - The number of bytes received by the instance on all network interfaces. This metric identifies the volume of incoming network traffic to a single instance.
- `NETWORK_OUT_BYTES_PER_SECOND` - The number of bytes sent out by the instance on all network interfaces. This metric identifies the volume of outgoing network traffic from a single instance.
- `NETWORK_PACKETS_IN_PER_SECOND` - The number of packets received by the instance on all network interfaces. This metric identifies the volume of incoming traffic in terms of the number of packets on a single instance.
- `NETWORK_PACKETS_OUT_PER_SECOND` - The number of packets sent out by the instance on all network interfaces. This metric identifies the volume of outgoing traffic in terms of the number of packets on a single instance.

statistic -> (string)

The statistic of the utilization metric.

The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.

The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the *Compute Optimizer User Guide* . You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

value -> (double)

The value of the utilization metric.

platformDifferences -> (list)

Describes the configuration differences between the current instance and the recommended instance type. You should consider the configuration differences before migrating your workloads from the current instance to the recommended instance type. The [Change the instance type guide for Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) and [Change the instance type guide for Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-resize.html) provide general guidance for getting started with an instance migration.

Platform differences include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id71)`Hypervisor` ** â The hypervisor of the recommended instance type is different than that of the current instance. For example, the recommended instance type uses a Nitro hypervisor and the current instance uses a Xen hypervisor. The differences that you should consider between these hypervisors are covered in the [Nitro Hypervisor](http://aws.amazon.com/ec2/faqs/#Nitro_Hypervisor) section of the Amazon EC2 frequently asked questions. For more information, see [Instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances) in the *Amazon EC2 User Guide for Linux* , or [Instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#ec2-nitro-instances) in the *Amazon EC2 User Guide for Windows* .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id73)`NetworkInterface` ** â The network interface of the recommended instance type is different than that of the current instance. For example, the recommended instance type supports enhanced networking and the current instance might not. To enable enhanced networking for the recommended instance type, you must install the Elastic Network Adapter (ENA) driver or the Intel 82599 Virtual Function driver. For more information, see [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-networking-storage) and [Enhanced networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) in the *Amazon EC2 User Guide for Linux* , or [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#instance-networking-storage) and [Enhanced networking on Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html) in the *Amazon EC2 User Guide for Windows* .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id75)`StorageInterface` ** â The storage interface of the recommended instance type is different than that of the current instance. For example, the recommended instance type uses an NVMe storage interface and the current instance does not. To access NVMe volumes for the recommended instance type, you will need to install or upgrade the NVMe driver. For more information, see [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-networking-storage) and [Amazon EBS and NVMe on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvme-ebs-volumes.html) in the *Amazon EC2 User Guide for Linux* , or [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#instance-networking-storage) and [Amazon EBS and NVMe on Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/nvme-ebs-volumes.html) in the *Amazon EC2 User Guide for Windows* .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id77)`InstanceStoreAvailability` ** â The recommended instance type does not support instance store volumes and the current instance does. Before migrating, you might need to back up the data on your instance store volumes if you want to preserve them. For more information, see [How do I back up an instance store volume on my Amazon EC2 instance to Amazon EBS?](https://aws.amazon.com/premiumsupport/knowledge-center/back-up-instance-store-ebs/) in the *Amazon Web Services Premium Support Knowledge Base* . For more information, see [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-networking-storage) and [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide for Linux* , or see [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#instance-networking-storage) and [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/InstanceStorage.html) in the *Amazon EC2 User Guide for Windows* .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id79)`VirtualizationType` ** â The recommended instance type uses the hardware virtual machine (HVM) virtualization type and the current instance uses the paravirtual (PV) virtualization type. For more information about the differences between these virtualization types, see [Linux AMI virtualization types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html) in the *Amazon EC2 User Guide for Linux* , or [Windows AMI virtualization types](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/windows-ami-version-history.html#virtualization-types) in the *Amazon EC2 User Guide for Windows* .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html#id81)`Architecture` ** â The CPU architecture between the recommended instance type and the current instance is different. For example, the recommended instance type might use an Arm CPU architecture and the current instance type might use a different one, such as x86. Before migrating, you should consider recompiling the software on your instance for the new architecture. Alternatively, you might switch to an Amazon Machine Image (AMI) that supports the new architecture. For more information about the CPU architecture for each instance type, see [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/) .

(string)

performanceRisk -> (double)

The performance risk of the instance recommendation option.

Performance risk indicates the likelihood of the recommended instance type not meeting the resource needs of your workload. Compute Optimizer calculates an individual performance risk score for each specification of the recommended instance, including CPU, memory, EBS throughput, EBS IOPS, disk throughput, disk IOPS, network throughput, and network PPS. The performance risk of the recommended instance is calculated as the maximum performance risk score across the analyzed resource specifications.

The value ranges from `0` - `4` , with `0` meaning that the recommended resource is predicted to always provide enough hardware capability. The higher the performance risk is, the more likely you should validate whether the recommendation will meet the performance requirements of your workload before migrating your resource.

rank -> (integer)

The rank of the instance recommendation option.

The top recommendation option is ranked as `1` .

savingsOpportunity -> (structure)

An object that describes the savings opportunity for the instance recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a given resource.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing..

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

savingsOpportunityAfterDiscounts -> (structure)

An object that describes the savings opportunity for the instance recommendation option that includes Savings Plans and Reserved Instances discounts. Savings opportunity includes the estimated monthly savings and percentage.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost after applying the Savings Plans and Reserved Instances discounts. This saving can be achieved by adopting Compute Optimizerâs EC2 instance recommendations.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings possible by adopting Compute Optimizerâs Amazon EC2 instance recommendations. This is based on pricing after applying the Savings Plans and Reserved Instances discounts.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

migrationEffort -> (string)

The level of effort required to migrate from the current instance type to the recommended instance type.

For example, the migration effort is `Low` if Amazon EMR is the inferred workload type and an Amazon Web Services Graviton instance type is recommended. The migration effort is `Medium` if a workload type couldnât be inferred but an Amazon Web Services Graviton instance type is recommended. The migration effort is `VeryLow` if both the current and recommended instance types are of the same CPU architecture.

recommendationSources -> (list)

An array of objects that describe the source resource of the recommendation.

(structure)

Describes the source of a recommendation, such as an Amazon EC2 instance or Auto Scaling group.

recommendationSourceArn -> (string)

The Amazon Resource Name (ARN) of the recommendation source.

recommendationSourceType -> (string)

The resource type of the recommendation source.

lastRefreshTimestamp -> (timestamp)

The timestamp of when the instance recommendation was last generated.

currentPerformanceRisk -> (string)

The risk of the current instance not meeting the performance needs of its workloads. The higher the risk, the more likely the current instance cannot meet the performance requirements of its workload.

effectiveRecommendationPreferences -> (structure)

An object that describes the effective recommendation preferences for the instance.

cpuVendorArchitectures -> (list)

Describes the CPU vendor and architecture for an instance or Auto Scaling group recommendations.

For example, when you specify `AWS_ARM64` with:

- A  GetEC2InstanceRecommendations or  GetAutoScalingGroupRecommendations request, Compute Optimizer returns recommendations that consist of Graviton instance types only.
- A  GetEC2RecommendationProjectedMetrics request, Compute Optimizer returns projected utilization metrics for Graviton instance type recommendations only.
- A  ExportEC2InstanceRecommendations or  ExportAutoScalingGroupRecommendations request, Compute Optimizer exports recommendations that consist of Graviton instance types only.

(string)

enhancedInfrastructureMetrics -> (string)

Describes the activation status of the enhanced infrastructure metrics preference.

A status of `Active` confirms that the preference is applied in the latest recommendation refresh, and a status of `Inactive` confirms that itâs not yet applied to recommendations.

For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

inferredWorkloadTypes -> (string)

Describes the activation status of the inferred workload types preference.

A status of `Active` confirms that the preference is applied in the latest recommendation refresh. A status of `Inactive` confirms that itâs not yet applied to recommendations.

externalMetricsPreference -> (structure)

An object that describes the external metrics recommendation preference.

If the preference is applied in the latest recommendation refresh, an object with a valid `source` value appears in the response. If the preference isnât applied to the recommendations already, then this object doesnât appear in the response.

source -> (string)

Contains the source options for external metrics preferences.

lookBackPeriod -> (string)

The number of days the utilization metrics of the Amazon Web Services resource are analyzed.

utilizationPreferences -> (list)

The resourceâs CPU and memory utilization preferences, such as threshold and headroom, that are used to generate rightsizing recommendations.

### Note

This preference is only available for the Amazon EC2 instance resource type.

(structure)

The preference to control the resourceâs CPU utilization threshold, CPU utilization headroom, and memory utilization headroom.

### Note

This preference is only available for the Amazon EC2 instance resource type.

metricName -> (string)

The name of the resource utilization metric name to customize.

metricParameters -> (structure)

The parameters to set when customizing the resource utilization thresholds.

threshold -> (string)

The threshold value used for the specified metric parameter.

### Note

You can only specify the threshold value for CPU utilization.

headroom -> (string)

The headroom value in percentage used for the specified metric parameter.

The following lists the valid values for CPU and memory utilization.

- CPU utilization: `PERCENT_30 | PERCENT_20 | PERCENT_0`
- Memory utilization: `PERCENT_30 | PERCENT_20 | PERCENT_10`

preferredResources -> (list)

The resource type values that are considered as candidates when generating rightsizing recommendations.

(structure)

Describes the effective preferred resources that Compute Optimizer considers as rightsizing recommendation candidates.

### Note

Compute Optimizer only supports Amazon EC2 instance types.

name -> (string)

The name of the preferred resource list.

includeList -> (list)

The list of preferred resource values that you want considered as rightsizing recommendation candidates.

(string)

effectiveIncludeList -> (list)

The expanded version of your preferred resourceâs include list.

(string)

excludeList -> (list)

The list of preferred resources values that you want excluded from rightsizing recommendation candidates.

(string)

savingsEstimationMode -> (structure)

Describes the savings estimation mode applied for calculating savings opportunity for a resource.

source -> (string)

Describes the source for calculating the savings opportunity for Amazon EC2 instances.

inferredWorkloadTypes -> (list)

The applications that might be running on the instance as inferred by Compute Optimizer.

Compute Optimizer can infer if one of the following applications might be running on the instance:

- `AmazonEmr` - Infers that Amazon EMR might be running on the instance.
- `ApacheCassandra` - Infers that Apache Cassandra might be running on the instance.
- `ApacheHadoop` - Infers that Apache Hadoop might be running on the instance.
- `Memcached` - Infers that Memcached might be running on the instance.
- `NGINX` - Infers that NGINX might be running on the instance.
- `PostgreSql` - Infers that PostgreSQL might be running on the instance.
- `Redis` - Infers that Redis might be running on the instance.
- `Kafka` - Infers that Kafka might be running on the instance.
- `SQLServer` - Infers that SQLServer might be running on the instance.

(string)

instanceState -> (string)

The state of the instance when the recommendation was generated.

tags -> (list)

A list of tags assigned to your Amazon EC2 instance recommendations.

(structure)

A list of tag key and value pairs that you define.

key -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

value -> (string)

One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.

externalMetricStatus -> (structure)

An object that describes Compute Optimizerâs integration status with your external metrics provider.

statusCode -> (string)

The status code for Compute Optimizerâs integration with an external metrics provider.

statusReason -> (string)

The reason for Compute Optimizerâs integration status with your external metric provider.

currentInstanceGpuInfo -> (structure)

Describes the GPU accelerator settings for the current instance type.

gpus -> (list)

Describes the GPU accelerators for the instance type.

(structure)

Describes the GPU accelerators for the instance type.

gpuCount -> (integer)

The number of GPUs for the instance type.

gpuMemorySizeInMiB -> (integer)

The total size of the memory for the GPU accelerators for the instance type, in MiB.

idle -> (string)

Describes if an Amazon EC2 instance is idle.

errors -> (list)

An array of objects that describe errors of the request.

For example, an error is returned if you request recommendations for an instance of an unsupported instance family.

(structure)

Describes an error experienced when getting recommendations.

For example, an error is returned if you request recommendations for an unsupported Auto Scaling group, or if you request recommendations for an instance of an unsupported instance family.

identifier -> (string)

The ID of the error.

code -> (string)

The error code.

message -> (string)

The message, or reason, for the error.