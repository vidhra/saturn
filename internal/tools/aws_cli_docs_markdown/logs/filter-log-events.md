# filter-log-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/filter-log-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/filter-log-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# filter-log-events

## Description

Lists log events from the specified log group. You can list all the log events or filter the results using one or more of the following:

- A filter pattern
- A time range
- The log stream name, or a log stream name prefix that matches mutltiple log streams

You must have the `logs:FilterLogEvents` permission to perform this operation.

You can specify the log group to search by using either `logGroupIdentifier` or `logGroupName` . You must include one of these two parameters, but you canât include both.

`FilterLogEvents` is a paginated operation. Each page returned can contain up to 1 MB of log events or up to 10,000 log events. A returned page might only be partially full, or even empty. For example, if the result of a query would return 15,000 log events, the first page isnât guaranteed to have 10,000 log events even if they all fit into 1 MB.

Partially full or empty pages donât necessarily mean that pagination is finished. If the results include a `nextToken` , there might be more log events available. You can return these additional log events by providing the nextToken in a subsequent `FilterLogEvents` operation. If the results donât include a `nextToken` , then pagination is finished.

Specifying the `limit` parameter only guarantees that a single page doesnât return more log events than the specified limit, but it might return fewer events than the limit. This is the expected API behavior.

The returned log events are sorted by event timestamp, the timestamp when the event was ingested by CloudWatch Logs, and the ID of the `PutLogEvents` request.

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) .

### Note

If you are using [log transformation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html) , the `FilterLogEvents` operation returns only the original versions of log events, before they were transformed. To view the transformed versions, you must use a [CloudWatch Logs query.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/FilterLogEvents)

`filter-log-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `events`, `searchedLogStreams`

## Synopsis

```
filter-log-events
[--log-group-name <value>]
[--log-group-identifier <value>]
[--log-stream-names <value>]
[--log-stream-name-prefix <value>]
[--start-time <value>]
[--end-time <value>]
[--filter-pattern <value>]
[--interleaved | --no-interleaved]
[--unmask | --no-unmask]
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

`--log-group-name` (string)

The name of the log group to search.

### Note

You must include either `logGroupIdentifier` or `logGroupName` , but not both.

`--log-group-identifier` (string)

Specify either the name or ARN of the log group to view log events from. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.

### Note

You must include either `logGroupIdentifier` or `logGroupName` , but not both.

`--log-stream-names` (list)

Filters the results to only logs from the log streams in this list.

If you specify a value for both `logStreamNames` and `logStreamNamePrefix` , the action returns an `InvalidParameterException` error.

(string)

Syntax:

```
"string" "string" ...
```

`--log-stream-name-prefix` (string)

Filters the results to include only events from log streams that have names starting with this prefix.

If you specify a value for both `logStreamNamePrefix` and `logStreamNames` , the action returns an `InvalidParameterException` error.

`--start-time` (long)

The start of the time range, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC` . Events with a timestamp before this time are not returned.

`--end-time` (long)

The end of the time range, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC` . Events with a timestamp later than this time are not returned.

`--filter-pattern` (string)

The filter pattern to use. For more information, see [Filter and Pattern Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) .

If not provided, all the events are matched.

`--interleaved` | `--no-interleaved` (boolean)

If the value is true, the operation attempts to provide responses that contain events from multiple log streams within the log group, interleaved in a single response. If the value is false, all the matched log events in the first log stream are searched first, then those in the next log stream, and so on.

**Important** As of June 17, 2019, this parameter is ignored and the value is assumed to be true. The response from this operation always interleaves events from multiple log streams within a log group.

`--unmask` | `--no-unmask` (boolean)

Specify `true` to display the log event fields with all sensitive data unmasked and visible. The default is `false` .

To use this operation with this parameter, you must be signed into an account with the `logs:Unmask` permission.

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

## Output

events -> (list)

The matched events.

(structure)

Represents a matched event.

logStreamName -> (string)

The name of the log stream to which this event belongs.

timestamp -> (long)

The time the event occurred, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC` .

message -> (string)

The data contained in the log event.

ingestionTime -> (long)

The time the event was ingested, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC` .

eventId -> (string)

The ID of the event.

searchedLogStreams -> (list)

**Important** As of May 15, 2020, this parameter is no longer supported. This parameter returns an empty list.

Indicates which log streams have been searched and whether each has been searched completely.

(structure)

Represents the search status of a log stream.

logStreamName -> (string)

The name of the log stream.

searchedCompletely -> (boolean)

Indicates whether all the events in this log stream were searched.

nextToken -> (string)

The token to use when requesting the next set of items. The token expires after 24 hours.

If the results donât include a `nextToken` , then pagination is finished.