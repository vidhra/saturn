# get-performance-analysis-reportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-performance-analysis-report.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-performance-analysis-report.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/index.html#cli-aws-pi) ]

# get-performance-analysis-report

## Description

Retrieves the report including the report ID, status, time details, and the insights with recommendations. The report status can be `RUNNING` , `SUCCEEDED` , or `FAILED` . The insights include the `description` and `recommendation` fields.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pi-2018-02-27/GetPerformanceAnalysisReport)

## Synopsis

```
get-performance-analysis-report
--service-type <value>
--identifier <value>
--analysis-report-id <value>
[--text-format <value>]
[--accept-language <value>]
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

`--service-type` (string)

The Amazon Web Services service for which Performance Insights will return metrics. Valid value is `RDS` .

Possible values:

- `RDS`
- `DOCDB`

`--identifier` (string)

An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as *ResourceID* . When you call `DescribeDBInstances` , the identifier is returned as `DbiResourceId` .

To use a DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X` .

`--analysis-report-id` (string)

A unique identifier of the created analysis report. For example, `report-12345678901234567`

`--text-format` (string)

Indicates the text format in the report. The options are `PLAIN_TEXT` or `MARKDOWN` . The default value is `plain text` .

Possible values:

- `PLAIN_TEXT`
- `MARKDOWN`

`--accept-language` (string)

The text language in the report. The default language is `EN_US` (English).

Possible values:

- `EN_US`

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

AnalysisReport -> (structure)

The summary of the performance analysis report created for a time period.

AnalysisReportId -> (string)

The name of the analysis report.

Identifier -> (string)

The unique identifier of the analysis report.

ServiceType -> (string)

List the tags for the Amazon Web Services service for which Performance Insights returns metrics. Valid values are as follows:

- `RDS`
- `DOCDB`

CreateTime -> (timestamp)

The time you created the analysis report.

StartTime -> (timestamp)

The analysis start time in the report.

EndTime -> (timestamp)

The analysis end time in the report.

Status -> (string)

The status of the created analysis report.

Insights -> (list)

The list of identified insights in the analysis report.

(structure)

Retrieves the list of performance issues which are identified.

InsightId -> (string)

The unique identifier for the insight. For example, `insight-12345678901234567` .

InsightType -> (string)

The type of insight. For example, `HighDBLoad` , `HighCPU` , or `DominatingSQLs` .

Context -> (string)

Indicates if the insight is causal or correlated insight.

StartTime -> (timestamp)

The start time of the insight. For example, `2018-10-30T00:00:00Z` .

EndTime -> (timestamp)

The end time of the insight. For example, `2018-10-30T00:00:00Z` .

Severity -> (string)

The severity of the insight. The values are: `Low` , `Medium` , or `High` .

SupportingInsights -> (list)

List of supporting insights that provide additional factors for the insight.

(structure)

Retrieves the list of performance issues which are identified.

InsightId -> (string)

The unique identifier for the insight. For example, `insight-12345678901234567` .

InsightType -> (string)

The type of insight. For example, `HighDBLoad` , `HighCPU` , or `DominatingSQLs` .

Context -> (string)

Indicates if the insight is causal or correlated insight.

StartTime -> (timestamp)

The start time of the insight. For example, `2018-10-30T00:00:00Z` .

EndTime -> (timestamp)

The end time of the insight. For example, `2018-10-30T00:00:00Z` .

Severity -> (string)

The severity of the insight. The values are: `Low` , `Medium` , or `High` .

Description -> (string)

Description of the insight. For example: `A high severity Insight found between 02:00 to 02:30, where there was an unusually high DB load 600x above baseline. Likely performance impact` .

Recommendations -> (list)

List of recommendations for the insight. For example, `Investigate the following SQLs that contributed to 100% of the total DBLoad during that time period: sql-id` .

(structure)

The list of recommendations for the insight.

RecommendationId -> (string)

The unique identifier for the recommendation.

RecommendationDescription -> (string)

The recommendation details to help resolve the performance issue. For example, `Investigate the following SQLs that contributed to 100% of the total DBLoad during that time period: sql-id`

InsightData -> (list)

List of data objects containing metrics and references from the time range while generating the insight.

(structure)

List of data objects which provide details about source metrics. This field can be used to determine the PI metric to render for the insight. This data type also includes static values for the metrics for the Insight that were calculated and included in text and annotations on the DB load chart.

PerformanceInsightsMetric -> (structure)

This field determines the Performance Insights metric to render for the insight. The `name` field refers to a Performance Insights metric.

Metric -> (string)

The Performance Insights metric.

DisplayName -> (string)

The Performance Insights metric name.

Dimensions -> (map)

A dimension map that contains the dimensions for this partition.

key -> (string)

value -> (string)

Filter -> (map)

The filter for the Performance Insights metric.

key -> (string)

value -> (string)

Value -> (double)

The value of the metric. For example, `9` for `db.load.avg` .

BaselineData -> (list)

Metric names and values from the timeframe used as baseline to generate the insight.

(structure)

List of data objects which provide details about source metrics. This field can be used to determine the PI metric to render for the insight. This data type also includes static values for the metrics for the Insight that were calculated and included in text and annotations on the DB load chart.

PerformanceInsightsMetric -> (structure)

This field determines the Performance Insights metric to render for the insight. The `name` field refers to a Performance Insights metric.

Metric -> (string)

The Performance Insights metric.

DisplayName -> (string)

The Performance Insights metric name.

Dimensions -> (map)

A dimension map that contains the dimensions for this partition.

key -> (string)

value -> (string)

Filter -> (map)

The filter for the Performance Insights metric.

key -> (string)

value -> (string)

Value -> (double)

The value of the metric. For example, `9` for `db.load.avg` .

Description -> (string)

Description of the insight. For example: `A high severity Insight found between 02:00 to 02:30, where there was an unusually high DB load 600x above baseline. Likely performance impact` .

Recommendations -> (list)

List of recommendations for the insight. For example, `Investigate the following SQLs that contributed to 100% of the total DBLoad during that time period: sql-id` .

(structure)

The list of recommendations for the insight.

RecommendationId -> (string)

The unique identifier for the recommendation.

RecommendationDescription -> (string)

The recommendation details to help resolve the performance issue. For example, `Investigate the following SQLs that contributed to 100% of the total DBLoad during that time period: sql-id`

InsightData -> (list)

List of data objects containing metrics and references from the time range while generating the insight.

(structure)

List of data objects which provide details about source metrics. This field can be used to determine the PI metric to render for the insight. This data type also includes static values for the metrics for the Insight that were calculated and included in text and annotations on the DB load chart.

PerformanceInsightsMetric -> (structure)

This field determines the Performance Insights metric to render for the insight. The `name` field refers to a Performance Insights metric.

Metric -> (string)

The Performance Insights metric.

DisplayName -> (string)

The Performance Insights metric name.

Dimensions -> (map)

A dimension map that contains the dimensions for this partition.

key -> (string)

value -> (string)

Filter -> (map)

The filter for the Performance Insights metric.

key -> (string)

value -> (string)

Value -> (double)

The value of the metric. For example, `9` for `db.load.avg` .

BaselineData -> (list)

Metric names and values from the timeframe used as baseline to generate the insight.

(structure)

List of data objects which provide details about source metrics. This field can be used to determine the PI metric to render for the insight. This data type also includes static values for the metrics for the Insight that were calculated and included in text and annotations on the DB load chart.

PerformanceInsightsMetric -> (structure)

This field determines the Performance Insights metric to render for the insight. The `name` field refers to a Performance Insights metric.

Metric -> (string)

The Performance Insights metric.

DisplayName -> (string)

The Performance Insights metric name.

Dimensions -> (map)

A dimension map that contains the dimensions for this partition.

key -> (string)

value -> (string)

Filter -> (map)

The filter for the Performance Insights metric.

key -> (string)

value -> (string)

Value -> (double)

The value of the metric. For example, `9` for `db.load.avg` .