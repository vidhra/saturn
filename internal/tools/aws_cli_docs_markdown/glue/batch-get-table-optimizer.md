# batch-get-table-optimizerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-get-table-optimizer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-get-table-optimizer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# batch-get-table-optimizer

## Description

Returns the configuration for the specified table optimizers.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchGetTableOptimizer)

## Synopsis

```
batch-get-table-optimizer
--entries <value>
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

`--entries` (list)

A list of `BatchGetTableOptimizerEntry` objects specifying the table optimizers to retrieve.

(structure)

Represents a table optimizer to retrieve in the `BatchGetTableOptimizer` operation.

catalogId -> (string)

The Catalog ID of the table.

databaseName -> (string)

The name of the database in the catalog in which the table resides.

tableName -> (string)

The name of the table.

type -> (string)

The type of table optimizer.

Shorthand Syntax:

```
catalogId=string,databaseName=string,tableName=string,type=string ...
```

JSON Syntax:

```
[
  {
    "catalogId": "string",
    "databaseName": "string",
    "tableName": "string",
    "type": "compaction"|"retention"|"orphan_file_deletion"
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

TableOptimizers -> (list)

A list of `BatchTableOptimizer` objects.

(structure)

Contains details for one of the table optimizers returned by the `BatchGetTableOptimizer` operation.

catalogId -> (string)

The Catalog ID of the table.

databaseName -> (string)

The name of the database in the catalog in which the table resides.

tableName -> (string)

The name of the table.

tableOptimizer -> (structure)

A `TableOptimizer` object that contains details on the configuration and last run of a table optimizer.

type -> (string)

The type of table optimizer. The valid values are:

- `compaction` : for managing compaction with a table optimizer.
- `retention` : for managing the retention of snapshot with a table optimizer.
- `orphan_file_deletion` : for managing the deletion of orphan files with a table optimizer.

configuration -> (structure)

A `TableOptimizerConfiguration` object that was specified when creating or updating a table optimizer.

roleArn -> (string)

A role passed by the caller which gives the service permission to update the resources associated with the optimizer on the callerâs behalf.

enabled -> (boolean)

Whether table optimization is enabled.

vpcConfiguration -> (tagged union structure)

A `TableOptimizerVpcConfiguration` object representing the VPC configuration for a table optimizer.

This configuration is necessary to perform optimization on tables that are in a customer VPC.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `glueConnectionName`.

glueConnectionName -> (string)

The name of the Glue connection used for the VPC for the table optimizer.

retentionConfiguration -> (structure)

The configuration for a snapshot retention optimizer.

icebergConfiguration -> (structure)

The configuration for an Iceberg snapshot retention optimizer.

snapshotRetentionPeriodInDays -> (integer)

The number of days to retain the Iceberg snapshots. If an input is not provided, the corresponding Iceberg table configuration field will be used or if not present, the default value 5 will be used.

numberOfSnapshotsToRetain -> (integer)

The number of Iceberg snapshots to retain within the retention period. If an input is not provided, the corresponding Iceberg table configuration field will be used or if not present, the default value 1 will be used.

cleanExpiredFiles -> (boolean)

If set to false, snapshots are only deleted from table metadata, and the underlying data and metadata files are not deleted.

orphanFileDeletionConfiguration -> (structure)

The configuration for an orphan file deletion optimizer.

icebergConfiguration -> (structure)

The configuration for an Iceberg orphan file deletion optimizer.

orphanFileRetentionPeriodInDays -> (integer)

The number of days that orphan files should be retained before file deletion. If an input is not provided, the default value 3 will be used.

location -> (string)

Specifies a directory in which to look for files (defaults to the tableâs location). You may choose a sub-directory rather than the top-level table location.

lastRun -> (structure)

A `TableOptimizerRun` object representing the last run of the table optimizer.

eventType -> (string)

An event type representing the status of the table optimizer run.

startTimestamp -> (timestamp)

Represents the epoch timestamp at which the compaction job was started within Lake Formation.

endTimestamp -> (timestamp)

Represents the epoch timestamp at which the compaction job ended.

metrics -> (structure)

A `RunMetrics` object containing metrics for the optimizer run.

This member is deprecated. See the individual metric members for compaction, retention, and orphan file deletion.

NumberOfBytesCompacted -> (string)

The number of bytes removed by the compaction job run.

NumberOfFilesCompacted -> (string)

The number of files removed by the compaction job run.

NumberOfDpus -> (string)

The number of DPUs consumed by the job, rounded up to the nearest whole number.

JobDurationInHour -> (string)

The duration of the job in hours.

error -> (string)

An error that occured during the optimizer run.

compactionMetrics -> (structure)

A `CompactionMetrics` object containing metrics for the optimizer run.

IcebergMetrics -> (structure)

A structure containing the Iceberg compaction metrics for the optimizer run.

NumberOfBytesCompacted -> (long)

The number of bytes removed by the compaction job run.

NumberOfFilesCompacted -> (long)

The number of files removed by the compaction job run.

DpuHours -> (double)

The number of DPU hours consumed by the job.

NumberOfDpus -> (integer)

The number of DPUs consumed by the job, rounded up to the nearest whole number.

JobDurationInHour -> (double)

The duration of the job in hours.

retentionMetrics -> (structure)

A `RetentionMetrics` object containing metrics for the optimizer run.

IcebergMetrics -> (structure)

A structure containing the Iceberg retention metrics for the optimizer run.

NumberOfDataFilesDeleted -> (long)

The number of data files deleted by the retention job run.

NumberOfManifestFilesDeleted -> (long)

The number of manifest files deleted by the retention job run.

NumberOfManifestListsDeleted -> (long)

The number of manifest lists deleted by the retention job run.

DpuHours -> (double)

The number of DPU hours consumed by the job.

NumberOfDpus -> (integer)

The number of DPUs consumed by the job, rounded up to the nearest whole number.

JobDurationInHour -> (double)

The duration of the job in hours.

orphanFileDeletionMetrics -> (structure)

An `OrphanFileDeletionMetrics` object containing metrics for the optimizer run.

IcebergMetrics -> (structure)

A structure containing the Iceberg orphan file deletion metrics for the optimizer run.

NumberOfOrphanFilesDeleted -> (long)

The number of orphan files deleted by the orphan file deletion job run.

DpuHours -> (double)

The number of DPU hours consumed by the job.

NumberOfDpus -> (integer)

The number of DPUs consumed by the job, rounded up to the nearest whole number.

JobDurationInHour -> (double)

The duration of the job in hours.

Failures -> (list)

A list of errors from the operation.

(structure)

Contains details on one of the errors in the error list returned by the `BatchGetTableOptimizer` operation.

error -> (structure)

An `ErrorDetail` object containing code and message details about the error.

ErrorCode -> (string)

The code associated with this error.

ErrorMessage -> (string)

A message describing the error.

catalogId -> (string)

The Catalog ID of the table.

databaseName -> (string)

The name of the database in the catalog in which the table resides.

tableName -> (string)

The name of the table.

type -> (string)

The type of table optimizer.