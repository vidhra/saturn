# get-resource-metricsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-resource-metrics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-resource-metrics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/index.html#cli-aws-pi) ]

# get-resource-metrics

## Description

Retrieve Performance Insights metrics for a set of data sources over a time period. You can provide specific dimension groups and dimensions, and provide filtering criteria for each group. You must specify an aggregate function for each metric.

### Note

Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pi-2018-02-27/GetResourceMetrics)

## Synopsis

```
get-resource-metrics
--service-type <value>
--identifier <value>
--metric-queries <value>
--start-time <value>
--end-time <value>
[--period-in-seconds <value>]
[--max-results <value>]
[--next-token <value>]
[--period-alignment <value>]
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

The Amazon Web Services service for which Performance Insights returns metrics. Valid values are as follows:

- `RDS`
- `DOCDB`

Possible values:

- `RDS`
- `DOCDB`

`--identifier` (string)

An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as *ResourceID* . When you call `DescribeDBInstances` , the identifier is returned as `DbiResourceId` .

To use a DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X` .

`--metric-queries` (list)

An array of one or more queries to perform. Each query must specify a Performance Insights metric and specify an aggregate function, and you can provide filtering criteria. You must append the aggregate function to the metric. For example, to find the average for the metric `db.load` you must use `db.load.avg` . Valid values for aggregate functions include `.avg` , `.min` , `.max` , and `.sum` .

(structure)

A single query to be processed. You must provide the metric to query and append an aggregate function to the metric. For example, to find the average for the metric `db.load` you must use `db.load.avg` . Valid values for aggregate functions include `.avg` , `.min` , `.max` , and `.sum` . If no other parameters are specified, Performance Insights returns all data points for the specified metric. Optionally, you can request that the data points be aggregated by dimension group (`GroupBy` ), and return only those data points that match your criteria (`Filter` ).

Metric -> (string)

The name of a Performance Insights metric to be measured.

Valid values for `Metric` are:

- `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - The raw number of active sessions for the database engine.
- The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon Aurora User Guide* .
- The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon RDS User Guide* .

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

GroupBy -> (structure)

A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.

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

Filter -> (map)

One or more filters to apply in the request. Restrictions:

- Any number of filters by the same dimension, as specified in the `GroupBy` parameter.
- A single filter for any other dimension in this dimension group.

### Note

The `db.sql.db_id` filter isnât available for RDS for SQL Server DB instances.

key -> (string)

A generic string type that forbids characters that could expose our service (or services downstream) to security risks around injections.

value -> (string)

Shorthand Syntax:

```
Metric=string,GroupBy={Group=string,Dimensions=[string,string],Limit=integer},Filter={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "Metric": "string",
    "GroupBy": {
      "Group": "string",
      "Dimensions": ["string", ...],
      "Limit": integer
    },
    "Filter": {"string": "string"
      ...}
  }
  ...
]
```

`--start-time` (timestamp)

The date and time specifying the beginning of the requested time series query range. You canât specify a `StartTime` that is earlier than 7 days ago. By default, Performance Insights has 7 days of retention, but you can extend this range up to 2 years. The value specified is *inclusive* . Thus, the command returns data points equal to or greater than `StartTime` .

The value for `StartTime` must be earlier than the value for `EndTime` .

`--end-time` (timestamp)

The date and time specifying the end of the requested time series query range. The value specified is *exclusive* . Thus, the command returns data points less than (but not equal to) `EndTime` .

The value for `EndTime` must be later than the value for `StartTime` .

`--period-in-seconds` (integer)

The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:

- `1` (one second)
- `60` (one minute)
- `300` (five minutes)
- `3600` (one hour)
- `86400` (twenty-four hours)

If you donât specify `PeriodInSeconds` , then Performance Insights will choose a value for you, with a goal of returning roughly 100-200 data points in the response.

`--max-results` (integer)

The maximum number of items to return in the response.

`--next-token` (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords` .

`--period-alignment` (string)

The returned timestamp which is the start or end time of the time periods. The default value is `END_TIME` .

Possible values:

- `END_TIME`
- `START_TIME`

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

**To get resource metrics**

This example requests data points for the *db.wait_event* dimension group, and for the *db.wait_event.name* dimension within that group. In the response, the relevant data points are grouped by the requested dimension (*db.wait_event.name*).

Command:

```
aws pi get-resource-metrics --service-type RDS --identifier db-LKCGOBK26374TPTDFXOIWVCPPM --start-time 1527026400 --end-time 1527080400 --period-in-seconds 300 --metric db.load.avg --metric-queries file://metric-queries.json
```

The arguments for `--metric-queries` are stored in a JSON file, `metric-queries.json`.  Here are the contents of that file:

```
[
    {
        "Metric": "db.load.avg",
        "GroupBy": {
            "Group":"db.wait_event"
        }
    }
]
```

Output:

```
{
    "AlignedEndTime": 1.5270804E9,
    "AlignedStartTime": 1.5270264E9,
    "Identifier": "db-LKCGOBK26374TPTDFXOIWVCPPM",
    "MetricList": [
        {
            "Key": {
                "Metric": "db.load.avg"
            },
            "DataPoints": [
                {
                    "Timestamp": 1527026700.0,
                    "Value": 1.3533333333333333
                },
                {
                    "Timestamp": 1527027000.0,
                    "Value": 0.88
                },
                <...remaining output omitted...>
            ]
        },
        {
            "Key": {
                "Metric": "db.load.avg",
                "Dimensions": {
                    "db.wait_event.name": "wait/synch/mutex/innodb/aurora_lock_thread_slot_futex"
                }
            },
            "DataPoints": [
                {
                    "Timestamp": 1527026700.0,
                    "Value": 0.8566666666666667
                },
                {
                    "Timestamp": 1527027000.0,
                    "Value": 0.8633333333333333
                },
                <...remaining output omitted...>
            ],
        },
            <...remaining output omitted...>
    ]
}
```

## Output

AlignedStartTime -> (timestamp)

The start time for the returned metrics, after alignment to a granular boundary (as specified by `PeriodInSeconds` ). `AlignedStartTime` will be less than or equal to the value of the user-specified `StartTime` .

AlignedEndTime -> (timestamp)

The end time for the returned metrics, after alignment to a granular boundary (as specified by `PeriodInSeconds` ). `AlignedEndTime` will be greater than or equal to the value of the user-specified `Endtime` .

Identifier -> (string)

An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as *ResourceID* . When you call `DescribeDBInstances` , the identifier is returned as `DbiResourceId` .

MetricList -> (list)

An array of metric results, where each array element contains all of the data points for a particular dimension.

(structure)

A time-ordered series of data points, corresponding to a dimension of a Performance Insights metric.

Key -> (structure)

The dimensions to which the data points apply.

Metric -> (string)

The name of a Performance Insights metric to be measured.

Valid values for `Metric` are:

- `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - The raw number of active sessions for the database engine.
- The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon Aurora User Guide* .
- The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon RDS User Guide* .

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

Dimensions -> (map)

The valid dimensions for the metric.

key -> (string)

value -> (string)

DataPoints -> (list)

An array of timestamp-value pairs, representing measurements over a period of time.

(structure)

A timestamp, and a single numerical value, which together represent a measurement at a particular point in time.

Timestamp -> (timestamp)

The time, in epoch format, associated with a particular `Value` .

Value -> (double)

The actual value associated with a particular `Timestamp` .

NextToken -> (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords` .