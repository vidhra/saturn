# list-recommendation-summariesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cost-optimization-hub/list-recommendation-summaries.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cost-optimization-hub/list-recommendation-summaries.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cost-optimization-hub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cost-optimization-hub/index.html#cli-aws-cost-optimization-hub) ]

# list-recommendation-summaries

## Description

Returns a concise representation of savings estimates for resources. Also returns de-duped savings across different types of recommendations.

### Note

The following filters are not supported for this API: `recommendationIds` , `resourceArns` , and `resourceIds` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)

`list-recommendation-summaries` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
list-recommendation-summaries
[--filter <value>]
--group-by <value>
[--metrics <value>]
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

`--filter` (structure)

Describes a filter that returns a more specific list of recommendations. Filters recommendations by different dimensions.

restartNeeded -> (boolean)

Whether or not implementing the recommendation requires a restart.

rollbackPossible -> (boolean)

Whether or not implementing the recommendation can be rolled back.

implementationEfforts -> (list)

The effort required to implement the recommendation.

(string)

accountIds -> (list)

The account to which the recommendation applies.

(string)

regions -> (list)

The Amazon Web Services Region of the resource.

(string)

resourceTypes -> (list)

The resource type of the recommendation.

(string)

actionTypes -> (list)

The type of action you can take by adopting the recommendation.

(string)

tags -> (list)

A list of tags assigned to the recommendation.

(structure)

The tag structure that contains a tag key and value.

key -> (string)

The key thatâs associated with the tag.

value -> (string)

The value thatâs associated with the tag.

resourceIds -> (list)

The resource ID of the recommendation.

(string)

resourceArns -> (list)

The Amazon Resource Name (ARN) of the recommendation.

(string)

recommendationIds -> (list)

The IDs for the recommendations.

(string)

Shorthand Syntax:

```
restartNeeded=boolean,rollbackPossible=boolean,implementationEfforts=string,string,accountIds=string,string,regions=string,string,resourceTypes=string,string,actionTypes=string,string,tags=[{key=string,value=string},{key=string,value=string}],resourceIds=string,string,resourceArns=string,string,recommendationIds=string,string
```

JSON Syntax:

```
{
  "restartNeeded": true|false,
  "rollbackPossible": true|false,
  "implementationEfforts": ["VeryLow"|"Low"|"Medium"|"High"|"VeryHigh", ...],
  "accountIds": ["string", ...],
  "regions": ["string", ...],
  "resourceTypes": ["Ec2Instance"|"LambdaFunction"|"EbsVolume"|"EcsService"|"Ec2AutoScalingGroup"|"Ec2InstanceSavingsPlans"|"ComputeSavingsPlans"|"SageMakerSavingsPlans"|"Ec2ReservedInstances"|"RdsReservedInstances"|"OpenSearchReservedInstances"|"RedshiftReservedInstances"|"ElastiCacheReservedInstances"|"RdsDbInstanceStorage"|"RdsDbInstance"|"DynamoDbReservedCapacity"|"MemoryDbReservedInstances", ...],
  "actionTypes": ["Rightsize"|"Stop"|"Upgrade"|"PurchaseSavingsPlans"|"PurchaseReservedInstances"|"MigrateToGraviton"|"Delete"|"ScaleIn", ...],
  "tags": [
    {
      "key": "string",
      "value": "string"
    }
    ...
  ],
  "resourceIds": ["string", ...],
  "resourceArns": ["string", ...],
  "recommendationIds": ["string", ...]
}
```

`--group-by` (string)

The grouping of recommendations by a dimension.

`--metrics` (list)

Additional metrics to be returned for the request. The only valid value is `savingsPercentage` .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  SavingsPercentage
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

estimatedTotalDedupedSavings -> (double)

The total overall savings for the aggregated view.

items -> (list)

A list of all savings recommendations.

(structure)

The summary of rightsizing recommendations, including de-duped savings from all types of recommendations.

group -> (string)

The grouping of recommendations.

estimatedMonthlySavings -> (double)

The estimated total savings resulting from modifications, on a monthly basis.

recommendationCount -> (integer)

The total number of instance recommendations.

groupBy -> (string)

The dimension used to group the recommendations by.

currencyCode -> (string)

The currency code used for the recommendation.

metrics -> (structure)

The results or descriptions for the additional metrics, based on whether the metrics were or were not requested.

savingsPercentage -> (string)

The savings percentage based on your Amazon Web Services spend over the past 30 days.

### Note

Savings percentage is only supported when filtering by Region, account ID, or tags.

nextToken -> (string)

The token to retrieve the next set of results.