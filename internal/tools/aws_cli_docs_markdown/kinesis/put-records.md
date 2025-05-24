# put-recordsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-records.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-records.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/index.html#cli-aws-kinesis) ]

# put-records

## Description

Writes multiple data records into a Kinesis data stream in a single call (also referred to as a `PutRecords` request). Use this operation to send data into the stream for data ingestion and processing.

### Note

When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

Each `PutRecords` request can support up to 500 records. Each record in the request can be as large as 1 MiB, up to a limit of 5 MiB for the entire request, including partition keys. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MiB per second.

You must specify the name of the stream that captures, stores, and transports the data; and an array of request `Records` , with each record in the array requiring a partition key and data blob. The record size limit applies to the total size of the partition key and data blob.

The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.

The partition key is used by Kinesis Data Streams as input to a hash function that maps the partition key and associated data to a specific shard. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream. For more information, see [Adding Data to a Stream](https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-add-data-to-stream) in the *Amazon Kinesis Data Streams Developer Guide* .

Each record in the `Records` array may include an optional parameter, `ExplicitHashKey` , which overrides the partition key to shard mapping. This parameter allows a data producer to determine explicitly the shard where the record is stored. For more information, see [Adding Multiple Records with PutRecords](https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-putrecords) in the *Amazon Kinesis Data Streams Developer Guide* .

The `PutRecords` response includes an array of response `Records` . Each record in the response array directly correlates with a record in the request array using natural ordering, from the top to the bottom of the request and response. The response `Records` array always includes the same number of records as the request array.

The response `Records` array includes both successfully and unsuccessfully processed records. Kinesis Data Streams attempts to process all records in each `PutRecords` request. A single record failure does not stop the processing of subsequent records. As a result, PutRecords doesnât guarantee the ordering of records. If you need to read records in the same order they are written to the stream, use  PutRecord instead of `PutRecords` , and write to the same shard.

A successfully processed record includes `ShardId` and `SequenceNumber` values. The `ShardId` parameter identifies the shard in the stream where the record is stored. The `SequenceNumber` parameter is an identifier assigned to the put record, unique to all records in the stream.

An unsuccessfully processed record includes `ErrorCode` and `ErrorMessage` values. `ErrorCode` reflects the type of error and can be one of the following values: `ProvisionedThroughputExceededException` or `InternalFailure` . `ErrorMessage` provides more detailed information about the `ProvisionedThroughputExceededException` exception including the account ID, stream name, and shard ID of the record that was throttled. For more information about partially successful responses, see [Adding Multiple Records with PutRecords](https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-add-data-to-stream.html#kinesis-using-sdk-java-putrecords) in the *Amazon Kinesis Data Streams Developer Guide* .

### Warning

After you write a record to a stream, you cannot modify that record or its order within the stream.

By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use  IncreaseStreamRetentionPeriod or  DecreaseStreamRetentionPeriod to modify this retention period.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/PutRecords)

## Synopsis

```
put-records
--records <value>
[--stream-name <value>]
[--stream-arn <value>]
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

`--records` (list)

The records associated with the request.

(structure)

Represents the output for `PutRecords` .

Data -> (blob)

The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MiB).

ExplicitHashKey -> (string)

The hash value used to determine explicitly the shard that the data record is assigned to by overriding the partition key hash.

PartitionKey -> (string)

Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.

Shorthand Syntax:

```
Data=blob,ExplicitHashKey=string,PartitionKey=string ...
```

JSON Syntax:

```
[
  {
    "Data": blob,
    "ExplicitHashKey": "string",
    "PartitionKey": "string"
  }
  ...
]
```

`--stream-name` (string)

The stream name associated with the request.

`--stream-arn` (string)

The ARN of the stream.

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

**To write multiple records into a data stream**

The following `put-records` example writes a data record using the specified partition key and another data record using a different partition key in a single call.

```
aws kinesis put-records \
    --stream-name samplestream \
    --records Data=blob1,PartitionKey=partitionkey1 Data=blob2,PartitionKey=partitionkey2
```

Output:

```
{
    "FailedRecordCount": 0,
    "Records": [
        {
            "SequenceNumber": "49600883331171471519674795588238531498465399900093808706",
            "ShardId": "shardId-000000000004"
        },
        {
            "SequenceNumber": "49600902273357540915989931256902715169698037101720764562",
            "ShardId": "shardId-000000000009"
        }
    ],
    "EncryptionType": "KMS"
}
```

For more information, see [Developing Producers Using the Amazon Kinesis Data Streams API with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-sdk.html) in the *Amazon Kinesis Data Streams Developer Guide*.

## Output

FailedRecordCount -> (integer)

The number of unsuccessfully processed records in a `PutRecords` request.

Records -> (list)

An array of successfully and unsuccessfully processed record results. A record that is successfully added to a stream includes `SequenceNumber` and `ShardId` in the result. A record that fails to be added to a stream includes `ErrorCode` and `ErrorMessage` in the result.

(structure)

Represents the result of an individual record from a `PutRecords` request. A record that is successfully added to a stream includes `SequenceNumber` and `ShardId` in the result. A record that fails to be added to the stream includes `ErrorCode` and `ErrorMessage` in the result.

SequenceNumber -> (string)

The sequence number for an individual record result.

ShardId -> (string)

The shard ID for an individual record result.

ErrorCode -> (string)

The error code for an individual record result. `ErrorCodes` can be either `ProvisionedThroughputExceededException` or `InternalFailure` .

ErrorMessage -> (string)

The error message for an individual record result. An `ErrorCode` value of `ProvisionedThroughputExceededException` has an error message that includes the account ID, stream name, and shard ID. An `ErrorCode` value of `InternalFailure` has the error message `"Internal Service Failure"` .

EncryptionType -> (string)

The encryption type used on the records. This parameter can be one of the following values:

- `NONE` : Do not encrypt the records.
- `KMS` : Use server-side encryption on the records using a customer-managed Amazon Web Services KMS key.