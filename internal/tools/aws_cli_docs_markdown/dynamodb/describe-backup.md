# describe-backupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-backup.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-backup.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# describe-backup

## Description

Describes an existing backup of a table.

You can call `DescribeBackup` at a maximum rate of 10 times per second.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/DescribeBackup)

## Synopsis

```
describe-backup
--backup-arn <value>
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

`--backup-arn` (string)

The Amazon Resource Name (ARN) associated with the backup.

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

**To get information about an existing backup of a table**

The following `describe-backup` example displays information about the specified existing backup.

```
aws dynamodb describe-backup \
    --backup-arn arn:aws:dynamodb:us-west-2:123456789012:table/MusicCollection/backup/01576616366715-b4e58d3a
```

Output:

```
{
    "BackupDescription": {
        "BackupDetails": {
            "BackupArn": "arn:aws:dynamodb:us-west-2:123456789012:table/MusicCollection/backup/01576616366715-b4e58d3a",
            "BackupName": "MusicCollectionBackup",
            "BackupSizeBytes": 0,
            "BackupStatus": "AVAILABLE",
            "BackupType": "USER",
            "BackupCreationDateTime": 1576616366.715
        },
        "SourceTableDetails": {
            "TableName": "MusicCollection",
            "TableId": "b0c04bcc-309b-4352-b2ae-9088af169fe2",
            "TableArn": "arn:aws:dynamodb:us-west-2:123456789012:table/MusicCollection",
            "TableSizeBytes": 0,
            "KeySchema": [
                {
                    "AttributeName": "Artist",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "SongTitle",
                    "KeyType": "RANGE"
                }
            ],
            "TableCreationDateTime": 1576615228.571,
            "ProvisionedThroughput": {
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5
            },
            "ItemCount": 0,
            "BillingMode": "PROVISIONED"
        },
        "SourceTableFeatureDetails": {}
    }
}
```

For more information, see [On-Demand Backup and Restore for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html) in the *Amazon DynamoDB Developer Guide*.

## Output

BackupDescription -> (structure)

Contains the description of the backup created for the table.

BackupDetails -> (structure)

Contains the details of the backup created for the table.

BackupArn -> (string)

ARN associated with the backup.

BackupName -> (string)

Name of the requested backup.

BackupSizeBytes -> (long)

Size of the backup in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

BackupStatus -> (string)

Backup can be in one of the following states: CREATING, ACTIVE, DELETED.

BackupType -> (string)

BackupType:

- `USER` - You create and manage these using the on-demand backup feature.
- `SYSTEM` - If you delete a table with point-in-time recovery enabled, a `SYSTEM` backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion.
- `AWS_BACKUP` - On-demand backup created by you from Backup service.

BackupCreationDateTime -> (timestamp)

Time at which the backup was created. This is the request time of the backup.

BackupExpiryDateTime -> (timestamp)

Time at which the automatic on-demand backup created by DynamoDB will expire. This `SYSTEM` on-demand backup expires automatically 35 days after its creation.

SourceTableDetails -> (structure)

Contains the details of the table when the backup was created.

TableName -> (string)

The name of the table for which the backup was created.

TableId -> (string)

Unique identifier for the table for which the backup was created.

TableArn -> (string)

ARN of the table for which backup was created.

TableSizeBytes -> (long)

Size of the table in bytes. Note that this is an approximate value.

KeySchema -> (list)

Schema of the table.

(structure)

Represents *a single element* of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.

A `KeySchemaElement` represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one `KeySchemaElement` (for the partition key). A composite primary key would require one `KeySchemaElement` for the partition key, and another `KeySchemaElement` for the sort key.

A `KeySchemaElement` must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName -> (string)

The name of a key attribute.

KeyType -> (string)

The role that this key attribute will assume:

- `HASH` - partition key
- `RANGE` - sort key

### Note

The partition key of an item is also known as its *hash attribute* . The term âhash attributeâ derives from DynamoDBâs usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

The sort key of an item is also known as its *range attribute* . The term ârange attributeâ derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

TableCreationDateTime -> (timestamp)

Time when the source table was created.

ProvisionedThroughput -> (structure)

Read IOPs and Write IOPS on the table when the backup was created.

ReadCapacityUnits -> (long)

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide* .

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.

WriteCapacityUnits -> (long)

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide* .

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.

OnDemandThroughput -> (structure)

Sets the maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits` , `MaxWriteRequestUnits` , or both.

MaxReadRequestUnits -> (long)

Maximum number of read request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxReadRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxReadRequestUnits` to -1.

MaxWriteRequestUnits -> (long)

Maximum number of write request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxWriteRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxWriteRequestUnits` to -1.

ItemCount -> (long)

Number of items in the table. Note that this is an approximate value.

BillingMode -> (string)

Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

- `PROVISIONED` - Sets the read/write capacity mode to `PROVISIONED` . We recommend using `PROVISIONED` for predictable workloads.
- `PAY_PER_REQUEST` - Sets the read/write capacity mode to `PAY_PER_REQUEST` . We recommend using `PAY_PER_REQUEST` for unpredictable workloads.

SourceTableFeatureDetails -> (structure)

Contains the details of the features enabled on the table when the backup was created. For example, LSIs, GSIs, streams, TTL.

LocalSecondaryIndexes -> (list)

Represents the LSI properties for the table when the backup was created. It includes the IndexName, KeySchema and Projection for the LSIs on the table at the time of backup.

(structure)

Represents the properties of a local secondary index for the table when the backup was created.

IndexName -> (string)

Represents the name of the local secondary index.

KeySchema -> (list)

The complete key schema for a local secondary index, which consists of one or more pairs of attribute names and key types:

- `HASH` - partition key
- `RANGE` - sort key

### Note

The partition key of an item is also known as its *hash attribute* . The term âhash attributeâ derives from DynamoDBâs usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

The sort key of an item is also known as its *range attribute* . The term ârange attributeâ derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

(structure)

Represents *a single element* of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.

A `KeySchemaElement` represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one `KeySchemaElement` (for the partition key). A composite primary key would require one `KeySchemaElement` for the partition key, and another `KeySchemaElement` for the sort key.

A `KeySchemaElement` must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName -> (string)

The name of a key attribute.

KeyType -> (string)

The role that this key attribute will assume:

- `HASH` - partition key
- `RANGE` - sort key

### Note

The partition key of an item is also known as its *hash attribute* . The term âhash attributeâ derives from DynamoDBâs usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

The sort key of an item is also known as its *range attribute* . The term ârange attributeâ derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

Projection -> (structure)

Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType -> (string)

The set of attributes that are projected into the index:

- `KEYS_ONLY` - Only the index and primary keys are projected into the index.
- `INCLUDE` - In addition to the attributes described in `KEYS_ONLY` , the secondary index will include other non-key attributes that you specify.
- `ALL` - All of the table attributes are projected into the index.

When using the DynamoDB console, `ALL` is selected by default.

NonKeyAttributes -> (list)

Represents the non-key attribute names which will be projected into the index.

For global and local secondary indexes, the total count of `NonKeyAttributes` summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE` . You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.

(string)

GlobalSecondaryIndexes -> (list)

Represents the GSI properties for the table when the backup was created. It includes the IndexName, KeySchema, Projection, and ProvisionedThroughput for the GSIs on the table at the time of backup.

(structure)

Represents the properties of a global secondary index for the table when the backup was created.

IndexName -> (string)

The name of the global secondary index.

KeySchema -> (list)

The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:

- `HASH` - partition key
- `RANGE` - sort key

### Note

The partition key of an item is also known as its *hash attribute* . The term âhash attributeâ derives from DynamoDBâs usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

The sort key of an item is also known as its *range attribute* . The term ârange attributeâ derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

(structure)

Represents *a single element* of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.

A `KeySchemaElement` represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one `KeySchemaElement` (for the partition key). A composite primary key would require one `KeySchemaElement` for the partition key, and another `KeySchemaElement` for the sort key.

A `KeySchemaElement` must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName -> (string)

The name of a key attribute.

KeyType -> (string)

The role that this key attribute will assume:

- `HASH` - partition key
- `RANGE` - sort key

### Note

The partition key of an item is also known as its *hash attribute* . The term âhash attributeâ derives from DynamoDBâs usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

The sort key of an item is also known as its *range attribute* . The term ârange attributeâ derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

Projection -> (structure)

Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType -> (string)

The set of attributes that are projected into the index:

- `KEYS_ONLY` - Only the index and primary keys are projected into the index.
- `INCLUDE` - In addition to the attributes described in `KEYS_ONLY` , the secondary index will include other non-key attributes that you specify.
- `ALL` - All of the table attributes are projected into the index.

When using the DynamoDB console, `ALL` is selected by default.

NonKeyAttributes -> (list)

Represents the non-key attribute names which will be projected into the index.

For global and local secondary indexes, the total count of `NonKeyAttributes` summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE` . You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.

(string)

ProvisionedThroughput -> (structure)

Represents the provisioned throughput settings for the specified global secondary index.

ReadCapacityUnits -> (long)

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide* .

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.

WriteCapacityUnits -> (long)

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide* .

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.

OnDemandThroughput -> (structure)

Sets the maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits` , `MaxWriteRequestUnits` , or both.

MaxReadRequestUnits -> (long)

Maximum number of read request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxReadRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxReadRequestUnits` to -1.

MaxWriteRequestUnits -> (long)

Maximum number of write request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxWriteRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxWriteRequestUnits` to -1.

StreamDescription -> (structure)

Stream settings on the table when the backup was created.

StreamEnabled -> (boolean)

Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType -> (string)

When an item in the table is modified, `StreamViewType` determines what information is written to the stream for this table. Valid values for `StreamViewType` are:

- `KEYS_ONLY` - Only the key attributes of the modified item are written to the stream.
- `NEW_IMAGE` - The entire item, as it appears after it was modified, is written to the stream.
- `OLD_IMAGE` - The entire item, as it appeared before it was modified, is written to the stream.
- `NEW_AND_OLD_IMAGES` - Both the new and the old item images of the item are written to the stream.

TimeToLiveDescription -> (structure)

Time to Live settings on the table when the backup was created.

TimeToLiveStatus -> (string)

The TTL status for the table.

AttributeName -> (string)

The name of the TTL attribute for items in the table.

SSEDescription -> (structure)

The description of the server-side encryption status on the table when the backup was created.

Status -> (string)

Represents the current state of server-side encryption. The only supported values are:

- `ENABLED` - Server-side encryption is enabled.
- `UPDATING` - Server-side encryption is being updated.

SSEType -> (string)

Server-side encryption type. The only supported value is:

- `KMS` - Server-side encryption that uses Key Management Service. The key is stored in your account and is managed by KMS (KMS charges apply).

KMSMasterKeyArn -> (string)

The KMS key ARN used for the KMS encryption.

InaccessibleEncryptionDateTime -> (timestamp)

Indicates the time, in UNIX epoch date format, when DynamoDB detected that the tableâs KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the tableâs KMS key is accessible again. DynamoDB will initiate the table archival process when tableâs KMS key remains inaccessible for more than seven days from this date.