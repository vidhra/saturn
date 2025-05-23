# get-ecs-service-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-ecs-service-recommendations

## Description

Returns Amazon ECS service recommendations.

Compute Optimizer generates recommendations for Amazon ECS services on Fargate that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetECSServiceRecommendations)

## Synopsis

```
get-ecs-service-recommendations
[--service-arns <value>]
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

`--service-arns` (list)

The ARN that identifies the Amazon ECS service.

The following is the format of the ARN:

`arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name`

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token to advance to the next page of Amazon ECS service recommendations.

`--max-results` (integer)

The maximum number of Amazon ECS service recommendations to return with a single request.

To retrieve the remaining results, make another request with the returned `nextToken` value.

`--filters` (list)

An array of objects to specify a filter that returns a more specific list of Amazon ECS service recommendations.

(structure)

Describes a filter that returns a more specific list of Amazon ECS service recommendations. Use this filter with the  GetECSServiceRecommendations action.

name -> (string)

The name of the filter.

Specify `Finding` to return recommendations with a specific finding classification.

Specify `FindingReasonCode` to return recommendations with a specific finding reason code.

You can filter your Amazon ECS service recommendations by `tag:key` and `tag-key` tags.

A `tag:key` is a key and value combination of a tag assigned to your Amazon ECS service recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all Amazon ECS service recommendations that have a tag with the key of `Owner` and the value of `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

A `tag-key` is the key of a tag assigned to your Amazon ECS service recommendations. Use this filter to find all of your Amazon ECS service recommendations that have a tag with a specific key. This doesnât consider the tag value. For example, you can find your Amazon ECS service recommendations with a tag key value of `Owner` or without any tag keys assigned.

values -> (list)

The value of the filter.

The valid values for this parameter are as follows:

- If you specify the `name` parameter as `Finding` , specify `Optimized` , `Underprovisioned` , or `Overprovisioned` .
- If you specify the `name` parameter as `FindingReasonCode` , specify `CPUUnderprovisioned` , `CPUOverprovisioned` , `MemoryUnderprovisioned` , or `MemoryOverprovisioned` .

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "Finding"|"FindingReasonCode",
    "values": ["string", ...]
  }
  ...
]
```

`--account-ids` (list)

Return the Amazon ECS service recommendations to the specified Amazon Web Services account IDs.

If your account is the management account or the delegated administrator of an organization, use this parameter to return the Amazon ECS service recommendations to specific member accounts.

You can only specify one account ID per request.

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

The token to advance to the next page of Amazon ECS service recommendations.

ecsServiceRecommendations -> (list)

An array of objects that describe the Amazon ECS service recommendations.

(structure)

Describes an Amazon ECS service recommendation.

serviceArn -> (string)

The Amazon Resource Name (ARN) of the current Amazon ECS service.

The following is the format of the ARN:

`arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name`

accountId -> (string)

The Amazon Web Services account ID of the Amazon ECS service.

currentServiceConfiguration -> (structure)

The configuration of the current Amazon ECS service.

memory -> (integer)

The amount of memory used by the tasks in the Amazon ECS service.

cpu -> (integer)

The number of CPU units used by the tasks in the Amazon ECS service.

containerConfigurations -> (list)

The container configurations within a task of an Amazon ECS service.

(structure)

Describes the container configurations within the tasks of your Amazon ECS service.

containerName -> (string)

The name of the container.

memorySizeConfiguration -> (structure)

The memory size configurations for the container.

memory -> (integer)

The amount of memory in the container.

memoryReservation -> (integer)

The limit of memory reserve for the container.

cpu -> (integer)

The number of CPU units reserved for the container.

autoScalingConfiguration -> (string)

Describes the Auto Scaling configuration methods for an Amazon ECS service. This affects the generated recommendations. For example, if Auto Scaling is configured on a serviceâs CPU, then Compute Optimizer doesnât generate CPU size recommendations.

The Auto Scaling configuration methods include:

- `TARGET_TRACKING_SCALING_CPU` â If the Amazon ECS service is configured to use target scaling on CPU, Compute Optimizer doesnât generate CPU recommendations.
- `TARGET_TRACKING_SCALING_MEMORY` â If the Amazon ECS service is configured to use target scaling on memory, Compute Optimizer doesnât generate memory recommendations.

For more information about step scaling and target scaling, see [Step scaling policies for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) and [Target tracking scaling policies for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide* .

taskDefinitionArn -> (string)

The task definition ARN used by the tasks in the Amazon ECS service.

utilizationMetrics -> (list)

An array of objects that describe the utilization metrics of the Amazon ECS service.

(structure)

Describes the utilization metric of an Amazon ECS service.

To determine the performance difference between your current Amazon ECS service and the recommended option, compare the utilization metric data of your service against its projected utilization metric data.

name -> (string)

The name of the utilization metric.

The following utilization metrics are available:

- `Cpu` â The amount of CPU capacity thatâs used in the service.
- `Memory` â The amount of memory thatâs used in the service.

statistic -> (string)

The statistic of the utilization metric.

The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.

The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the *Compute Optimizer User Guide* . You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

value -> (double)

The value of the utilization metric.

lookbackPeriodInDays -> (double)

The number of days the Amazon ECS service utilization metrics were analyzed.

launchType -> (string)

The launch type the Amazon ECS service is using.

### Note

Compute Optimizer only supports the Fargate launch type.

lastRefreshTimestamp -> (timestamp)

The timestamp of when the Amazon ECS service recommendation was last generated.

finding -> (string)

The finding classification of an Amazon ECS service.

Findings for Amazon ECS services include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html#id1)`Underprovisioned` ** â When Compute Optimizer detects that thereâs not enough memory or CPU, an Amazon ECS service is considered under-provisioned. An under-provisioned service might result in poor application performance.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html#id3)`Overprovisioned` ** â When Compute Optimizer detects that thereâs excessive memory or CPU, an Amazon ECS service is considered over-provisioned. An over-provisioned service might result in additional infrastructure costs.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html#id5)`Optimized` ** â When both the CPU and memory of your Amazon ECS service meet the performance requirements of your workload, the service is considered optimized.

findingReasonCodes -> (list)

The reason for the finding classification of an Amazon ECS service.

Finding reason codes for Amazon ECS services include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html#id7)`CPUUnderprovisioned` ** â The service CPU configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the `CPUUtilization` metric of the current service during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html#id9)`CPUOverprovisioned` ** â The service CPU configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `CPUUtilization` metric of the current service during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html#id11)`MemoryUnderprovisioned` ** â The service memory configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the `MemoryUtilization` metric of the current service during the look-back period.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html#id13)`MemoryOverprovisioned` ** â The service memory configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `MemoryUtilization` metric of the current service during the look-back period.

(string)

serviceRecommendationOptions -> (list)

An array of objects that describe the recommendation options for the Amazon ECS service.

(structure)

Describes the recommendation options for an Amazon ECS service.

memory -> (integer)

The memory size of the Amazon ECS service recommendation option.

cpu -> (integer)

The CPU size of the Amazon ECS service recommendation option.

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

Describes the savings opportunity for Amazon ECS service recommendations or for the recommendation option.

Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizerâs Amazon ECS service recommendations. This includes any applicable Savings Plans discounts.

estimatedMonthlySavings -> (structure)

The estimated monthly savings possible by adopting Compute Optimizerâs Amazon ECS service recommendations. This includes any applicable Savings Plans discounts.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings for Amazon ECS services.

projectedUtilizationMetrics -> (list)

An array of objects that describe the projected utilization metrics of the Amazon ECS service recommendation option.

(structure)

Describes the projected utilization metrics of an Amazon ECS service recommendation option.

To determine the performance difference between your current Amazon ECS service and the recommended option, compare the utilization metric data of your service against its projected utilization metric data.

name -> (string)

The name of the projected utilization metric.

The following utilization metrics are available:

- `Cpu` â The percentage of allocated compute units that are currently in use on the service tasks.
- `Memory` â The percentage of memory thatâs currently in use on the service tasks.

statistic -> (string)

The statistic of the projected utilization metric.

The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.

The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the *Compute Optimizer User Guide* . You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

lowerBoundValue -> (double)

The lower bound values for the projected utilization metrics.

upperBoundValue -> (double)

The upper bound values for the projected utilization metrics.

containerRecommendations -> (list)

The CPU and memory size recommendations for the containers within the task of your Amazon ECS service.

(structure)

The CPU and memory recommendations for a container within the tasks of your Amazon ECS service.

containerName -> (string)

The name of the container.

memorySizeConfiguration -> (structure)

The recommended memory size configurations for the container.

memory -> (integer)

The amount of memory in the container.

memoryReservation -> (integer)

The limit of memory reserve for the container.

cpu -> (integer)

The recommended number of CPU units reserved for the container.

currentPerformanceRisk -> (string)

The risk of the current Amazon ECS service not meeting the performance needs of its workloads. The higher the risk, the more likely the current service canât meet the performance requirements of its workload.

effectiveRecommendationPreferences -> (structure)

Describes the effective recommendation preferences for Amazon ECS services.

savingsEstimationMode -> (structure)

Describes the savings estimation mode preference applied for calculating savings opportunity for Amazon ECS services.

source -> (string)

Describes the source for calculating the savings opportunity for Amazon ECS services.

tags -> (list)

A list of tags assigned to your Amazon ECS service recommendations.

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