# create-global-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-global-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-global-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# create-global-table

## Description

Creates a global table from an existing table. A global table creates a replication relationship between two or more DynamoDB tables with the same table name in the provided Regions.

### Warning

This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use [Global Tables version 2019.11.21 (Current)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).

To determine which version youâre using, see [Determining the global table version you are using](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html) . To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see [Upgrading global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html) .

If you want to add a new replica table to a global table, each of the following conditions must be true:

- The table must have the same primary key as all of the other replicas.
- The table must have the same name as all of the other replicas.
- The table must have DynamoDB Streams enabled, with the stream containing both the new and the old images of the item.
- None of the replica tables in the global table can contain any data.

If global secondary indexes are specified, then the following conditions must also be met:

- The global secondary indexes must have the same name.
- The global secondary indexes must have the same hash key and sort key (if present).

If local secondary indexes are specified, then the following conditions must also be met:

- The local secondary indexes must have the same name.
- The local secondary indexes must have the same hash key and sort key (if present).

### Warning

Write capacity settings should be set consistently across your replica tables and secondary indexes. DynamoDB strongly recommends enabling auto scaling to manage the write capacity settings for all of your global tables replicas and indexes.

If you prefer to manage write capacity settings manually, you should provision equal replicated write capacity units to your replica tables. You should also provision equal replicated write capacity units to matching secondary indexes across your global table.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/CreateGlobalTable)

## Synopsis

```
create-global-table
--global-table-name <value>
--replication-group <value>
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

`--global-table-name` (string)

The global table name.

`--replication-group` (list)

The Regions where the global table needs to be created.

(structure)

Represents the properties of a replica.

RegionName -> (string)

The Region where the replica needs to be created.

Shorthand Syntax:

```
RegionName=string ...
```

JSON Syntax:

```
[
  {
    "RegionName": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a global table**

The following `create-global-table` example creates a global table from two identical tables in the specified, separate AWS Regions.

```
aws dynamodb create-global-table \
    --global-table-name MusicCollection \
    --replication-group RegionName=us-east-2 RegionName=us-east-1 \
    --region us-east-2
```

Output:

```
{
    "GlobalTableDescription": {
        "ReplicationGroup": [
            {
                "RegionName": "us-east-2"
            },
            {
                "RegionName": "us-east-1"
            }
        ],
        "GlobalTableArn": "arn:aws:dynamodb::123456789012:global-table/MusicCollection",
        "CreationDateTime": 1576625818.532,
        "GlobalTableStatus": "CREATING",
        "GlobalTableName": "MusicCollection"
    }
}
```

For more information, see [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) in the *Amazon DynamoDB Developer Guide*.

## Output

GlobalTableDescription -> (structure)

Contains the details of the global table.

ReplicationGroup -> (list)

The Regions where the global table has replicas.

(structure)

Contains the details of the replica.

RegionName -> (string)

The name of the Region.

ReplicaStatus -> (string)

The current state of the replica:

- `CREATING` - The replica is being created.
- `UPDATING` - The replica is being updated.
- `DELETING` - The replica is being deleted.
- `ACTIVE` - The replica is ready for use.
- `REGION_DISABLED` - The replica is inaccessible because the Amazon Web Services Region has been disabled.

### Note

If the Amazon Web Services Region remains inaccessible for more than 20 hours, DynamoDB will remove this replica from the replication group. The replica will not be deleted and replication will stop from and to this region.

- `INACCESSIBLE_ENCRYPTION_CREDENTIALS` - The KMS key used to encrypt the table is inaccessible.

### Note

If the KMS key remains inaccessible for more than 20 hours, DynamoDB will remove this replica from the replication group. The replica will not be deleted and replication will stop from and to this region.

ReplicaStatusDescription -> (string)

Detailed information about the replica status.

ReplicaStatusPercentProgress -> (string)

Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId -> (string)

The KMS key of the replica that will be used for KMS encryption.

ProvisionedThroughputOverride -> (structure)

Replica-specific provisioned throughput. If not described, uses the source tableâs provisioned throughput settings.

ReadCapacityUnits -> (long)

Replica-specific read capacity units. If not specified, uses the source tableâs read capacity settings.

OnDemandThroughputOverride -> (structure)

Overrides the maximum on-demand throughput settings for the specified replica table.

MaxReadRequestUnits -> (long)

Maximum number of read request units for the specified replica table.

WarmThroughput -> (structure)

Represents the warm throughput value for this replica.

ReadUnitsPerSecond -> (long)

Represents the base tableâs warm throughput value in read units per second.

WriteUnitsPerSecond -> (long)

Represents the base tableâs warm throughput value in write units per second.

Status -> (string)

Represents warm throughput value of the base table.

GlobalSecondaryIndexes -> (list)

Replica-specific global secondary index settings.

(structure)

Represents the properties of a replica global secondary index.

IndexName -> (string)

The name of the global secondary index.

ProvisionedThroughputOverride -> (structure)

If not described, uses the source table GSIâs read capacity settings.

ReadCapacityUnits -> (long)

Replica-specific read capacity units. If not specified, uses the source tableâs read capacity settings.

OnDemandThroughputOverride -> (structure)

Overrides the maximum on-demand throughput for the specified global secondary index in the specified replica table.

MaxReadRequestUnits -> (long)

Maximum number of read request units for the specified replica table.

WarmThroughput -> (structure)

Represents the warm throughput of the global secondary index for this replica.

ReadUnitsPerSecond -> (long)

Represents warm throughput read units per second value for a global secondary index.

WriteUnitsPerSecond -> (long)

Represents warm throughput write units per second value for a global secondary index.

Status -> (string)

Represents the warm throughput status being created or updated on a global secondary index. The status can only be `UPDATING` or `ACTIVE` .

ReplicaInaccessibleDateTime -> (timestamp)

The time at which the replica was first detected as inaccessible. To determine cause of inaccessibility check the `ReplicaStatus` property.

ReplicaTableClassSummary -> (structure)

Contains details of the table class.

TableClass -> (string)

The table class of the specified table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS` .

LastUpdateDateTime -> (timestamp)

The date and time at which the table class was last updated.

GlobalTableArn -> (string)

The unique identifier of the global table.

CreationDateTime -> (timestamp)

The creation time of the global table.

GlobalTableStatus -> (string)

The current state of the global table:

- `CREATING` - The global table is being created.
- `UPDATING` - The global table is being updated.
- `DELETING` - The global table is being deleted.
- `ACTIVE` - The global table is ready for use.

GlobalTableName -> (string)

The global table name.