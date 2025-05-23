# get-recordsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-records.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-records.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/index.html#cli-aws-kinesis) ]

# get-records

## Description

Gets data records from a Kinesis data streamâs shard.

### Note

When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

Specify a shard iterator using the `ShardIterator` parameter. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. If there are no records available in the portion of the shard that the iterator points to,  GetRecords returns an empty list. It might take multiple calls to get to a portion of the shard that contains records.

You can scale by provisioning multiple shards per stream while considering service limits (for more information, see [Amazon Kinesis Data Streams Limits](https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide* ). Your application should have one thread per shard, each reading continuously from its stream. To read from a stream continually, call  GetRecords in a loop. Use  GetShardIterator to get the shard iterator to specify in the first  GetRecords call.  GetRecords returns a new shard iterator in `NextShardIterator` . Specify the shard iterator returned in `NextShardIterator` in subsequent calls to  GetRecords . If the shard has been closed, the shard iterator canât return more data and  GetRecords returns `null` in `NextShardIterator` . You can terminate the loop when the shard is closed, or when the shard iterator reaches the record with the sequence number or other attribute that marks it as the last record to process.

Each data record can be up to 1 MiB in size, and each shard can read up to 2 MiB per second. You can ensure that your calls donât exceed the maximum supported size or throughput by using the `Limit` parameter to specify the maximum number of records that  GetRecords can return. Consider your average record size when determining this limit. The maximum number of records that can be returned per call is 10,000.

The size of the data returned by  GetRecords varies depending on the utilization of the shard. It is recommended that consumer applications retrieve records via the `GetRecords` command using the 5 TPS limit to remain caught up. Retrieving records less frequently can lead to consumer applications falling behind. The maximum size of data that  GetRecords can return is 10 MiB. If a call returns this amount of data, subsequent calls made within the next 5 seconds throw `ProvisionedThroughputExceededException` . If there is insufficient provisioned throughput on the stream, subsequent calls made within the next 1 second throw `ProvisionedThroughputExceededException` .  GetRecords doesnât return any data when it throws an exception. For this reason, we recommend that you wait 1 second between calls to  GetRecords . However, itâs possible that the application will get exceptions for longer than 1 second.

To detect whether the application is falling behind in processing, you can use the `MillisBehindLatest` response attribute. You can also monitor the stream using CloudWatch metrics and other mechanisms (see [Monitoring](https://docs.aws.amazon.com/kinesis/latest/dev/monitoring.html) in the *Amazon Kinesis Data Streams Developer Guide* ).

Each Amazon Kinesis record includes a value, `ApproximateArrivalTimestamp` , that is set when a stream successfully receives and stores a record. This is commonly referred to as a server-side time stamp, whereas a client-side time stamp is set when a data producer creates or sends the record to a stream (a data producer is any data source putting data records into a stream, for example with  PutRecords ). The time stamp has millisecond precision. There are no guarantees about the time stamp accuracy, or that the time stamp is always increasing. For example, records in a shard or across a stream might have time stamps that are out of order.

This operation has a limit of five transactions per second per shard.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/GetRecords)

## Synopsis

```
get-records
--shard-iterator <value>
[--limit <value>]
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

`--shard-iterator` (string)

The position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.

`--limit` (integer)

The maximum number of records to return. Specify a value of up to 10,000. If you specify a value that is greater than 10,000,  GetRecords throws `InvalidArgumentException` . The default value is 10,000.

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

**To obtain records from a shard**

The following `get-records` example gets data records from a Kinesis data streamâs shard using the specified shard iterator.

```
aws kinesis get-records \
    --shard-iterator AAAAAAAAAAF7/0mWD7IuHj1yGv/TKuNgx2ukD5xipCY4cy4gU96orWwZwcSXh3K9tAmGYeOZyLZrvzzeOFVf9iN99hUPw/w/b0YWYeehfNvnf1DYt5XpDJghLKr3DzgznkTmMymDP3R+3wRKeuEw6/kdxY2yKJH0veaiekaVc4N2VwK/GvaGP2Hh9Fg7N++q0Adg6fIDQPt4p8RpavDbk+A4sL9SWGE1
```

Output:

```
{
    "Records": [],
    "MillisBehindLatest": 80742000
}
```

For more information, see [Developing Consumers Using the Kinesis Data Streams API with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-consumers-with-sdk.html) in the *Amazon Kinesis Data Streams Developer Guide*.

## Output

Records -> (list)

The data records retrieved from the shard.

(structure)

The unit of data of the Kinesis data stream, which is composed of a sequence number, a partition key, and a data blob.

SequenceNumber -> (string)

The unique identifier of the record within its shard.

ApproximateArrivalTimestamp -> (timestamp)

The approximate time that the record was inserted into the stream.

Data -> (blob)

The data blob. The data in the blob is both opaque and immutable to Kinesis Data Streams, which does not inspect, interpret, or change the data in the blob in any way. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MiB).

PartitionKey -> (string)

Identifies which shard in the stream the data record is assigned to.

EncryptionType -> (string)

The encryption type used on the record. This parameter can be one of the following values:

- `NONE` : Do not encrypt the records in the stream.
- `KMS` : Use server-side encryption on the records in the stream using a customer-managed Amazon Web Services KMS key.

NextShardIterator -> (string)

The next position in the shard from which to start sequentially reading data records. If set to `null` , the shard has been closed and the requested iterator does not return any more data.

MillisBehindLatest -> (long)

The number of milliseconds the  GetRecords response is from the tip of the stream, indicating how far behind current time the consumer is. A value of zero indicates that record processing is caught up, and there are no new records to process at this moment.

ChildShards -> (list)

The list of the current shardâs child shards, returned in the `GetRecords` APIâs response only when the end of the current shard is reached.

(structure)

Output parameter of the GetRecords API. The existing child shard of the current shard.

ShardId -> (string)

The shard ID of the existing child shard of the current shard.

ParentShards -> (list)

The current shard that is the parent of the existing child shard.

(string)

HashKeyRange -> (structure)

The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.

StartingHashKey -> (string)

The starting hash key of the hash key range.

EndingHashKey -> (string)

The ending hash key of the hash key range.