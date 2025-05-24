# get-journey-date-range-kpiÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-journey-date-range-kpi.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-journey-date-range-kpi.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# get-journey-date-range-kpi

## Description

Retrieves (queries) pre-aggregated data for a standard engagement metric that applies to a journey.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/GetJourneyDateRangeKpi)

## Synopsis

```
get-journey-date-range-kpi
--application-id <value>
[--end-time <value>]
--journey-id <value>
--kpi-name <value>
[--next-token <value>]
[--page-size <value>]
[--start-time <value>]
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

`--application-id` (string)

The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console.

`--end-time` (timestamp)

The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.

`--journey-id` (string)

The unique identifier for the journey.

`--kpi-name` (string)

The name of the metric, also referred to as a *key performance indicator (KPI)* , to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html) .

`--next-token` (string)

The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.

`--page-size` (string)

The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.

`--start-time` (timestamp)

The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.

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

JourneyDateRangeKpiResponse -> (structure)

Provides the results of a query that retrieved the data for a standard engagement metric that applies to a journey, and provides information about that query.

ApplicationId -> (string)

The unique identifier for the application that the metric applies to.

EndTime -> (timestamp)

The last date and time of the date range that was used to filter the query results, in extended ISO 8601 format. The date range is inclusive.

JourneyId -> (string)

The unique identifier for the journey that the metric applies to.

KpiName -> (string)

The name of the metric, also referred to as a *key performance indicator (KPI)* , that the data was retrieved for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. For a list of possible values, see the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html) .

KpiResult -> (structure)

An array of objects that contains the results of the query. Each object contains the value for the metric and metadata about that value.

Rows -> (list)

An array of objects that provides the results of a query that retrieved the data for a standard metric that applies to an application, campaign, or journey.

(structure)

Provides the results of a query that retrieved the data for a standard metric that applies to an application, campaign, or journey.

GroupedBys -> (list)

An array of objects that defines the field and field values that were used to group data in a result set that contains multiple results. This value is null if the data in a result set isnât grouped.

(structure)

Provides a single value and metadata about that value as part of an array of query results for a standard metric that applies to an application, campaign, or journey.

Key -> (string)

The friendly name of the metric whose value is specified by the Value property.

Type -> (string)

The data type of the value specified by the Value property.

Value -> (string)

In a Values object, the value for the metric that the query retrieved data for. In a GroupedBys object, the value for the field that was used to group data in a result set that contains multiple results (Values objects).

Values -> (list)

An array of objects that provides pre-aggregated values for a standard metric that applies to an application, campaign, or journey.

(structure)

Provides a single value and metadata about that value as part of an array of query results for a standard metric that applies to an application, campaign, or journey.

Key -> (string)

The friendly name of the metric whose value is specified by the Value property.

Type -> (string)

The data type of the value specified by the Value property.

Value -> (string)

In a Values object, the value for the metric that the query retrieved data for. In a GroupedBys object, the value for the field that was used to group data in a result set that contains multiple results (Values objects).

NextToken -> (string)

The string to use in a subsequent request to get the next page of results in a paginated response. This value is null for the Journey Engagement Metrics resource because the resource returns all results in a single page.

StartTime -> (timestamp)

The first date and time of the date range that was used to filter the query results, in extended ISO 8601 format. The date range is inclusive.