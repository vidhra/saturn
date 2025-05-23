# get-ebs-volume-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ebs-volume-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ebs-volume-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-ebs-volume-recommendations

## Description

Returns Amazon Elastic Block Store (Amazon EBS) volume recommendations.

Compute Optimizer generates recommendations for Amazon EBS volumes that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)

## Synopsis

```
get-ebs-volume-recommendations
[--volume-arns <value>]
[--next-token <value>]
[--max-results <value>]
[--filters <value>]
[--account-ids <value>]
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

`--volume-arns` (list)

The Amazon Resource Name (ARN) of the volumes for which to return recommendations.

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token to advance to the next page of volume recommendations.

`--max-results` (integer)

The maximum number of volume recommendations to return with a single request.

To retrieve the remaining results, make another request with the returned `nextToken` value.

`--filters` (list)

An array of objects to specify a filter that returns a more specific list of volume recommendations.

(structure)

Describes a filter that returns a more specific list of Amazon Elastic Block Store (Amazon EBS) volume recommendations. Use this filter with the  GetEBSVolumeRecommendations action.

You can use `LambdaFunctionRecommendationFilter` with the  GetLambdaFunctionRecommendations action, `JobFilter` with the  DescribeRecommendationExportJobs action, and `Filter` with the  GetAutoScalingGroupRecommendations and  GetEC2InstanceRecommendations actions.

name -> (string)

The name of the filter.

Specify `Finding` to return recommendations with a specific finding classification (for example, `NotOptimized` ).

You can filter your Amazon EBS volume recommendations by `tag:key` and `tag-key` tags.

A `tag:key` is a key and value combination of a tag assigned to your Amazon EBS volume recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all Amazon EBS volume recommendations that have a tag with the key of `Owner` and the value of `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

A `tag-key` is the key of a tag assigned to your Amazon EBS volume recommendations. Use this filter to find all of your Amazon EBS volume recommendations that have a tag with a specific key. This doesnât consider the tag value. For example, you can find your Amazon EBS volume recommendations with a tag key value of `Owner` or without any tag keys assigned.

values -> (list)

The value of the filter.

The valid values are `Optimized` , or `NotOptimized` .

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "Finding",
    "values": ["string", ...]
  }
  ...
]
```

`--account-ids` (list)

The ID of the Amazon Web Services account for which to return volume recommendations.

If your account is the management account of an organization, use this parameter to specify the member account for which you want to return volume recommendations.

Only one account ID can be specified per request.

(string)

Syntax:

```
"string" "string" ...
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

The token to use to advance to the next page of volume recommendations.

This value is null when there are no more pages of volume recommendations to return.

volumeRecommendations -> (list)

An array of objects that describe volume recommendations.

(structure)

Describes an Amazon Elastic Block Store (Amazon EBS) volume recommendation.

volumeArn -> (string)

The Amazon Resource Name (ARN) of the current volume.

accountId -> (string)

The Amazon Web Services account ID of the volume.

currentConfiguration -> (structure)

An array of objects that describe the current configuration of the volume.

volumeType -> (string)

The volume type.

The volume types can be the following:

- General Purpose SSD `gp2` and `gp3`
- Provisioned IOPS SSD `io1` , `io2` , and `io2 Block Express`
- Throughput Optimized HDD `st1`
- Cold HDD `sc1`
- Magnetic volumes `standard`

volumeSize -> (integer)

The size of the volume, in GiB.

volumeBaselineIOPS -> (integer)

The baseline IOPS of the volume.

volumeBurstIOPS -> (integer)

The burst IOPS of the volume.

volumeBaselineThroughput -> (integer)

The baseline throughput of the volume.

volumeBurstThroughput -> (integer)

The burst throughput of the volume.

rootVolume -> (boolean)

Contains the image used to boot the instance during launch.

finding -> (string)

The finding classification of the volume.

Findings for volumes include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ebs-volume-recommendations.html#id1)`NotOptimized` ** âA volume is considered not optimized when Compute Optimizer identifies a recommendation that can provide better performance for your workload.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ebs-volume-recommendations.html#id3)`Optimized` ** âAn volume is considered optimized when Compute Optimizer determines that the volume is correctly provisioned to run your workload based on the chosen volume type. For optimized resources, Compute Optimizer might recommend a new generation volume type.

utilizationMetrics -> (list)

An array of objects that describe the utilization metrics of the volume.

(structure)

Describes a utilization metric of an Amazon Elastic Block Store (Amazon EBS) volume.

Compare the utilization metric data of your resource against its projected utilization metric data to determine the performance difference between your current resource and the recommended option.

name -> (string)

The name of the utilization metric.

The following utilization metrics are available:

- `VolumeReadOpsPerSecond` - The completed read operations per second from the volume in a specified period of time. Unit: Count
- `VolumeWriteOpsPerSecond` - The completed write operations per second to the volume in a specified period of time. Unit: Count
- `VolumeReadBytesPerSecond` - The bytes read per second from the volume in a specified period of time. Unit: Bytes
- `VolumeWriteBytesPerSecond` - The bytes written to the volume in a specified period of time. Unit: Bytes

statistic -> (string)

The statistic of the utilization metric.

The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.

The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the *Compute Optimizer User Guide* . You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

value -> (double)

The value of the utilization metric.

lookBackPeriodInDays -> (double)

The number of days for which utilization metrics were analyzed for the volume.

volumeRecommendationOptions -> (list)

An array of objects that describe the recommendation options for the volume.

(structure)

Describes a recommendation option for an Amazon Elastic Block Store (Amazon EBS) instance.

configuration -> (structure)

An array of objects that describe a volume configuration.

volumeType -> (string)

The volume type.

The volume types can be the following:

- General Purpose SSD `gp2` and `gp3`
- Provisioned IOPS SSD `io1` , `io2` , and `io2 Block Express`
- Throughput Optimized HDD `st1`
- Cold HDD `sc1`
- Magnetic volumes `standard`

volumeSize -> (integer)

The size of the volume, in GiB.

volumeBaselineIOPS -> (integer)

The baseline IOPS of the volume.

volumeBurstIOPS -> (integer)

The burst IOPS of the volume.

volumeBaselineThroughput -> (integer)

The baseline throughput of the volume.

volumeBurstThroughput -> (integer)

The burst throughput of the volume.

rootVolume -> (boolean)

Contains the image used to boot the instance during launch.

performanceRisk -> (double)

The performance risk of the volume recommendation option.

Performance risk is the likelihood of the recommended volume type meeting the performance requirement of your workload.

The value ranges from `0` - `4` , with `0` meaning that the recommended resource is predicted to always provide enough hardware capability. The higher the performance risk is, the more likely you should validate whether the recommendation will meet the performance requirements of your workload before migrating your resource.

rank -> (integer)

The rank of the volume recommendation option.

The top recommendation option is ranked as `1` .

savingsOpportunity -> (structure)

An object that describes the savings opportunity for the EBS volume recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a given resource.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing..

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

savingsOpportunityAfterDiscounts -> (structure)

An object that describes the savings opportunity for the Amazon EBS volume recommendation option with specific discounts. Savings opportunity includes the estimated monthly savings and percentage.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost after applying the specific discounts. This saving can be achieved by adopting Compute Optimizerâs Amazon EBS volume recommendations.

estimatedMonthlySavings -> (structure)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizerâs Amazon EBS volume recommendations. This saving includes any applicable discounts.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

lastRefreshTimestamp -> (timestamp)

The timestamp of when the volume recommendation was last generated.

currentPerformanceRisk -> (string)

The risk of the current EBS volume not meeting the performance needs of its workloads. The higher the risk, the more likely the current EBS volume doesnât have sufficient capacity.

effectiveRecommendationPreferences -> (structure)

Describes the effective recommendation preferences for Amazon EBS volume.

savingsEstimationMode -> (structure)

Describes the savings estimation mode preference applied for calculating savings opportunity for Amazon EBS volumes.

source -> (string)

Describes the source for calculating the savings opportunity for Amazon EBS volumes.

tags -> (list)

A list of tags assigned to your Amazon EBS volume recommendations.

(structure)

A list of tag key and value pairs that you define.

key -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

value -> (string)

One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.

errors -> (list)

An array of objects that describe errors of the request.

For example, an error is returned if you request recommendations for an unsupported volume.

(structure)

Describes an error experienced when getting recommendations.

For example, an error is returned if you request recommendations for an unsupported Auto Scaling group, or if you request recommendations for an instance of an unsupported instance family.

identifier -> (string)

The ID of the error.

code -> (string)

The error code.

message -> (string)

The message, or reason, for the error.