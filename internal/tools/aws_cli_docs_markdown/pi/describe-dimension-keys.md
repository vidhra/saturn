# describe-dimension-keysÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/describe-dimension-keys.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/describe-dimension-keys.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/index.html#cli-aws-pi) ]

# describe-dimension-keys

## Description

For a specific time period, retrieve the top `N` dimension keys for a metric.

### Note

Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pi-2018-02-27/DescribeDimensionKeys)

## Synopsis

```
describe-dimension-keys
--service-type <value>
--identifier <value>
--start-time <value>
--end-time <value>
--metric <value>
[--period-in-seconds <value>]
--group-by <value>
[--additional-metrics <value>]
[--partition-by <value>]
[--filter <value>]
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

`--service-type` (string)

The Amazon Web Services service for which Performance Insights will return metrics. Valid values are as follows:

- `RDS`
- `DOCDB`

Possible values:

- `RDS`
- `DOCDB`

`--identifier` (string)

An immutable, Amazon Web Services Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.

To use an Amazon RDS instance as a data source, you specify its `DbiResourceId` value. For example, specify `db-FAIHNTYBKTGAUSUZQYPDS2GW4A` .

`--start-time` (timestamp)

The date and time specifying the beginning of the requested time series data. You must specify a `StartTime` within the past 7 days. The value specified is *inclusive* , which means that data points equal to or greater than `StartTime` are returned.

The value for `StartTime` must be earlier than the value for `EndTime` .

`--end-time` (timestamp)

The date and time specifying the end of the requested time series data. The value specified is *exclusive* , which means that data points less than (but not equal to) `EndTime` are returned.

The value for `EndTime` must be later than the value for `StartTime` .

`--metric` (string)

The name of a Performance Insights metric to be measured.

Valid values for `Metric` are:

- `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - The raw number of active sessions for the database engine.

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

`--period-in-seconds` (integer)

The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:

- `1` (one second)
- `60` (one minute)
- `300` (five minutes)
- `3600` (one hour)
- `86400` (twenty-four hours)

If you donât specify `PeriodInSeconds` , then Performance Insights chooses a value for you, with a goal of returning roughly 100-200 data points in the response.

`--group-by` (structure)

A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights returns all dimensions within this group, unless you provide the names of specific dimensions within this group. You can also request that Performance Insights return a limited number of values for a dimension.

Group -> (string)

The name of the dimension group. Valid values are as follows:

- `db` - The name of the database to which the client is connected. The following values are permitted:
- Aurora PostgreSQL
- Amazon RDS PostgreSQL
- Aurora MySQL
- Amazon RDS MySQL
- Amazon RDS MariaDB
- Amazon DocumentDB
- `db.application` - The name of the application that is connected to the database. The following values are permitted:
- Aurora PostgreSQL
- Amazon RDS PostgreSQL
- Amazon DocumentDB
- `db.blocking_sql` - The SQL queries blocking the most DB load.
- `db.blocking_session` - The sessions blocking the most DB load.
- `db.blocking_object` - The object resources acquired by other sessions that are blocking the most DB load.
- `db.host` - The host name of the connected client (all engines).
- `db.plans` - The execution plans for the query (only Aurora PostgreSQL).
- `db.query` - The query that is currently running (only Amazon DocumentDB).
- `db.query_tokenized` - The digest query (only Amazon DocumentDB).
- `db.session_type` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL).
- `db.sql` - The text of the SQL statement that is currently running (all engines except Amazon DocumentDB).
- `db.sql_tokenized` - The SQL digest (all engines except Amazon DocumentDB).
- `db.user` - The user logged in to the database (all engines except Amazon DocumentDB).
- `db.wait_event` - The event for which the database backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_event_type` - The type of event for which the database backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_state` - The event for which the database backend is waiting (only Amazon DocumentDB).

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested, or are present in the response.

Valid values for elements in the `Dimensions` array are:

- `db.application.name` - The name of the application that is connected to the database. Valid values are as follows:
- Aurora PostgreSQL
- Amazon RDS PostgreSQL
- Amazon DocumentDB
- `db.blocking_sql.id` - The ID for each of the SQL queries blocking the most DB load.
- `db.blocking_sql.sql` - The SQL text for each of the SQL queries blocking the most DB load.
- `db.blocking_session.id` - The ID for each of the sessions blocking the most DB load.
- `db.blocking_object.id` - The ID for each of the object resources acquired by other sessions that are blocking the most DB load.
- `db.blocking_object.type` - The object type for each of the object resources acquired by other sessions that are blocking the most DB load.
- `db.blocking_object.value` - The value for each of the object resources acquired by other sessions that are blocking the most DB load.
- `db.host.id` - The host ID of the connected client (all engines).
- `db.host.name` - The host name of the connected client (all engines).
- `db.name` - The name of the database to which the client is connected. Valid values are as follows:
- Aurora PostgreSQL
- Amazon RDS PostgreSQL
- Aurora MySQL
- Amazon RDS MySQL
- Amazon RDS MariaDB
- Amazon DocumentDB
- `db.query.id` - The query ID generated by Performance Insights (only Amazon DocumentDB).
- `db.query.db_id` - The query ID generated by the database (only Amazon DocumentDB).
- `db.query.statement` - The text of the query that is being run (only Amazon DocumentDB).
- `db.query.tokenized_id`
- `db.query.tokenized.id` - The query digest ID generated by Performance Insights (only Amazon DocumentDB).
- `db.query.tokenized.db_id` - The query digest ID generated by Performance Insights (only Amazon DocumentDB).
- `db.query.tokenized.statement` - The text of the query digest (only Amazon DocumentDB).
- `db.session_type.name` - The type of the current session (only Amazon DocumentDB).
- `db.sql.id` - The hash of the full, non-tokenized SQL statement generated by Performance Insights (all engines except Amazon DocumentDB).
- `db.sql.db_id` - Either the SQL ID generated by the database engine, or a value generated by Performance Insights that begins with `pi-` (all engines except Amazon DocumentDB).
- `db.sql.statement` - The full text of the SQL statement that is running, as in `SELECT * FROM employees` (all engines except Amazon DocumentDB)
- `db.sql.tokenized_id` - The hash of the SQL digest generated by Performance Insights (all engines except Amazon DocumentDB). The `db.sql.tokenized_id` dimension fetches the value of the `db.sql_tokenized.id` dimension. Amazon RDS returns `db.sql.tokenized_id` from the `db.sql` dimension group.
- `db.sql_tokenized.id` - The hash of the SQL digest generated by Performance Insights (all engines except Amazon DocumentDB). In the console, `db.sql_tokenized.id` is called the Support ID because Amazon Web Services Support can look at this data to help you troubleshoot database issues.
- `db.sql_tokenized.db_id` - Either the native database ID used to refer to the SQL statement, or a synthetic ID such as `pi-2372568224` that Performance Insights generates if the native database ID isnât available (all engines except Amazon DocumentDB).
- `db.sql_tokenized.statement` - The text of the SQL digest, as in `SELECT * FROM employees WHERE employee_id = ?` (all engines except Amazon DocumentDB)
- `db.user.id` - The ID of the user logged in to the database (all engines except Amazon DocumentDB).
- `db.user.name` - The name of the user logged in to the database (all engines except Amazon DocumentDB).
- `db.wait_event.name` - The event for which the backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_event.type` - The type of event for which the backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_event_type.name` - The name of the event type for which the backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_state.name` - The event for which the backend is waiting (only Amazon DocumentDB).

(string)

A generic string type that forbids characters that could expose our service (or services downstream) to security risks around injections.

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Shorthand Syntax:

```
Group=string,Dimensions=string,string,Limit=integer
```

JSON Syntax:

```
{
  "Group": "string",
  "Dimensions": ["string", ...],
  "Limit": integer
}
```

`--additional-metrics` (list)

Additional metrics for the top `N` dimension keys. If the specified dimension group in the `GroupBy` parameter is `db.sql_tokenized` , you can specify per-SQL metrics to get the values for the top `N` SQL digests. The response syntax is as follows: `"AdditionalMetrics" : { "*string* " : "*string* " }` .

The only supported statistic function is `.avg` .

(string)

A generic string type that forbids characters that could expose our service (or services downstream) to security risks around injections.

Syntax:

```
"string" "string" ...
```

`--partition-by` (structure)

For each dimension specified in `GroupBy` , specify a secondary dimension to further subdivide the partition keys in the response.

Group -> (string)

The name of the dimension group. Valid values are as follows:

- `db` - The name of the database to which the client is connected. The following values are permitted:
- Aurora PostgreSQL
- Amazon RDS PostgreSQL
- Aurora MySQL
- Amazon RDS MySQL
- Amazon RDS MariaDB
- Amazon DocumentDB
- `db.application` - The name of the application that is connected to the database. The following values are permitted:
- Aurora PostgreSQL
- Amazon RDS PostgreSQL
- Amazon DocumentDB
- `db.blocking_sql` - The SQL queries blocking the most DB load.
- `db.blocking_session` - The sessions blocking the most DB load.
- `db.blocking_object` - The object resources acquired by other sessions that are blocking the most DB load.
- `db.host` - The host name of the connected client (all engines).
- `db.plans` - The execution plans for the query (only Aurora PostgreSQL).
- `db.query` - The query that is currently running (only Amazon DocumentDB).
- `db.query_tokenized` - The digest query (only Amazon DocumentDB).
- `db.session_type` - The type of the current session (only Aurora PostgreSQL and RDS PostgreSQL).
- `db.sql` - The text of the SQL statement that is currently running (all engines except Amazon DocumentDB).
- `db.sql_tokenized` - The SQL digest (all engines except Amazon DocumentDB).
- `db.user` - The user logged in to the database (all engines except Amazon DocumentDB).
- `db.wait_event` - The event for which the database backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_event_type` - The type of event for which the database backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_state` - The event for which the database backend is waiting (only Amazon DocumentDB).

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested, or are present in the response.

Valid values for elements in the `Dimensions` array are:

- `db.application.name` - The name of the application that is connected to the database. Valid values are as follows:
- Aurora PostgreSQL
- Amazon RDS PostgreSQL
- Amazon DocumentDB
- `db.blocking_sql.id` - The ID for each of the SQL queries blocking the most DB load.
- `db.blocking_sql.sql` - The SQL text for each of the SQL queries blocking the most DB load.
- `db.blocking_session.id` - The ID for each of the sessions blocking the most DB load.
- `db.blocking_object.id` - The ID for each of the object resources acquired by other sessions that are blocking the most DB load.
- `db.blocking_object.type` - The object type for each of the object resources acquired by other sessions that are blocking the most DB load.
- `db.blocking_object.value` - The value for each of the object resources acquired by other sessions that are blocking the most DB load.
- `db.host.id` - The host ID of the connected client (all engines).
- `db.host.name` - The host name of the connected client (all engines).
- `db.name` - The name of the database to which the client is connected. Valid values are as follows:
- Aurora PostgreSQL
- Amazon RDS PostgreSQL
- Aurora MySQL
- Amazon RDS MySQL
- Amazon RDS MariaDB
- Amazon DocumentDB
- `db.query.id` - The query ID generated by Performance Insights (only Amazon DocumentDB).
- `db.query.db_id` - The query ID generated by the database (only Amazon DocumentDB).
- `db.query.statement` - The text of the query that is being run (only Amazon DocumentDB).
- `db.query.tokenized_id`
- `db.query.tokenized.id` - The query digest ID generated by Performance Insights (only Amazon DocumentDB).
- `db.query.tokenized.db_id` - The query digest ID generated by Performance Insights (only Amazon DocumentDB).
- `db.query.tokenized.statement` - The text of the query digest (only Amazon DocumentDB).
- `db.session_type.name` - The type of the current session (only Amazon DocumentDB).
- `db.sql.id` - The hash of the full, non-tokenized SQL statement generated by Performance Insights (all engines except Amazon DocumentDB).
- `db.sql.db_id` - Either the SQL ID generated by the database engine, or a value generated by Performance Insights that begins with `pi-` (all engines except Amazon DocumentDB).
- `db.sql.statement` - The full text of the SQL statement that is running, as in `SELECT * FROM employees` (all engines except Amazon DocumentDB)
- `db.sql.tokenized_id` - The hash of the SQL digest generated by Performance Insights (all engines except Amazon DocumentDB). The `db.sql.tokenized_id` dimension fetches the value of the `db.sql_tokenized.id` dimension. Amazon RDS returns `db.sql.tokenized_id` from the `db.sql` dimension group.
- `db.sql_tokenized.id` - The hash of the SQL digest generated by Performance Insights (all engines except Amazon DocumentDB). In the console, `db.sql_tokenized.id` is called the Support ID because Amazon Web Services Support can look at this data to help you troubleshoot database issues.
- `db.sql_tokenized.db_id` - Either the native database ID used to refer to the SQL statement, or a synthetic ID such as `pi-2372568224` that Performance Insights generates if the native database ID isnât available (all engines except Amazon DocumentDB).
- `db.sql_tokenized.statement` - The text of the SQL digest, as in `SELECT * FROM employees WHERE employee_id = ?` (all engines except Amazon DocumentDB)
- `db.user.id` - The ID of the user logged in to the database (all engines except Amazon DocumentDB).
- `db.user.name` - The name of the user logged in to the database (all engines except Amazon DocumentDB).
- `db.wait_event.name` - The event for which the backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_event.type` - The type of event for which the backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_event_type.name` - The name of the event type for which the backend is waiting (all engines except Amazon DocumentDB).
- `db.wait_state.name` - The event for which the backend is waiting (only Amazon DocumentDB).

(string)

A generic string type that forbids characters that could expose our service (or services downstream) to security risks around injections.

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Shorthand Syntax:

```
Group=string,Dimensions=string,string,Limit=integer
```

JSON Syntax:

```
{
  "Group": "string",
  "Dimensions": ["string", ...],
  "Limit": integer
}
```

`--filter` (map)

One or more filters to apply in the request. Restrictions:

- Any number of filters by the same dimension, as specified in the `GroupBy` or `Partition` parameters.
- A single filter for any other dimension in this dimension group.

### Note

The `db.sql.db_id` filter isnât available for RDS for SQL Server DB instances.

key -> (string)

A generic string type that forbids characters that could expose our service (or services downstream) to security risks around injections.

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

`--max-results` (integer)

The maximum number of items to return in the response. If more items exist than the specified `MaxRecords` value, a pagination token is included in the response so that the remaining results can be retrieved.

`--next-token` (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords` .

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

**To describe dimension keys**

This example requests the names of all wait events. The data is summarized by event name, and the aggregate values of those events over the specified time period.

Command:

```
aws pi describe-dimension-keys --service-type RDS --identifier db-LKCGOBK26374TPTDFXOIWVCPPM --start-time 1527026400 --end-time 1527080400 --metric db.load.avg --group-by '{"Group":"db.wait_event"}'
```

Output:

```
{
    "AlignedEndTime": 1.5270804E9,
    "AlignedStartTime": 1.5270264E9,
    "Keys": [
        {
            "Dimensions": {"db.wait_event.name": "wait/synch/mutex/innodb/aurora_lock_thread_slot_futex"},
            "Total": 0.05906906851195666
        },
        {
            "Dimensions": {"db.wait_event.name": "wait/io/aurora_redo_log_flush"},
            "Total": 0.015824722186149193
        },
        {
            "Dimensions": {"db.wait_event.name": "CPU"},
            "Total": 0.008014396230265477
        },
        {
            "Dimensions": {"db.wait_event.name": "wait/io/aurora_respond_to_client"},
            "Total": 0.0036361612526204477
        },
        {
            "Dimensions": {"db.wait_event.name": "wait/io/table/sql/handler"},
            "Total": 0.0019108398419382965
        },
        {
            "Dimensions": {"db.wait_event.name": "wait/synch/cond/mysys/my_thread_var::suspend"},
            "Total": 8.533847837782684E-4
        },
        {
            "Dimensions": {"db.wait_event.name": "wait/io/file/csv/data"},
            "Total": 6.864181956477376E-4
        },
        {
            "Dimensions": {"db.wait_event.name": "Unknown"},
            "Total": 3.895887056379051E-4
        },
        {
            "Dimensions": {"db.wait_event.name": "wait/synch/mutex/sql/FILE_AS_TABLE::LOCK_shim_lists"},
            "Total": 3.710368625122906E-5
        },
        {
            "Dimensions": {"db.wait_event.name": "wait/lock/table/sql/handler"},
            "Total": 0
        }
    ]
}
```

## Output

AlignedStartTime -> (timestamp)

The start time for the returned dimension keys, after alignment to a granular boundary (as specified by `PeriodInSeconds` ). `AlignedStartTime` will be less than or equal to the value of the user-specified `StartTime` .

AlignedEndTime -> (timestamp)

The end time for the returned dimension keys, after alignment to a granular boundary (as specified by `PeriodInSeconds` ). `AlignedEndTime` will be greater than or equal to the value of the user-specified `Endtime` .

PartitionKeys -> (list)

If `PartitionBy` was present in the request, `PartitionKeys` contains the breakdown of dimension keys by the specified partitions.

(structure)

If `PartitionBy` was specified in a `DescribeDimensionKeys` request, the dimensions are returned in an array. Each element in the array specifies one dimension.

Dimensions -> (map)

A dimension map that contains the dimensions for this partition.

key -> (string)

value -> (string)

Keys -> (list)

The dimension keys that were requested.

(structure)

An object that includes the requested dimension key values and aggregated metric values within a dimension group.

Dimensions -> (map)

A map of name-value pairs for the dimensions in the group.

key -> (string)

value -> (string)

Total -> (double)

The aggregated metric value for the dimensions, over the requested time range.

AdditionalMetrics -> (map)

A map that contains the value for each additional metric.

key -> (string)

value -> (double)

Partitions -> (list)

If `PartitionBy` was specified, `PartitionKeys` contains the dimensions that were.

(double)

NextToken -> (string)

A pagination token that indicates the response didnât return all available records because `MaxRecords` was specified in the previous request. To get the remaining records, specify `NextToken` in a separate request with this value.