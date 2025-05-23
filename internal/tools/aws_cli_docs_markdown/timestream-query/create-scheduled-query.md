# create-scheduled-queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/create-scheduled-query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/create-scheduled-query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [timestream-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/index.html#cli-aws-timestream-query) ]

# create-scheduled-query

## Description

Create a scheduled query that will be run on your behalf at the configured schedule. Timestream assumes the execution role provided as part of the `ScheduledQueryExecutionRoleArn` parameter to run the query. You can use the `NotificationConfiguration` parameter to configure notification for your scheduled query operations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/timestream-query-2018-11-01/CreateScheduledQuery)

## Synopsis

```
create-scheduled-query
--name <value>
--query-string <value>
--schedule-configuration <value>
--notification-configuration <value>
[--target-configuration <value>]
[--client-token <value>]
--scheduled-query-execution-role-arn <value>
[--tags <value>]
[--kms-key-id <value>]
--error-report-configuration <value>
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

Name of the scheduled query.

`--query-string` (string)

The query string to run. Parameter names can be specified in the query string `@` character followed by an identifier. The named Parameter `@scheduled_runtime` is reserved and can be used in the query to get the time at which the query is scheduled to run.

The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of `@scheduled_runtime` paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the `@scheduled_runtime` parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.

`--schedule-configuration` (structure)

The schedule configuration for the query.

ScheduleExpression -> (string)

An expression that denotes when to trigger the scheduled query run. This can be a cron expression or a rate expression.

Shorthand Syntax:

```
ScheduleExpression=string
```

JSON Syntax:

```
{
  "ScheduleExpression": "string"
}
```

`--notification-configuration` (structure)

Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.

SnsConfiguration -> (structure)

Details about the Amazon Simple Notification Service (SNS) configuration. This field is visible only when SNS Topic is provided when updating the account settings.

TopicArn -> (string)

SNS topic ARN that the scheduled query status notifications will be sent to.

Shorthand Syntax:

```
SnsConfiguration={TopicArn=string}
```

JSON Syntax:

```
{
  "SnsConfiguration": {
    "TopicArn": "string"
  }
}
```

`--target-configuration` (structure)

Configuration used for writing the result of a query.

TimestreamConfiguration -> (structure)

Configuration needed to write data into the Timestream database and table.

DatabaseName -> (string)

Name of Timestream database to which the query result will be written.

TableName -> (string)

Name of Timestream table that the query result will be written to. The table should be within the same database that is provided in Timestream configuration.

TimeColumn -> (string)

Column from query result that should be used as the time column in destination table. Column type for this should be TIMESTAMP.

DimensionMappings -> (list)

This is to allow mapping column(s) from the query result to the dimension in the destination table.

(structure)

This type is used to map column(s) from the query result to a dimension in the destination table.

Name -> (string)

Column name from query result.

DimensionValueType -> (string)

Type for the dimension.

MultiMeasureMappings -> (structure)

Multi-measure mappings.

TargetMultiMeasureName -> (string)

The name of the target multi-measure name in the derived table. This input is required when measureNameColumn is not provided. If MeasureNameColumn is provided, then value from that column will be used as multi-measure name.

MultiMeasureAttributeMappings -> (list)

Required. Attribute mappings to be used for mapping query results to ingest data for multi-measure attributes.

(structure)

Attribute mapping for MULTI value measures.

SourceColumn -> (string)

Source column from where the attribute value is to be read.

TargetMultiMeasureAttributeName -> (string)

Custom name to be used for attribute name in derived table. If not provided, source column name would be used.

MeasureValueType -> (string)

Type of the attribute to be read from the source column.

MixedMeasureMappings -> (list)

Specifies how to map measures to multi-measure records.

(structure)

MixedMeasureMappings are mappings that can be used to ingest data into a mixture of narrow and multi measures in the derived table.

MeasureName -> (string)

Refers to the value of measure_name in a result row. This field is required if MeasureNameColumn is provided.

SourceColumn -> (string)

This field refers to the source column from which measure-value is to be read for result materialization.

TargetMeasureName -> (string)

Target measure name to be used. If not provided, the target measure name by default would be measure-name if provided, or sourceColumn otherwise.

MeasureValueType -> (string)

Type of the value that is to be read from sourceColumn. If the mapping is for MULTI, use MeasureValueType.MULTI.

MultiMeasureAttributeMappings -> (list)

Required when measureValueType is MULTI. Attribute mappings for MULTI value measures.

(structure)

Attribute mapping for MULTI value measures.

SourceColumn -> (string)

Source column from where the attribute value is to be read.

TargetMultiMeasureAttributeName -> (string)

Custom name to be used for attribute name in derived table. If not provided, source column name would be used.

MeasureValueType -> (string)

Type of the attribute to be read from the source column.

MeasureNameColumn -> (string)

Name of the measure column.

JSON Syntax:

```
{
  "TimestreamConfiguration": {
    "DatabaseName": "string",
    "TableName": "string",
    "TimeColumn": "string",
    "DimensionMappings": [
      {
        "Name": "string",
        "DimensionValueType": "VARCHAR"
      }
      ...
    ],
    "MultiMeasureMappings": {
      "TargetMultiMeasureName": "string",
      "MultiMeasureAttributeMappings": [
        {
          "SourceColumn": "string",
          "TargetMultiMeasureAttributeName": "string",
          "MeasureValueType": "BIGINT"|"BOOLEAN"|"DOUBLE"|"VARCHAR"|"TIMESTAMP"
        }
        ...
      ]
    },
    "MixedMeasureMappings": [
      {
        "MeasureName": "string",
        "SourceColumn": "string",
        "TargetMeasureName": "string",
        "MeasureValueType": "BIGINT"|"BOOLEAN"|"DOUBLE"|"VARCHAR"|"MULTI",
        "MultiMeasureAttributeMappings": [
          {
            "SourceColumn": "string",
            "TargetMultiMeasureAttributeName": "string",
            "MeasureValueType": "BIGINT"|"BOOLEAN"|"DOUBLE"|"VARCHAR"|"TIMESTAMP"
          }
          ...
        ]
      }
      ...
    ],
    "MeasureNameColumn": "string"
  }
}
```

`--client-token` (string)

Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result. Making multiple identical CreateScheduledQuery requests has the same effect as making a single request.

- If CreateScheduledQuery is called without a `ClientToken` , the Query SDK generates a `ClientToken` on your behalf.
- After 8 hours, any request with the same `ClientToken` is treated as a new request.

`--scheduled-query-execution-role-arn` (string)

The ARN for the IAM role that Timestream will assume when running the scheduled query.

`--tags` (list)

A list of key-value pairs to label the scheduled query.

(structure)

A tag is a label that you assign to a Timestream database and/or table. Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize databases and/or tables, for example, by purpose, owner, or environment.

Key -> (string)

The key of the tag. Tag keys are case sensitive.

Value -> (string)

The value of the tag. Tag values are case sensitive and can be null.

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

`--kms-key-id` (string)

The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with *alias/*

If ErrorReportConfiguration uses `SSE_KMS` as encryption type, the same KmsKeyId is used to encrypt the error report at rest.

`--error-report-configuration` (structure)

Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.

S3Configuration -> (structure)

The S3 configuration for the error reports.

BucketName -> (string)

Name of the S3 bucket under which error reports will be created.

ObjectKeyPrefix -> (string)

Prefix for the error report key. Timestream by default adds the following prefix to the error report path.

EncryptionOption -> (string)

Encryption at rest options for the error reports. If no encryption option is specified, Timestream will choose SSE_S3 as default.

Shorthand Syntax:

```
S3Configuration={BucketName=string,ObjectKeyPrefix=string,EncryptionOption=string}
```

JSON Syntax:

```
{
  "S3Configuration": {
    "BucketName": "string",
    "ObjectKeyPrefix": "string",
    "EncryptionOption": "SSE_S3"|"SSE_KMS"
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

Arn -> (string)

ARN for the created scheduled query.