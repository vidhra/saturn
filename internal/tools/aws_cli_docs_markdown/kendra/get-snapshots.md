# get-snapshotsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/get-snapshots.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/get-snapshots.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# get-snapshots

## Description

Retrieves search metrics data. The data provides a snapshot of how your users interact with your search application and how effective the application is.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/GetSnapshots)

## Synopsis

```
get-snapshots
--index-id <value>
--interval <value>
--metric-type <value>
[--next-token <value>]
[--max-results <value>]
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

`--index-id` (string)

The identifier of the index to get search metrics data.

`--interval` (string)

The time interval or time window to get search metrics data. The time interval uses the time zone of your index. You can view data in the following time windows:

- `THIS_WEEK` : The current week, starting on the Sunday and ending on the day before the current date.
- `ONE_WEEK_AGO` : The previous week, starting on the Sunday and ending on the following Saturday.
- `TWO_WEEKS_AGO` : The week before the previous week, starting on the Sunday and ending on the following Saturday.
- `THIS_MONTH` : The current month, starting on the first day of the month and ending on the day before the current date.
- `ONE_MONTH_AGO` : The previous month, starting on the first day of the month and ending on the last day of the month.
- `TWO_MONTHS_AGO` : The month before the previous month, starting on the first day of the month and ending on last day of the month.

Possible values:

- `THIS_MONTH`
- `THIS_WEEK`
- `ONE_WEEK_AGO`
- `TWO_WEEKS_AGO`
- `ONE_MONTH_AGO`
- `TWO_MONTHS_AGO`

`--metric-type` (string)

The metric you want to retrieve. You can specify only one metric per call.

For more information about the metrics you can view, see [Gaining insights with search analytics](https://docs.aws.amazon.com/kendra/latest/dg/search-analytics.html) .

Possible values:

- `QUERIES_BY_COUNT`
- `QUERIES_BY_ZERO_CLICK_RATE`
- `QUERIES_BY_ZERO_RESULT_RATE`
- `DOCS_BY_CLICK_COUNT`
- `AGG_QUERY_DOC_METRICS`
- `TREND_QUERY_DOC_METRICS`

`--next-token` (string)

If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of search metrics data.

`--max-results` (integer)

The maximum number of returned data for the metric.

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

SnapShotTimeFilter -> (structure)

The Unix timestamp for the beginning and end of the time window for the search metrics data.

StartTime -> (timestamp)

The Unix timestamp for the beginning of the time range.

EndTime -> (timestamp)

The Unix timestamp for the end of the time range.

SnapshotsDataHeader -> (list)

The column headers for the search metrics data.

(string)

SnapshotsData -> (list)

The search metrics data. The data returned depends on the metric type you requested.

(list)

(string)

NextToken -> (string)

If the response is truncated, Amazon Kendra returns this token, which you can use in a later request to retrieve the next set of search metrics data.