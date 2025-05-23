# get-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-data-exports/get-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-data-exports/get-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bcm-data-exports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-data-exports/index.html#cli-aws-bcm-data-exports) ]

# get-execution

## Description

Exports data based on the source data update.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bcm-data-exports-2023-11-26/GetExecution)

## Synopsis

```
get-execution
--execution-id <value>
--export-arn <value>
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

`--execution-id` (string)

The ID for this specific execution.

`--export-arn` (string)

The Amazon Resource Name (ARN) of the Export object that generated this specific execution.

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

ExecutionId -> (string)

The ID for this specific execution.

ExecutionStatus -> (structure)

The status of this specific execution.

CompletedAt -> (timestamp)

The time when the execution was completed.

CreatedAt -> (timestamp)

The time when the execution was created.

LastUpdatedAt -> (timestamp)

The time when the execution was last updated.

StatusCode -> (string)

The code for the status of the execution.

StatusReason -> (string)

The reason for the failed status.

Export -> (structure)

The export data for this specific execution. This export data is a snapshot from when the execution was generated. The data could be different from the current export data if the export was updated since the execution was generated.

DataQuery -> (structure)

The data query for this specific data export.

QueryStatement -> (string)

The query statement.

TableConfigurations -> (map)

The table configuration.

key -> (string)

value -> (map)

key -> (string)

value -> (string)

Description -> (string)

The description for this specific data export.

DestinationConfigurations -> (structure)

The destination configuration for this specific data export.

S3Destination -> (structure)

An object that describes the destination of the data exports file.

S3Bucket -> (string)

The name of the Amazon S3 bucket used as the destination of a data export file.

S3OutputConfigurations -> (structure)

The output configuration for the data export.

Compression -> (string)

The compression type for the data export.

Format -> (string)

The file format for the data export.

OutputType -> (string)

The output type for the data export.

Overwrite -> (string)

The rule to follow when generating a version of the data export file. You have the choice to overwrite the previous version or to be delivered in addition to the previous versions. Overwriting exports can save on Amazon S3 storage costs. Creating new export versions allows you to track the changes in cost and usage data over time.

S3Prefix -> (string)

The S3 path prefix you want prepended to the name of your data export.

S3Region -> (string)

The S3 bucket Region.

ExportArn -> (string)

The Amazon Resource Name (ARN) for this export.

Name -> (string)

The name of this specific data export.

RefreshCadence -> (structure)

The cadence for Amazon Web Services to update the export in your S3 bucket.

Frequency -> (string)

The frequency that data exports are updated. The export refreshes each time the source data updates, up to three times daily.