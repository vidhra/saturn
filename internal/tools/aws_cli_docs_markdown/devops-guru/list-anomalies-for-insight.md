# list-anomalies-for-insightÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-anomalies-for-insight.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-anomalies-for-insight.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devops-guru](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/index.html#cli-aws-devops-guru) ]

# list-anomalies-for-insight

## Description

Returns a list of the anomalies that belong to an insight that you specify using its ID.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devops-guru-2020-12-01/ListAnomaliesForInsight)

`list-anomalies-for-insight` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ReactiveAnomalies`, `ProactiveAnomalies`

## Synopsis

```
list-anomalies-for-insight
--insight-id <value>
[--start-time-range <value>]
[--account-id <value>]
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

`--insight-id` (string)

The ID of the insight. The returned anomalies belong to this insight.

`--start-time-range` (structure)

A time range used to specify when the requested anomalies started. All returned anomalies started during this time range.

FromTime -> (timestamp)

The start time of the time range.

ToTime -> (timestamp)

The end time of the time range.

Shorthand Syntax:

```
FromTime=timestamp,ToTime=timestamp
```

JSON Syntax:

```
{
  "FromTime": timestamp,
  "ToTime": timestamp
}
```

`--account-id` (string)

The ID of the Amazon Web Services account.

`--filters` (structure)

Specifies one or more service names that are used to list anomalies.

ServiceCollection -> (structure)

A collection of the names of Amazon Web Services services.

ServiceNames -> (list)

An array of strings that each specifies the name of an Amazon Web Services service.

(string)

Shorthand Syntax:

```
ServiceCollection={ServiceNames=[string,string]}
```

JSON Syntax:

```
{
  "ServiceCollection": {
    "ServiceNames": ["API_GATEWAY"|"APPLICATION_ELB"|"AUTO_SCALING_GROUP"|"CLOUD_FRONT"|"DYNAMO_DB"|"EC2"|"ECS"|"EKS"|"ELASTIC_BEANSTALK"|"ELASTI_CACHE"|"ELB"|"ES"|"KINESIS"|"LAMBDA"|"NAT_GATEWAY"|"NETWORK_ELB"|"RDS"|"REDSHIFT"|"ROUTE_53"|"S3"|"SAGE_MAKER"|"SNS"|"SQS"|"STEP_FUNCTIONS"|"SWF", ...]
  }
}
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

ProactiveAnomalies -> (list)

An array of `ProactiveAnomalySummary` objects that represent the requested anomalies

(structure)

Details about a proactive anomaly. This object is returned by `DescribeAnomaly.`

Id -> (string)

The ID of the anomaly.

Severity -> (string)

The severity of the anomaly. The severity of anomalies that generate an insight determine that insightâs severity. For more information, see [Understanding insight severities](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities) in the *Amazon DevOps Guru User Guide* .

Status -> (string)

The status of the anomaly.

UpdateTime -> (timestamp)

The time of the anomalyâs most recent update.

AnomalyTimeRange -> (structure)

A time range that specifies when the observed unusual behavior in an anomaly started and ended. This is different from `AnomalyReportedTimeRange` , which specifies the time range when DevOps Guru opens and then closes an anomaly.

StartTime -> (timestamp)

The time when the anomalous behavior started.

EndTime -> (timestamp)

The time when the anomalous behavior ended.

AnomalyReportedTimeRange -> (structure)

An `AnomalyReportedTimeRange` object that specifies the time range between when the anomaly is opened and the time when it is closed.

OpenTime -> (timestamp)

The time when an anomaly is opened.

CloseTime -> (timestamp)

The time when an anomaly is closed.

PredictionTimeRange -> (structure)

The time range during which anomalous behavior in a proactive anomaly or an insight is expected to occur.

StartTime -> (timestamp)

The time range during which a metric limit is expected to be exceeded. This applies to proactive insights only.

EndTime -> (timestamp)

The time when the behavior in a proactive insight is expected to end.

SourceDetails -> (structure)

Details about the source of the analyzed operational data that triggered the anomaly. The one supported source is Amazon CloudWatch metrics.

CloudWatchMetrics -> (list)

An array of `CloudWatchMetricsDetail` objects that contain information about analyzed CloudWatch metrics that show anomalous behavior.

(structure)

Information about an Amazon CloudWatch metric.

MetricName -> (string)

The name of the CloudWatch metric.

Namespace -> (string)

The namespace of the CloudWatch metric. A namespace is a container for CloudWatch metrics.

Dimensions -> (list)

An array of CloudWatch dimensions associated with

(structure)

The dimension of an Amazon CloudWatch metric that is used when DevOps Guru analyzes the resources in your account for operational problems and anomalous behavior. A dimension is a name/value pair that is part of the identity of a metric. A metric can have up to 10 dimensions. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) in the *Amazon CloudWatch User Guide* .

Name -> (string)

The name of the CloudWatch dimension.

Value -> (string)

The value of the CloudWatch dimension.

Stat -> (string)

The type of statistic associated with the CloudWatch metric. For more information, see [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide* .

Unit -> (string)

The unit of measure used for the CloudWatch metric. For example, `Bytes` , `Seconds` , `Count` , and `Percent` .

Period -> (integer)

The length of time associated with the CloudWatch metric in number of seconds.

MetricDataSummary -> (structure)

This object returns anomaly metric data.

TimestampMetricValuePairList -> (list)

This is a list of Amazon CloudWatch metric values at given timestamp.

(structure)

A pair that contains metric values at the respective timestamp.

Timestamp -> (timestamp)

A `Timestamp` that specifies the time the event occurred.

MetricValue -> (double)

Value of the anomalous metric data point at respective Timestamp.

StatusCode -> (string)

This is an enum of the status showing whether the metric value pair list has partial or complete data, or if there was an error.

PerformanceInsightsMetrics -> (list)

An array of `PerformanceInsightsMetricsDetail` objects that contain information about analyzed Performance Insights metrics that show anomalous behavior.

(structure)

Details about Performance Insights metrics.

Amazon RDS Performance Insights enables you to monitor and explore different dimensions of database load based on data captured from a running DB instance. DB load is measured as average active sessions. Performance Insights provides the data to API consumers as a two-dimensional time-series dataset. The time dimension provides DB load data for each time point in the queried time range. Each time point decomposes overall load in relation to the requested dimensions, measured at that time point. Examples include SQL, Wait event, User, and Host.

- To learn more about Performance Insights and Amazon Aurora DB instances, go to the [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html) .
- To learn more about Performance Insights and Amazon RDS DB instances, go to the [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) .

MetricDisplayName -> (string)

The name used for a specific Performance Insights metric.

Unit -> (string)

The unit of measure for a metric. For example, a session or a process.

MetricQuery -> (structure)

A single query to be processed for the metric. For more information, see `` [PerformanceInsightsMetricQuery](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsMetricQuery.html) `` .

Metric -> (string)

The name of the meteric used used when querying an Performance Insights `GetResourceMetrics` API for anomaly metrics.

Valid values for `Metric` are:

- `db.load.avg` - a scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - the raw number of active sessions for the database engine.

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

GroupBy -> (structure)

The specification for how to aggregate the data points from a Performance Insights `GetResourceMetrics` API query. The Performance Insights query returns all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.

Group -> (string)

The name of the dimension group. Its valid values are:

- `db` - The name of the database to which the client is connected (only Aurora PostgreSQL, Amazon RDS PostgreSQL, Aurora MySQL, Amazon RDS MySQL, and MariaDB)
- `db.application` - The name of the application that is connected to the database (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.host` - The host name of the connected client (all engines)
- `db.session_type` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.sql` - The SQL that is currently executing (all engines)
- `db.sql_tokenized` - The SQL digest (all engines)
- `db.wait_event` - The event for which the database backend is waiting (all engines)
- `db.wait_event_type` - The type of event for which the database backend is waiting (all engines)
- `db.user` - The user logged in to the database (all engines)

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested or are present in the response.

Valid values for elements in the `Dimensions` array are:

- `db.application.name` - The name of the application that is connected to the database (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.host.id` - The host ID of the connected client (all engines)
- `db.host.name` - The host name of the connected client (all engines)
- `db.name` - The name of the database to which the client is connected (only Aurora PostgreSQL, Amazon RDS PostgreSQL, Aurora MySQL, Amazon RDS MySQL, and MariaDB)
- `db.session_type.name` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.sql.id` - The SQL ID generated by Performance Insights (all engines)
- `db.sql.db_id` - The SQL ID generated by the database (all engines)
- `db.sql.statement` - The SQL text that is being executed (all engines)
- `db.sql.tokenized_id`
- `db.sql_tokenized.id` - The SQL digest ID generated by Performance Insights (all engines)
- `db.sql_tokenized.db_id` - SQL digest ID generated by the database (all engines)
- `db.sql_tokenized.statement` - The SQL digest text (all engines)
- `db.user.id` - The ID of the user logged in to the database (all engines)
- `db.user.name` - The name of the user logged in to the database (all engines)
- `db.wait_event.name` - The event for which the backend is waiting (all engines)
- `db.wait_event.type` - The type of event for which the backend is waiting (all engines)
- `db.wait_event_type.name` - The name of the event type for which the backend is waiting (all engines)

(string)

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Filter -> (map)

One or more filters to apply to a Performance Insights `GetResourceMetrics` API query. Restrictions:

- Any number of filters by the same dimension, as specified in the `GroupBy` parameter.
- A single filter for any other dimension in this dimension group.

key -> (string)

value -> (string)

ReferenceData -> (list)

For more information, see `` [PerformanceInsightsReferenceData](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsReferenceData.html) `` .

(structure)

Reference data used to evaluate Performance Insights to determine if its performance is anomalous or not.

Name -> (string)

The name of the reference data.

ComparisonValues -> (structure)

The specific reference values used to evaluate the Performance Insights. For more information, see `` [PerformanceInsightsReferenceComparisonValues](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsReferenceComparisonValues.html) `` .

ReferenceScalar -> (structure)

A scalar value DevOps Guru for a metric that DevOps Guru compares to actual metric values. This reference value is used to determine if an actual metric value should be considered anomalous.

Value -> (double)

The reference value.

ReferenceMetric -> (structure)

A metric that DevOps Guru compares to actual metric values. This reference metric is used to determine if an actual metric should be considered anomalous.

MetricQuery -> (structure)

A query to be processed on the metric.

Metric -> (string)

The name of the meteric used used when querying an Performance Insights `GetResourceMetrics` API for anomaly metrics.

Valid values for `Metric` are:

- `db.load.avg` - a scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - the raw number of active sessions for the database engine.

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

GroupBy -> (structure)

The specification for how to aggregate the data points from a Performance Insights `GetResourceMetrics` API query. The Performance Insights query returns all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.

Group -> (string)

The name of the dimension group. Its valid values are:

- `db` - The name of the database to which the client is connected (only Aurora PostgreSQL, Amazon RDS PostgreSQL, Aurora MySQL, Amazon RDS MySQL, and MariaDB)
- `db.application` - The name of the application that is connected to the database (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.host` - The host name of the connected client (all engines)
- `db.session_type` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.sql` - The SQL that is currently executing (all engines)
- `db.sql_tokenized` - The SQL digest (all engines)
- `db.wait_event` - The event for which the database backend is waiting (all engines)
- `db.wait_event_type` - The type of event for which the database backend is waiting (all engines)
- `db.user` - The user logged in to the database (all engines)

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested or are present in the response.

Valid values for elements in the `Dimensions` array are:

- `db.application.name` - The name of the application that is connected to the database (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.host.id` - The host ID of the connected client (all engines)
- `db.host.name` - The host name of the connected client (all engines)
- `db.name` - The name of the database to which the client is connected (only Aurora PostgreSQL, Amazon RDS PostgreSQL, Aurora MySQL, Amazon RDS MySQL, and MariaDB)
- `db.session_type.name` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.sql.id` - The SQL ID generated by Performance Insights (all engines)
- `db.sql.db_id` - The SQL ID generated by the database (all engines)
- `db.sql.statement` - The SQL text that is being executed (all engines)
- `db.sql.tokenized_id`
- `db.sql_tokenized.id` - The SQL digest ID generated by Performance Insights (all engines)
- `db.sql_tokenized.db_id` - SQL digest ID generated by the database (all engines)
- `db.sql_tokenized.statement` - The SQL digest text (all engines)
- `db.user.id` - The ID of the user logged in to the database (all engines)
- `db.user.name` - The name of the user logged in to the database (all engines)
- `db.wait_event.name` - The event for which the backend is waiting (all engines)
- `db.wait_event.type` - The type of event for which the backend is waiting (all engines)
- `db.wait_event_type.name` - The name of the event type for which the backend is waiting (all engines)

(string)

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Filter -> (map)

One or more filters to apply to a Performance Insights `GetResourceMetrics` API query. Restrictions:

- Any number of filters by the same dimension, as specified in the `GroupBy` parameter.
- A single filter for any other dimension in this dimension group.

key -> (string)

value -> (string)

StatsAtAnomaly -> (list)

The metric statistics during the anomalous period detected by DevOps Guru;

(structure)

A statistic in a Performance Insights collection.

Type -> (string)

The statistic type.

Value -> (double)

The value of the statistic.

StatsAtBaseline -> (list)

Typical metric statistics that are not considered anomalous. When DevOps Guru analyzes metrics, it compares them to `StatsAtBaseline` to help determine if they are anomalous.

(structure)

A statistic in a Performance Insights collection.

Type -> (string)

The statistic type.

Value -> (double)

The value of the statistic.

AssociatedInsightId -> (string)

The ID of the insight that contains this anomaly. An insight is composed of related anomalies.

ResourceCollection -> (structure)

A collection of Amazon Web Services resources supported by DevOps Guru. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag *key* . You can specify up to 500 Amazon Web Services CloudFormation stacks.

CloudFormation -> (structure)

An array of the names of Amazon Web Services CloudFormation stacks. The stacks define Amazon Web Services resources that DevOps Guru analyzes. You can specify up to 500 Amazon Web Services CloudFormation stacks.

StackNames -> (list)

An array of CloudFormation stack names.

(string)

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

A collection of Amazon Web Services tags.

Tags help you identify and organize your Amazon Web Services resources. Many Amazon Web Services services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an Lambda function. For more information about using tags, see the [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) whitepaper.

Each Amazon Web Services tag has two parts.

- A tag *key* (for example, `CostCenter` , `Environment` , `Project` , or `Secret` ). Tag *keys* are case-sensitive.
- An optional field known as a tag *value* (for example, `111122223333` , `Production` , or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive.

Together these are known as *key* -*value* pairs.

### Warning

The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix `Devops-guru-` . The tag *key* might be `DevOps-Guru-deployment-application` or `devops-guru-rds-application` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS` , and these act as two different *keys* . Possible *key* /*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers` .

AppBoundaryKey -> (string)

An Amazon Web Services tag *key* that is used to identify the Amazon Web Services resources that DevOps Guru analyzes. All Amazon Web Services resources in your account and Region tagged with this *key* make up your DevOps Guru application and analysis boundary.

### Warning

The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix `Devops-guru-` . The tag *key* might be `DevOps-Guru-deployment-application` or `devops-guru-rds-application` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS` , and these act as two different *keys* . Possible *key* /*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers` .

TagValues -> (list)

The values in an Amazon Web Services tag collection.

The tagâs *value* is an optional field used to associate a string with the tag *key* (for example, `111122223333` , `Production` , or a team name). The *key* and *value* are the tagâs *key* pair. Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive. You can specify a maximum of 256 characters for a tag value.

(string)

Limit -> (double)

A threshold that was exceeded by behavior in analyzed resources. Exceeding this threshold is related to the anomalous behavior that generated this anomaly.

SourceMetadata -> (structure)

The metadata of the source which detects proactive anomalies.

Source -> (string)

The source of the anomaly.

SourceResourceName -> (string)

The name of the anomalyâs resource.

SourceResourceType -> (string)

The anomalyâs resource type.

AnomalyResources -> (list)

Information about a resource in which DevOps Guru detected anomalous behavior.

(structure)

The Amazon Web Services resources in which DevOps Guru detected unusual behavior that resulted in the generation of an anomaly. When DevOps Guru detects multiple related anomalies, it creates and insight with details about the anomalous behavior and suggestions about how to correct the problem.

Name -> (string)

The name of the Amazon Web Services resource.

Type -> (string)

The type of the Amazon Web Services resource.

Description -> (string)

A description of the proactive anomaly.

ReactiveAnomalies -> (list)

An array of `ReactiveAnomalySummary` objects that represent the requested anomalies

(structure)

Details about a reactive anomaly. This object is returned by `DescribeAnomaly.`

Id -> (string)

The ID of the reactive anomaly.

Severity -> (string)

The severity of the anomaly. The severity of anomalies that generate an insight determine that insightâs severity. For more information, see [Understanding insight severities](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities) in the *Amazon DevOps Guru User Guide* .

Status -> (string)

The status of the reactive anomaly.

AnomalyTimeRange -> (structure)

A time range that specifies when the observed unusual behavior in an anomaly started and ended. This is different from `AnomalyReportedTimeRange` , which specifies the time range when DevOps Guru opens and then closes an anomaly.

StartTime -> (timestamp)

The time when the anomalous behavior started.

EndTime -> (timestamp)

The time when the anomalous behavior ended.

AnomalyReportedTimeRange -> (structure)

An `AnomalyReportedTimeRange` object that specifies the time range between when the anomaly is opened and the time when it is closed.

OpenTime -> (timestamp)

The time when an anomaly is opened.

CloseTime -> (timestamp)

The time when an anomaly is closed.

SourceDetails -> (structure)

Details about the source of the analyzed operational data that triggered the anomaly. The one supported source is Amazon CloudWatch metrics.

CloudWatchMetrics -> (list)

An array of `CloudWatchMetricsDetail` objects that contain information about analyzed CloudWatch metrics that show anomalous behavior.

(structure)

Information about an Amazon CloudWatch metric.

MetricName -> (string)

The name of the CloudWatch metric.

Namespace -> (string)

The namespace of the CloudWatch metric. A namespace is a container for CloudWatch metrics.

Dimensions -> (list)

An array of CloudWatch dimensions associated with

(structure)

The dimension of an Amazon CloudWatch metric that is used when DevOps Guru analyzes the resources in your account for operational problems and anomalous behavior. A dimension is a name/value pair that is part of the identity of a metric. A metric can have up to 10 dimensions. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) in the *Amazon CloudWatch User Guide* .

Name -> (string)

The name of the CloudWatch dimension.

Value -> (string)

The value of the CloudWatch dimension.

Stat -> (string)

The type of statistic associated with the CloudWatch metric. For more information, see [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide* .

Unit -> (string)

The unit of measure used for the CloudWatch metric. For example, `Bytes` , `Seconds` , `Count` , and `Percent` .

Period -> (integer)

The length of time associated with the CloudWatch metric in number of seconds.

MetricDataSummary -> (structure)

This object returns anomaly metric data.

TimestampMetricValuePairList -> (list)

This is a list of Amazon CloudWatch metric values at given timestamp.

(structure)

A pair that contains metric values at the respective timestamp.

Timestamp -> (timestamp)

A `Timestamp` that specifies the time the event occurred.

MetricValue -> (double)

Value of the anomalous metric data point at respective Timestamp.

StatusCode -> (string)

This is an enum of the status showing whether the metric value pair list has partial or complete data, or if there was an error.

PerformanceInsightsMetrics -> (list)

An array of `PerformanceInsightsMetricsDetail` objects that contain information about analyzed Performance Insights metrics that show anomalous behavior.

(structure)

Details about Performance Insights metrics.

Amazon RDS Performance Insights enables you to monitor and explore different dimensions of database load based on data captured from a running DB instance. DB load is measured as average active sessions. Performance Insights provides the data to API consumers as a two-dimensional time-series dataset. The time dimension provides DB load data for each time point in the queried time range. Each time point decomposes overall load in relation to the requested dimensions, measured at that time point. Examples include SQL, Wait event, User, and Host.

- To learn more about Performance Insights and Amazon Aurora DB instances, go to the [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html) .
- To learn more about Performance Insights and Amazon RDS DB instances, go to the [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) .

MetricDisplayName -> (string)

The name used for a specific Performance Insights metric.

Unit -> (string)

The unit of measure for a metric. For example, a session or a process.

MetricQuery -> (structure)

A single query to be processed for the metric. For more information, see `` [PerformanceInsightsMetricQuery](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsMetricQuery.html) `` .

Metric -> (string)

The name of the meteric used used when querying an Performance Insights `GetResourceMetrics` API for anomaly metrics.

Valid values for `Metric` are:

- `db.load.avg` - a scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - the raw number of active sessions for the database engine.

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

GroupBy -> (structure)

The specification for how to aggregate the data points from a Performance Insights `GetResourceMetrics` API query. The Performance Insights query returns all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.

Group -> (string)

The name of the dimension group. Its valid values are:

- `db` - The name of the database to which the client is connected (only Aurora PostgreSQL, Amazon RDS PostgreSQL, Aurora MySQL, Amazon RDS MySQL, and MariaDB)
- `db.application` - The name of the application that is connected to the database (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.host` - The host name of the connected client (all engines)
- `db.session_type` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.sql` - The SQL that is currently executing (all engines)
- `db.sql_tokenized` - The SQL digest (all engines)
- `db.wait_event` - The event for which the database backend is waiting (all engines)
- `db.wait_event_type` - The type of event for which the database backend is waiting (all engines)
- `db.user` - The user logged in to the database (all engines)

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested or are present in the response.

Valid values for elements in the `Dimensions` array are:

- `db.application.name` - The name of the application that is connected to the database (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.host.id` - The host ID of the connected client (all engines)
- `db.host.name` - The host name of the connected client (all engines)
- `db.name` - The name of the database to which the client is connected (only Aurora PostgreSQL, Amazon RDS PostgreSQL, Aurora MySQL, Amazon RDS MySQL, and MariaDB)
- `db.session_type.name` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.sql.id` - The SQL ID generated by Performance Insights (all engines)
- `db.sql.db_id` - The SQL ID generated by the database (all engines)
- `db.sql.statement` - The SQL text that is being executed (all engines)
- `db.sql.tokenized_id`
- `db.sql_tokenized.id` - The SQL digest ID generated by Performance Insights (all engines)
- `db.sql_tokenized.db_id` - SQL digest ID generated by the database (all engines)
- `db.sql_tokenized.statement` - The SQL digest text (all engines)
- `db.user.id` - The ID of the user logged in to the database (all engines)
- `db.user.name` - The name of the user logged in to the database (all engines)
- `db.wait_event.name` - The event for which the backend is waiting (all engines)
- `db.wait_event.type` - The type of event for which the backend is waiting (all engines)
- `db.wait_event_type.name` - The name of the event type for which the backend is waiting (all engines)

(string)

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Filter -> (map)

One or more filters to apply to a Performance Insights `GetResourceMetrics` API query. Restrictions:

- Any number of filters by the same dimension, as specified in the `GroupBy` parameter.
- A single filter for any other dimension in this dimension group.

key -> (string)

value -> (string)

ReferenceData -> (list)

For more information, see `` [PerformanceInsightsReferenceData](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsReferenceData.html) `` .

(structure)

Reference data used to evaluate Performance Insights to determine if its performance is anomalous or not.

Name -> (string)

The name of the reference data.

ComparisonValues -> (structure)

The specific reference values used to evaluate the Performance Insights. For more information, see `` [PerformanceInsightsReferenceComparisonValues](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsReferenceComparisonValues.html) `` .

ReferenceScalar -> (structure)

A scalar value DevOps Guru for a metric that DevOps Guru compares to actual metric values. This reference value is used to determine if an actual metric value should be considered anomalous.

Value -> (double)

The reference value.

ReferenceMetric -> (structure)

A metric that DevOps Guru compares to actual metric values. This reference metric is used to determine if an actual metric should be considered anomalous.

MetricQuery -> (structure)

A query to be processed on the metric.

Metric -> (string)

The name of the meteric used used when querying an Performance Insights `GetResourceMetrics` API for anomaly metrics.

Valid values for `Metric` are:

- `db.load.avg` - a scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - the raw number of active sessions for the database engine.

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

GroupBy -> (structure)

The specification for how to aggregate the data points from a Performance Insights `GetResourceMetrics` API query. The Performance Insights query returns all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.

Group -> (string)

The name of the dimension group. Its valid values are:

- `db` - The name of the database to which the client is connected (only Aurora PostgreSQL, Amazon RDS PostgreSQL, Aurora MySQL, Amazon RDS MySQL, and MariaDB)
- `db.application` - The name of the application that is connected to the database (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.host` - The host name of the connected client (all engines)
- `db.session_type` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.sql` - The SQL that is currently executing (all engines)
- `db.sql_tokenized` - The SQL digest (all engines)
- `db.wait_event` - The event for which the database backend is waiting (all engines)
- `db.wait_event_type` - The type of event for which the database backend is waiting (all engines)
- `db.user` - The user logged in to the database (all engines)

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested or are present in the response.

Valid values for elements in the `Dimensions` array are:

- `db.application.name` - The name of the application that is connected to the database (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.host.id` - The host ID of the connected client (all engines)
- `db.host.name` - The host name of the connected client (all engines)
- `db.name` - The name of the database to which the client is connected (only Aurora PostgreSQL, Amazon RDS PostgreSQL, Aurora MySQL, Amazon RDS MySQL, and MariaDB)
- `db.session_type.name` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL)
- `db.sql.id` - The SQL ID generated by Performance Insights (all engines)
- `db.sql.db_id` - The SQL ID generated by the database (all engines)
- `db.sql.statement` - The SQL text that is being executed (all engines)
- `db.sql.tokenized_id`
- `db.sql_tokenized.id` - The SQL digest ID generated by Performance Insights (all engines)
- `db.sql_tokenized.db_id` - SQL digest ID generated by the database (all engines)
- `db.sql_tokenized.statement` - The SQL digest text (all engines)
- `db.user.id` - The ID of the user logged in to the database (all engines)
- `db.user.name` - The name of the user logged in to the database (all engines)
- `db.wait_event.name` - The event for which the backend is waiting (all engines)
- `db.wait_event.type` - The type of event for which the backend is waiting (all engines)
- `db.wait_event_type.name` - The name of the event type for which the backend is waiting (all engines)

(string)

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Filter -> (map)

One or more filters to apply to a Performance Insights `GetResourceMetrics` API query. Restrictions:

- Any number of filters by the same dimension, as specified in the `GroupBy` parameter.
- A single filter for any other dimension in this dimension group.

key -> (string)

value -> (string)

StatsAtAnomaly -> (list)

The metric statistics during the anomalous period detected by DevOps Guru;

(structure)

A statistic in a Performance Insights collection.

Type -> (string)

The statistic type.

Value -> (double)

The value of the statistic.

StatsAtBaseline -> (list)

Typical metric statistics that are not considered anomalous. When DevOps Guru analyzes metrics, it compares them to `StatsAtBaseline` to help determine if they are anomalous.

(structure)

A statistic in a Performance Insights collection.

Type -> (string)

The statistic type.

Value -> (double)

The value of the statistic.

AssociatedInsightId -> (string)

The ID of the insight that contains this anomaly. An insight is composed of related anomalies.

ResourceCollection -> (structure)

A collection of Amazon Web Services resources supported by DevOps Guru. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag *key* . You can specify up to 500 Amazon Web Services CloudFormation stacks.

CloudFormation -> (structure)

An array of the names of Amazon Web Services CloudFormation stacks. The stacks define Amazon Web Services resources that DevOps Guru analyzes. You can specify up to 500 Amazon Web Services CloudFormation stacks.

StackNames -> (list)

An array of CloudFormation stack names.

(string)

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

A collection of Amazon Web Services tags.

Tags help you identify and organize your Amazon Web Services resources. Many Amazon Web Services services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an Lambda function. For more information about using tags, see the [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) whitepaper.

Each Amazon Web Services tag has two parts.

- A tag *key* (for example, `CostCenter` , `Environment` , `Project` , or `Secret` ). Tag *keys* are case-sensitive.
- An optional field known as a tag *value* (for example, `111122223333` , `Production` , or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive.

Together these are known as *key* -*value* pairs.

### Warning

The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix `Devops-guru-` . The tag *key* might be `DevOps-Guru-deployment-application` or `devops-guru-rds-application` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS` , and these act as two different *keys* . Possible *key* /*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers` .

AppBoundaryKey -> (string)

An Amazon Web Services tag *key* that is used to identify the Amazon Web Services resources that DevOps Guru analyzes. All Amazon Web Services resources in your account and Region tagged with this *key* make up your DevOps Guru application and analysis boundary.

### Warning

The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix `Devops-guru-` . The tag *key* might be `DevOps-Guru-deployment-application` or `devops-guru-rds-application` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS` , and these act as two different *keys* . Possible *key* /*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers` .

TagValues -> (list)

The values in an Amazon Web Services tag collection.

The tagâs *value* is an optional field used to associate a string with the tag *key* (for example, `111122223333` , `Production` , or a team name). The *key* and *value* are the tagâs *key* pair. Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive. You can specify a maximum of 256 characters for a tag value.

(string)

Type -> (string)

The type of the reactive anomaly. It can be one of the following types.

- `CAUSAL` - the anomaly can cause a new insight.
- `CONTEXTUAL` - the anomaly contains additional information about an insight or its causal anomaly.

Name -> (string)

The name of the reactive anomaly.

Description -> (string)

A description of the reactive anomaly.

CausalAnomalyId -> (string)

The ID of the causal anomaly that is associated with this reactive anomaly. The ID of a CAUSAL anomaly is always NULL.

AnomalyResources -> (list)

The Amazon Web Services resources in which anomalous behavior was detected by DevOps Guru.

(structure)

The Amazon Web Services resources in which DevOps Guru detected unusual behavior that resulted in the generation of an anomaly. When DevOps Guru detects multiple related anomalies, it creates and insight with details about the anomalous behavior and suggestions about how to correct the problem.

Name -> (string)

The name of the Amazon Web Services resource.

Type -> (string)

The type of the Amazon Web Services resource.

NextToken -> (string)

The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.