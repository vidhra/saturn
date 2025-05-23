# create-metric-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutmetrics/create-metric-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutmetrics/create-metric-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutmetrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutmetrics/index.html#cli-aws-lookoutmetrics) ]

# create-metric-set

## Description

Creates a dataset.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutmetrics-2017-07-25/CreateMetricSet)

## Synopsis

```
create-metric-set
--anomaly-detector-arn <value>
--metric-set-name <value>
[--metric-set-description <value>]
--metric-list <value>
[--offset <value>]
[--timestamp-column <value>]
[--dimension-list <value>]
[--metric-set-frequency <value>]
--metric-source <value>
[--timezone <value>]
[--tags <value>]
[--dimension-filter-list <value>]
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

The ARN of the anomaly detector that will use the dataset.

`--metric-set-name` (string)

The name of the dataset.

`--metric-set-description` (string)

A description of the dataset you are creating.

`--metric-list` (list)

A list of metrics that the dataset will contain.

(structure)

A calculation made by contrasting a measure and a dimension from your source data.

MetricName -> (string)

The name of the metric.

AggregationFunction -> (string)

The function with which the metric is calculated.

Namespace -> (string)

The namespace for the metric.

Shorthand Syntax:

```
MetricName=string,AggregationFunction=string,Namespace=string ...
```

JSON Syntax:

```
[
  {
    "MetricName": "string",
    "AggregationFunction": "AVG"|"SUM",
    "Namespace": "string"
  }
  ...
]
```

`--offset` (integer)

After an interval ends, the amount of seconds that the detector waits before importing data. Offset is only supported for S3, Redshift, Athena and datasources.

`--timestamp-column` (structure)

Contains information about the column used for tracking time in your source data.

ColumnName -> (string)

The name of the timestamp column.

ColumnFormat -> (string)

The format of the timestamp column.

Shorthand Syntax:

```
ColumnName=string,ColumnFormat=string
```

JSON Syntax:

```
{
  "ColumnName": "string",
  "ColumnFormat": "string"
}
```

`--dimension-list` (list)

A list of the fields you want to treat as dimensions.

(string)

Syntax:

```
"string" "string" ...
```

`--metric-set-frequency` (string)

The frequency with which the source data will be analyzed for anomalies.

Possible values:

- `P1D`
- `PT1H`
- `PT10M`
- `PT5M`

`--metric-source` (structure)

Contains information about how the source data should be interpreted.

S3SourceConfig -> (structure)

Contains information about the configuration of the S3 bucket that contains source files.

RoleArn -> (string)

The ARN of an IAM role that has read and write access permissions to the source S3 bucket.

TemplatedPathList -> (list)

A list of templated paths to the source files.

(string)

HistoricalDataPathList -> (list)

A list of paths to the historical data files.

(string)

FileFormatDescriptor -> (structure)

Contains information about a source fileâs formatting.

CsvFormatDescriptor -> (structure)

Contains information about how a source CSV data file should be analyzed.

FileCompression -> (string)

The level of compression of the source CSV file.

Charset -> (string)

The character set in which the source CSV file is written.

ContainsHeader -> (boolean)

Whether or not the source CSV file contains a header.

Delimiter -> (string)

The character used to delimit the source CSV file.

HeaderList -> (list)

A list of the source CSV fileâs headers, if any.

(string)

QuoteSymbol -> (string)

The character used as a quote character.

JsonFormatDescriptor -> (structure)

Contains information about how a source JSON data file should be analyzed.

FileCompression -> (string)

The level of compression of the source CSV file.

Charset -> (string)

The character set in which the source JSON file is written.

AppFlowConfig -> (structure)

Details about an AppFlow datasource.

RoleArn -> (string)

An IAM role that gives Amazon Lookout for Metrics permission to access the flow.

FlowName -> (string)

name of the flow.

CloudWatchConfig -> (structure)

Details about an Amazon CloudWatch monitoring datasource.

RoleArn -> (string)

An IAM role that gives Amazon Lookout for Metrics permission to access data in Amazon CloudWatch.

BackTestConfiguration -> (structure)

Settings for backtest mode.

RunBackTestMode -> (boolean)

Run a backtest instead of monitoring new data.

RDSSourceConfig -> (structure)

Details about an Amazon Relational Database Service (RDS) datasource.

DBInstanceIdentifier -> (string)

A string identifying the database instance.

DatabaseHost -> (string)

The host name of the database.

DatabasePort -> (integer)

The port number where the database can be accessed.

SecretManagerArn -> (string)

The Amazon Resource Name (ARN) of the AWS Secrets Manager role.

DatabaseName -> (string)

The name of the RDS database.

TableName -> (string)

The name of the table in the database.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role.

VpcConfiguration -> (structure)

An object containing information about the Amazon Virtual Private Cloud (VPC) configuration.

SubnetIdList -> (list)

An array of strings containing the Amazon VPC subnet IDs (e.g., `subnet-0bb1c79de3EXAMPLE` .

(string)

SecurityGroupIdList -> (list)

An array of strings containing the list of security groups.

(string)

RedshiftSourceConfig -> (structure)

Details about an Amazon Redshift database datasource.

ClusterIdentifier -> (string)

A string identifying the Redshift cluster.

DatabaseHost -> (string)

The name of the database host.

DatabasePort -> (integer)

The port number where the database can be accessed.

SecretManagerArn -> (string)

The Amazon Resource Name (ARN) of the AWS Secrets Manager role.

DatabaseName -> (string)

The Redshift database name.

TableName -> (string)

The table name of the Redshift database.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role providing access to the database.

VpcConfiguration -> (structure)

Contains information about the Amazon Virtual Private Cloud (VPC) configuration.

SubnetIdList -> (list)

An array of strings containing the Amazon VPC subnet IDs (e.g., `subnet-0bb1c79de3EXAMPLE` .

(string)

SecurityGroupIdList -> (list)

An array of strings containing the list of security groups.

(string)

AthenaSourceConfig -> (structure)

Details about an Amazon Athena datasource.

RoleArn -> (string)

An IAM role that gives Amazon Lookout for Metrics permission to access the data.

DatabaseName -> (string)

The databaseâs name.

DataCatalog -> (string)

The databaseâs data catalog.

TableName -> (string)

The databaseâs table name.

WorkGroupName -> (string)

The databaseâs work group name.

S3ResultsPath -> (string)

The databaseâs results path.

BackTestConfiguration -> (structure)

Settings for backtest mode.

RunBackTestMode -> (boolean)

Run a backtest instead of monitoring new data.

JSON Syntax:

```
{
  "S3SourceConfig": {
    "RoleArn": "string",
    "TemplatedPathList": ["string", ...],
    "HistoricalDataPathList": ["string", ...],
    "FileFormatDescriptor": {
      "CsvFormatDescriptor": {
        "FileCompression": "NONE"|"GZIP",
        "Charset": "string",
        "ContainsHeader": true|false,
        "Delimiter": "string",
        "HeaderList": ["string", ...],
        "QuoteSymbol": "string"
      },
      "JsonFormatDescriptor": {
        "FileCompression": "NONE"|"GZIP",
        "Charset": "string"
      }
    }
  },
  "AppFlowConfig": {
    "RoleArn": "string",
    "FlowName": "string"
  },
  "CloudWatchConfig": {
    "RoleArn": "string",
    "BackTestConfiguration": {
      "RunBackTestMode": true|false
    }
  },
  "RDSSourceConfig": {
    "DBInstanceIdentifier": "string",
    "DatabaseHost": "string",
    "DatabasePort": integer,
    "SecretManagerArn": "string",
    "DatabaseName": "string",
    "TableName": "string",
    "RoleArn": "string",
    "VpcConfiguration": {
      "SubnetIdList": ["string", ...],
      "SecurityGroupIdList": ["string", ...]
    }
  },
  "RedshiftSourceConfig": {
    "ClusterIdentifier": "string",
    "DatabaseHost": "string",
    "DatabasePort": integer,
    "SecretManagerArn": "string",
    "DatabaseName": "string",
    "TableName": "string",
    "RoleArn": "string",
    "VpcConfiguration": {
      "SubnetIdList": ["string", ...],
      "SecurityGroupIdList": ["string", ...]
    }
  },
  "AthenaSourceConfig": {
    "RoleArn": "string",
    "DatabaseName": "string",
    "DataCatalog": "string",
    "TableName": "string",
    "WorkGroupName": "string",
    "S3ResultsPath": "string",
    "BackTestConfiguration": {
      "RunBackTestMode": true|false
    }
  }
}
```

`--timezone` (string)

The time zone in which your source data was recorded.

`--tags` (map)

A list of [tags](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/detectors-tags.html) to apply to the dataset.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--dimension-filter-list` (list)

A list of filters that specify which data is kept for anomaly detection.

(structure)

Describes a list of filters for choosing a subset of dimension values. Each filter consists of the dimension and one of its values that you want to include. When multiple dimensions or values are specified, the dimensions are joined with an AND operation and the values are joined with an OR operation.

Name -> (string)

The dimension that you want to filter on.

FilterList -> (list)

The list of filters that you are applying.

(structure)

Describes a filter for choosing a subset of dimension values. Each filter consists of the dimension that you want to include and the condition statement. The condition statement is specified in the `FilterOperation` object.

DimensionValue -> (string)

The value that you want to include in the filter.

FilterOperation -> (string)

The condition to apply.

Shorthand Syntax:

```
Name=string,FilterList=[{DimensionValue=string,FilterOperation=string},{DimensionValue=string,FilterOperation=string}] ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "FilterList": [
      {
        "DimensionValue": "string",
        "FilterOperation": "EQUALS"
      }
      ...
    ]
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

MetricSetArn -> (string)

The ARN of the dataset.