# get-idle-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-idle-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-idle-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-idle-recommendations

## Description

Returns idle resource recommendations. Compute Optimizer generates recommendations for idle resources that meet a specific set of requirements. For more information, see [Resource requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the *Compute Optimizer User Guide*

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetIdleRecommendations)

## Synopsis

```
get-idle-recommendations
[--resource-arns <value>]
[--next-token <value>]
[--max-results <value>]
[--filters <value>]
[--account-ids <value>]
[--order-by <value>]
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

The ARN that identifies the idle resource.

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token to advance to the next page of idle resource recommendations.

`--max-results` (integer)

The maximum number of idle resource recommendations to return with a single request.

To retrieve the remaining results, make another request with the returned `nextToken` value.

`--filters` (list)

An array of objects to specify a filter that returns a more specific list of idle resource recommendations.

(structure)

Describes a filter that returns a more specific list of idle resource recommendations.

name -> (string)

The name of the filter.

Specify `Finding` to return recommendations with a specific finding classification.

You can filter your idle resource recommendations by `tag:key` and `tag-key` tags.

A `tag:key` is a key and value combination of a tag assigned to your idle resource recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all idle resource service recommendations that have a tag with the key of `Owner` and the value of `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

A `tag-key` is the key of a tag assigned to your idle resource recommendations. Use this filter to find all of your idle resource recommendations that have a tag with a specific key. This doesnât consider the tag value. For example, you can find your idle resource service recommendations with a tag key value of `Owner` or without any tag keys assigned.

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
    "name": "Finding"|"ResourceType",
    "values": ["string", ...]
  }
  ...
]
```

`--account-ids` (list)

Return the idle resource recommendations to the specified Amazon Web Services account IDs.

If your account is the management account or the delegated administrator of an organization, use this parameter to return the idle resource recommendations to specific member accounts.

You can only specify one account ID per request.

(string)

Syntax:

```
"string" "string" ...
```

`--order-by` (structure)

The order to sort the idle resource recommendations.

dimension -> (string)

The dimension values to sort the recommendations.

order -> (string)

The order to sort the recommendations.

Shorthand Syntax:

```
dimension=string,order=string
```

JSON Syntax:

```
{
  "dimension": "SavingsValue"|"SavingsValueAfterDiscount",
  "order": "Asc"|"Desc"
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

The token to advance to the next page of idle resource recommendations.

idleRecommendations -> (list)

An array of objects that describe the idle resource recommendations.

(structure)

Describes an Idle resource recommendation.

resourceArn -> (string)

The ARN of the current idle resource.

resourceId -> (string)

The unique identifier for the resource.

resourceType -> (string)

The type of resource that is idle.

accountId -> (string)

The Amazon Web Services account ID of the idle resource.

finding -> (string)

The finding classification of an idle resource.

findingDescription -> (string)

A summary of the findings for the resource.

savingsOpportunity -> (structure)

The savings opportunity for the idle resource.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizerâs idle resource recommendations.

estimatedMonthlySavings -> (structure)

The estimated monthly savings possible by adopting Compute Optimizerâs idle resource recommendations.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings for Idle resources.

savingsOpportunityAfterDiscounts -> (structure)

The savings opportunity for the idle resource after any applying discounts.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizerâs idle resource recommendations. This includes any applicable discounts.

estimatedMonthlySavings -> (structure)

The estimated monthly savings possible by adopting Compute Optimizerâs idle resource recommendations. This includes any applicable discounts.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings for Idle resources.

utilizationMetrics -> (list)

An array of objects that describe the utilization metrics of the idle resource.

(structure)

Describes the utilization metric of an idle resource.

name -> (string)

The name of the utilization metric.

statistic -> (string)

The statistic of the utilization metric.

The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.

The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the *Compute Optimizer User Guide* . You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

value -> (double)

The value of the utilization metric.

lookBackPeriodInDays -> (double)

The number of days the idle resource utilization metrics were analyzed.

lastRefreshTimestamp -> (timestamp)

The timestamp of when the idle resource recommendation was last generated.

tags -> (list)

A list of tags assigned to your idle resource recommendations.

(structure)

A list of tag key and value pairs that you define.

key -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

value -> (string)

One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.

errors -> (list)

An array of objects that describe errors of the request.

(structure)

Returns of list of resources that doesnât have idle recommendations.

identifier -> (string)

The ID of the error.

code -> (string)

The error code.

message -> (string)

The error message.

resourceType -> (string)

The type of resource associated with the error.