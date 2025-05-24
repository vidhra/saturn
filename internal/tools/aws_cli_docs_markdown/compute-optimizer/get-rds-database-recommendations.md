# get-rds-database-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-rds-database-recommendations

## Description

Returns Amazon RDS recommendations.

Compute Optimizer generates recommendations for Amazon RDS that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)

## Synopsis

```
get-rds-database-recommendations
[--resource-arns <value>]
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

`--resource-arns` (list)

The ARN that identifies the Amazon RDS.

The following is the format of the ARN:

`arn:aws:rds:{region}:{accountId}:db:{resourceName}`

The following is the format of a DB Cluster ARN:

`arn:aws:rds:{region}:{accountId}:cluster:{resourceName}`

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token to advance to the next page of Amazon RDS recommendations.

`--max-results` (integer)

The maximum number of Amazon RDS recommendations to return with a single request.

To retrieve the remaining results, make another request with the returned `nextToken` value.

`--filters` (list)

An array of objects to specify a filter that returns a more specific list of Amazon RDS recommendations.

(structure)

Describes a filter that returns a more specific list of Amazon RDS recommendations. Use this filter with the  GetECSServiceRecommendations action.

name -> (string)

The name of the filter.

Specify `Finding` to return recommendations with a specific finding classification.

You can filter your Amazon RDS recommendations by `tag:key` and `tag-key` tags.

A `tag:key` is a key and value combination of a tag assigned to your Amazon RDS recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all Amazon RDS service recommendations that have a tag with the key of `Owner` and the value of `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

A `tag-key` is the key of a tag assigned to your Amazon RDS recommendations. Use this filter to find all of your Amazon RDS recommendations that have a tag with a specific key. This doesnât consider the tag value. For example, you can find your Amazon RDS service recommendations with a tag key value of `Owner` or without any tag keys assigned.

values -> (list)

The value of the filter.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "InstanceFinding"|"InstanceFindingReasonCode"|"StorageFinding"|"StorageFindingReasonCode"|"Idle",
    "values": ["string", ...]
  }
  ...
]
```

`--account-ids` (list)

Return the Amazon RDS recommendations to the specified Amazon Web Services account IDs.

If your account is the management account or the delegated administrator of an organization, use this parameter to return the Amazon RDS recommendations to specific member accounts.

You can only specify one account ID per request.

(string)

Syntax:

```
"string" "string" ...
```

`--recommendation-preferences` (structure)

Describes the recommendation preferences to return in the response of a  GetAutoScalingGroupRecommendations ,  GetEC2InstanceRecommendations ,  GetEC2RecommendationProjectedMetrics ,  GetRDSDatabaseRecommendations , and  GetRDSDatabaseRecommendationProjectedMetrics request.

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

The token to advance to the next page of Amazon RDS recommendations.

rdsDBRecommendations -> (list)

An array of objects that describe the Amazon RDS recommendations.

(structure)

Describes an Amazon RDS recommendation.

resourceArn -> (string)

The ARN of the current Amazon RDS.

The following is the format of the ARN:

`arn:aws:rds:{region}:{accountId}:db:{resourceName}`

accountId -> (string)

The Amazon Web Services account ID of the Amazon RDS.

engine -> (string)

The engine of the RDS instance.

engineVersion -> (string)

The database engine version.

promotionTier -> (integer)

The promotion tier for the Aurora instance.

currentDBInstanceClass -> (string)

The DB instance class of the current RDS instance.

currentStorageConfiguration -> (structure)

The configuration of the current RDS storage.

storageType -> (string)

The type of RDS storage.

allocatedStorage -> (integer)

The size of the RDS storage in gigabytes (GB).

iops -> (integer)

The provisioned IOPs of the RDS storage.

maxAllocatedStorage -> (integer)

The maximum limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the RDS instance.

storageThroughput -> (integer)

The storage throughput of the RDS storage.

dbClusterIdentifier -> (string)

The identifier for DB cluster.

idle -> (string)

This indicates if the RDS instance is idle or not.

instanceFinding -> (string)

The finding classification of an Amazon RDS instance.

Findings for Amazon RDS instance include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendations.html#id1)`Underprovisioned` ** â When Compute Optimizer detects that thereâs not enough resource specifications, an Amazon RDS is considered under-provisioned.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendations.html#id3)`Overprovisioned` ** â When Compute Optimizer detects that thereâs excessive resource specifications, an Amazon RDS is considered over-provisioned.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendations.html#id5)`Optimized` ** â When the specifications of your Amazon RDS instance meet the performance requirements of your workload, the service is considered optimized.

storageFinding -> (string)

The finding classification of Amazon RDS storage.

Findings for Amazon RDS instance include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendations.html#id7)`Underprovisioned` ** â When Compute Optimizer detects that thereâs not enough storage, an Amazon RDS is considered under-provisioned.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendations.html#id9)`Overprovisioned` ** â When Compute Optimizer detects that thereâs excessive storage, an Amazon RDS is considered over-provisioned.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendations.html#id11)`Optimized` ** â When the storage of your Amazon RDS meet the performance requirements of your workload, the service is considered optimized.

instanceFindingReasonCodes -> (list)

The reason for the finding classification of an Amazon RDS instance.

(string)

currentInstancePerformanceRisk -> (string)

The performance risk for the current DB instance.

storageFindingReasonCodes -> (list)

The reason for the finding classification of Amazon RDS storage.

(string)

instanceRecommendationOptions -> (list)

An array of objects that describe the recommendation options for the Amazon RDS instance.

(structure)

Describes the recommendation options for an Amazon RDS instance.

dbInstanceClass -> (string)

Describes the DB instance class recommendation option for your Amazon RDS instance.

projectedUtilizationMetrics -> (list)

An array of objects that describe the projected utilization metrics of the RDS instance recommendation option.

(structure)

Describes the utilization metric of an Amazon RDS.

To determine the performance difference between your current Amazon RDS and the recommended option, compare the utilization metric data of your service against its projected utilization metric data.

name -> (string)

The name of the utilization metric.

statistic -> (string)

The statistic of the utilization metric.

The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.

The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the *Compute Optimizer User Guide* . You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

value -> (double)

The value of the utilization metric.

performanceRisk -> (double)

The performance risk of the RDS instance recommendation option.

rank -> (integer)

The rank identifier of the RDS instance recommendation option.

savingsOpportunity -> (structure)

Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.

Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.

### Warning

Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide* .

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a given resource.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing..

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

savingsOpportunityAfterDiscounts -> (structure)

Describes the savings opportunity for Amazon RDS recommendations or for the recommendation option.

Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizerâs Amazon RDS instance recommendations. This includes any applicable Savings Plans discounts.

estimatedMonthlySavings -> (structure)

The estimated monthly savings possible by adopting Compute Optimizerâs Amazon RDS instance recommendations. This includes any applicable Savings Plans discounts.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings for Amazon RDS instances.

storageRecommendationOptions -> (list)

An array of objects that describe the recommendation options for Amazon RDS storage.

(structure)

Describes the recommendation options for Amazon RDS storage.

storageConfiguration -> (structure)

The recommended storage configuration.

storageType -> (string)

The type of RDS storage.

allocatedStorage -> (integer)

The size of the RDS storage in gigabytes (GB).

iops -> (integer)

The provisioned IOPs of the RDS storage.

maxAllocatedStorage -> (integer)

The maximum limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the RDS instance.

storageThroughput -> (integer)

The storage throughput of the RDS storage.

rank -> (integer)

The rank identifier of the RDS storage recommendation option.

savingsOpportunity -> (structure)

Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.

Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.

### Warning

Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide* .

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a given resource.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing..

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

savingsOpportunityAfterDiscounts -> (structure)

Describes the savings opportunity for Amazon RDS storage recommendations or for the recommendation option.

Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizerâs Amazon RDS storage recommendations. This includes any applicable Savings Plans discounts.

estimatedMonthlySavings -> (structure)

The estimated monthly savings possible by adopting Compute Optimizerâs Amazon RDS storage recommendations. This includes any applicable Savings Plans discounts.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings for Amazon RDS storage.

utilizationMetrics -> (list)

An array of objects that describe the utilization metrics of the Amazon RDS.

(structure)

Describes the utilization metric of an Amazon RDS.

To determine the performance difference between your current Amazon RDS and the recommended option, compare the utilization metric data of your service against its projected utilization metric data.

name -> (string)

The name of the utilization metric.

statistic -> (string)

The statistic of the utilization metric.

The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.

The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the *Compute Optimizer User Guide* . You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

value -> (double)

The value of the utilization metric.

effectiveRecommendationPreferences -> (structure)

Describes the effective recommendation preferences for Amazon RDS.

cpuVendorArchitectures -> (list)

Describes the CPU vendor and architecture for Amazon RDS recommendations.

(string)

enhancedInfrastructureMetrics -> (string)

Describes the activation status of the enhanced infrastructure metrics preference.

A status of `Active` confirms that the preference is applied in the latest recommendation refresh, and a status of `Inactive` confirms that itâs not yet applied to recommendations.

For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

lookBackPeriod -> (string)

The number of days the utilization metrics of the Amazon RDS are analyzed.

savingsEstimationMode -> (structure)

Describes the savings estimation mode preference applied for calculating savings opportunity for Amazon RDS.

source -> (string)

Describes the source for calculating the savings opportunity for Amazon RDS.

lookbackPeriodInDays -> (double)

The number of days the Amazon RDS utilization metrics were analyzed.

lastRefreshTimestamp -> (timestamp)

The timestamp of when the Amazon RDS recommendation was last generated.

tags -> (list)

A list of tags assigned to your Amazon RDS recommendations.

(structure)

A list of tag key and value pairs that you define.

key -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

value -> (string)

One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.

errors -> (list)

An array of objects that describe errors of the request.

(structure)

Describes an error experienced when getting recommendations.

For example, an error is returned if you request recommendations for an unsupported Auto Scaling group, or if you request recommendations for an instance of an unsupported instance family.

identifier -> (string)

The ID of the error.

code -> (string)

The error code.

message -> (string)

The message, or reason, for the error.