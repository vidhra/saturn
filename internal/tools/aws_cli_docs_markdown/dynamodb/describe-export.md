# describe-exportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-export.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-export.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# describe-export

## Description

Describes an existing table export.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/DescribeExport)

## Synopsis

```
describe-export
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

`--export-arn` (string)

The Amazon Resource Name (ARN) associated with the export.

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

ExportDescription -> (structure)

Represents the properties of the export.

ExportArn -> (string)

The Amazon Resource Name (ARN) of the table export.

ExportStatus -> (string)

Export can be in one of the following states: IN_PROGRESS, COMPLETED, or FAILED.

StartTime -> (timestamp)

The time at which the export task began.

EndTime -> (timestamp)

The time at which the export task completed.

ExportManifest -> (string)

The name of the manifest file for the export task.

TableArn -> (string)

The Amazon Resource Name (ARN) of the table that was exported.

TableId -> (string)

Unique ID of the table that was exported.

ExportTime -> (timestamp)

Point in time from which table data was exported.

ClientToken -> (string)

The client token that was provided for the export task. A client token makes calls to `ExportTableToPointInTimeInput` idempotent, meaning that multiple identical calls have the same effect as one single call.

S3Bucket -> (string)

The name of the Amazon S3 bucket containing the export.

S3BucketOwner -> (string)

The ID of the Amazon Web Services account that owns the bucket containing the export.

S3Prefix -> (string)

The Amazon S3 bucket prefix used as the file name and path of the exported snapshot.

S3SseAlgorithm -> (string)

Type of encryption used on the bucket where export data is stored. Valid values for `S3SseAlgorithm` are:

- `AES256` - server-side encryption with Amazon S3 managed keys
- `KMS` - server-side encryption with KMS managed keys

S3SseKmsKeyId -> (string)

The ID of the KMS managed key used to encrypt the S3 bucket where export data is stored (if applicable).

FailureCode -> (string)

Status code for the result of the failed export.

FailureMessage -> (string)

Export failure reason description.

ExportFormat -> (string)

The format of the exported data. Valid values for `ExportFormat` are `DYNAMODB_JSON` or `ION` .

BilledSizeBytes -> (long)

The billable size of the table export.

ItemCount -> (long)

The number of items exported.

ExportType -> (string)

The type of export that was performed. Valid values are `FULL_EXPORT` or `INCREMENTAL_EXPORT` .

IncrementalExportSpecification -> (structure)

Optional object containing the parameters specific to an incremental export.

ExportFromTime -> (timestamp)

Time in the past which provides the inclusive start range for the export tableâs data, counted in seconds from the start of the Unix epoch. The incremental export will reflect the tableâs state including and after this point in time.

ExportToTime -> (timestamp)

Time in the past which provides the exclusive end range for the export tableâs data, counted in seconds from the start of the Unix epoch. The incremental export will reflect the tableâs state just prior to this point in time. If this is not provided, the latest time with data available will be used.

ExportViewType -> (string)

The view type that was chosen for the export. Valid values are `NEW_AND_OLD_IMAGES` and `NEW_IMAGES` . The default value is `NEW_AND_OLD_IMAGES` .