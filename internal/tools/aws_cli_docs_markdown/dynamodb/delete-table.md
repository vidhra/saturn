# delete-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# delete-table

## Description

The `DeleteTable` operation deletes a table and all of its items. After a `DeleteTable` request, the specified table is in the `DELETING` state until DynamoDB completes the deletion. If the table is in the `ACTIVE` state, you can delete it. If a table is in `CREATING` or `UPDATING` states, then DynamoDB returns a `ResourceInUseException` . If the specified table does not exist, DynamoDB returns a `ResourceNotFoundException` . If table is already in the `DELETING` state, no error is returned.

### Warning

For global tables, this operation only applies to global tables using Version 2019.11.21 (Current version).

### Note

DynamoDB might continue to accept data read and write operations, such as `GetItem` and `PutItem` , on a table in the `DELETING` state until the table deletion is complete. For the full list of table states, see [TableStatus](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableDescription.html#DDB-Type-TableDescription-TableStatus) .

When you delete a table, any indexes on that table are also deleted.

If you have DynamoDB Streams enabled on the table, then the corresponding stream on that table goes into the `DISABLED` state, and the stream is automatically deleted after 24 hours.

Use the `DescribeTable` action to check the status of the table.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/DeleteTable)

## Synopsis

```
delete-table
--table-name <value>
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

`--table-name` (string)

The name of the table to delete. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.

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

**To delete a table**

The following `delete-table` example deletes the `MusicCollection` table.

```
aws dynamodb delete-table \
    --table-name MusicCollection
```

Output:

```
{
    "TableDescription": {
        "TableStatus": "DELETING",
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableName": "MusicCollection",
        "ProvisionedThroughput": {
            "NumberOfDecreasesToday": 0,
            "WriteCapacityUnits": 5,
            "ReadCapacityUnits": 5
        }
    }
}
```

For more information, see [Deleting a Table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.Basics.html#WorkingWithTables.Basics.DeleteTable) in the *Amazon DynamoDB Developer Guide*.

## Output

TableDescription -> (structure)

Represents the properties of a table.

AttributeDefinitions -> (list)

An array of `AttributeDefinition` objects. Each of these objects describes one attribute in the table and index key schema.

Each `AttributeDefinition` object in this array is composed of:

- `AttributeName` - The name of the attribute.
- `AttributeType` - The data type for the attribute.

(structure)

Represents an attribute for describing the schema for the table and indexes.

AttributeName -> (string)

A name for the attribute.

AttributeType -> (string)

The data type for the attribute, where:

- `S` - the attribute is of type String
- `N` - the attribute is of type Number
- `B` - the attribute is of type Binary

TableName -> (string)

The name of the table.

KeySchema -> (list)

The primary key structure for the table. Each `KeySchemaElement` consists of:

- `AttributeName` - The name of the attribute.
- `KeyType` - The role of the attribute:
- `HASH` - partition key
- `RANGE` - sort key

### Note

The partition key of an item is also known as its *hash attribute* . The term âhash attributeâ derives from DynamoDBâs usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

The sort key of an item is also known as its *range attribute* . The term ârange attributeâ derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

For more information about primary keys, see [Primary Key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html#DataModelPrimaryKey) in the *Amazon DynamoDB Developer Guide* .

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

TableStatus -> (string)

The current state of the table:

- `CREATING` - The table is being created.
- `UPDATING` - The table/index configuration is being updated. The table/index remains available for data operations when `UPDATING` .
- `DELETING` - The table is being deleted.
- `ACTIVE` - The table is ready for use.
- `INACCESSIBLE_ENCRYPTION_CREDENTIALS` - The KMS key used to encrypt the table in inaccessible. Table operations may fail due to failure to use the KMS key. DynamoDB will initiate the table archival process when a tableâs KMS key remains inaccessible for more than seven days.
- `ARCHIVING` - The table is being archived. Operations are not allowed until archival is complete.
- `ARCHIVED` - The table has been archived. See the ArchivalReason for more information.

CreationDateTime -> (timestamp)

The date and time when the table was created, in [UNIX epoch time](http://www.epochconverter.com/) format.

ProvisionedThroughput -> (structure)

The provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.

LastIncreaseDateTime -> (timestamp)

The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime -> (timestamp)

The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday -> (long)

The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide* .

ReadCapacityUnits -> (long)

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException` . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 `ReadCapacityUnits` per second provides 100 eventually consistent `ReadCapacityUnits` per second.

WriteCapacityUnits -> (long)

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException` .

TableSizeBytes -> (long)

The total size of the specified table, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount -> (long)

The number of items in the specified table. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

TableArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the table.

TableId -> (string)

Unique identifier for the table for which the backup was created.

BillingModeSummary -> (structure)

Contains the details for the read/write capacity mode.

BillingMode -> (string)

Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

- `PROVISIONED` - Sets the read/write capacity mode to `PROVISIONED` . We recommend using `PROVISIONED` for predictable workloads.
- `PAY_PER_REQUEST` - Sets the read/write capacity mode to `PAY_PER_REQUEST` . We recommend using `PAY_PER_REQUEST` for unpredictable workloads.

LastUpdateToPayPerRequestDateTime -> (timestamp)

Represents the time when `PAY_PER_REQUEST` was last set as the read/write capacity mode.

LocalSecondaryIndexes -> (list)

Represents one or more local secondary indexes on the table. Each index is scoped to a given partition key value. Tables with one or more local secondary indexes are subject to an item collection size limit, where the amount of data within a given item collection cannot exceed 10 GB. Each element is composed of:

- `IndexName` - The name of the local secondary index.
- `KeySchema` - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
- `Projection` - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
- `ProjectionType` - One of the following:
- `KEYS_ONLY` - Only the index and primary keys are projected into the index.
- `INCLUDE` - Only the specified table attributes are projected into the index. The list of projected attributes is in `NonKeyAttributes` .
- `ALL` - All of the table attributes are projected into the index.
- `NonKeyAttributes` - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes` , summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE` . You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.
- `IndexSizeBytes` - Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
- `ItemCount` - Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

If the table is in the `DELETING` state, no information about indexes will be returned.

(structure)

Represents the properties of a local secondary index.

IndexName -> (string)

Represents the name of the local secondary index.

KeySchema -> (list)

The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:

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

IndexSizeBytes -> (long)

The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount -> (long)

The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the index.

GlobalSecondaryIndexes -> (list)

The global secondary indexes, if any, on the table. Each index is scoped to a given partition key value. Each element is composed of:

- `Backfilling` - If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table. It is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a `CreateTable` operation.)  You can delete an index that is being created during the `Backfilling` phase when `IndexStatus` is set to CREATING and `Backfilling` is true. You canât delete the index that is being created when `IndexStatus` is set to CREATING and `Backfilling` is false. (This attribute does not appear for indexes that were created during a `CreateTable` operation.)
- `IndexName` - The name of the global secondary index.
- `IndexSizeBytes` - The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
- `IndexStatus` - The current status of the global secondary index:
- `CREATING` - The index is being created.
- `UPDATING` - The index is being updated.
- `DELETING` - The index is being deleted.
- `ACTIVE` - The index is ready for use.
- `ItemCount` - The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
- `KeySchema` - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
- `Projection` - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
- `ProjectionType` - One of the following:
- `KEYS_ONLY` - Only the index and primary keys are projected into the index.
- `INCLUDE` - In addition to the attributes described in `KEYS_ONLY` , the secondary index will include other non-key attributes that you specify.
- `ALL` - All of the table attributes are projected into the index.
- `NonKeyAttributes` - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes` , summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE` . You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.
- `ProvisionedThroughput` - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases.

If the table is in the `DELETING` state, no information about indexes will be returned.

(structure)

Represents the properties of a global secondary index.

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

IndexStatus -> (string)

The current state of the global secondary index:

- `CREATING` - The index is being created.
- `UPDATING` - The index is being updated.
- `DELETING` - The index is being deleted.
- `ACTIVE` - The index is ready for use.

Backfilling -> (boolean)

Indicates whether the index is currently backfilling. *Backfilling* is the process of reading items from the table and determining whether they can be added to the index. (Not all items will qualify: For example, a partition key cannot have any duplicate values.) If an item can be added to the index, DynamoDB will do so. After all items have been processed, the backfilling operation is complete and `Backfilling` is false.

You can delete an index that is being created during the `Backfilling` phase when `IndexStatus` is set to CREATING and `Backfilling` is true. You canât delete the index that is being created when `IndexStatus` is set to CREATING and `Backfilling` is false.

### Note

For indexes that were created during a `CreateTable` operation, the `Backfilling` attribute does not appear in the `DescribeTable` output.

ProvisionedThroughput -> (structure)

Represents the provisioned throughput settings for the specified global secondary index.

For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide* .

LastIncreaseDateTime -> (timestamp)

The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime -> (timestamp)

The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday -> (long)

The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide* .

ReadCapacityUnits -> (long)

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException` . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 `ReadCapacityUnits` per second provides 100 eventually consistent `ReadCapacityUnits` per second.

WriteCapacityUnits -> (long)

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException` .

IndexSizeBytes -> (long)

The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount -> (long)

The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the index.

OnDemandThroughput -> (structure)

The maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify `MaxReadRequestUnits` , `MaxWriteRequestUnits` , or both.

MaxReadRequestUnits -> (long)

Maximum number of read request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxReadRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxReadRequestUnits` to -1.

MaxWriteRequestUnits -> (long)

Maximum number of write request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxWriteRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxWriteRequestUnits` to -1.

WarmThroughput -> (structure)

Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index.

ReadUnitsPerSecond -> (long)

Represents warm throughput read units per second value for a global secondary index.

WriteUnitsPerSecond -> (long)

Represents warm throughput write units per second value for a global secondary index.

Status -> (string)

Represents the warm throughput status being created or updated on a global secondary index. The status can only be `UPDATING` or `ACTIVE` .

StreamSpecification -> (structure)

The current DynamoDB Streams configuration for the table.

StreamEnabled -> (boolean)

Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType -> (string)

When an item in the table is modified, `StreamViewType` determines what information is written to the stream for this table. Valid values for `StreamViewType` are:

- `KEYS_ONLY` - Only the key attributes of the modified item are written to the stream.
- `NEW_IMAGE` - The entire item, as it appears after it was modified, is written to the stream.
- `OLD_IMAGE` - The entire item, as it appeared before it was modified, is written to the stream.
- `NEW_AND_OLD_IMAGES` - Both the new and the old item images of the item are written to the stream.

LatestStreamLabel -> (string)

A timestamp, in ISO 8601 format, for this stream.

Note that `LatestStreamLabel` is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:

- Amazon Web Services customer ID
- Table name
- `StreamLabel`

LatestStreamArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.

GlobalTableVersion -> (string)

Represents the version of [global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) in use, if the table is replicated across Amazon Web Services Regions.

Replicas -> (list)

Represents replicas of the table.

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

RestoreSummary -> (structure)

Contains details for the restore.

SourceBackupArn -> (string)

The Amazon Resource Name (ARN) of the backup from which the table was restored.

SourceTableArn -> (string)

The ARN of the source table of the backup that is being restored.

RestoreDateTime -> (timestamp)

Point in time or source backup time.

RestoreInProgress -> (boolean)

Indicates if a restore is in progress or not.

SSEDescription -> (structure)

The description of the server-side encryption status on the specified table.

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

ArchivalSummary -> (structure)

Contains information about the table archive.

ArchivalDateTime -> (timestamp)

The date and time when table archival was initiated by DynamoDB, in UNIX epoch time format.

ArchivalReason -> (string)

The reason DynamoDB archived the table. Currently, the only possible value is:

- `INACCESSIBLE_ENCRYPTION_CREDENTIALS` - The table was archived due to the tableâs KMS key being inaccessible for more than seven days. An On-Demand backup was created at the archival time.

ArchivalBackupArn -> (string)

The Amazon Resource Name (ARN) of the backup the table was archived to, when applicable in the archival reason. If you wish to restore this backup to the same table name, you will need to delete the original table.

TableClassSummary -> (structure)

Contains details of the table class.

TableClass -> (string)

The table class of the specified table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS` .

LastUpdateDateTime -> (timestamp)

The date and time at which the table class was last updated.

DeletionProtectionEnabled -> (boolean)

Indicates whether deletion protection is enabled (true) or disabled (false) on the table.

OnDemandThroughput -> (structure)

The maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits` , `MaxWriteRequestUnits` , or both.

MaxReadRequestUnits -> (long)

Maximum number of read request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxReadRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxReadRequestUnits` to -1.

MaxWriteRequestUnits -> (long)

Maximum number of write request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxWriteRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxWriteRequestUnits` to -1.

WarmThroughput -> (structure)

Describes the warm throughput value of the base table.

ReadUnitsPerSecond -> (long)

Represents the base tableâs warm throughput value in read units per second.

WriteUnitsPerSecond -> (long)

Represents the base tableâs warm throughput value in write units per second.

Status -> (string)

Represents warm throughput value of the base table.

MultiRegionConsistency -> (string)

Indicates one of the following consistency modes for a global table:

- `EVENTUAL` : Indicates that the global table is configured for multi-Region eventual consistency.
- `STRONG` : Indicates that the global table is configured for multi-Region strong consistency (preview).

### Note

Multi-Region strong consistency (MRSC) is a new DynamoDB global tables capability currently available in preview mode. For more information, see [Global tables multi-Region strong consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PreviewFeatures.html#multi-region-strong-consistency-gt) .

If you donât specify this field, the global table consistency mode defaults to `EVENTUAL` .