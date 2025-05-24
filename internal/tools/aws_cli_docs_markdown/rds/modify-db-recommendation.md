# modify-db-recommendationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-recommendation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-recommendation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# modify-db-recommendation

## Description

Updates the recommendation status and recommended action status for the specified recommendation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/ModifyDBRecommendation)

## Synopsis

```
modify-db-recommendation
--recommendation-id <value>
[--locale <value>]
[--status <value>]
[--recommended-action-updates <value>]
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

`--recommendation-id` (string)

The identifier of the recommendation to update.

`--locale` (string)

The language of the modified recommendation.

`--status` (string)

The recommendation status to update.

Valid values:

- active
- dismissed

`--recommended-action-updates` (list)

The list of recommended action status to update. You can update multiple recommended actions at one time.

(structure)

The recommended status to update for the specified recommendation action ID.

ActionId -> (string)

A unique identifier of the updated recommendation action.

Status -> (string)

The status of the updated recommendation action.

- `applied`
- `scheduled`

Shorthand Syntax:

```
ActionId=string,Status=string ...
```

JSON Syntax:

```
[
  {
    "ActionId": "string",
    "Status": "string"
  }
  ...
]
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

DBRecommendation -> (structure)

The recommendation for your DB instances, DB clusters, and DB parameter groups.

RecommendationId -> (string)

The unique identifier of the recommendation.

TypeId -> (string)

A value that indicates the type of recommendation. This value determines how the description is rendered.

Severity -> (string)

The severity level of the recommendation. The severity level can help you decide the urgency with which to address the recommendation.

Valid values:

- `high`
- `medium`
- `low`
- `informational`

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the RDS resource associated with the recommendation.

Status -> (string)

The current status of the recommendation.

Valid values:

- `active` - The recommendations which are ready for you to apply.
- `pending` - The applied or scheduled recommendations which are in progress.
- `resolved` - The recommendations which are completed.
- `dismissed` - The recommendations that you dismissed.

CreatedTime -> (timestamp)

The time when the recommendation was created. For example, `2023-09-28T01:13:53.931000+00:00` .

UpdatedTime -> (timestamp)

The time when the recommendation was last updated.

Detection -> (string)

A short description of the issue identified for this recommendation. The description might contain markdown.

Recommendation -> (string)

A short description of the recommendation to resolve an issue. The description might contain markdown.

Description -> (string)

A detailed description of the recommendation. The description might contain markdown.

Reason -> (string)

The reason why this recommendation was created. The information might contain markdown.

RecommendedActions -> (list)

A list of recommended actions.

(structure)

The recommended actions to apply to resolve the issues associated with your DB instances, DB clusters, and DB parameter groups.

ActionId -> (string)

The unique identifier of the recommended action.

Title -> (string)

A short description to summarize the action. The description might contain markdown.

Description -> (string)

A detailed description of the action. The description might contain markdown.

Operation -> (string)

An API operation for the action.

Parameters -> (list)

The parameters for the API operation.

(structure)

A single parameter to use with the `RecommendedAction` API operation to apply the action.

Key -> (string)

The key of the parameter to use with the `RecommendedAction` API operation.

Value -> (string)

The value of the parameter to use with the `RecommendedAction` API operation.

ApplyModes -> (list)

The methods to apply the recommended action.

Valid values:

- `manual` - The action requires you to resolve the recommendation manually.
- `immediately` - The action is applied immediately.
- `next-maintainance-window` - The action is applied during the next scheduled maintainance.

(string)

Status -> (string)

The status of the action.

- `ready`
- `applied`
- `scheduled`
- `resolved`

IssueDetails -> (structure)

The details of the issue.

PerformanceIssueDetails -> (structure)

A detailed description of the issue when the recommendation category is `performance` .

StartTime -> (timestamp)

The time when the performance issue started.

EndTime -> (timestamp)

The time when the performance issue stopped.

Metrics -> (list)

The metrics that are relevant to the performance issue.

(structure)

The representation of a metric.

Name -> (string)

The name of a metric.

References -> (list)

A list of metric references (thresholds).

(structure)

The reference (threshold) for a metric.

Name -> (string)

The name of the metric reference.

ReferenceDetails -> (structure)

The details of a performance issue.

ScalarReferenceDetails -> (structure)

The metric reference details when the reference is a scalar.

Value -> (double)

The value of a scalar reference.

StatisticsDetails -> (string)

The details of different statistics for a metric. The description might contain markdown.

MetricQuery -> (structure)

The query to retrieve metric data points.

PerformanceInsightsMetricQuery -> (structure)

The Performance Insights query that you can use to retrieve Performance Insights metric data points.

GroupBy -> (structure)

A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this list isnât included, then all of the dimensions in the group were requested, or are present in the response.

(string)

Group -> (string)

The available dimension groups for Performance Insights metric type.

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Metric -> (string)

The name of a Performance Insights metric to be measured.

Valid Values:

- `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - The raw number of active sessions for the database engine.
- The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon Aurora User Guide* .

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

Analysis -> (string)

The analysis of the performance issue. The information might contain markdown.

ContextAttributes -> (list)

The supporting attributes to explain the recommended action.

(structure)

The additional attributes of `RecommendedAction` data type.

Key -> (string)

The key of `ContextAttribute` .

Value -> (string)

The value of `ContextAttribute` .

Category -> (string)

The category of the recommendation.

Valid values:

- `performance efficiency`
- `security`
- `reliability`
- `cost optimization`
- `operational excellence`
- `sustainability`

Source -> (string)

The Amazon Web Services service that generated the recommendations.

TypeDetection -> (string)

A short description of the recommendation type. The description might contain markdown.

TypeRecommendation -> (string)

A short description that summarizes the recommendation to fix all the issues of the recommendation type. The description might contain markdown.

Impact -> (string)

A short description that explains the possible impact of an issue.

AdditionalInfo -> (string)

Additional information about the recommendation. The information might contain markdown.

Links -> (list)

A link to documentation that provides additional information about the recommendation.

(structure)

A link to documentation that provides additional information for a recommendation.

Text -> (string)

The text with the link to documentation for the recommendation.

Url -> (string)

The URL for the documentation for the recommendation.

IssueDetails -> (structure)

Details of the issue that caused the recommendation.

PerformanceIssueDetails -> (structure)

A detailed description of the issue when the recommendation category is `performance` .

StartTime -> (timestamp)

The time when the performance issue started.

EndTime -> (timestamp)

The time when the performance issue stopped.

Metrics -> (list)

The metrics that are relevant to the performance issue.

(structure)

The representation of a metric.

Name -> (string)

The name of a metric.

References -> (list)

A list of metric references (thresholds).

(structure)

The reference (threshold) for a metric.

Name -> (string)

The name of the metric reference.

ReferenceDetails -> (structure)

The details of a performance issue.

ScalarReferenceDetails -> (structure)

The metric reference details when the reference is a scalar.

Value -> (double)

The value of a scalar reference.

StatisticsDetails -> (string)

The details of different statistics for a metric. The description might contain markdown.

MetricQuery -> (structure)

The query to retrieve metric data points.

PerformanceInsightsMetricQuery -> (structure)

The Performance Insights query that you can use to retrieve Performance Insights metric data points.

GroupBy -> (structure)

A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this list isnât included, then all of the dimensions in the group were requested, or are present in the response.

(string)

Group -> (string)

The available dimension groups for Performance Insights metric type.

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Metric -> (string)

The name of a Performance Insights metric to be measured.

Valid Values:

- `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - The raw number of active sessions for the database engine.
- The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon Aurora User Guide* .

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

Analysis -> (string)

The analysis of the performance issue. The information might contain markdown.