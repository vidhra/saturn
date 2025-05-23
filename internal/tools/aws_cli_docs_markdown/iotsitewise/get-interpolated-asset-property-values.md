# get-interpolated-asset-property-valuesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/get-interpolated-asset-property-values.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/get-interpolated-asset-property-values.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsitewise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html#cli-aws-iotsitewise) ]

# get-interpolated-asset-property-values

## Description

Get interpolated values for an asset property for a specified time interval, during a period of time. If your time series is missing data points during the specified time interval, you can use interpolation to estimate the missing data.

For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days.

To identify an asset property, you must specify one of the following:

- The `assetId` and `propertyId` of an asset property.
- A `propertyAlias` , which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature` ). To define an asset propertyâs alias, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)

`get-interpolated-asset-property-values` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `interpolatedAssetPropertyValues`

## Synopsis

```
get-interpolated-asset-property-values
[--asset-id <value>]
[--property-id <value>]
[--property-alias <value>]
--start-time-in-seconds <value>
[--start-time-offset-in-nanos <value>]
--end-time-in-seconds <value>
[--end-time-offset-in-nanos <value>]
--quality <value>
--interval-in-seconds <value>
--type <value>
[--interval-window-in-seconds <value>]
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

`--asset-id` (string)

The ID of the asset, in UUID format.

`--property-id` (string)

The ID of the asset property, in UUID format.

`--property-alias` (string)

The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature` ). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the *IoT SiteWise User Guide* .

`--start-time-in-seconds` (long)

The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time.

`--start-time-offset-in-nanos` (integer)

The nanosecond offset converted from `startTimeInSeconds` .

`--end-time-in-seconds` (long)

The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time.

`--end-time-offset-in-nanos` (integer)

The nanosecond offset converted from `endTimeInSeconds` .

`--quality` (string)

The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality.

Possible values:

- `GOOD`
- `BAD`
- `UNCERTAIN`

`--interval-in-seconds` (long)

The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends.

`--type` (string)

The interpolation type.

Valid values: `LINEAR_INTERPOLATION | LOCF_INTERPOLATION`

- `LINEAR_INTERPOLATION` â Estimates missing data using [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation) . For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.
- `LOCF_INTERPOLATION` â Estimates missing data using last observation carried forward interpolation If no data point is found for an interval, IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found. For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isnât found after 9 AM on July 2, 2021, IoT SiteWise uses the same interpolated value for the rest of the days.

`--interval-window-in-seconds` (long)

The query interval for the window, in seconds. IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.

### Note

- If you specify a value for the `intervalWindowInSeconds` parameter, the value for the `type` parameter must be `LINEAR_INTERPOLATION` .
- If a data point isnât found during the specified query window, IoT SiteWise wonât return an interpolated value for the interval. This indicates that thereâs a gap in the ingested data points.

For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on.

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

interpolatedAssetPropertyValues -> (list)

The requested interpolated values.

(structure)

Contains information about an interpolated asset property value.

timestamp -> (structure)

Contains a timestamp with optional nanosecond granularity.

timeInSeconds -> (long)

The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by `offsetInNanos` .

offsetInNanos -> (integer)

The nanosecond offset from `timeInSeconds` .

value -> (structure)

Contains an asset property value (of a single type only).

stringValue -> (string)

Asset property data of type string (sequence of characters). The allowed pattern: â^$|[^u0000-u001Fu007F]+â. The max length is 1024.

integerValue -> (integer)

Asset property data of type integer (whole number).

doubleValue -> (double)

Asset property data of type double (floating point number). The min value is -10^10. The max value is 10^10. Double.NaN is allowed.

booleanValue -> (boolean)

Asset property data of type Boolean (true or false).

nullValue -> (structure)

The type of null asset property data with BAD and UNCERTAIN qualities.

valueType -> (string)

The type of null asset property data.

nextToken -> (string)

The token for the next set of results, or null if there are no additional results.