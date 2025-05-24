# describe-journal-kinesis-streamÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/describe-journal-kinesis-stream.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/describe-journal-kinesis-stream.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qldb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/index.html#cli-aws-qldb) ]

# describe-journal-kinesis-stream

## Description

Returns detailed information about a given Amazon QLDB journal stream. The output includes the Amazon Resource Name (ARN), stream name, current status, creation time, and the parameters of the original stream creation request.

This action does not return any expired journal streams. For more information, see [Expiration for terminal streams](https://docs.aws.amazon.com/qldb/latest/developerguide/streams.create.html#streams.create.states.expiration) in the *Amazon QLDB Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/DescribeJournalKinesisStream)

## Synopsis

```
describe-journal-kinesis-stream
--ledger-name <value>
--stream-id <value>
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

`--ledger-name` (string)

The name of the ledger.

`--stream-id` (string)

The UUID (represented in Base62-encoded text) of the QLDB journal stream to describe.

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

**To describe a journal stream**

The following `describe-journal-kinesis-stream` example displays the details for the specified journal stream from a ledger.

```
aws qldb describe-journal-kinesis-stream \
    --ledger-name myExampleLedger \
    --stream-id 7ISCkqwe4y25YyHLzYUFAf
```

Output:

```
{
    "Stream": {
        "LedgerName": "myExampleLedger",
        "CreationTime": 1591221984.677,
        "InclusiveStartTime": 1590710400.0,
        "ExclusiveEndTime": 1590796799.0,
        "RoleArn": "arn:aws:iam::123456789012:role/my-kinesis-stream-role",
        "StreamId": "7ISCkqwe4y25YyHLzYUFAf",
        "Arn": "arn:aws:qldb:us-east-1:123456789012:stream/myExampleLedger/7ISCkqwe4y25YyHLzYUFAf",
        "Status": "ACTIVE",
        "KinesisConfiguration": {
            "StreamArn": "arn:aws:kinesis:us-east-1:123456789012:stream/stream-for-qldb",
            "AggregationEnabled": true
        },
        "StreamName": "myExampleLedger-stream"
    }
}
```

For more information, see [Streaming journal data from Amazon QLDB](https://docs.aws.amazon.com/qldb/latest/developerguide/streams.html) in the *Amazon QLDB Developer Guide*.

## Output

Stream -> (structure)

Information about the QLDB journal stream returned by a `DescribeJournalS3Export` request.

LedgerName -> (string)

The name of the ledger.

CreationTime -> (timestamp)

The date and time, in epoch time format, when the QLDB journal stream was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

InclusiveStartTime -> (timestamp)

The inclusive start date and time from which to start streaming journal data.

ExclusiveEndTime -> (timestamp)

The exclusive date and time that specifies when the stream ends. If this parameter is undefined, the stream runs indefinitely until you cancel it.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource.

StreamId -> (string)

The UUID (represented in Base62-encoded text) of the QLDB journal stream.

Arn -> (string)

The Amazon Resource Name (ARN) of the QLDB journal stream.

Status -> (string)

The current state of the QLDB journal stream.

KinesisConfiguration -> (structure)

The configuration settings of the Amazon Kinesis Data Streams destination for a QLDB journal stream.

StreamArn -> (string)

The Amazon Resource Name (ARN) of the Kinesis Data Streams resource.

AggregationEnabled -> (boolean)

Enables QLDB to publish multiple data records in a single Kinesis Data Streams record, increasing the number of records sent per API call.

Default: `True`

### Warning

Record aggregation has important implications for processing records and requires de-aggregation in your stream consumer. To learn more, see [KPL Key Concepts](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-concepts.html) and [Consumer De-aggregation](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-consumer-deaggregation.html) in the *Amazon Kinesis Data Streams Developer Guide* .

ErrorCause -> (string)

The error message that describes the reason that a stream has a status of `IMPAIRED` or `FAILED` . This is not applicable to streams that have other status values.

StreamName -> (string)

The user-defined name of the QLDB journal stream.