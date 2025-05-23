# queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [timestream-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/index.html#cli-aws-timestream-query) ]

# query

## Description

`Query` is a synchronous operation that enables you to run a query against your Amazon Timestream data.

If you enabled `QueryInsights` , this API also returns insights and metrics related to the query that you executed. `QueryInsights` helps with performance tuning of your query. For more information about `QueryInsights` , see [Using query insights to optimize queries in Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/using-query-insights.html) .

### Note

The maximum number of `Query` API requests youâre allowed to make with `QueryInsights` enabled is 1 query per second (QPS). If you exceed this query rate, it might result in throttling.

`Query` will time out after 60 seconds. You must update the default timeout in the SDK to support a timeout of 60 seconds. See the [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.run-query.html) for details.

Your query request will fail in the following cases:

- If you submit a `Query` request with the same client token outside of the 5-minute idempotency window.
- If you submit a `Query` request with the same client token, but change other parameters, within the 5-minute idempotency window.
- If the size of the row (including the query metadata) exceeds 1 MB, then the query will fail with the following error message:   `Query aborted as max page response size has been exceeded by the output result row`
- If the IAM principal of the query initiator and the result reader are not the same and/or the query initiator and the result reader do not have the same query string in the query requests, the query will fail with an `Invalid pagination token` error.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/timestream-query-2018-11-01/Query)

`query` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Rows`

## Synopsis

```
query
--query-string <value>
[--client-token <value>]
[--query-insights <value>]
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

`--query-string` (string)

The query to be run by Timestream.

`--client-token` (string)

Unique, case-sensitive string of up to 64 ASCII characters specified when a `Query` request is made. Providing a `ClientToken` makes the call to `Query` *idempotent* . This means that running the same query repeatedly will produce the same result. In other words, making multiple identical `Query` requests has the same effect as making a single request. When using `ClientToken` in a query, note the following:

- If the Query API is instantiated without a `ClientToken` , the Query SDK generates a `ClientToken` on your behalf.
- If the `Query` invocation only contains the `ClientToken` but does not include a `NextToken` , that invocation of `Query` is assumed to be a new query run.
- If the invocation contains `NextToken` , that particular invocation is assumed to be a subsequent invocation of a prior call to the Query API, and a result set is returned.
- After 4 hours, any request with the same `ClientToken` is treated as a new request.

`--query-insights` (structure)

Encapsulates settings for enabling `QueryInsights` .

Enabling `QueryInsights` returns insights and metrics in addition to query results for the query that you executed. You can use `QueryInsights` to tune your query performance.

Mode -> (string)

Provides the following modes to enable `QueryInsights` :

- `ENABLED_WITH_RATE_CONTROL` â Enables `QueryInsights` for the queries being processed. This mode also includes a rate control mechanism, which limits the `QueryInsights` feature to 1 query per second (QPS).
- `DISABLED` â Disables `QueryInsights` .

Shorthand Syntax:

```
Mode=string
```

JSON Syntax:

```
{
  "Mode": "ENABLED_WITH_RATE_CONTROL"|"DISABLED"
}
```

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

QueryId -> (string)

A unique ID for the given query.

NextToken -> (string)

A pagination token that can be used again on a `Query` call to get the next set of results.

Rows -> (list)

The result set rows returned by the query.

(structure)

Represents a single row in the query results.

Data -> (list)

List of data points in a single row of the result set.

(structure)

Datum represents a single data point in a query result.

ScalarValue -> (string)

Indicates if the data point is a scalar value such as integer, string, double, or Boolean.

TimeSeriesValue -> (list)

Indicates if the data point is a timeseries data type.

(structure)

The timeseries data type represents the values of a measure over time. A time series is an array of rows of timestamps and measure values, with rows sorted in ascending order of time. A TimeSeriesDataPoint is a single data point in the time series. It represents a tuple of (time, measure value) in a time series.

Time -> (string)

The timestamp when the measure value was collected.

Value -> (structure)

The measure value for the data point.

ScalarValue -> (string)

Indicates if the data point is a scalar value such as integer, string, double, or Boolean.

TimeSeriesValue -> (list)

Indicates if the data point is a timeseries data type.

(structure)

The timeseries data type represents the values of a measure over time. A time series is an array of rows of timestamps and measure values, with rows sorted in ascending order of time. A TimeSeriesDataPoint is a single data point in the time series. It represents a tuple of (time, measure value) in a time series.

Time -> (string)

The timestamp when the measure value was collected.

( â¦ recursive â¦ )

ArrayValue -> (list)

Indicates if the data point is an array.

( â¦ recursive â¦ )

RowValue -> (structure)

Indicates if the data point is a row.

Data -> (list)

List of data points in a single row of the result set.

( â¦ recursive â¦ )

NullValue -> (boolean)

Indicates if the data point is null.

ArrayValue -> (list)

Indicates if the data point is an array.

(structure)

Datum represents a single data point in a query result.

ScalarValue -> (string)

Indicates if the data point is a scalar value such as integer, string, double, or Boolean.

TimeSeriesValue -> (list)

Indicates if the data point is a timeseries data type.

(structure)

The timeseries data type represents the values of a measure over time. A time series is an array of rows of timestamps and measure values, with rows sorted in ascending order of time. A TimeSeriesDataPoint is a single data point in the time series. It represents a tuple of (time, measure value) in a time series.

Time -> (string)

The timestamp when the measure value was collected.

( â¦ recursive â¦ )

RowValue -> (structure)

Indicates if the data point is a row.

NullValue -> (boolean)

Indicates if the data point is null.

RowValue -> (structure)

Indicates if the data point is a row.

Data -> (list)

List of data points in a single row of the result set.

(structure)

Datum represents a single data point in a query result.

ScalarValue -> (string)

Indicates if the data point is a scalar value such as integer, string, double, or Boolean.

TimeSeriesValue -> (list)

Indicates if the data point is a timeseries data type.

(structure)

The timeseries data type represents the values of a measure over time. A time series is an array of rows of timestamps and measure values, with rows sorted in ascending order of time. A TimeSeriesDataPoint is a single data point in the time series. It represents a tuple of (time, measure value) in a time series.

Time -> (string)

The timestamp when the measure value was collected.

( â¦ recursive â¦ )

( â¦ recursive â¦ )NullValue -> (boolean)

Indicates if the data point is null.

NullValue -> (boolean)

Indicates if the data point is null.

ColumnInfo -> (list)

The column data types of the returned result set.

(structure)

Contains the metadata for query results such as the column names, data types, and other attributes.

Name -> (string)

The name of the result set column. The name of the result set is available for columns of all data types except for arrays.

Type -> (structure)

The data type of the result set column. The data type can be a scalar or complex. Scalar data types are integers, strings, doubles, Booleans, and others. Complex data types are types such as arrays, rows, and others.

ScalarType -> (string)

Indicates if the column is of type string, integer, Boolean, double, timestamp, date, time. For more information, see [Supported data types](https://docs.aws.amazon.com/timestream/latest/developerguide/supported-data-types.html) .

ArrayColumnInfo -> (structure)

Indicates if the column is an array.

Name -> (string)

The name of the result set column. The name of the result set is available for columns of all data types except for arrays.

Type -> (structure)

The data type of the result set column. The data type can be a scalar or complex. Scalar data types are integers, strings, doubles, Booleans, and others. Complex data types are types such as arrays, rows, and others.

ScalarType -> (string)

Indicates if the column is of type string, integer, Boolean, double, timestamp, date, time. For more information, see [Supported data types](https://docs.aws.amazon.com/timestream/latest/developerguide/supported-data-types.html) .

( â¦ recursive â¦ )( â¦ recursive â¦ )RowColumnInfo -> (list)

Indicates if the column is a row.

( â¦ recursive â¦ )

TimeSeriesMeasureValueColumnInfo -> (structure)

Indicates if the column is a timeseries data type.

Name -> (string)

The name of the result set column. The name of the result set is available for columns of all data types except for arrays.

Type -> (structure)

The data type of the result set column. The data type can be a scalar or complex. Scalar data types are integers, strings, doubles, Booleans, and others. Complex data types are types such as arrays, rows, and others.

ScalarType -> (string)

Indicates if the column is of type string, integer, Boolean, double, timestamp, date, time. For more information, see [Supported data types](https://docs.aws.amazon.com/timestream/latest/developerguide/supported-data-types.html) .

( â¦ recursive â¦ )( â¦ recursive â¦ )RowColumnInfo -> (list)

Indicates if the column is a row.

( â¦ recursive â¦ )

RowColumnInfo -> (list)

Indicates if the column is a row.

(structure)

Contains the metadata for query results such as the column names, data types, and other attributes.

Name -> (string)

The name of the result set column. The name of the result set is available for columns of all data types except for arrays.

Type -> (structure)

The data type of the result set column. The data type can be a scalar or complex. Scalar data types are integers, strings, doubles, Booleans, and others. Complex data types are types such as arrays, rows, and others.

ScalarType -> (string)

Indicates if the column is of type string, integer, Boolean, double, timestamp, date, time. For more information, see [Supported data types](https://docs.aws.amazon.com/timestream/latest/developerguide/supported-data-types.html) .

( â¦ recursive â¦ )( â¦ recursive â¦ )

QueryStatus -> (structure)

Information about the status of the query, including progress and bytes scanned.

ProgressPercentage -> (double)

The progress of the query, expressed as a percentage.

CumulativeBytesScanned -> (long)

The amount of data scanned by the query in bytes. This is a cumulative sum and represents the total amount of bytes scanned since the query was started.

CumulativeBytesMetered -> (long)

The amount of data scanned by the query in bytes that you will be charged for. This is a cumulative sum and represents the total amount of data that you will be charged for since the query was started. The charge is applied only once and is either applied when the query completes running or when the query is cancelled.

QueryInsightsResponse -> (structure)

Encapsulates `QueryInsights` containing insights and metrics related to the query that you executed.

QuerySpatialCoverage -> (structure)

Provides insights into the spatial coverage of the query, including the table with sub-optimal (max) spatial pruning. This information can help you identify areas for improvement in your partitioning strategy to enhance spatial pruning.

Max -> (structure)

Provides insights into the spatial coverage of the executed query and the table with the most inefficient spatial pruning.

- `Value` â The maximum ratio of spatial coverage.
- `TableArn` â The Amazon Resource Name (ARN) of the table with sub-optimal spatial pruning.
- `PartitionKey` â The partition key used for partitioning, which can be a default `measure_name` or a CDPK.

Value -> (double)

The maximum ratio of spatial coverage.

TableArn -> (string)

The Amazon Resource Name (ARN) of the table with the most sub-optimal spatial pruning.

PartitionKey -> (list)

The partition key used for partitioning, which can be a default `measure_name` or a [customer defined partition key](https://docs.aws.amazon.com/timestream/latest/developerguide/customer-defined-partition-keys.html) .

(string)

QueryTemporalRange -> (structure)

Provides insights into the temporal range of the query, including the table with the largest (max) time range. Following are some of the potential options for optimizing time-based pruning:

- Add missing time-predicates.
- Remove functions around the time predicates.
- Add time predicates to all the sub-queries.

Max -> (structure)

Encapsulates the following properties that provide insights into the most sub-optimal performing table on the temporal axis:

- `Value` â The maximum duration in nanoseconds between the start and end of the query.
- `TableArn` â The Amazon Resource Name (ARN) of the table which is queried with the largest time range.

Value -> (long)

The maximum duration in nanoseconds between the start and end of the query.

TableArn -> (string)

The Amazon Resource Name (ARN) of the table which is queried with the largest time range.

QueryTableCount -> (long)

Indicates the number of tables in the query.

OutputRows -> (long)

Indicates the total number of rows returned as part of the query result set. You can use this data to validate if the number of rows in the result set have changed as part of the query tuning exercise.

OutputBytes -> (long)

Indicates the size of query result set in bytes. You can use this data to validate if the result set has changed as part of the query tuning exercise.

UnloadPartitionCount -> (long)

Indicates the partitions created by the `Unload` operation.

UnloadWrittenRows -> (long)

Indicates the rows written by the `Unload` query.

UnloadWrittenBytes -> (long)

Indicates the size, in bytes, written by the `Unload` operation.