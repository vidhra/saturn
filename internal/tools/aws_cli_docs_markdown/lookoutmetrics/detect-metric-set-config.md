# detect-metric-set-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutmetrics/detect-metric-set-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutmetrics/detect-metric-set-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutmetrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutmetrics/index.html#cli-aws-lookoutmetrics) ]

# detect-metric-set-config

## Description

Detects an Amazon S3 datasetâs file format, interval, and offset.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutmetrics-2017-07-25/DetectMetricSetConfig)

## Synopsis

```
detect-metric-set-config
--anomaly-detector-arn <value>
--auto-detection-metric-source <value>
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

`--anomaly-detector-arn` (string)

An anomaly detector ARN.

`--auto-detection-metric-source` (structure)

A data source.

S3SourceConfig -> (structure)

The sourceâs source config.

TemplatedPathList -> (list)

The configâs templated path list.

(string)

HistoricalDataPathList -> (list)

The configâs historical data path list.

(string)

Shorthand Syntax:

```
S3SourceConfig={TemplatedPathList=[string,string],HistoricalDataPathList=[string,string]}
```

JSON Syntax:

```
{
  "S3SourceConfig": {
    "TemplatedPathList": ["string", ...],
    "HistoricalDataPathList": ["string", ...]
  }
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

DetectedMetricSetConfig -> (structure)

The inferred dataset configuration for the datasource.

Offset -> (structure)

The datasetâs offset.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.

MetricSetFrequency -> (structure)

The datasetâs interval.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.

MetricSource -> (structure)

The datasetâs data source.

S3SourceConfig -> (structure)

The data sourceâs source configuration.

FileFormatDescriptor -> (structure)

The sourceâs file format descriptor.

CsvFormatDescriptor -> (structure)

Details about a CSV format.

FileCompression -> (structure)

The formatâs file compression.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.

Charset -> (structure)

The formatâs charset.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.

ContainsHeader -> (structure)

Whether the format includes a header.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.

Delimiter -> (structure)

The formatâs delimiter.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.

HeaderList -> (structure)

The formatâs header list.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.

QuoteSymbol -> (structure)

The formatâs quote symbol.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.

JsonFormatDescriptor -> (structure)

Details about a JSON format.

FileCompression -> (structure)

The formatâs file compression.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.

Charset -> (structure)

The formatâs character set.

Value -> (structure)

The fieldâs value.

S -> (string)

A string.

N -> (string)

A number.

B -> (string)

A binary value.

SS -> (list)

A list of strings.

(string)

NS -> (list)

A list of numbers.

(string)

BS -> (list)

A list of binary values.

(string)

Confidence -> (string)

The fieldâs confidence.

Message -> (string)

The fieldâs message.