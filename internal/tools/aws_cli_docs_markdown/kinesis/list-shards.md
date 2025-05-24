# list-shardsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-shards.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-shards.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/index.html#cli-aws-kinesis) ]

# list-shards

## Description

Lists the shards in a stream and provides information about each shard. This operation has a limit of 1000 transactions per second per data stream.

### Note

When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

This action does not list expired shards. For information about expired shards, see [Data Routing, Data Persistence, and Shard State after a Reshard](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-after-resharding.html#kinesis-using-sdk-java-resharding-data-routing) .

### Warning

This API is a new operation that is used by the Amazon Kinesis Client Library (KCL). If you have a fine-grained IAM policy that only allows specific operations, you must update your policy to allow calls to this API. For more information, see [Controlling Access to Amazon Kinesis Data Streams Resources Using IAM](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/ListShards)

`list-shards` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Shards`

## Synopsis

```
list-shards
[--stream-name <value>]
[--exclusive-start-shard-id <value>]
[--stream-creation-timestamp <value>]
[--shard-filter <value>]
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

The name of the data stream whose shards you want to list.

You cannot specify this parameter if you specify the `NextToken` parameter.

`--exclusive-start-shard-id` (string)

Specify this parameter to indicate that you want to list the shards starting with the shard whose ID immediately follows `ExclusiveStartShardId` .

If you donât specify this parameter, the default behavior is for `ListShards` to list the shards starting with the first one in the stream.

You cannot specify this parameter if you specify `NextToken` .

`--stream-creation-timestamp` (timestamp)

Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the shards for.

You cannot specify this parameter if you specify the `NextToken` parameter.

`--shard-filter` (structure)

Enables you to filter out the response of the `ListShards` API. You can only specify one filter at a time.

If you use the `ShardFilter` parameter when invoking the ListShards API, the `Type` is the required property and must be specified. If you specify the `AT_TRIM_HORIZON` , `FROM_TRIM_HORIZON` , or `AT_LATEST` types, you do not need to specify either the `ShardId` or the `Timestamp` optional properties.

If you specify the `AFTER_SHARD_ID` type, you must also provide the value for the optional `ShardId` property. The `ShardId` property is identical in fuctionality to the `ExclusiveStartShardId` parameter of the `ListShards` API. When `ShardId` property is specified, the response includes the shards starting with the shard whose ID immediately follows the `ShardId` that you provided.

If you specify the `AT_TIMESTAMP` or `FROM_TIMESTAMP_ID` type, you must also provide the value for the optional `Timestamp` property. If you specify the AT_TIMESTAMP type, then all shards that were open at the provided timestamp are returned. If you specify the FROM_TIMESTAMP type, then all shards starting from the provided timestamp to TIP are returned.

Type -> (string)

The shard type specified in the `ShardFilter` parameter. This is a required property of the `ShardFilter` parameter.

You can specify the following valid values:

- `AFTER_SHARD_ID` - the response includes all the shards, starting with the shard whose ID immediately follows the `ShardId` that you provided.
- `AT_TRIM_HORIZON` - the response includes all the shards that were open at `TRIM_HORIZON` .
- `FROM_TRIM_HORIZON` - (default), the response includes all the shards within the retention period of the data stream (trim to tip).
- `AT_LATEST` - the response includes only the currently open shards of the data stream.
- `AT_TIMESTAMP` - the response includes all shards whose start timestamp is less than or equal to the given timestamp and end timestamp is greater than or equal to the given timestamp or still open.
- `FROM_TIMESTAMP` - the response incldues all closed shards whose end timestamp is greater than or equal to the given timestamp and also all open shards. Corrected to `TRIM_HORIZON` of the data stream if `FROM_TIMESTAMP` is less than the `TRIM_HORIZON` value.

ShardId -> (string)

The exclusive start `shardID` speified in the `ShardFilter` parameter. This property can only be used if the `AFTER_SHARD_ID` shard type is specified.

Timestamp -> (timestamp)

The timestamps specified in the `ShardFilter` parameter. A timestamp is a Unix epoch date with precision in milliseconds. For example, 2016-04-04T19:58:46.480-00:00 or 1459799926.480. This property can only be used if `FROM_TIMESTAMP` or `AT_TIMESTAMP` shard types are specified.

Shorthand Syntax:

```
Type=string,ShardId=string,Timestamp=timestamp
```

JSON Syntax:

```
{
  "Type": "AFTER_SHARD_ID"|"AT_TRIM_HORIZON"|"FROM_TRIM_HORIZON"|"AT_LATEST"|"AT_TIMESTAMP"|"FROM_TIMESTAMP",
  "ShardId": "string",
  "Timestamp": timestamp
}
```

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

**To list shards in a data stream**

The following `list-shards` example lists all shards in the specified stream starting with the shard whose ID immediately follows the specified `exclusive-start-shard-id` of `shardId-000000000000`.

```
aws kinesis list-shards \
    --stream-name samplestream \
    --exclusive-start-shard-id shardId-000000000000
```

Output:

```
{
    "Shards": [
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
    ]
}
```

For more information, see [Listing Shards](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-list-shards.html) in the *Amazon Kinesis Data Streams Developer Guide*.

## Output

Shards -> (list)

An array of JSON objects. Each object represents one shard and specifies the IDs of the shard, the shardâs parent, and the shard thatâs adjacent to the shardâs parent. Each object also contains the starting and ending hash keys and the starting and ending sequence numbers for the shard.

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

NextToken -> (string)

When the number of shards in the data stream is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of shards in the data stream, the response includes a pagination token named `NextToken` . You can specify this `NextToken` value in a subsequent call to `ListShards` to list the next set of shards. For more information about the use of this pagination token when calling the `ListShards` operation, see  ListShardsInput$NextToken .

### Warning

Tokens expire after 300 seconds. When you obtain a value for `NextToken` in the response to a call to `ListShards` , you have 300 seconds to use that value. If you specify an expired token in a call to `ListShards` , you get `ExpiredNextTokenException` .