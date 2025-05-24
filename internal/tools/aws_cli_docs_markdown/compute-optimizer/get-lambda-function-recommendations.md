# get-lambda-function-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-lambda-function-recommendations

## Description

Returns Lambda function recommendations.

Compute Optimizer generates recommendations for functions that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)

`get-lambda-function-recommendations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `lambdaFunctionRecommendations`

## Synopsis

```
get-lambda-function-recommendations
[--function-arns <value>]
[--account-ids <value>]
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--function-arns` (list)

The Amazon Resource Name (ARN) of the functions for which to return recommendations.

You can specify a qualified or unqualified ARN. If you specify an unqualified ARN without a function version suffix, Compute Optimizer will return recommendations for the latest (`$LATEST` ) version of the function. If you specify a qualified ARN with a version suffix, Compute Optimizer will return recommendations for the specified function version. For more information about using function versions, see [Using versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html#versioning-versions-using) in the *Lambda Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--account-ids` (list)

The ID of the Amazon Web Services account for which to return function recommendations.

If your account is the management account of an organization, use this parameter to specify the member account for which you want to return function recommendations.

Only one account ID can be specified per request.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

An array of objects to specify a filter that returns a more specific list of function recommendations.

(structure)

Describes a filter that returns a more specific list of Lambda function recommendations. Use this filter with the  GetLambdaFunctionRecommendations action.

You can use `EBSFilter` with the  GetEBSVolumeRecommendations action, `JobFilter` with the  DescribeRecommendationExportJobs action, and `Filter` with the  GetAutoScalingGroupRecommendations and  GetEC2InstanceRecommendations actions.

name -> (string)

The name of the filter.

Specify `Finding` to return recommendations with a specific finding classification (for example, `NotOptimized` ).

Specify `FindingReasonCode` to return recommendations with a specific finding reason code (for example, `MemoryUnderprovisioned` ).

You can filter your Lambda function recommendations by `tag:key` and `tag-key` tags.

A `tag:key` is a key and value combination of a tag assigned to your Lambda function recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all Lambda function recommendations that have a tag with the key of `Owner` and the value of `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

A `tag-key` is the key of a tag assigned to your Lambda function recommendations. Use this filter to find all of your Lambda function recommendations that have a tag with a specific key. This doesnât consider the tag value. For example, you can find your Lambda function recommendations with a tag key value of `Owner` or without any tag keys assigned.

values -> (list)

The value of the filter.

The valid values for this parameter are as follows, depending on what you specify for the `name` parameter:

- Specify `Optimized` , `NotOptimized` , or `Unavailable` if you specify the `name` parameter as `Finding` .
- Specify `MemoryOverprovisioned` , `MemoryUnderprovisioned` , `InsufficientData` , or `Inconclusive` if you specify the `name` parameter as `FindingReasonCode` .

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

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

The token to use to advance to the next page of function recommendations.

This value is null when there are no more pages of function recommendations to return.

lambdaFunctionRecommendations -> (list)

An array of objects that describe function recommendations.

(structure)

Describes an Lambda function recommendation.

functionArn -> (string)

The Amazon Resource Name (ARN) of the current function.

functionVersion -> (string)

The version number of the current function.

accountId -> (string)

The Amazon Web Services account ID of the function.

currentMemorySize -> (integer)

The amount of memory, in MB, thatâs allocated to the current function.

numberOfInvocations -> (long)

The number of times your function code was applied during the look-back period.

utilizationMetrics -> (list)

An array of objects that describe the utilization metrics of the function.

(structure)

Describes a utilization metric of an Lambda function.

name -> (string)

The name of the utilization metric.

The following utilization metrics are available:

- `Duration` - The amount of time that your function code spends processing an event.
- `Memory` - The amount of memory used per invocation.

statistic -> (string)

The statistic of the utilization metric.

The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.

The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the *Compute Optimizer User Guide* . You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

value -> (double)

The value of the utilization metric.

lookbackPeriodInDays -> (double)

The number of days for which utilization metrics were analyzed for the function.

lastRefreshTimestamp -> (timestamp)

The timestamp of when the function recommendation was last generated.

finding -> (string)

The finding classification of the function.

Findings for functions include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html#id1)`Optimized` ** â The function is correctly provisioned to run your workload based on its current configuration and its utilization history. This finding classification does not include finding reason codes.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html#id3)`NotOptimized` ** â The function is performing at a higher level (over-provisioned) or at a lower level (under-provisioned) than required for your workload because its current configuration is not optimal. Over-provisioned resources might lead to unnecessary infrastructure cost, and under-provisioned resources might lead to poor application performance. This finding classification can include the `MemoryUnderprovisioned` and `MemoryUnderprovisioned` finding reason codes.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html#id5)`Unavailable` ** â Compute Optimizer was unable to generate a recommendation for the function. This could be because the function has not accumulated sufficient metric data, or the function does not qualify for a recommendation. This finding classification can include the `InsufficientData` and `Inconclusive` finding reason codes.

### Note

Functions with a finding of unavailable are not returned unless you specify the `filter` parameter with a value of `Unavailable` in your `GetLambdaFunctionRecommendations` request.

findingReasonCodes -> (list)

The reason for the finding classification of the function.

### Note

Functions that have a finding classification of `Optimized` donât have a finding reason code.

Finding reason codes for functions include:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html#id7)`MemoryOverprovisioned` ** â The function is over-provisioned when its memory configuration can be sized down while still meeting the performance requirements of your workload. An over-provisioned function might lead to unnecessary infrastructure cost. This finding reason code is part of the `NotOptimized` finding classification.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html#id9)`MemoryUnderprovisioned` ** â The function is under-provisioned when its memory configuration doesnât meet the performance requirements of the workload. An under-provisioned function might lead to poor application performance. This finding reason code is part of the `NotOptimized` finding classification.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html#id11)`InsufficientData` ** â The function does not have sufficient metric data for Compute Optimizer to generate a recommendation. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the *Compute Optimizer User Guide* . This finding reason code is part of the `Unavailable` finding classification.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html#id13)`Inconclusive` ** â The function does not qualify for a recommendation because Compute Optimizer cannot generate a recommendation with a high degree of confidence. This finding reason code is part of the `Unavailable` finding classification.

(string)

memorySizeRecommendationOptions -> (list)

An array of objects that describe the memory configuration recommendation options for the function.

(structure)

Describes a recommendation option for an Lambda function.

rank -> (integer)

The rank of the function recommendation option.

The top recommendation option is ranked as `1` .

memorySize -> (integer)

The memory size, in MB, of the function recommendation option.

projectedUtilizationMetrics -> (list)

An array of objects that describe the projected utilization metrics of the function recommendation option.

(structure)

Describes a projected utilization metric of an Lambda function recommendation option.

name -> (string)

The name of the projected utilization metric.

statistic -> (string)

The statistic of the projected utilization metric.

value -> (double)

The values of the projected utilization metrics.

savingsOpportunity -> (structure)

An object that describes the savings opportunity for the Lambda function recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a given resource.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing..

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

savingsOpportunityAfterDiscounts -> (structure)

An object that describes the savings opportunity for the Lambda recommendation option which includes Saving Plans discounts. Savings opportunity includes the estimated monthly savings and percentage.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizerâs Lambda function recommendations. This includes any applicable Savings Plans discounts.

estimatedMonthlySavings -> (structure)

The estimated monthly savings possible by adopting Compute Optimizerâs Lambda function recommendations. This includes any applicable Savings Plans discounts.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

currentPerformanceRisk -> (string)

The risk of the current Lambda function not meeting the performance needs of its workloads. The higher the risk, the more likely the current Lambda function requires more memory.

effectiveRecommendationPreferences -> (structure)

Describes the effective recommendation preferences for Lambda functions.

savingsEstimationMode -> (structure)

Describes the savings estimation mode applied for calculating savings opportunity for Lambda functions.

source -> (string)

Describes the source for calculation of savings opportunity for Lambda functions.

tags -> (list)

A list of tags assigned to your Lambda function recommendations.

(structure)

A list of tag key and value pairs that you define.

key -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

value -> (string)

One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.