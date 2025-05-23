# get-log-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/get-log-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/get-log-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# get-log-events

## Description

Lists log events from the specified log stream. You can list all of the log events or filter using a time range.

`GetLogEvents` is a paginated operation. Each page returned can contain up to 1 MB of log events or up to 10,000 log events. A returned page might only be partially full, or even empty. For example, if the result of a query would return 15,000 log events, the first page isnât guaranteed to have 10,000 log events even if they all fit into 1 MB.

Partially full or empty pages donât necessarily mean that pagination is finished. As long as the `nextBackwardToken` or `nextForwardToken` returned is NOT equal to the `nextToken` that you passed into the API call, there might be more log events available. The token that you use depends on the direction you want to move in along the log stream. The returned tokens are never null.

### Note

If you set `startFromHead` to `true` and you donât include `endTime` in your request, you can end up in a situation where the pagination doesnât terminate. This can happen when the new log events are being added to the target log streams faster than they are being read. This situation is a good use case for the CloudWatch Logs [Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) feature.

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) .

You can specify the log group to search by using either `logGroupIdentifier` or `logGroupName` . You must include one of these two parameters, but you canât include both.

### Note

If you are using [log transformation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html) , the `GetLogEvents` operation returns only the original versions of log events, before they were transformed. To view the transformed versions, you must use a [CloudWatch Logs query.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/GetLogEvents)

## Synopsis

```
get-log-events
[--log-group-name <value>]
[--log-group-identifier <value>]
--log-stream-name <value>
[--start-time <value>]
[--end-time <value>]
[--next-token <value>]
[--limit <value>]
[--start-from-head | --no-start-from-head]
[--unmask | --no-unmask]
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

`--log-group-name` (string)

The name of the log group.

### Note

You must include either `logGroupIdentifier` or `logGroupName` , but not both.

`--log-group-identifier` (string)

Specify either the name or ARN of the log group to view events from. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.

### Note

You must include either `logGroupIdentifier` or `logGroupName` , but not both.

`--log-stream-name` (string)

The name of the log stream.

`--start-time` (long)

The start of the time range, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC` . Events with a timestamp equal to this time or later than this time are included. Events with a timestamp earlier than this time are not included.

`--end-time` (long)

The end of the time range, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC` . Events with a timestamp equal to or later than this time are not included.

`--next-token` (string)

The token for the next set of items to return. (You received this token from a previous call.)

`--limit` (integer)

The maximum number of log events returned. If you donât specify a limit, the default is as many log events as can fit in a response size of 1 MB (up to 10,000 log events).

`--start-from-head` | `--no-start-from-head` (boolean)

If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. The default value is false.

If you are using a previous `nextForwardToken` value as the `nextToken` in this operation, you must specify `true` for `startFromHead` .

`--unmask` | `--no-unmask` (boolean)

Specify `true` to display the log event fields with all sensitive data unmasked and visible. The default is `false` .

To use this operation with this parameter, you must be signed into an account with the `logs:Unmask` permission.

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

The following command retrieves log events from a log stream named `20150601` in the log group `my-logs`:

```
aws logs get-log-events --log-group-name my-logs --log-stream-name 20150601
```

Output:

```
{
    "nextForwardToken": "f/31961209122447488583055879464742346735121166569214640130",
    "events": [
        {
            "ingestionTime": 1433190494190,
            "timestamp": 1433190184356,
            "message": "Example Event 1"
        },
        {
            "ingestionTime": 1433190516679,
            "timestamp": 1433190184356,
            "message": "Example Event 1"
        },
        {
            "ingestionTime": 1433190494190,
            "timestamp": 1433190184358,
            "message": "Example Event 2"
        }
    ],
    "nextBackwardToken": "b/31961209122358285602261756944988674324553373268216709120"
}
```

## Output

events -> (list)

The events.

(structure)

Represents a log event.

timestamp -> (long)

The time the event occurred, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC` .

message -> (string)

The data contained in the log event.

ingestionTime -> (long)

The time the event was ingested, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC` .

nextForwardToken -> (string)

The token for the next set of items in the forward direction. The token expires after 24 hours. If you have reached the end of the stream, it returns the same token you passed in.

nextBackwardToken -> (string)

The token for the next set of items in the backward direction. The token expires after 24 hours. This token is not null. If you have reached the end of the stream, it returns the same token you passed in.