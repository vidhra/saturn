# export-auto-scaling-group-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# export-auto-scaling-group-recommendations

## Description

Exports optimization recommendations for Auto Scaling groups.

Recommendations are exported in a comma-separated values (.csv) file, and its metadata in a JavaScript Object Notation (JSON) (.json) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see [Exporting Recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html) in the *Compute Optimizer User Guide* .

You can have only one Auto Scaling group export job in progress per Amazon Web Services Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/ExportAutoScalingGroupRecommendations)

## Synopsis

```
export-auto-scaling-group-recommendations
[--account-ids <value>]
[--filters <value>]
[--fields-to-export <value>]
--s3-destination-config <value>
[--file-format <value>]
[--include-member-accounts | --no-include-member-accounts]
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

The IDs of the Amazon Web Services accounts for which to export Auto Scaling group recommendations.

If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.

This parameter cannot be specified together with the include member accounts parameter. The parameters are mutually exclusive.

Recommendations for member accounts are not included in the export if this parameter, or the include member accounts parameter, is omitted.

You can specify multiple account IDs per request.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

An array of objects to specify a filter that exports a more specific set of Auto Scaling group recommendations.

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
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id1)`CPUOverprovisioned` ** â The instanceâs CPU configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id3)`CPUUnderprovisioned` ** â The instanceâs CPU configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better CPU performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id5)`MemoryOverprovisioned` ** â The instanceâs memory configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id7)`MemoryUnderprovisioned` ** â The instanceâs memory configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better memory performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id9)`EBSThroughputOverprovisioned` ** â The instanceâs EBS throughput configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id11)`EBSThroughputUnderprovisioned` ** â The instanceâs EBS throughput configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id13)`EBSIOPSOverprovisioned` ** â The instanceâs EBS IOPS configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id15)`EBSIOPSUnderprovisioned` ** â The instanceâs EBS IOPS configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better EBS IOPS performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id17)`NetworkBandwidthOverprovisioned` ** â The instanceâs network bandwidth configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id19)`NetworkBandwidthUnderprovisioned` ** â The instanceâs network bandwidth configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better network bandwidth performance. This finding reason happens when the `NetworkIn` or `NetworkOut` performance of an instance is impacted.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id21)`NetworkPPSOverprovisioned` ** â The instanceâs network PPS (packets per second) configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id23)`NetworkPPSUnderprovisioned` ** â The instanceâs network PPS (packets per second) configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better network PPS performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id25)`DiskIOPSOverprovisioned` ** â The instanceâs disk IOPS configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id27)`DiskIOPSUnderprovisioned` ** â The instanceâs disk IOPS configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better disk IOPS performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id29)`DiskThroughputOverprovisioned` ** â The instanceâs disk throughput configuration can be sized down while still meeting the performance requirements of your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html#id31)`DiskThroughputUnderprovisioned` ** â The instanceâs disk throughput configuration doesnât meet the performance requirements of your workload and there is an alternative instance type that provides better disk throughput performance.

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

`--fields-to-export` (list)

The recommendations data to include in the export file. For more information about the fields that can be exported, see [Exported files](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files) in the *Compute Optimizer User Guide* .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  AccountId
  AutoScalingGroupArn
  AutoScalingGroupName
  Finding
  UtilizationMetricsCpuMaximum
  UtilizationMetricsMemoryMaximum
  UtilizationMetricsEbsReadOpsPerSecondMaximum
  UtilizationMetricsEbsWriteOpsPerSecondMaximum
  UtilizationMetricsEbsReadBytesPerSecondMaximum
  UtilizationMetricsEbsWriteBytesPerSecondMaximum
  UtilizationMetricsDiskReadOpsPerSecondMaximum
  UtilizationMetricsDiskWriteOpsPerSecondMaximum
  UtilizationMetricsDiskReadBytesPerSecondMaximum
  UtilizationMetricsDiskWriteBytesPerSecondMaximum
  UtilizationMetricsNetworkInBytesPerSecondMaximum
  UtilizationMetricsNetworkOutBytesPerSecondMaximum
  UtilizationMetricsNetworkPacketsInPerSecondMaximum
  UtilizationMetricsNetworkPacketsOutPerSecondMaximum
  LookbackPeriodInDays
  CurrentConfigurationInstanceType
  CurrentConfigurationDesiredCapacity
  CurrentConfigurationMinSize
  CurrentConfigurationMaxSize
  CurrentConfigurationAllocationStrategy
  CurrentConfigurationMixedInstanceTypes
  CurrentConfigurationType
  CurrentOnDemandPrice
  CurrentStandardOneYearNoUpfrontReservedPrice
  CurrentStandardThreeYearNoUpfrontReservedPrice
  CurrentVCpus
  CurrentMemory
  CurrentStorage
  CurrentNetwork
  RecommendationOptionsConfigurationInstanceType
  RecommendationOptionsConfigurationDesiredCapacity
  RecommendationOptionsConfigurationMinSize
  RecommendationOptionsConfigurationMaxSize
  RecommendationOptionsConfigurationEstimatedInstanceHourReductionPercentage
  RecommendationOptionsConfigurationAllocationStrategy
  RecommendationOptionsConfigurationMixedInstanceTypes
  RecommendationOptionsConfigurationType
  RecommendationOptionsProjectedUtilizationMetricsCpuMaximum
  RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum
  RecommendationOptionsPerformanceRisk
  RecommendationOptionsOnDemandPrice
  RecommendationOptionsStandardOneYearNoUpfrontReservedPrice
  RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice
  RecommendationOptionsVcpus
  RecommendationOptionsMemory
  RecommendationOptionsStorage
  RecommendationOptionsNetwork
  LastRefreshTimestamp
  CurrentPerformanceRisk
  RecommendationOptionsSavingsOpportunityPercentage
  RecommendationOptionsEstimatedMonthlySavingsCurrency
  RecommendationOptionsEstimatedMonthlySavingsValue
  EffectiveRecommendationPreferencesCpuVendorArchitectures
  EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics
  EffectiveRecommendationPreferencesInferredWorkloadTypes
  EffectiveRecommendationPreferencesPreferredResources
  EffectiveRecommendationPreferencesLookBackPeriod
  InferredWorkloadTypes
  RecommendationOptionsMigrationEffort
  CurrentInstanceGpuInfo
  RecommendationOptionsInstanceGpuInfo
  UtilizationMetricsGpuPercentageMaximum
  UtilizationMetricsGpuMemoryPercentageMaximum
  RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum
  RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum
  EffectiveRecommendationPreferencesSavingsEstimationMode
  RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage
  RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts
  RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts
```

`--s3-destination-config` (structure)

An object to specify the destination Amazon Simple Storage Service (Amazon S3) bucket name and key prefix for the export job.

You must create the destination Amazon S3 bucket for your recommendations export before you create the export job. Compute Optimizer does not create the S3 bucket for you. After you create the S3 bucket, ensure that it has the required permissions policy to allow Compute Optimizer to write the export file to it. If you plan to specify an object prefix when you create the export job, you must include the object prefix in the policy that you add to the S3 bucket. For more information, see [Amazon S3 Bucket Policy for Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html) in the *Compute Optimizer User Guide* .

bucket -> (string)

The name of the Amazon S3 bucket to use as the destination for an export job.

keyPrefix -> (string)

The Amazon S3 bucket prefix for an export job.

Shorthand Syntax:

```
bucket=string,keyPrefix=string
```

JSON Syntax:

```
{
  "bucket": "string",
  "keyPrefix": "string"
}
```

`--file-format` (string)

The format of the export file.

The only export file format currently supported is `Csv` .

Possible values:

- `Csv`

`--include-member-accounts` | `--no-include-member-accounts` (boolean)

Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.

The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see [Compute Optimizer and Amazon Web Services Organizations trusted access](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access) in the *Compute Optimizer User Guide* .

Recommendations for member accounts of the organization are not included in the export file if this parameter is omitted.

This parameter cannot be specified together with the account IDs parameter. The parameters are mutually exclusive.

Recommendations for member accounts are not included in the export if this parameter, or the account IDs parameter, is omitted.

`--recommendation-preferences` (structure)

An object to specify the preferences for the Auto Scaling group recommendations to export.

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

jobId -> (string)

The identification number of the export job.

Use the  DescribeRecommendationExportJobs action, and specify the job ID to view the status of an export job.

s3Destination -> (structure)

An object that describes the destination Amazon S3 bucket of a recommendations export file.

bucket -> (string)

The name of the Amazon S3 bucket used as the destination of an export file.

key -> (string)

The Amazon S3 bucket key of an export file.

The key uniquely identifies the object, or export file, in the S3 bucket.

metadataKey -> (string)

The Amazon S3 bucket key of a metadata file.

The key uniquely identifies the object, or metadata file, in the S3 bucket.