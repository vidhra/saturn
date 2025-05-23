# get-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/get-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/get-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [keyspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/index.html#cli-aws-keyspaces) ]

# get-table

## Description

Returns information about the table, including the tableâs name and current status, the keyspace name, configuration settings, and metadata.

To read table metadata using `GetTable` , the IAM principal needs `Select` action permissions for the table and the system keyspace.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/keyspaces-2022-02-10/GetTable)

## Synopsis

```
get-table
--keyspace-name <value>
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

`--keyspace-name` (string)

The name of the keyspace that the table is stored in.

`--table-name` (string)

The name of the table.

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

keyspaceName -> (string)

The name of the keyspace that the specified table is stored in.

tableName -> (string)

The name of the specified table.

resourceArn -> (string)

The Amazon Resource Name (ARN) of the specified table.

creationTimestamp -> (timestamp)

The creation timestamp of the specified table.

status -> (string)

The current status of the specified table.

schemaDefinition -> (structure)

The schema definition of the specified table.

allColumns -> (list)

The regular columns of the table.

(structure)

The names and data types of regular columns.

name -> (string)

The name of the column.

type -> (string)

The data type of the column. For a list of available data types, see [Data types](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types) in the *Amazon Keyspaces Developer Guide* .

partitionKeys -> (list)

The columns that are part of the partition key of the table .

(structure)

The partition key portion of the primary key is required and determines how Amazon Keyspaces stores the data. The partition key can be a single column, or it can be a compound value composed of two or more columns.

name -> (string)

The name(s) of the partition key column(s).

clusteringKeys -> (list)

The columns that are part of the clustering key of the table.

(structure)

The optional clustering column portion of your primary key determines how the data is clustered and sorted within each partition.

name -> (string)

The name(s) of the clustering column(s).

orderBy -> (string)

Sets the ascendant (`ASC` ) or descendant (`DESC` ) order modifier.

staticColumns -> (list)

The columns that have been defined as `STATIC` . Static columns store values that are shared by all rows in the same partition.

(structure)

The static columns of the table. Static columns store values that are shared by all rows in the same partition.

name -> (string)

The name of the static column.

capacitySpecification -> (structure)

The read/write throughput capacity mode for a table. The options are:

- `throughputMode:PAY_PER_REQUEST`
- `throughputMode:PROVISIONED`

throughputMode -> (string)

The read/write throughput capacity mode for a table. The options are:

- `throughputMode:PAY_PER_REQUEST` and
- `throughputMode:PROVISIONED` - Provisioned capacity mode requires `readCapacityUnits` and `writeCapacityUnits` as input.

The default is `throughput_mode:PAY_PER_REQUEST` .

For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide* .

readCapacityUnits -> (long)

The throughput capacity specified for `read` operations defined in `read capacity units` `(RCUs)` .

writeCapacityUnits -> (long)

The throughput capacity specified for `write` operations defined in `write capacity units` `(WCUs)` .

lastUpdateToPayPerRequestTimestamp -> (timestamp)

The timestamp of the last operation that changed the provisioned throughput capacity of a table.

encryptionSpecification -> (structure)

The encryption settings of the specified table.

type -> (string)

The encryption option specified for the table. You can choose one of the following KMS keys (KMS keys):

- `type:AWS_OWNED_KMS_KEY` - This key is owned by Amazon Keyspaces.
- `type:CUSTOMER_MANAGED_KMS_KEY` - This key is stored in your account and is created, owned, and managed by you. This option requires the `kms_key_identifier` of the KMS key in Amazon Resource Name (ARN) format as input.

The default is `type:AWS_OWNED_KMS_KEY` .

For more information, see [Encryption at rest](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the *Amazon Keyspaces Developer Guide* .

kmsKeyIdentifier -> (string)

The Amazon Resource Name (ARN) of the customer managed KMS key, for example `kms_key_identifier:ARN` .

pointInTimeRecovery -> (structure)

The point-in-time recovery status of the specified table.

status -> (string)

Shows if point-in-time recovery is enabled or disabled for the specified table.

earliestRestorableTimestamp -> (timestamp)

Specifies the earliest possible restore point of the table in ISO 8601 format.

ttl -> (structure)

The custom Time to Live settings of the specified table.

status -> (string)

Shows how to enable custom Time to Live (TTL) settings for the specified table.

defaultTimeToLive -> (integer)

The default Time to Live settings in seconds of the specified table.

comment -> (structure)

The the description of the specified table.

message -> (string)

An optional description of the table.

clientSideTimestamps -> (structure)

The client-side timestamps setting of the table.

status -> (string)

Shows how to enable client-side timestamps settings for the specified table.

replicaSpecifications -> (list)

Returns the Amazon Web Services Region specific settings of all Regions a multi-Region table is replicated in.

(structure)

The Region-specific settings of a multi-Region table in the specified Amazon Web Services Region.

If the multi-Region table is using provisioned capacity and has optional auto scaling policies configured, note that the Region specific summary returns both read and write capacity settings. But only Region specific read capacity settings can be configured for a multi-Region table. In a multi-Region table, your write capacity units will be synced across all Amazon Web Services Regions to ensure that there is enough capacity to replicate write events across Regions.

region -> (string)

The Amazon Web Services Region.

status -> (string)

The status of the multi-Region table in the specified Amazon Web Services Region.

capacitySpecification -> (structure)

The read/write throughput capacity mode for a table. The options are:

- `throughputMode:PAY_PER_REQUEST` and
- `throughputMode:PROVISIONED` .

For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide* .

throughputMode -> (string)

The read/write throughput capacity mode for a table. The options are:

- `throughputMode:PAY_PER_REQUEST` and
- `throughputMode:PROVISIONED` - Provisioned capacity mode requires `readCapacityUnits` and `writeCapacityUnits` as input.

The default is `throughput_mode:PAY_PER_REQUEST` .

For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide* .

readCapacityUnits -> (long)

The throughput capacity specified for `read` operations defined in `read capacity units` `(RCUs)` .

writeCapacityUnits -> (long)

The throughput capacity specified for `write` operations defined in `write capacity units` `(WCUs)` .

lastUpdateToPayPerRequestTimestamp -> (timestamp)

The timestamp of the last operation that changed the provisioned throughput capacity of a table.