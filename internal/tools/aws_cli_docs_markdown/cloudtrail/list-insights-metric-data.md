# list-insights-metric-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-insights-metric-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-insights-metric-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# list-insights-metric-data

## Description

Returns Insights metrics data for trails that have enabled Insights. The request must include the `EventSource` , `EventName` , and `InsightType` parameters.

If the `InsightType` is set to `ApiErrorRateInsight` , the request must also include the `ErrorCode` parameter.

The following are the available time periods for `ListInsightsMetricData` . Each cutoff is inclusive.

- Data points with a period of 60 seconds (1-minute) are available for 15 days.
- Data points with a period of 300 seconds (5-minute) are available for 63 days.
- Data points with a period of 3600 seconds (1 hour) are available for 90 days.

Access to the `ListInsightsMetricData` API operation is linked to the `cloudtrail:LookupEvents` action. To use this operation, you must have permissions to perform the `cloudtrail:LookupEvents` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/ListInsightsMetricData)

## Synopsis

```
list-insights-metric-data
--event-source <value>
--event-name <value>
--insight-type <value>
[--error-code <value>]
[--start-time <value>]
[--end-time <value>]
[--period <value>]
[--data-type <value>]
[--max-results <value>]
[--next-token <value>]
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

`--event-source` (string)

The Amazon Web Services service to which the request was made, such as `iam.amazonaws.com` or `s3.amazonaws.com` .

`--event-name` (string)

The name of the event, typically the Amazon Web Services API on which unusual levels of activity were recorded.

`--insight-type` (string)

The type of CloudTrail Insights event, which is either `ApiCallRateInsight` or `ApiErrorRateInsight` . The `ApiCallRateInsight` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The `ApiErrorRateInsight` Insights type analyzes management API calls that result in error codes.

Possible values:

- `ApiCallRateInsight`
- `ApiErrorRateInsight`

`--error-code` (string)

Conditionally required if the `InsightType` parameter is set to `ApiErrorRateInsight` .

If returning metrics for the `ApiErrorRateInsight` Insights type, this is the error to retrieve data for. For example, `AccessDenied` .

`--start-time` (timestamp)

Specifies, in UTC, the start time for time-series data. The value specified is inclusive; results include data points with the specified time stamp.

The default is 90 days before the time of request.

`--end-time` (timestamp)

Specifies, in UTC, the end time for time-series data. The value specified is exclusive; results include data points up to the specified time stamp.

The default is the time of request.

`--period` (integer)

Granularity of data to retrieve, in seconds. Valid values are `60` , `300` , and `3600` . If you specify any other value, you will get an error. The default is 3600 seconds.

`--data-type` (string)

Type of data points to return. Valid values are `NonZeroData` and `FillWithZeros` . The default is `NonZeroData` .

Possible values:

- `FillWithZeros`
- `NonZeroData`

`--max-results` (integer)

The maximum number of data points to return. Valid values are integers from 1 to 21600. The default value is 21600.

`--next-token` (string)

Returned if all datapoints canât be returned in a single call. For example, due to reaching `MaxResults` .

Add this parameter to the request to continue retrieving results starting from the last evaluated point.

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

EventSource -> (string)

The Amazon Web Services service to which the request was made, such as `iam.amazonaws.com` or `s3.amazonaws.com` .

EventName -> (string)

The name of the event, typically the Amazon Web Services API on which unusual levels of activity were recorded.

InsightType -> (string)

The type of CloudTrail Insights event, which is either `ApiCallRateInsight` or `ApiErrorRateInsight` . The `ApiCallRateInsight` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The `ApiErrorRateInsight` Insights type analyzes management API calls that result in error codes.

ErrorCode -> (string)

Only returned if `InsightType` parameter was set to `ApiErrorRateInsight` .

If returning metrics for the `ApiErrorRateInsight` Insights type, this is the error to retrieve data for. For example, `AccessDenied` .

Timestamps -> (list)

List of timestamps at intervals corresponding to the specified time period.

(timestamp)

Values -> (list)

List of values representing the API call rate or error rate at each timestamp. The number of values is equal to the number of timestamps.

(double)

NextToken -> (string)

Only returned if the full results could not be returned in a single query. You can set the `NextToken` parameter in the next request to this value to continue retrieval.