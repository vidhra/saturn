# batch-get-asset-property-aggregatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/batch-get-asset-property-aggregates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/batch-get-asset-property-aggregates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsitewise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html#cli-aws-iotsitewise) ]

# batch-get-asset-property-aggregates

## Description

Gets aggregated values (for example, average, minimum, and maximum) for one or more asset properties. For more information, see [Querying aggregates](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates) in the *IoT SiteWise User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregates)

## Synopsis

```
batch-get-asset-property-aggregates
--entries <value>
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

`--entries` (list)

The list of asset property aggregate entries for the batch get request. You can specify up to 16 entries per request.

(structure)

Contains information for an asset property aggregate entry that is associated with the [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) API.

To identify an asset property, you must specify one of the following:

- The `assetId` and `propertyId` of an asset property.
- A `propertyAlias` , which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature` ). To define an asset propertyâs alias, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html) .

entryId -> (string)

The ID of the entry.

assetId -> (string)

The ID of the asset in which the asset property was created.

propertyId -> (string)

The ID of the asset property, in UUID format.

propertyAlias -> (string)

The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature` ). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the *IoT SiteWise User Guide* .

aggregateTypes -> (list)

The data aggregating function.

(string)

resolution -> (string)

The time interval over which to aggregate data.

startDate -> (timestamp)

The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.

endDate -> (timestamp)

The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.

qualities -> (list)

The quality by which to filter asset data.

(string)

timeOrdering -> (string)

The chronological sorting order of the requested information.

Default: `ASCENDING`

Shorthand Syntax:

```
entryId=string,assetId=string,propertyId=string,propertyAlias=string,aggregateTypes=string,string,resolution=string,startDate=timestamp,endDate=timestamp,qualities=string,string,timeOrdering=string ...
```

JSON Syntax:

```
[
  {
    "entryId": "string",
    "assetId": "string",
    "propertyId": "string",
    "propertyAlias": "string",
    "aggregateTypes": ["AVERAGE"|"COUNT"|"MAXIMUM"|"MINIMUM"|"SUM"|"STANDARD_DEVIATION", ...],
    "resolution": "string",
    "startDate": timestamp,
    "endDate": timestamp,
    "qualities": ["GOOD"|"BAD"|"UNCERTAIN", ...],
    "timeOrdering": "ASCENDING"|"DESCENDING"
  }
  ...
]
```

`--next-token` (string)

The token to be used for the next set of paginated results.

`--max-results` (integer)

The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.

- The size of the result set is equal to 1 MB.
- The number of data points in the result set is equal to the value of `maxResults` . The maximum value of `maxResults` is 4000.

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

errorEntries -> (list)

A list of the errors (if any) associated with the batch request. Each error entry contains the `entryId` of the entry that failed.

(structure)

Contains error information for an asset property aggregate entry that is associated with the [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) API.

errorCode -> (string)

The error code.

errorMessage -> (string)

The associated error message.

entryId -> (string)

The ID of the entry.

successEntries -> (list)

A list of entries that were processed successfully by this batch request. Each success entry contains the `entryId` of the entry that succeeded and the latest query result.

(structure)

Contains success information for an entry that is associated with the [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) API.

entryId -> (string)

The ID of the entry.

aggregatedValues -> (list)

The requested aggregated asset property values (for example, average, minimum, and maximum).

(structure)

Contains aggregated asset property values (for example, average, minimum, and maximum).

timestamp -> (timestamp)

The date the aggregating computations occurred, in Unix epoch time.

quality -> (string)

The quality of the aggregated data.

value -> (structure)

The value of the aggregates.

average -> (double)

The average (mean) value of the time series over a time interval window.

count -> (double)

The count of data points in the time series over a time interval window.

maximum -> (double)

The maximum value of the time series over a time interval window.

minimum -> (double)

The minimum value of the time series over a time interval window.

sum -> (double)

The sum of the time series over a time interval window.

standardDeviation -> (double)

The standard deviation of the time series over a time interval window.

skippedEntries -> (list)

A list of entries that were not processed by this batch request. because these entries had been completely processed by previous paginated requests. Each skipped entry contains the `entryId` of the entry that skipped.

(structure)

Contains information for an entry that has been processed by the previous [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) request.

entryId -> (string)

The ID of the entry.

completionStatus -> (string)

The completion status of each entry that is associated with the [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) API.

errorInfo -> (structure)

The error information, such as the error code and the timestamp.

errorCode -> (string)

The error code.

errorTimestamp -> (timestamp)

The date the error occurred, in Unix epoch time.

nextToken -> (string)

The token for the next set of results, or null if there are no additional results.