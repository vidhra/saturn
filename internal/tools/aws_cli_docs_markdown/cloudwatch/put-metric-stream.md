# put-metric-streamÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-stream.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-stream.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudwatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html#cli-aws-cloudwatch) ]

# put-metric-stream

## Description

Creates or updates a metric stream. Metric streams can automatically stream CloudWatch metrics to Amazon Web Services destinations, including Amazon S3, and to many third-party solutions.

For more information, see [Using Metric Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html) .

To create a metric stream, you must be signed in to an account that has the `iam:PassRole` permission and either the `CloudWatchFullAccess` policy or the `cloudwatch:PutMetricStream` permission.

When you create or update a metric stream, you choose one of the following:

- Stream metrics from all metric namespaces in the account.
- Stream metrics from all metric namespaces in the account, except for the namespaces that you list in `ExcludeFilters` .
- Stream metrics from only the metric namespaces that you list in `IncludeFilters` .

By default, a metric stream always sends the `MAX` , `MIN` , `SUM` , and `SAMPLECOUNT` statistics for each metric that is streamed. You can use the `StatisticsConfigurations` parameter to have the metric stream send additional statistics in the stream. Streaming additional statistics incurs additional costs. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) .

When you use `PutMetricStream` to create a new metric stream, the stream is created in the `running` state. If you use it to update an existing stream, the state of the stream is not changed.

If you are using CloudWatch cross-account observability and you create a metric stream in a monitoring account, you can choose whether to include metrics from source accounts in the stream. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricStream)

## Synopsis

```
put-metric-stream
--name <value>
[--include-filters <value>]
[--exclude-filters <value>]
--firehose-arn <value>
--role-arn <value>
--output-format <value>
[--tags <value>]
[--statistics-configurations <value>]
[--include-linked-accounts-metrics | --no-include-linked-accounts-metrics]
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

`--name` (string)

If you are creating a new metric stream, this is the name for the new stream. The name must be different than the names of other metric streams in this account and Region.

If you are updating a metric stream, specify the name of that stream here.

Valid characters are A-Z, a-z, 0-9, â-â and â_â.

`--include-filters` (list)

If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.

You cannot include `IncludeFilters` and `ExcludeFilters` in the same operation.

(structure)

This structure contains a metric namespace and optionally, a list of metric names, to either include in a metric stream or exclude from a metric stream.

A metric streamâs filters can include up to 1000 total names. This limit applies to the sum of namespace names and metric names in the filters. For example, this could include 10 metric namespace filters with 99 metrics each, or 20 namespace filters with 49 metrics specified in each filter.

Namespace -> (string)

The name of the metric namespace for this filter.

The namespace can contain only ASCII printable characters (ASCII range 32 through 126). It must contain at least one non-whitespace character.

MetricNames -> (list)

The names of the metrics to either include or exclude from the metric stream.

If you omit this parameter, all metrics in the namespace are included or excluded, depending on whether this filter is specified as an exclude filter or an include filter.

Each metric name can contain only ASCII printable characters (ASCII range 32 through 126). Each metric name must contain at least one non-whitespace character.

(string)

Shorthand Syntax:

```
Namespace=string,MetricNames=string,string ...
```

JSON Syntax:

```
[
  {
    "Namespace": "string",
    "MetricNames": ["string", ...]
  }
  ...
]
```

`--exclude-filters` (list)

If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.

You cannot include `ExcludeFilters` and `IncludeFilters` in the same operation.

(structure)

This structure contains a metric namespace and optionally, a list of metric names, to either include in a metric stream or exclude from a metric stream.

A metric streamâs filters can include up to 1000 total names. This limit applies to the sum of namespace names and metric names in the filters. For example, this could include 10 metric namespace filters with 99 metrics each, or 20 namespace filters with 49 metrics specified in each filter.

Namespace -> (string)

The name of the metric namespace for this filter.

The namespace can contain only ASCII printable characters (ASCII range 32 through 126). It must contain at least one non-whitespace character.

MetricNames -> (list)

The names of the metrics to either include or exclude from the metric stream.

If you omit this parameter, all metrics in the namespace are included or excluded, depending on whether this filter is specified as an exclude filter or an include filter.

Each metric name can contain only ASCII printable characters (ASCII range 32 through 126). Each metric name must contain at least one non-whitespace character.

(string)

Shorthand Syntax:

```
Namespace=string,MetricNames=string,string ...
```

JSON Syntax:

```
[
  {
    "Namespace": "string",
    "MetricNames": ["string", ...]
  }
  ...
]
```

`--firehose-arn` (string)

The ARN of the Amazon Kinesis Data Firehose delivery stream to use for this metric stream. This Amazon Kinesis Data Firehose delivery stream must already exist and must be in the same account as the metric stream.

`--role-arn` (string)

The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Data Firehose resources. This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the following permissions:

- firehose:PutRecord
- firehose:PutRecordBatch

`--output-format` (string)

The output format for the stream. Valid values are `json` , `opentelemetry1.0` , and `opentelemetry0.7` . For more information about metric stream output formats, see [Metric streams output formats](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html) .

Possible values:

- `json`
- `opentelemetry0.7`
- `opentelemetry1.0`

`--tags` (list)

A list of key-value pairs to associate with the metric stream. You can associate as many as 50 tags with a metric stream.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

You can use this parameter only when you are creating a new metric stream. If you are using this operation to update an existing metric stream, any tags you specify in this parameter are ignored. To change the tags of an existing metric stream, use [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html) or [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html) .

(structure)

A key-value pair associated with a CloudWatch resource.

Key -> (string)

A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.

Value -> (string)

The value for the specified tag key.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--statistics-configurations` (list)

By default, a metric stream always sends the `MAX` , `MIN` , `SUM` , and `SAMPLECOUNT` statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.

For each entry in this array, you specify one or more metrics and the list of additional statistics to stream for those metrics. The additional statistics that you can stream depend on the streamâs `OutputFormat` . If the `OutputFormat` is `json` , you can stream any additional statistic that is supported by CloudWatch, listed in [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html.html) . If the `OutputFormat` is `opentelemetry1.0` or `opentelemetry0.7` , you can stream percentile statistics such as p95, p99.9, and so on.

(structure)

By default, a metric stream always sends the `MAX` , `MIN` , `SUM` , and `SAMPLECOUNT` statistics for each metric that is streamed. This structure contains information for one metric that includes additional statistics in the stream. For more information about statistics, see CloudWatch, listed in [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html.html) .

IncludeMetrics -> (list)

An array of metric name and namespace pairs that stream the additional statistics listed in the value of the `AdditionalStatistics` parameter. There can be as many as 100 pairs in the array.

All metrics that match the combination of metric name and namespace will be streamed with the additional statistics, no matter their dimensions.

(structure)

This object contains the information for one metric that is to be streamed with additional statistics.

Namespace -> (string)

The namespace of the metric.

MetricName -> (string)

The name of the metric.

AdditionalStatistics -> (list)

The list of additional statistics that are to be streamed for the metrics listed in the `IncludeMetrics` array in this structure. This list can include as many as 20 statistics.

If the `OutputFormat` for the stream is `opentelemetry1.0` or `opentelemetry0.7` , the only valid values are `p*??* `` percentile statistics such as ``p90` , `p99` and so on.

If the `OutputFormat` for the stream is `json` , the valid values include the abbreviations for all of the statistics listed in [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html.html) . For example, this includes `tm98,` `wm90` , `PR(:300)` , and so on.

(string)

Shorthand Syntax:

```
IncludeMetrics=[{Namespace=string,MetricName=string},{Namespace=string,MetricName=string}],AdditionalStatistics=string,string ...
```

JSON Syntax:

```
[
  {
    "IncludeMetrics": [
      {
        "Namespace": "string",
        "MetricName": "string"
      }
      ...
    ],
    "AdditionalStatistics": ["string", ...]
  }
  ...
]
```

`--include-linked-accounts-metrics` | `--no-include-linked-accounts-metrics` (boolean)

If you are creating a metric stream in a monitoring account, specify `true` to include metrics from source accounts in the metric stream.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a metric stream**

The following `put-metric-stream` example creates a metric stream named `QuickFull-GuaFb` in the specified account.

```
aws cloudwatch put-metric-stream \
    --name QuickFull-GuaFbs \
    --firehose-arn arn:aws:firehose:us-east-1:123456789012:deliverystream/MetricStreams-QuickFull-GuaFbs-WnySbECG \
    --role-arn arn:aws:iam::123456789012:role/service-role/MetricStreams-FirehosePutRecords-JN10W9B3 \
    --output-format json \
    --no-include-linked-accounts-metrics
```

Output:

```
{
    "Arn": "arn:aws:cloudwatch:us-east-1:123456789012:metric-stream/QuickFull-GuaFbs"
}
```

For more information, see [Set up a metric stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-setup.html) in the *Amazon CloudWatch User Guide*.

## Output

Arn -> (string)

The ARN of the metric stream.