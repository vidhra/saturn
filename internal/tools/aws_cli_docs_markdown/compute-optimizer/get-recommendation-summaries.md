# get-recommendation-summariesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-recommendation-summaries.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-recommendation-summaries.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-recommendation-summaries

## Description

Returns the optimization findings for an account.

It returns the number of:

- Amazon EC2 instances in an account that are `Underprovisioned` , `Overprovisioned` , or `Optimized` .
- Auto Scaling groups in an account that are `NotOptimized` , or `Optimized` .
- Amazon EBS volumes in an account that are `NotOptimized` , or `Optimized` .
- Lambda functions in an account that are `NotOptimized` , or `Optimized` .
- Amazon ECS services in an account that are `Underprovisioned` , `Overprovisioned` , or `Optimized` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetRecommendationSummaries)

`get-recommendation-summaries` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `recommendationSummaries`

## Synopsis

```
get-recommendation-summaries
[--account-ids <value>]
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

`--account-ids` (list)

The ID of the Amazon Web Services account for which to return recommendation summaries.

If your account is the management account of an organization, use this parameter to specify the member account for which you want to return recommendation summaries.

Only one account ID can be specified per request.

(string)

Syntax:

```
"string" "string" ...
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

The token to use to advance to the next page of recommendation summaries.

This value is null when there are no more pages of recommendation summaries to return.

recommendationSummaries -> (list)

An array of objects that summarize a recommendation.

(structure)

A summary of a recommendation.

summaries -> (list)

An array of objects that describe a recommendation summary.

(structure)

The summary of a recommendation.

name -> (string)

The finding classification of the recommendation.

value -> (double)

The value of the recommendation summary.

reasonCodeSummaries -> (list)

An array of objects that summarize a finding reason code.

(structure)

A summary of a finding reason code.

name -> (string)

The name of the finding reason code.

value -> (double)

The value of the finding reason code summary.

idleSummaries -> (list)

Describes the findings summary of the idle resources.

(structure)

Describes the findings summary of the idle resources.

name -> (string)

The name of the finding group for the idle resources.

value -> (double)

The count of idle resources in the finding group.

recommendationResourceType -> (string)

The resource type that the recommendation summary applies to.

accountId -> (string)

The Amazon Web Services account ID of the recommendation summary.

savingsOpportunity -> (structure)

An object that describes the savings opportunity for a given resource type. Savings opportunity includes the estimated monthly savings amount and percentage.

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a given resource.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing..

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

idleSavingsOpportunity -> (structure)

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

aggregatedSavingsOpportunity -> (structure)

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

currentPerformanceRiskRatings -> (structure)

An object that describes the performance risk ratings for a given resource type.

high -> (long)

A count of the applicable resource types with a high performance risk rating.

medium -> (long)

A count of the applicable resource types with a medium performance risk rating.

low -> (long)

A count of the applicable resource types with a low performance risk rating.

veryLow -> (long)

A count of the applicable resource types with a very low performance risk rating.

inferredWorkloadSavings -> (list)

An array of objects that describes the estimated monthly saving amounts for the instances running on the specified `inferredWorkloadTypes` . The array contains the top five savings opportunites for the instances that run inferred workload types.

(structure)

The estimated monthly savings after you adjust the configurations of your instances running on the inferred workload types to the recommended configurations. If the `inferredWorkloadTypes` list contains multiple entries, then the savings are the sum of the monthly savings from instances that run the exact combination of the inferred workload types.

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

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing.

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.