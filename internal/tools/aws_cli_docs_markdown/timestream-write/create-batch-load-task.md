# create-batch-load-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-batch-load-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-batch-load-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [timestream-write](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/index.html#cli-aws-timestream-write) ]

# create-batch-load-task

## Description

Creates a new Timestream batch load task. A batch load task processes data from a CSV source in an S3 location and writes to a Timestream table. A mapping from source to target is defined in a batch load task. Errors and events are written to a report at an S3 location. For the report, if the KMS key is not specified, the report will be encrypted with an S3 managed key when `SSE_S3` is the option. Otherwise an error is thrown. For more information, see [Amazon Web Services managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) . [Service quotas apply](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html) . For details, see [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.create-batch-load.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/timestream-write-2018-11-01/CreateBatchLoadTask)

## Synopsis

```
create-batch-load-task
[--client-token <value>]
[--data-model-configuration <value>]
--data-source-configuration <value>
--report-configuration <value>
--target-database-name <value>
--target-table-name <value>
[--record-version <value>]
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

`--client-token` (string)

`--data-model-configuration` (structure)

DataModel -> (structure)

TimeColumn -> (string)

Source column to be mapped to time.

TimeUnit -> (string)

The granularity of the timestamp unit. It indicates if the time value is in seconds, milliseconds, nanoseconds, or other supported values. Default is `MILLISECONDS` .

DimensionMappings -> (list)

Source to target mappings for dimensions.

(structure)

SourceColumn -> (string)

DestinationColumn -> (string)

MultiMeasureMappings -> (structure)

Source to target mappings for multi-measure records.

TargetMultiMeasureName -> (string)

MultiMeasureAttributeMappings -> (list)

(structure)

SourceColumn -> (string)

TargetMultiMeasureAttributeName -> (string)

MeasureValueType -> (string)

MixedMeasureMappings -> (list)

Source to target mappings for measures.

(structure)

MeasureName -> (string)

SourceColumn -> (string)

TargetMeasureName -> (string)

MeasureValueType -> (string)

MultiMeasureAttributeMappings -> (list)

(structure)

SourceColumn -> (string)

TargetMultiMeasureAttributeName -> (string)

MeasureValueType -> (string)

MeasureNameColumn -> (string)

DataModelS3Configuration -> (structure)

BucketName -> (string)

ObjectKey -> (string)

JSON Syntax:

```
{
  "DataModel": {
    "TimeColumn": "string",
    "TimeUnit": "MILLISECONDS"|"SECONDS"|"MICROSECONDS"|"NANOSECONDS",
    "DimensionMappings": [
      {
        "SourceColumn": "string",
        "DestinationColumn": "string"
      }
      ...
    ],
    "MultiMeasureMappings": {
      "TargetMultiMeasureName": "string",
      "MultiMeasureAttributeMappings": [
        {
          "SourceColumn": "string",
          "TargetMultiMeasureAttributeName": "string",
          "MeasureValueType": "DOUBLE"|"BIGINT"|"BOOLEAN"|"VARCHAR"|"TIMESTAMP"
        }
        ...
      ]
    },
    "MixedMeasureMappings": [
      {
        "MeasureName": "string",
        "SourceColumn": "string",
        "TargetMeasureName": "string",
        "MeasureValueType": "DOUBLE"|"BIGINT"|"VARCHAR"|"BOOLEAN"|"TIMESTAMP"|"MULTI",
        "MultiMeasureAttributeMappings": [
          {
            "SourceColumn": "string",
            "TargetMultiMeasureAttributeName": "string",
            "MeasureValueType": "DOUBLE"|"BIGINT"|"BOOLEAN"|"VARCHAR"|"TIMESTAMP"
          }
          ...
        ]
      }
      ...
    ],
    "MeasureNameColumn": "string"
  },
  "DataModelS3Configuration": {
    "BucketName": "string",
    "ObjectKey": "string"
  }
}
```

`--data-source-configuration` (structure)

Defines configuration details about the data source for a batch load task.

DataSourceS3Configuration -> (structure)

Configuration of an S3 location for a file which contains data to load.

BucketName -> (string)

The bucket name of the customer S3 bucket.

ObjectKeyPrefix -> (string)

CsvConfiguration -> (structure)

A delimited data format where the column separator can be a comma and the record separator is a newline character.

ColumnSeparator -> (string)

Column separator can be one of comma (â,â), pipe (â[|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-batch-load-task.html#id1)), semicolon (â;â), tab(â/tâ), or blank space (â â).

EscapeChar -> (string)

Escape character can be one of

QuoteChar -> (string)

Can be single quote (â) or double quote (â).

NullValue -> (string)

Can be blank space (â â).

TrimWhiteSpace -> (boolean)

Specifies to trim leading and trailing white space.

DataFormat -> (string)

This is currently CSV.

Shorthand Syntax:

```
DataSourceS3Configuration={BucketName=string,ObjectKeyPrefix=string},CsvConfiguration={ColumnSeparator=string,EscapeChar=string,QuoteChar=string,NullValue=string,TrimWhiteSpace=boolean},DataFormat=string
```

JSON Syntax:

```
{
  "DataSourceS3Configuration": {
    "BucketName": "string",
    "ObjectKeyPrefix": "string"
  },
  "CsvConfiguration": {
    "ColumnSeparator": "string",
    "EscapeChar": "string",
    "QuoteChar": "string",
    "NullValue": "string",
    "TrimWhiteSpace": true|false
  },
  "DataFormat": "CSV"
}
```

`--report-configuration` (structure)

Report configuration for a batch load task. This contains details about where error reports are stored.

ReportS3Configuration -> (structure)

Configuration of an S3 location to write error reports and events for a batch load.

BucketName -> (string)

ObjectKeyPrefix -> (string)

EncryptionOption -> (string)

KmsKeyId -> (string)

Shorthand Syntax:

```
ReportS3Configuration={BucketName=string,ObjectKeyPrefix=string,EncryptionOption=string,KmsKeyId=string}
```

JSON Syntax:

```
{
  "ReportS3Configuration": {
    "BucketName": "string",
    "ObjectKeyPrefix": "string",
    "EncryptionOption": "SSE_S3"|"SSE_KMS",
    "KmsKeyId": "string"
  }
}
```

`--target-database-name` (string)

Target Timestream database for a batch load task.

`--target-table-name` (string)

Target Timestream table for a batch load task.

`--record-version` (long)

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

TaskId -> (string)

The ID of the batch load task.