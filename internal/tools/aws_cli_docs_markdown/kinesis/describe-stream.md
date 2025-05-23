# describe-streamÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/index.html#cli-aws-kinesis) ]

# describe-stream

## Description

Describes the specified Kinesis data stream.

### Note

This API has been revised. Itâs highly recommended that you use the  DescribeStreamSummary API to get a summarized description of the specified Kinesis data stream and the  ListShards API to list the shards in a specified data stream and obtain information about each shard.

### Note

When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

The information returned includes the stream name, Amazon Resource Name (ARN), creation time, enhanced metric configuration, and shard map. The shard map is an array of shard objects. For each shard object, there is the hash key and sequence number ranges that the shard spans, and the IDs of any earlier shards that played in a role in creating the shard. Every record ingested in the stream is identified by a sequence number, which is assigned when the record is put into the stream.

You can limit the number of shards returned by each call. For more information, see [Retrieving Shards from a Stream](https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-retrieve-shards.html) in the *Amazon Kinesis Data Streams Developer Guide* .

There are no guarantees about the chronological order shards returned. To process shards in chronological order, use the ID of the parent shard to track the lineage to the oldest shard.

This operation has a limit of 10 transactions per second per account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeStream)

`describe-stream` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `StreamDescription.Shards`

## Synopsis

```
describe-stream
[--stream-name <value>]
[--stream-arn <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--stream-name` (string)

The name of the stream to describe.

`--stream-arn` (string)

The ARN of the stream.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To describe a data stream**

The following `describe-stream` example returns the details of the specified data stream.

```
aws kinesis describe-stream \
    --stream-name samplestream
```

Output:

```
{
    "StreamDescription": {
        "Shards": [
            {
                "ShardId": "shardId-000000000000",
                "HashKeyRange": {
                    "StartingHashKey": "0",
                    "EndingHashKey": "113427455640312821154458202477256070484"
                },
                "SequenceNumberRange": {
                    "StartingSequenceNumber": "49600871682957036442365024926191073437251060580128653314"
                }
            },
            {
                "ShardId": "shardId-000000000001",
                "HashKeyRange": {
                    "StartingHashKey": "113427455640312821154458202477256070485",
                    "EndingHashKey": "226854911280625642308916404954512140969"
                },
                "SequenceNumberRange": {
                    "StartingSequenceNumber": "49600871682979337187563555549332609155523708941634633746"
                }
            },
            {
                "ShardId": "shardId-000000000002",
                "HashKeyRange": {
                    "StartingHashKey": "226854911280625642308916404954512140970",
                    "EndingHashKey": "340282366920938463463374607431768211455"
                },
                "SequenceNumberRange": {
                    "StartingSequenceNumber": "49600871683001637932762086172474144873796357303140614178"
                }
            }
        ],
        "StreamARN": "arn:aws:kinesis:us-west-2:123456789012:stream/samplestream",
        "StreamName": "samplestream",
        "StreamStatus": "ACTIVE",
        "RetentionPeriodHours": 24,
        "EnhancedMonitoring": [
            {
                "ShardLevelMetrics": []
            }
        ],
        "EncryptionType": "NONE",
        "KeyId": null,
        "StreamCreationTimestamp": 1572297168.0
    }
}
```

For more information, see [Creating and Managing Streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html) in the *Amazon Kinesis Data Streams Developer Guide*.

## Output

StreamDescription -> (structure)

The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard objects that comprise the stream, and whether there are more shards available.

StreamName -> (string)

The name of the stream being described.

StreamARN -> (string)

The Amazon Resource Name (ARN) for the stream being described.

StreamStatus -> (string)

The current status of the stream being described. The stream status is one of the following states:

- `CREATING` - The stream is being created. Kinesis Data Streams immediately returns and sets `StreamStatus` to `CREATING` .
- `DELETING` - The stream is being deleted. The specified stream is in the `DELETING` state until Kinesis Data Streams completes the deletion.
- `ACTIVE` - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an `ACTIVE` stream.
- `UPDATING` - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the `UPDATING` state.

StreamModeDetails -> (structure)

Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an **on-demand** capacity mode and a **provisioned** capacity mode for your data streams.

StreamMode -> (string)

Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an **on-demand** capacity mode and a **provisioned** capacity mode for your data streams.

Shards -> (list)

The shards that comprise the stream.

(structure)

A uniquely identified group of data records in a Kinesis data stream.

ShardId -> (string)

The unique identifier of the shard within the stream.

ParentShardId -> (string)

The shard ID of the shardâs parent.

AdjacentParentShardId -> (string)

The shard ID of the shard adjacent to the shardâs parent.

HashKeyRange -> (structure)

The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.

StartingHashKey -> (string)

The starting hash key of the hash key range.

EndingHashKey -> (string)

The ending hash key of the hash key range.

SequenceNumberRange -> (structure)

The range of possible sequence numbers for the shard.

StartingSequenceNumber -> (string)

The starting sequence number for the range.

EndingSequenceNumber -> (string)

The ending sequence number for the range. Shards that are in the OPEN state have an ending sequence number of `null` .

HasMoreShards -> (boolean)

If set to `true` , more shards in the stream are available to describe.

RetentionPeriodHours -> (integer)

The current retention period, in hours. Minimum value of 24. Maximum value of 168.

StreamCreationTimestamp -> (timestamp)

The approximate time that the stream was created.

EnhancedMonitoring -> (list)

Represents the current enhanced monitoring settings of the stream.

(structure)

Represents enhanced metrics types.

ShardLevelMetrics -> (list)

List of shard-level metrics.

The following are the valid shard-level metrics. The value â`ALL` â enhances every metric.

- `IncomingBytes`
- `IncomingRecords`
- `OutgoingBytes`
- `OutgoingRecords`
- `WriteProvisionedThroughputExceeded`
- `ReadProvisionedThroughputExceeded`
- `IteratorAgeMilliseconds`
- `ALL`

For more information, see [Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch](https://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html) in the *Amazon Kinesis Data Streams Developer Guide* .

(string)

EncryptionType -> (string)

The server-side encryption type used on the stream. This parameter can be one of the following values:

- `NONE` : Do not encrypt the records in the stream.
- `KMS` : Use server-side encryption on the records in the stream using a customer-managed Amazon Web Services KMS key.

KeyId -> (string)

The GUID for the customer-managed Amazon Web Services KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by âalias/â.You can also use a master key owned by Kinesis Data Streams by specifying the alias `aws/kinesis` .

- Key ARN example: `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
- Alias ARN example: `arn:aws:kms:us-east-1:123456789012:alias/MyAliasName`
- Globally unique key ID example: `12345678-1234-1234-1234-123456789012`
- Alias name example: `alias/MyAliasName`
- Master key owned by Kinesis Data Streams: `alias/aws/kinesis`