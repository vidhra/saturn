# list-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devops-guru](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/index.html#cli-aws-devops-guru) ]

# list-recommendations

## Description

Returns a list of a specified insightâs recommendations. Each recommendation includes a list of related metrics and a list of related events.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devops-guru-2020-12-01/ListRecommendations)

`list-recommendations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Recommendations`

## Synopsis

```
list-recommendations
--insight-id <value>
[--locale <value>]
[--account-id <value>]
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

`--insight-id` (string)

The ID of the requested insight.

`--locale` (string)

A locale that specifies the language to use for recommendations.

Possible values:

- `DE_DE`
- `EN_US`
- `EN_GB`
- `ES_ES`
- `FR_FR`
- `IT_IT`
- `JA_JP`
- `KO_KR`
- `PT_BR`
- `ZH_CN`
- `ZH_TW`

`--account-id` (string)

The ID of the Amazon Web Services account.

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

Recommendations -> (list)

An array of the requested recommendations.

(structure)

Recommendation information to help you remediate detected anomalous behavior that generated an insight.

Description -> (string)

A description of the problem.

Link -> (string)

A hyperlink to information to help you address the problem.

Name -> (string)

The name of the recommendation.

Reason -> (string)

The reason DevOps Guru flagged the anomalous behavior as a problem.

RelatedEvents -> (list)

Events that are related to the problem. Use these events to learn more about whatâs happening and to help address the issue.

(structure)

Information about an event that is related to a recommendation.

Name -> (string)

The name of the event. This corresponds to the `Name` field in an `Event` object.

Resources -> (list)

A `ResourceCollection` object that contains arrays of the names of Amazon Web Services CloudFormation stacks. You can specify up to 500 Amazon Web Services CloudFormation stacks.

(structure)

Information about an Amazon Web Services resource that emitted and event that is related to a recommendation in an insight.

Name -> (string)

The name of the resource that emitted the event. This corresponds to the `Name` field in an `EventResource` object.

Type -> (string)

The type of the resource that emitted the event. This corresponds to the `Type` field in an `EventResource` object.

RelatedAnomalies -> (list)

Anomalies that are related to the problem. Use these Anomalies to learn more about whatâs happening and to help address the issue.

(structure)

Information about an anomaly that is related to a recommendation.

Resources -> (list)

An array of objects that represent resources in which DevOps Guru detected anomalous behavior. Each object contains the name and type of the resource.

(structure)

Information about a resource in which DevOps Guru detected anomalous behavior.

Name -> (string)

The name of the resource.

Type -> (string)

The type of the resource. Resource types take the same form that is used by Amazon Web Services CloudFormation resource type identifiers, `service-provider::service-name::data-type-name` . For example, `AWS::RDS::DBCluster` . For more information, see [Amazon Web Services resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the *Amazon Web Services CloudFormation User Guide* .

SourceDetails -> (list)

Information about where the anomalous behavior related the recommendation was found. For example, details in Amazon CloudWatch metrics.

(structure)

Contains an array of `RecommendationRelatedCloudWatchMetricsSourceDetail` objects that contain the name and namespace of an Amazon CloudWatch metric.

CloudWatchMetrics -> (list)

An array of `CloudWatchMetricsDetail` objects that contains information about the analyzed metrics that displayed anomalous behavior.

(structure)

Information about an Amazon CloudWatch metric that is analyzed by DevOps Guru. It is one of many analyzed metrics that are used to generate insights.

MetricName -> (string)

The name of the CloudWatch metric.

Namespace -> (string)

The namespace of the CloudWatch metric. A namespace is a container for CloudWatch metrics.

AnomalyId -> (string)

The ID of an anomaly that generated the insight with this recommendation.

Category -> (string)

The category type of the recommendation.

NextToken -> (string)

The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.