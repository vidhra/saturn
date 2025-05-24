# describe-resource-collection-healthÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-resource-collection-health.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-resource-collection-health.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devops-guru](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/index.html#cli-aws-devops-guru) ]

# describe-resource-collection-health

## Description

Returns the number of open proactive insights, open reactive insights, and the Mean Time to Recover (MTTR) for all closed insights in resource collections in your account. You specify the type of Amazon Web Services resources collection. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag *key* . You can specify up to 500 Amazon Web Services CloudFormation stacks.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devops-guru-2020-12-01/DescribeResourceCollectionHealth)

`describe-resource-collection-health` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `CloudFormation`, `Service`, `Tags`

## Synopsis

```
describe-resource-collection-health
--resource-collection-type <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--resource-collection-type` (string)

An Amazon Web Services resource collection type. This type specifies how analyzed Amazon Web Services resources are defined. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag *key* . You can specify up to 500 Amazon Web Services CloudFormation stacks.

Possible values:

- `AWS_CLOUD_FORMATION`
- `AWS_SERVICE`
- `AWS_TAGS`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

CloudFormation -> (list)

The returned `CloudFormationHealthOverview` object that contains an `InsightHealthOverview` object with the requested system health information.

(structure)

Information about the health of Amazon Web Services resources in your account that are specified by an Amazon Web Services CloudFormation stack.

StackName -> (string)

The name of the CloudFormation stack.

Insight -> (structure)

Information about the health of the Amazon Web Services resources in your account that are specified by an Amazon Web Services CloudFormation stack, including the number of open proactive, open reactive insights, and the Mean Time to Recover (MTTR) of closed insights.

OpenProactiveInsights -> (integer)

The number of open proactive insights.

OpenReactiveInsights -> (integer)

The number of open reactive insights.

MeanTimeToRecoverInMilliseconds -> (long)

The Meant Time to Recover (MTTR) for the insight.

AnalyzedResourceCount -> (long)

Number of resources that DevOps Guru is monitoring in your account that are specified by an Amazon Web Services CloudFormation stack.

Service -> (list)

An array of `ServiceHealth` objects that describes the health of the Amazon Web Services services associated with the resources in the collection.

(structure)

Represents the health of an Amazon Web Services service.

ServiceName -> (string)

The name of the Amazon Web Services service.

Insight -> (structure)

Represents the health of an Amazon Web Services service. This is a `ServiceInsightHealth` that contains the number of open proactive and reactive insights for this service.

OpenProactiveInsights -> (integer)

The number of open proactive insights in the Amazon Web Services service

OpenReactiveInsights -> (integer)

The number of open reactive insights in the Amazon Web Services service

AnalyzedResourceCount -> (long)

Number of resources that DevOps Guru is monitoring in an analyzed Amazon Web Services service.

NextToken -> (string)

The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.

Tags -> (list)

The Amazon Web Services tags that are used by resources in the resource collection.

Tags help you identify and organize your Amazon Web Services resources. Many Amazon Web Services services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an Lambda function. For more information about using tags, see the [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) whitepaper.

Each Amazon Web Services tag has two parts.

- A tag *key* (for example, `CostCenter` , `Environment` , `Project` , or `Secret` ). Tag *keys* are case-sensitive.
- An optional field known as a tag *value* (for example, `111122223333` , `Production` , or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive.

Together these are known as *key* -*value* pairs.

### Warning

The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix `Devops-guru-` . The tag *key* might be `DevOps-Guru-deployment-application` or `devops-guru-rds-application` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS` , and these act as two different *keys* . Possible *key* /*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers` .

(structure)

Information about the health of Amazon Web Services resources in your account that are specified by an Amazon Web Services tag *key* .

AppBoundaryKey -> (string)

An Amazon Web Services tag *key* that is used to identify the Amazon Web Services resources that DevOps Guru analyzes. All Amazon Web Services resources in your account and Region tagged with this *key* make up your DevOps Guru application and analysis boundary.

### Warning

The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix `Devops-guru-` . The tag *key* might be `DevOps-Guru-deployment-application` or `devops-guru-rds-application` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS` , and these act as two different *keys* . Possible *key* /*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers` .

TagValue -> (string)

The value in an Amazon Web Services tag.

The tagâs *value* is an optional field used to associate a string with the tag *key* (for example, `111122223333` , `Production` , or a team name). The *key* and *value* are the tagâs *key* pair. Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive. You can specify a maximum of 256 characters for a tag value.

Insight -> (structure)

Information about the health of the Amazon Web Services resources in your account that are specified by an Amazon Web Services tag, including the number of open proactive, open reactive insights, and the Mean Time to Recover (MTTR) of closed insights.

OpenProactiveInsights -> (integer)

The number of open proactive insights.

OpenReactiveInsights -> (integer)

The number of open reactive insights.

MeanTimeToRecoverInMilliseconds -> (long)

The Meant Time to Recover (MTTR) for the insight.

AnalyzedResourceCount -> (long)

Number of resources that DevOps Guru is monitoring in your account that are specified by an Amazon Web Services tag.