# restore-table-from-cluster-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-table-from-cluster-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-table-from-cluster-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# restore-table-from-cluster-snapshot

## Description

Creates a new table from a table in an Amazon Redshift cluster snapshot. You must create the new table within the Amazon Redshift cluster that the snapshot was taken from.

You cannot use `RestoreTableFromClusterSnapshot` to restore a table with the same name as an existing table in an Amazon Redshift cluster. That is, you cannot overwrite an existing table in a cluster with a restored table. If you want to replace your original table with a new, restored table, then rename or drop your original table before you call `RestoreTableFromClusterSnapshot` . When you have renamed your original table, then you can pass the original name of the table as the `NewTableName` parameter value in the call to `RestoreTableFromClusterSnapshot` . This way, you can replace the original table with the table created from the snapshot.

You canât use this operation to restore tables with [interleaved sort keys](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html#t_Sorting_data-interleaved) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/RestoreTableFromClusterSnapshot)

## Synopsis

```
restore-table-from-cluster-snapshot
--cluster-identifier <value>
--snapshot-identifier <value>
--source-database-name <value>
[--source-schema-name <value>]
--source-table-name <value>
[--target-database-name <value>]
[--target-schema-name <value>]
--new-table-name <value>
[--enable-case-sensitive-identifier | --no-enable-case-sensitive-identifier]
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

`--cluster-identifier` (string)

The identifier of the Amazon Redshift cluster to restore the table to.

`--snapshot-identifier` (string)

The identifier of the snapshot to restore the table from. This snapshot must have been created from the Amazon Redshift cluster specified by the `ClusterIdentifier` parameter.

`--source-database-name` (string)

The name of the source database that contains the table to restore from.

`--source-schema-name` (string)

The name of the source schema that contains the table to restore from. If you do not specify a `SourceSchemaName` value, the default is `public` .

`--source-table-name` (string)

The name of the source table to restore from.

`--target-database-name` (string)

The name of the database to restore the table to.

`--target-schema-name` (string)

The name of the schema to restore the table to.

`--new-table-name` (string)

The name of the table to create as a result of the current request.

`--enable-case-sensitive-identifier` | `--no-enable-case-sensitive-identifier` (boolean)

Indicates whether name identifiers for database, schema, and table are case sensitive. If `true` , the names are case sensitive. If `false` (default), the names are not case sensitive.

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

**To restore table from a cluster snapshot**

The following `restore-table-from-cluster-snapshot` example creates a new table from the specified table in the specified cluster snapshot.

```
aws redshift restore-table-from-cluster-snapshot /
    --cluster-identifier mycluster /
    --snapshot-identifier mycluster-2019-11-19-16-17 /
    --source-database-name dev /
    --source-schema-name public /
    --source-table-name mytable /
    --target-database-name dev /
    --target-schema-name public /
    --new-table-name mytable-clone
```

Output:

```
{
    "TableRestoreStatus": {
        "TableRestoreRequestId": "a123a12b-abc1-1a1a-a123-a1234ab12345",
        "Status": "PENDING",
        "RequestTime": "2019-12-20T00:20:16.402Z",
        "ClusterIdentifier": "mycluster",
        "SnapshotIdentifier": "mycluster-2019-11-19-16-17",
        "SourceDatabaseName": "dev",
        "SourceSchemaName": "public",
        "SourceTableName": "mytable",
        "TargetDatabaseName": "dev",
        "TargetSchemaName": "public",
        "NewTableName": "mytable-clone"
    }
}
```

For more information, see [Restoring a Table from a Snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#working-with-snapshot-restore-table-from-snapshot) in the *Amazon Redshift Cluster Management Guide*.

## Output

TableRestoreStatus -> (structure)

Describes the status of a  RestoreTableFromClusterSnapshot operation.

TableRestoreRequestId -> (string)

The unique identifier for the table restore request.

Status -> (string)

A value that describes the current state of the table restore request.

Valid Values: `SUCCEEDED` , `FAILED` , `CANCELED` , `PENDING` , `IN_PROGRESS`

Message -> (string)

A description of the status of the table restore request. Status values include `SUCCEEDED` , `FAILED` , `CANCELED` , `PENDING` , `IN_PROGRESS` .

RequestTime -> (timestamp)

The time that the table restore request was made, in Universal Coordinated Time (UTC).

ProgressInMegaBytes -> (long)

The amount of data restored to the new table so far, in megabytes (MB).

TotalDataInMegaBytes -> (long)

The total amount of data to restore to the new table, in megabytes (MB).

ClusterIdentifier -> (string)

The identifier of the Amazon Redshift cluster that the table is being restored to.

SnapshotIdentifier -> (string)

The identifier of the snapshot that the table is being restored from.

SourceDatabaseName -> (string)

The name of the source database that contains the table being restored.

SourceSchemaName -> (string)

The name of the source schema that contains the table being restored.

SourceTableName -> (string)

The name of the source table being restored.

TargetDatabaseName -> (string)

The name of the database to restore the table to.

TargetSchemaName -> (string)

The name of the schema to restore the table to.

NewTableName -> (string)

The name of the table to create as a result of the table restore request.