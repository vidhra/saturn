# stream-journal-to-kinesisÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/stream-journal-to-kinesis.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/stream-journal-to-kinesis.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qldb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/index.html#cli-aws-qldb) ]

# stream-journal-to-kinesis

## Description

Creates a journal stream for a given Amazon QLDB ledger. The stream captures every document revision that is committed to the ledgerâs journal and delivers the data to a specified Amazon Kinesis Data Streams resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/StreamJournalToKinesis)

## Synopsis

```
stream-journal-to-kinesis
--ledger-name <value>
--role-arn <value>
[--tags <value>]
--inclusive-start-time <value>
[--exclusive-end-time <value>]
--kinesis-configuration <value>
--stream-name <value>
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

`--role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource.

To pass a role to QLDB when requesting a journal stream, you must have permissions to perform the `iam:PassRole` action on the IAM role resource. This is required for all journal stream requests.

`--tags` (map)

The key-value pairs to add as tags to the stream that you want to create. Tag keys are case sensitive. Tag values are case sensitive and can be null.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--inclusive-start-time` (timestamp)

The inclusive start date and time from which to start streaming journal data. This parameter must be in `ISO 8601` date and time format and in Universal Coordinated Time (UTC). For example: `2019-06-13T21:36:34Z` .

The `InclusiveStartTime` cannot be in the future and must be before `ExclusiveEndTime` .

If you provide an `InclusiveStartTime` that is before the ledgerâs `CreationDateTime` , QLDB effectively defaults it to the ledgerâs `CreationDateTime` .

`--exclusive-end-time` (timestamp)

The exclusive date and time that specifies when the stream ends. If you donât define this parameter, the stream runs indefinitely until you cancel it.

The `ExclusiveEndTime` must be in `ISO 8601` date and time format and in Universal Coordinated Time (UTC). For example: `2019-06-13T21:36:34Z` .

`--kinesis-configuration` (structure)

The configuration settings of the Kinesis Data Streams destination for your stream request.

StreamArn -> (string)

The Amazon Resource Name (ARN) of the Kinesis Data Streams resource.

AggregationEnabled -> (boolean)

Enables QLDB to publish multiple data records in a single Kinesis Data Streams record, increasing the number of records sent per API call.

Default: `True`

### Warning

Record aggregation has important implications for processing records and requires de-aggregation in your stream consumer. To learn more, see [KPL Key Concepts](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-concepts.html) and [Consumer De-aggregation](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-consumer-deaggregation.html) in the *Amazon Kinesis Data Streams Developer Guide* .

Shorthand Syntax:

```
StreamArn=string,AggregationEnabled=boolean
```

JSON Syntax:

```
{
  "StreamArn": "string",
  "AggregationEnabled": true|false
}
```

`--stream-name` (string)

The name that you want to assign to the QLDB journal stream. User-defined names can help identify and indicate the purpose of a stream.

Your stream name must be unique among other *active* streams for a given ledger. Stream names have the same naming constraints as ledger names, as defined in [Quotas in Amazon QLDB](https://docs.aws.amazon.com/qldb/latest/developerguide/limits.html#limits.naming) in the *Amazon QLDB Developer Guide* .

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

**Example 1: To stream journal data to Kinesis Data Streams using input files**

The following `stream-journal-to-kinesis` example creates a stream of journal data within a specified date and time range from a ledger with the name `myExampleLedger`. The stream sends the data to a specified Amazon Kinesis data stream.

```
aws qldb stream-journal-to-kinesis \
    --ledger-name myExampleLedger \
    --inclusive-start-time 2020-05-29T00:00:00Z \
    --exclusive-end-time 2020-05-29T23:59:59Z \
    --role-arn arn:aws:iam::123456789012:role/my-kinesis-stream-role \
    --kinesis-configuration file://my-kinesis-config.json \
    --stream-name myExampleLedger-stream
```

Contents of `my-kinesis-config.json`:

```
{
    "StreamArn": "arn:aws:kinesis:us-east-1:123456789012:stream/stream-for-qldb",
    "AggregationEnabled": true
}
```

Output:

```
{
    "StreamId": "7ISCkqwe4y25YyHLzYUFAf"
}
```

For more information, see [Streaming journal data from Amazon QLDB](https://docs.aws.amazon.com/qldb/latest/developerguide/streams.html) in the *Amazon QLDB Developer Guide*.

**Example 2: To stream journal data to Kinesis Data Streams using shorthand syntax**

The following `stream-journal-to-kinesis` example creates a stream of journal data within a specified date and time range from a ledger with the name `myExampleLedger`. The stream sends the data to a specified Amazon Kinesis data stream.

```
aws qldb stream-journal-to-kinesis \
    --ledger-name myExampleLedger \
    --inclusive-start-time 2020-05-29T00:00:00Z \
    --exclusive-end-time 2020-05-29T23:59:59Z \
    --role-arn arn:aws:iam::123456789012:role/my-kinesis-stream-role \
    --stream-name myExampleLedger-stream \
    --kinesis-configuration StreamArn=arn:aws:kinesis:us-east-1:123456789012:stream/stream-for-qldb,AggregationEnabled=true
```

Output:

```
{
    "StreamId": "7ISCkqwe4y25YyHLzYUFAf"
}
```

For more information, see [Streaming journal data from Amazon QLDB](https://docs.aws.amazon.com/qldb/latest/developerguide/streams.html) in the *Amazon QLDB Developer Guide*.

## Output

StreamId -> (string)

The UUID (represented in Base62-encoded text) that QLDB assigns to each QLDB journal stream.