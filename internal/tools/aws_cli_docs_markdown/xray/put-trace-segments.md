# put-trace-segmentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/put-trace-segments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/put-trace-segments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [xray](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/index.html#cli-aws-xray) ]

# put-trace-segments

## Description

Uploads segment documents to Amazon Web Services X-Ray. A segment document can be a completed segment, an in-progress segment, or an array of subsegments.

Segments must include the following fields. For the full segment document schema, see [Amazon Web Services X-Ray Segment Documents](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-api.html#xray-api-segmentdocuments.html) in the *Amazon Web Services X-Ray Developer Guide* .

**Required segment document fields**

- `name` - The name of the service that handled the request.
- `id` - A 64-bit identifier for the segment, unique among segments in the same trace, in 16 hexadecimal digits.
- `trace_id` - A unique identifier that connects all segments and subsegments originating from a single client request.
- `start_time` - Time the segment or subsegment was created, in floating point seconds in epoch time, accurate to milliseconds. For example, `1480615200.010` or `1.480615200010E9` .
- `end_time` - Time the segment or subsegment was closed. For example, `1480615200.090` or `1.480615200090E9` . Specify either an `end_time` or `in_progress` .
- `in_progress` - Set to `true` instead of specifying an `end_time` to record that a segment has been started, but is not complete. Send an in-progress segment when your application receives a request that will take a long time to serve, to trace that the request was received. When the response is sent, send the complete segment to overwrite the in-progress segment.

A `trace_id` consists of three numbers separated by hyphens. For example, 1-58406520-a006649127e371903a2de979. For trace IDs created by an X-Ray SDK, or by Amazon Web Services services integrated with X-Ray, a trace ID includes:

**Trace ID Format**

- The version number, for instance, `1` .
- The time of the original request, in Unix epoch time, in 8 hexadecimal digits. For example, 10:00AM December 2nd, 2016 PST in epoch time is `1480615200` seconds, or `58406520` in hexadecimal.
- A 96-bit identifier for the trace, globally unique, in 24 hexadecimal digits.

### Note

Trace IDs created via OpenTelemetry have a different format based on the [W3C Trace Context specification](https://www.w3.org/TR/trace-context/) . A W3C trace ID must be formatted in the X-Ray trace ID format when sending to X-Ray. For example, a W3C trace ID `4efaaf4d1e8720b39541901950019ee5` should be formatted as `1-4efaaf4d-1e8720b39541901950019ee5` when sending to X-Ray. While X-Ray trace IDs include the original request timestamp in Unix epoch time, this is not required or validated.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/PutTraceSegments)

## Synopsis

```
put-trace-segments
--trace-segment-documents <value>
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

`--trace-segment-documents` (list)

A string containing a JSON document defining one or more segments or subsegments.

(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To upload a segment**

The following `put-trace-segments` example uploads segment documents to AWS X-Ray. The segment document is consumed as a list of JSON segment documents.

```
aws xray put-trace-segments \
    --trace-segment-documents "{\"id\":\"20312a0e2b8809f4\",\"name\":\"DynamoDB\",\"trace_id\":\"1-5832862d-a43aafded3334a971fe312db\",\"start_time\":1.479706157195E9,\"end_time\":1.479706157202E9,\"parent_id\":\"79736b962fe3239e\",\"http\":{\"response\":{\"content_length\":60,\"status\":200}},\"inferred\":true,\"aws\":{\"consistent_read\":false,\"table_name\":\"scorekeep-session-xray\",\"operation\":\"GetItem\",\"request_id\":\"SCAU23OM6M8FO38UASGC7785ARVV4KQNSO5AEMVJF66Q9ASUAAJG\",\"resource_names\":[\"scorekeep-session-xray\"]},\"origin\":\"AWS::DynamoDB::Table\"}"
```

Output:

```
{
    "UnprocessedTraceSegments": []
}
```

For more information, see [Sending Trace Data to AWS X-Ray](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-sendingdata.html#xray-api-segments) in the *AWS X-Ray Developer Guide*.

## Output

UnprocessedTraceSegments -> (list)

Segments that failed processing.

(structure)

Information about a segment that failed processing.

Id -> (string)

The segmentâs ID.

ErrorCode -> (string)

The error that caused processing to fail.

Message -> (string)

The error message.