# get-data-quality-resultÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-data-quality-result.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-data-quality-result.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-data-quality-result

## Description

Retrieves the result of a data quality rule evaluation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDataQualityResult)

## Synopsis

```
get-data-quality-result
--result-id <value>
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

`--result-id` (string)

A unique result ID for the data quality result.

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

ResultId -> (string)

A unique result ID for the data quality result.

ProfileId -> (string)

The Profile ID for the data quality result.

Score -> (double)

An aggregate data quality score. Represents the ratio of rules that passed to the total number of rules.

DataSource -> (structure)

The table associated with the data quality result, if any.

GlueTable -> (structure)

An Glue table.

DatabaseName -> (string)

A database name in the Glue Data Catalog.

TableName -> (string)

A table name in the Glue Data Catalog.

CatalogId -> (string)

A unique identifier for the Glue Data Catalog.

ConnectionName -> (string)

The name of the connection to the Glue Data Catalog.

AdditionalOptions -> (map)

Additional options for the table. Currently there are two keys supported:

- `pushDownPredicate` : to filter on partitions without having to list and read all the files in your dataset.
- `catalogPartitionPredicate` : to use server-side partition pruning using partition indexes in the Glue Data Catalog.

key -> (string)

value -> (string)

RulesetName -> (string)

The name of the ruleset associated with the data quality result.

EvaluationContext -> (string)

In the context of a job in Glue Studio, each node in the canvas is typically assigned some sort of name and data quality nodes will have names. In the case of multiple nodes, the `evaluationContext` can differentiate the nodes.

StartedOn -> (timestamp)

The date and time when the run for this data quality result started.

CompletedOn -> (timestamp)

The date and time when the run for this data quality result was completed.

JobName -> (string)

The job name associated with the data quality result, if any.

JobRunId -> (string)

The job run ID associated with the data quality result, if any.

RulesetEvaluationRunId -> (string)

The unique run ID associated with the ruleset evaluation.

RuleResults -> (list)

A list of `DataQualityRuleResult` objects representing the results for each rule.

(structure)

Describes the result of the evaluation of a data quality rule.

Name -> (string)

The name of the data quality rule.

Description -> (string)

A description of the data quality rule.

EvaluationMessage -> (string)

An evaluation message.

Result -> (string)

A pass or fail status for the rule.

EvaluatedMetrics -> (map)

A map of metrics associated with the evaluation of the rule.

key -> (string)

value -> (double)

EvaluatedRule -> (string)

The evaluated rule.

AnalyzerResults -> (list)

A list of `DataQualityAnalyzerResult` objects representing the results for each analyzer.

(structure)

Describes the result of the evaluation of a data quality analyzer.

Name -> (string)

The name of the data quality analyzer.

Description -> (string)

A description of the data quality analyzer.

EvaluationMessage -> (string)

An evaluation message.

EvaluatedMetrics -> (map)

A map of metrics associated with the evaluation of the analyzer.

key -> (string)

value -> (double)

Observations -> (list)

A list of `DataQualityObservation` objects representing the observations generated after evaluating the rules and analyzers.

(structure)

Describes the observation generated after evaluating the rules and analyzers.

Description -> (string)

A description of the data quality observation.

MetricBasedObservation -> (structure)

An object of type `MetricBasedObservation` representing the observation that is based on evaluated data quality metrics.

MetricName -> (string)

The name of the data quality metric used for generating the observation.

StatisticId -> (string)

The Statistic ID.

MetricValues -> (structure)

An object of type `DataQualityMetricValues` representing the analysis of the data quality metric value.

ActualValue -> (double)

The actual value of the data quality metric.

ExpectedValue -> (double)

The expected value of the data quality metric according to the analysis of historical data.

LowerLimit -> (double)

The lower limit of the data quality metric value according to the analysis of historical data.

UpperLimit -> (double)

The upper limit of the data quality metric value according to the analysis of historical data.

NewRules -> (list)

A list of new data quality rules generated as part of the observation based on the data quality metric value.

(string)