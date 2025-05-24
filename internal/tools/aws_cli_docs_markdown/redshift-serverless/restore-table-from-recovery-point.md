# restore-table-from-recovery-pointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/restore-table-from-recovery-point.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/restore-table-from-recovery-point.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift-serverless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/index.html#cli-aws-redshift-serverless) ]

# restore-table-from-recovery-point

## Description

Restores a table from a recovery point to your Amazon Redshift Serverless instance. You canât use this operation to restore tables with interleaved sort keys.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-serverless-2021-04-21/RestoreTableFromRecoveryPoint)

## Synopsis

```
restore-table-from-recovery-point
[--activate-case-sensitive-identifier | --no-activate-case-sensitive-identifier]
--namespace-name <value>
--new-table-name <value>
--recovery-point-id <value>
--source-database-name <value>
[--source-schema-name <value>]
--source-table-name <value>
[--target-database-name <value>]
[--target-schema-name <value>]
--workgroup-name <value>
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

`--activate-case-sensitive-identifier` | `--no-activate-case-sensitive-identifier` (boolean)

Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.

`--namespace-name` (string)

Namespace of the recovery point to restore from.

`--new-table-name` (string)

The name of the table to create from the restore operation.

`--recovery-point-id` (string)

The ID of the recovery point to restore the table from.

`--source-database-name` (string)

The name of the source database that contains the table being restored.

`--source-schema-name` (string)

The name of the source schema that contains the table being restored.

`--source-table-name` (string)

The name of the source table being restored.

`--target-database-name` (string)

The name of the database to restore the table to.

`--target-schema-name` (string)

The name of the schema to restore the table to.

`--workgroup-name` (string)

The workgroup to restore the table to.

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

tableRestoreStatus -> (structure)

Contains information about a table restore request.

message -> (string)

A message that explains the returned status. For example, if the status of the operation is `FAILED` , the message explains why the operation failed.

namespaceName -> (string)

The namespace of the table being restored from.

newTableName -> (string)

The name of the table to create from the restore operation.

progressInMegaBytes -> (long)

The amount of data restored to the new table so far, in megabytes (MB).

recoveryPointId -> (string)

The ID of the recovery point being restored from.

requestTime -> (timestamp)

The time that the table restore request was made, in Universal Coordinated Time (UTC).

snapshotName -> (string)

The name of the snapshot being restored from.

sourceDatabaseName -> (string)

The name of the source database being restored from.

sourceSchemaName -> (string)

The name of the source schema being restored from.

sourceTableName -> (string)

The name of the source table being restored from.

status -> (string)

A value that describes the current state of the table restore request. Possible values are `SUCCEEDED` , `FAILED` , `CANCELED` , `PENDING` , and `IN_PROGRESS` .

tableRestoreRequestId -> (string)

The ID of the RestoreTableFromSnapshot request.

targetDatabaseName -> (string)

The name of the database to restore to.

targetSchemaName -> (string)

The name of the schema to restore to.

totalDataInMegaBytes -> (long)

The total amount of data to restore to the new table, in megabytes (MB).

workgroupName -> (string)

The name of the workgroup being restored from.