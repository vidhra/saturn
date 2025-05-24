# import-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/import-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/import-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# import-table

## Description

Imports table data from an S3 bucket.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/ImportTable)

## Synopsis

```
import-table
[--client-token <value>]
--s3-bucket-source <value>
--input-format <value>
[--input-format-options <value>]
[--input-compression-type <value>]
--table-creation-parameters <value>
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

`--client-token` (string)

Providing a `ClientToken` makes the call to `ImportTableInput` idempotent, meaning that multiple identical calls have the same effect as one single call.

A client token is valid for 8 hours after the first request that uses it is completed. After 8 hours, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 8 hours, or the result might not be idempotent.

If you submit a request with the same client token but a change in other parameters within the 8-hour idempotency window, DynamoDB returns an `IdempotentParameterMismatch` exception.

`--s3-bucket-source` (structure)

The S3 bucket that provides the source for the import.

S3BucketOwner -> (string)

The account number of the S3 bucket that is being imported from. If the bucket is owned by the requester this is optional.

S3Bucket -> (string)

The S3 bucket that is being imported from.

S3KeyPrefix -> (string)

The key prefix shared by all S3 Objects that are being imported.

Shorthand Syntax:

```
S3BucketOwner=string,S3Bucket=string,S3KeyPrefix=string
```

JSON Syntax:

```
{
  "S3BucketOwner": "string",
  "S3Bucket": "string",
  "S3KeyPrefix": "string"
}
```

`--input-format` (string)

The format of the source data. Valid values for `ImportFormat` are `CSV` , `DYNAMODB_JSON` or `ION` .

Possible values:

- `DYNAMODB_JSON`
- `ION`
- `CSV`

`--input-format-options` (structure)

Additional properties that specify how the input is formatted,

Csv -> (structure)

The options for imported source files in CSV format. The values are Delimiter and HeaderList.

Delimiter -> (string)

The delimiter used for separating items in the CSV file being imported.

HeaderList -> (list)

List of the headers used to specify a common header for all source CSV files being imported. If this field is specified then the first line of each CSV file is treated as data instead of the header. If this field is not specified the the first line of each CSV file is treated as the header.

(string)

Shorthand Syntax:

```
Csv={Delimiter=string,HeaderList=[string,string]}
```

JSON Syntax:

```
{
  "Csv": {
    "Delimiter": "string",
    "HeaderList": ["string", ...]
  }
}
```

`--input-compression-type` (string)

Type of compression to be used on the input coming from the imported table.

Possible values:

- `GZIP`
- `ZSTD`
- `NONE`

`--table-creation-parameters` (structure)

Parameters for the table to import the data into.

TableName -> (string)

The name of the table created as part of the import operation.

AttributeDefinitions -> (list)

The attributes of the table created as part of the import operation.

(structure)

Represents an attribute for describing the schema for the table and indexes.

AttributeName -> (string)

A name for the attribute.

AttributeType -> (string)

The data type for the attribute, where:

- `S` - the attribute is of type String
- `N` - the attribute is of type Number
- `B` - the attribute is of type Binary

KeySchema -> (list)

The primary key and option sort key of the table created as part of the import operation.

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

BillingMode -> (string)

The billing mode for provisioning the table created as part of the import operation.

ProvisionedThroughput -> (structure)

Represents the provisioned throughput settings for the specified global secondary index. You must use `ProvisionedThroughput` or `OnDemandThroughput` based on your tableâs capacity mode.

For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide* .

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

SSESpecification -> (structure)

Represents the settings used to enable server-side encryption.

Enabled -> (boolean)

Indicates whether server-side encryption is done using an Amazon Web Services managed key or an Amazon Web Services owned key. If enabled (true), server-side encryption type is set to `KMS` and an Amazon Web Services managed key is used (KMS charges apply). If disabled (false) or not specified, server-side encryption is set to Amazon Web Services owned key.

SSEType -> (string)

Server-side encryption type. The only supported value is:

- `KMS` - Server-side encryption that uses Key Management Service. The key is stored in your account and is managed by KMS (KMS charges apply).

KMSMasterKeyId -> (string)

The KMS key that should be used for the KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB key `alias/aws/dynamodb` .

GlobalSecondaryIndexes -> (list)

The Global Secondary Indexes (GSI) of the table to be created as part of the import operation.

(structure)

Represents the properties of a global secondary index.

IndexName -> (string)

The name of the global secondary index. The name must be unique among all other indexes on this table.

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

Represents the provisioned throughput settings for the specified global secondary index. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your tableâs capacity mode.

For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide* .

ReadCapacityUnits -> (long)

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide* .

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.

WriteCapacityUnits -> (long)

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide* .

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.

OnDemandThroughput -> (structure)

The maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify `MaxReadRequestUnits` , `MaxWriteRequestUnits` , or both. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your tableâs capacity mode.

MaxReadRequestUnits -> (long)

Maximum number of read request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxReadRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxReadRequestUnits` to -1.

MaxWriteRequestUnits -> (long)

Maximum number of write request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxWriteRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxWriteRequestUnits` to -1.

WarmThroughput -> (structure)

Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index. If you use this parameter, you must specify `ReadUnitsPerSecond` , `WriteUnitsPerSecond` , or both.

ReadUnitsPerSecond -> (long)

Represents the number of read operations your base table can instantaneously support.

WriteUnitsPerSecond -> (long)

Represents the number of write operations your base table can instantaneously support.

JSON Syntax:

```
{
  "TableName": "string",
  "AttributeDefinitions": [
    {
      "AttributeName": "string",
      "AttributeType": "S"|"N"|"B"
    }
    ...
  ],
  "KeySchema": [
    {
      "AttributeName": "string",
      "KeyType": "HASH"|"RANGE"
    }
    ...
  ],
  "BillingMode": "PROVISIONED"|"PAY_PER_REQUEST",
  "ProvisionedThroughput": {
    "ReadCapacityUnits": long,
    "WriteCapacityUnits": long
  },
  "OnDemandThroughput": {
    "MaxReadRequestUnits": long,
    "MaxWriteRequestUnits": long
  },
  "SSESpecification": {
    "Enabled": true|false,
    "SSEType": "AES256"|"KMS",
    "KMSMasterKeyId": "string"
  },
  "GlobalSecondaryIndexes": [
    {
      "IndexName": "string",
      "KeySchema": [
        {
          "AttributeName": "string",
          "KeyType": "HASH"|"RANGE"
        }
        ...
      ],
      "Projection": {
        "ProjectionType": "ALL"|"KEYS_ONLY"|"INCLUDE",
        "NonKeyAttributes": ["string", ...]
      },
      "ProvisionedThroughput": {
        "ReadCapacityUnits": long,
        "WriteCapacityUnits": long
      },
      "OnDemandThroughput": {
        "MaxReadRequestUnits": long,
        "MaxWriteRequestUnits": long
      },
      "WarmThroughput": {
        "ReadUnitsPerSecond": long,
        "WriteUnitsPerSecond": long
      }
    }
    ...
  ]
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

ImportTableDescription -> (structure)

Represents the properties of the table created for the import, and parameters of the import. The import parameters include import status, how many items were processed, and how many errors were encountered.

ImportArn -> (string)

The Amazon Resource Number (ARN) corresponding to the import request.

ImportStatus -> (string)

The status of the import.

TableArn -> (string)

The Amazon Resource Number (ARN) of the table being imported into.

TableId -> (string)

The table id corresponding to the table created by import table process.

ClientToken -> (string)

The client token that was provided for the import task. Reusing the client token on retry makes a call to `ImportTable` idempotent.

S3BucketSource -> (structure)

Values for the S3 bucket the source file is imported from. Includes bucket name (required), key prefix (optional) and bucket account owner ID (optional).

S3BucketOwner -> (string)

The account number of the S3 bucket that is being imported from. If the bucket is owned by the requester this is optional.

S3Bucket -> (string)

The S3 bucket that is being imported from.

S3KeyPrefix -> (string)

The key prefix shared by all S3 Objects that are being imported.

ErrorCount -> (long)

The number of errors occurred on importing the source file into the target table.

CloudWatchLogGroupArn -> (string)

The Amazon Resource Number (ARN) of the Cloudwatch Log Group associated with the target table.

InputFormat -> (string)

The format of the source data going into the target table.

InputFormatOptions -> (structure)

The format options for the data that was imported into the target table. There is one value, CsvOption.

Csv -> (structure)

The options for imported source files in CSV format. The values are Delimiter and HeaderList.

Delimiter -> (string)

The delimiter used for separating items in the CSV file being imported.

HeaderList -> (list)

List of the headers used to specify a common header for all source CSV files being imported. If this field is specified then the first line of each CSV file is treated as data instead of the header. If this field is not specified the the first line of each CSV file is treated as the header.

(string)

InputCompressionType -> (string)

The compression options for the data that has been imported into the target table. The values are NONE, GZIP, or ZSTD.

TableCreationParameters -> (structure)

The parameters for the new table that is being imported into.

TableName -> (string)

The name of the table created as part of the import operation.

AttributeDefinitions -> (list)

The attributes of the table created as part of the import operation.

(structure)

Represents an attribute for describing the schema for the table and indexes.

AttributeName -> (string)

A name for the attribute.

AttributeType -> (string)

The data type for the attribute, where:

- `S` - the attribute is of type String
- `N` - the attribute is of type Number
- `B` - the attribute is of type Binary

KeySchema -> (list)

The primary key and option sort key of the table created as part of the import operation.

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

BillingMode -> (string)

The billing mode for provisioning the table created as part of the import operation.

ProvisionedThroughput -> (structure)

Represents the provisioned throughput settings for the specified global secondary index. You must use `ProvisionedThroughput` or `OnDemandThroughput` based on your tableâs capacity mode.

For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide* .

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

SSESpecification -> (structure)

Represents the settings used to enable server-side encryption.

Enabled -> (boolean)

Indicates whether server-side encryption is done using an Amazon Web Services managed key or an Amazon Web Services owned key. If enabled (true), server-side encryption type is set to `KMS` and an Amazon Web Services managed key is used (KMS charges apply). If disabled (false) or not specified, server-side encryption is set to Amazon Web Services owned key.

SSEType -> (string)

Server-side encryption type. The only supported value is:

- `KMS` - Server-side encryption that uses Key Management Service. The key is stored in your account and is managed by KMS (KMS charges apply).

KMSMasterKeyId -> (string)

The KMS key that should be used for the KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB key `alias/aws/dynamodb` .

GlobalSecondaryIndexes -> (list)

The Global Secondary Indexes (GSI) of the table to be created as part of the import operation.

(structure)

Represents the properties of a global secondary index.

IndexName -> (string)

The name of the global secondary index. The name must be unique among all other indexes on this table.

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

Represents the provisioned throughput settings for the specified global secondary index. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your tableâs capacity mode.

For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide* .

ReadCapacityUnits -> (long)

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide* .

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.

WriteCapacityUnits -> (long)

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html) in the *Amazon DynamoDB Developer Guide* .

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0.

OnDemandThroughput -> (structure)

The maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify `MaxReadRequestUnits` , `MaxWriteRequestUnits` , or both. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your tableâs capacity mode.

MaxReadRequestUnits -> (long)

Maximum number of read request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxReadRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxReadRequestUnits` to -1.

MaxWriteRequestUnits -> (long)

Maximum number of write request units for the specified table.

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxWriteRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxWriteRequestUnits` to -1.

WarmThroughput -> (structure)

Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index. If you use this parameter, you must specify `ReadUnitsPerSecond` , `WriteUnitsPerSecond` , or both.

ReadUnitsPerSecond -> (long)

Represents the number of read operations your base table can instantaneously support.

WriteUnitsPerSecond -> (long)

Represents the number of write operations your base table can instantaneously support.

StartTime -> (timestamp)

The time when this import task started.

EndTime -> (timestamp)

The time at which the creation of the table associated with this import task completed.

ProcessedSizeBytes -> (long)

The total size of data processed from the source file, in Bytes.

ProcessedItemCount -> (long)

The total number of items processed from the source file.

ImportedItemCount -> (long)

The number of items successfully imported into the new table.

FailureCode -> (string)

The error code corresponding to the failure that the import job ran into during execution.

FailureMessage -> (string)

The error message corresponding to the failure that the import job ran into during execution.