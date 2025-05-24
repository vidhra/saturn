# start-data-migrationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-data-migration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-data-migration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# start-data-migration

## Description

Starts the specified data migration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/StartDataMigration)

## Synopsis

```
start-data-migration
--data-migration-identifier <value>
--start-type <value>
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

`--data-migration-identifier` (string)

The identifier (name or ARN) of the data migration to start.

`--start-type` (string)

Specifies the start type for the data migration. Valid values include `start-replication` , `reload-target` , and `resume-processing` .

Possible values:

- `reload-target`
- `resume-processing`
- `start-replication`

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

DataMigration -> (structure)

The data migration that DMS started.

DataMigrationName -> (string)

The user-friendly name for the data migration.

DataMigrationArn -> (string)

The Amazon Resource Name (ARN) that identifies this replication.

DataMigrationCreateTime -> (timestamp)

The UTC time when DMS created the data migration.

DataMigrationStartTime -> (timestamp)

The UTC time when DMS started the data migration.

DataMigrationEndTime -> (timestamp)

The UTC time when data migration ended.

ServiceAccessRoleArn -> (string)

The IAM role that the data migration uses to access Amazon Web Services resources.

MigrationProjectArn -> (string)

The Amazon Resource Name (ARN) of the data migrationâs associated migration project.

DataMigrationType -> (string)

Specifies whether the data migration is full-load only, change data capture (CDC) only, or full-load and CDC.

DataMigrationSettings -> (structure)

Specifies CloudWatch settings and selection rules for the data migration.

NumberOfJobs -> (integer)

The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.

CloudwatchLogsEnabled -> (boolean)

Whether to enable CloudWatch logging for the data migration.

SelectionRules -> (string)

A JSON-formatted string that defines what objects to include and exclude from the migration.

SourceDataSettings -> (list)

Specifies information about the data migrationâs source data provider.

(structure)

Defines settings for a source data provider for a data migration.

CDCStartPosition -> (string)

The change data capture (CDC) start position for the source data provider.

CDCStartTime -> (timestamp)

The change data capture (CDC) start time for the source data provider.

CDCStopTime -> (timestamp)

The change data capture (CDC) stop time for the source data provider.

SlotName -> (string)

The name of the replication slot on the source data provider. This attribute is only valid for a PostgreSQL or Aurora PostgreSQL source.

TargetDataSettings -> (list)

Specifies information about the data migrationâs target data provider.

(structure)

Defines settings for a target data provider for a data migration.

TablePreparationMode -> (string)

This setting determines how DMS handles the target tables before starting a data migration, either by leaving them untouched, dropping and recreating them, or truncating the existing data in the target tables.

DataMigrationStatistics -> (structure)

Provides information about the data migrationâs run, including start and stop time, latency, and data migration progress.

TablesLoaded -> (integer)

The number of tables loaded in the current data migration run.

ElapsedTimeMillis -> (long)

The elapsed duration of the data migration run.

TablesLoading -> (integer)

The data migrationâs table loading progress.

FullLoadPercentage -> (integer)

The data migrationâs progress in the full-load migration phase.

CDCLatency -> (integer)

The current latency of the change data capture (CDC) operation.

TablesQueued -> (integer)

The number of tables that are waiting for processing.

TablesErrored -> (integer)

The number of tables that DMS failed to process.

StartTime -> (timestamp)

The time when the migration started.

StopTime -> (timestamp)

The time when the migration stopped or failed.

DataMigrationStatus -> (string)

The current status of the data migration.

PublicIpAddresses -> (list)

The IP addresses of the endpoints for the data migration.

(string)

DataMigrationCidrBlocks -> (list)

The CIDR blocks of the endpoints for the data migration.

(string)

LastFailureMessage -> (string)

Information about the data migrationâs most recent error or failure.

StopReason -> (string)

The reason the data migration last stopped.