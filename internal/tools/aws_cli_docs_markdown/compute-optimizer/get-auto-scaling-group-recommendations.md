# get-auto-scaling-group-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-auto-scaling-group-recommendations

## Description

Returns Auto Scaling group recommendations.

Compute Optimizer generates recommendations for Amazon EC2 Auto Scaling groups that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)

## Synopsis

```
get-auto-scaling-group-recommendations
[--account-ids <value>]
[--auto-scaling-group-arns <value>]
[--next-token <value>]
[--max-results <value>]
[--filters <value>]
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

`--account-ids` (list)

The ID of the Amazon Web Services account for which to return Auto Scaling group recommendations.

If your account is the management account of an organization, use this parameter to specify the member account for which you want to return Auto Scaling group recommendations.

Only one account ID can be specified per request.

(string)

Syntax:

```
"string" "string" ...
```

`--auto-scaling-group-arns` (list)

The Amazon Resource Name (ARN) of the Auto Scaling groups for which to return recommendations.

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token to advance to the next page of Auto Scaling group recommendations.

`--max-results` (integer)

The maximum number of Auto Scaling group recommendations to return with a single request.

To retrieve the remaining results, make another request with the returned `nextToken` value.

`--filters` (list)

An array of objects to specify a filter that returns a more specific list of Auto Scaling group recommendations.

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
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id1)`CPUOverprovisioned` ** â The instanceâs CPU configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id3)`CPUUnderprovisioned` ** â The instanceâs CPU configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better CPU performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id5)`MemoryOverprovisioned` ** â The instanceâs memory configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id7)`MemoryUnderprovisioned` ** â The instanceâs memory configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better memory performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id9)`EBSThroughputOverprovisioned` ** â The instanceâs EBS throughput configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id11)`EBSThroughputUnderprovisioned` ** â The instanceâs EBS throughput configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id13)`EBSIOPSOverprovisioned` ** â The instanceâs EBS IOPS configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id15)`EBSIOPSUnderprovisioned` ** â The instanceâs EBS IOPS configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better EBS IOPS performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id17)`NetworkBandwidthOverprovisioned` ** â The instanceâs network bandwidth configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id19)`NetworkBandwidthUnderprovisioned` ** â The instanceâs network bandwidth configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better network bandwidth performance. This finding reason happens when the `NetworkIn` or `NetworkOut` performance of an instance is impacted.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id21)`NetworkPPSOverprovisioned` ** â The instanceâs network PPS (packets per second) configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id23)`NetworkPPSUnderprovisioned` ** â The instanceâs network PPS (packets per second) configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better network PPS performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id25)`DiskIOPSOverprovisioned` ** â The instanceâs disk IOPS configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id27)`DiskIOPSUnderprovisioned` ** â The instanceâs disk IOPS configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better disk IOPS performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id29)`DiskThroughputOverprovisioned` ** â The instanceâs disk throughput configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id31)`DiskThroughputUnderprovisioned` ** â The instanceâs disk throughput configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better disk throughput performance.

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

`--recommendation-preferences` (structure)

An object to specify the preferences for the Auto Scaling group recommendations to return in the response.

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

The token to use to advance to the next page of Auto Scaling group recommendations.

This value is null when there are no more pages of Auto Scaling group recommendations to return.

autoScalingGroupRecommendations -> (list)

An array of objects that describe Auto Scaling group recommendations.

(structure)

Describes an Auto Scaling group recommendation.

accountId -> (string)

The Amazon Web Services account ID of the Auto Scaling group.

autoScalingGroupArn -> (string)

The Amazon Resource Name (ARN) of the Auto Scaling group.

autoScalingGroupName -> (string)

The name of the Auto Scaling group.

finding -> (string)

The finding classification of the Auto Scaling group.

Findings for Auto Scaling groups include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id33)`NotOptimized` ** âAn Auto Scaling group is considered not optimized when Compute Optimizer identifies a recommendation that can provide better performance for your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html#id35)`Optimized` ** âAn Auto Scaling group is considered optimized when Compute Optimizer determines that the group is correctly provisioned to run your workload based on the chosen instance type. For optimized resources, Compute Optimizer might recommend a new generation instance type.

utilizationMetrics -> (list)

An array of objects that describe the utilization metrics of the Auto Scaling group.

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

The number of days for which utilization metrics were analyzed for the Auto Scaling group.

currentConfiguration -> (structure)

An array of objects that describe the current configuration of the Auto Scaling group.

desiredCapacity -> (integer)

The desired capacity, or number of instances, for the EC2 Auto Scaling group.

minSize -> (integer)

The minimum size, or minimum number of instances, for the EC2 Auto Scaling group.

maxSize -> (integer)

The maximum size, or maximum number of instances, for the EC2 Auto Scaling group.

instanceType -> (string)

The instance type for the EC2 Auto Scaling group.

allocationStrategy -> (string)

Describes the allocation strategy that the EC2 Auto Scaling group uses. This field is only available for EC2 Auto Scaling groups with mixed instance types.

estimatedInstanceHourReductionPercentage -> (double)

Describes the projected percentage reduction in instance hours after adopting the recommended configuration. This field is only available for EC2 Auto Scaling groups with scaling policies.

type -> (string)

Describes whether the EC2 Auto Scaling group has a single instance type or a mixed instance type configuration.

mixedInstanceTypes -> (list)

List the instance types within an EC2 Auto Scaling group that has mixed instance types.

(string)

currentInstanceGpuInfo -> (structure)

Describes the GPU accelerator settings for the current instance type of the Auto Scaling group.

gpus -> (list)

Describes the GPU accelerators for the instance type.

(structure)

Describes the GPU accelerators for the instance type.

gpuCount -> (integer)

The number of GPUs for the instance type.

gpuMemorySizeInMiB -> (integer)

The total size of the memory for the GPU accelerators for the instance type, in MiB.

recommendationOptions -> (list)

An array of objects that describe the recommendation options for the Auto Scaling group.

(structure)

Describes a recommendation option for an Auto Scaling group.

configuration -> (structure)

An array of objects that describe an Auto Scaling group configuration.

desiredCapacity -> (integer)

The desired capacity, or number of instances, for the EC2 Auto Scaling group.

minSize -> (integer)

The minimum size, or minimum number of instances, for the EC2 Auto Scaling group.

maxSize -> (integer)

The maximum size, or maximum number of instances, for the EC2 Auto Scaling group.

instanceType -> (string)

The instance type for the EC2 Auto Scaling group.

allocationStrategy -> (string)

Describes the allocation strategy that the EC2 Auto Scaling group uses. This field is only available for EC2 Auto Scaling groups with mixed instance types.

estimatedInstanceHourReductionPercentage -> (double)

Describes the projected percentage reduction in instance hours after adopting the recommended configuration. This field is only available for EC2 Auto Scaling groups with scaling policies.

type -> (string)

Describes whether the EC2 Auto Scaling group has a single instance type or a mixed instance type configuration.

mixedInstanceTypes -> (list)

List the instance types within an EC2 Auto Scaling group that has mixed instance types.

(string)

instanceGpuInfo -> (structure)

Describes the GPU accelerator settings for the recommended instance type of the Auto Scaling group.

gpus -> (list)

Describes the GPU accelerators for the instance type.

(structure)

Describes the GPU accelerators for the instance type.

gpuCount -> (integer)

The number of GPUs for the instance type.

gpuMemorySizeInMiB -> (integer)

The total size of the memory for the GPU accelerators for the instance type, in MiB.

projectedUtilizationMetrics -> (list)

An array of objects that describe the projected utilization metrics of the Auto Scaling group recommendation option.

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

performanceRisk -> (double)

The performance risk of the Auto Scaling group configuration recommendation.

Performance risk indicates the likelihood of the recommended instance type not meeting the resource needs of your workload. Compute Optimizer calculates an individual performance risk score for each specification of the recommended instance, including CPU, memory, EBS throughput, EBS IOPS, disk throughput, disk IOPS, network throughput, and network PPS. The performance risk of the recommended instance is calculated as the maximum performance risk score across the analyzed resource specifications.

The value ranges from `0` - `4` , with `0` meaning that the recommended resource is predicted to always provide enough hardware capability. The higher the performance risk is, the more likely you should validate whether the recommendation will meet the performance requirements of your workload before migrating your resource.

rank -> (integer)

The rank of the Auto Scaling group recommendation option.

The top recommendation option is ranked as `1` .

savingsOpportunity -> (structure)

An object that describes the savings opportunity for the Auto Scaling group recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a given resource.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing..

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

savingsOpportunityAfterDiscounts -> (structure)

An object that describes the savings opportunity for the Auto Scaling group recommendation option that includes Savings Plans and Reserved Instances discounts. Savings opportunity includes the estimated monthly savings and percentage.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost after applying the Savings Plans and Reserved Instances discounts. This saving can be achieved by adopting Compute Optimizerâs Auto Scaling group recommendations.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings possible by adopting Compute Optimizerâs Auto Scaling group recommendations. This is based on the Savings Plans and Reserved Instances pricing discounts.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

migrationEffort -> (string)

The level of effort required to migrate from the current instance type to the recommended instance type.

For example, the migration effort is `Low` if Amazon EMR is the inferred workload type and an Amazon Web Services Graviton instance type is recommended. The migration effort is `Medium` if a workload type couldnât be inferred but an Amazon Web Services Graviton instance type is recommended. The migration effort is `VeryLow` if both the current and recommended instance types are of the same CPU architecture.

lastRefreshTimestamp -> (timestamp)

The timestamp of when the Auto Scaling group recommendation was last generated.

currentPerformanceRisk -> (string)

The risk of the current Auto Scaling group not meeting the performance needs of its workloads. The higher the risk, the more likely the current Auto Scaling group configuration has insufficient capacity and cannot meet workload requirements.

effectiveRecommendationPreferences -> (structure)

An object that describes the effective recommendation preferences for the Auto Scaling group.

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

The applications that might be running on the instances in the Auto Scaling group as inferred by Compute Optimizer.

Compute Optimizer can infer if one of the following applications might be running on the instances:

- `AmazonEmr` - Infers that Amazon EMR might be running on the instances.
- `ApacheCassandra` - Infers that Apache Cassandra might be running on the instances.
- `ApacheHadoop` - Infers that Apache Hadoop might be running on the instances.
- `Memcached` - Infers that Memcached might be running on the instances.
- `NGINX` - Infers that NGINX might be running on the instances.
- `PostgreSql` - Infers that PostgreSQL might be running on the instances.
- `Redis` - Infers that Redis might be running on the instances.
- `Kafka` - Infers that Kafka might be running on the instance.
- `SQLServer` - Infers that SQLServer might be running on the instance.

(string)

errors -> (list)

An array of objects that describe errors of the request.

For example, an error is returned if you request recommendations for an unsupported Auto Scaling group.

(structure)

Describes an error experienced when getting recommendations.

For example, an error is returned if you request recommendations for an unsupported Auto Scaling group, or if you request recommendations for an instance of an unsupported instance family.

identifier -> (string)

The ID of the error.

code -> (string)

The error code.

message -> (string)

The message, or reason, for the error.