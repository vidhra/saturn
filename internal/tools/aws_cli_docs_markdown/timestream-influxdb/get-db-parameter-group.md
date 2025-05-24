# get-db-parameter-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-influxdb/get-db-parameter-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-influxdb/get-db-parameter-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [timestream-influxdb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-influxdb/index.html#cli-aws-timestream-influxdb) ]

# get-db-parameter-group

## Description

Returns a Timestream for InfluxDB DB parameter group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/timestream-influxdb-2023-01-27/GetDbParameterGroup)

## Synopsis

```
get-db-parameter-group
--identifier <value>
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

`--identifier` (string)

The id of the DB parameter group.

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

id -> (string)

A service-generated unique identifier.

name -> (string)

The customer-supplied name that uniquely identifies the DB parameter group when interacting with the Amazon Timestream for InfluxDB API and CLI commands.

arn -> (string)

The Amazon Resource Name (ARN) of the DB parameter group.

description -> (string)

A description of the DB parameter group.

parameters -> (tagged union structure)

The parameters that comprise the DB parameter group.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `InfluxDBv2`.

InfluxDBv2 -> (structure)

All the customer-modifiable InfluxDB v2 parameters in Timestream for InfluxDB.

fluxLogEnabled -> (boolean)

Include option to show detailed logs for Flux queries.

Default: false

logLevel -> (string)

Log output level. InfluxDB outputs log entries with severity levels greater than or equal to the level specified.

Default: info

noTasks -> (boolean)

Disable the task scheduler. If problematic tasks prevent InfluxDB from starting, use this option to start InfluxDB without scheduling or executing tasks.

Default: false

queryConcurrency -> (integer)

Number of queries allowed to execute concurrently. Setting to 0 allows an unlimited number of concurrent queries.

Default: 0

queryQueueSize -> (integer)

Maximum number of queries allowed in execution queue. When queue limit is reached, new queries are rejected. Setting to 0 allows an unlimited number of queries in the queue.

Default: 0

tracingType -> (string)

Enable tracing in InfluxDB and specifies the tracing type. Tracing is disabled by default.

metricsDisabled -> (boolean)

Disable the HTTP /metrics endpoint which exposes [internal InfluxDB metrics](https://docs.influxdata.com/influxdb/v2/reference/internals/metrics/) .

Default: false

httpIdleTimeout -> (structure)

Maximum duration the server should keep established connections alive while waiting for new requests. Set to 0 for no timeout.

Default: 3 minutes

durationType -> (string)

The type of duration for InfluxDB parameters.

value -> (long)

The value of duration for InfluxDB parameters.

httpReadHeaderTimeout -> (structure)

Maximum duration the server should try to read HTTP headers for new requests. Set to 0 for no timeout.

Default: 10 seconds

durationType -> (string)

The type of duration for InfluxDB parameters.

value -> (long)

The value of duration for InfluxDB parameters.

httpReadTimeout -> (structure)

Maximum duration the server should try to read the entirety of new requests. Set to 0 for no timeout.

Default: 0

durationType -> (string)

The type of duration for InfluxDB parameters.

value -> (long)

The value of duration for InfluxDB parameters.

httpWriteTimeout -> (structure)

Maximum duration the server should spend processing and responding to write requests. Set to 0 for no timeout.

Default: 0

durationType -> (string)

The type of duration for InfluxDB parameters.

value -> (long)

The value of duration for InfluxDB parameters.

influxqlMaxSelectBuckets -> (long)

Maximum number of group by time buckets a SELECT statement can create. 0 allows an unlimited number of buckets.

Default: 0

influxqlMaxSelectPoint -> (long)

Maximum number of points a SELECT statement can process. 0 allows an unlimited number of points. InfluxDB checks the point count every second (so queries exceeding the maximum arenât immediately aborted).

Default: 0

influxqlMaxSelectSeries -> (long)

Maximum number of series a SELECT statement can return. 0 allows an unlimited number of series.

Default: 0

pprofDisabled -> (boolean)

Disable the /debug/pprof HTTP endpoint. This endpoint provides runtime profiling data and can be helpful when debugging.

Default: true

queryInitialMemoryBytes -> (long)

Initial bytes of memory allocated for a query.

Default: 0

queryMaxMemoryBytes -> (long)

Maximum number of queries allowed in execution queue. When queue limit is reached, new queries are rejected. Setting to 0 allows an unlimited number of queries in the queue.

Default: 0

queryMemoryBytes -> (long)

Maximum bytes of memory allowed for a single query. Must be greater or equal to queryInitialMemoryBytes.

Default: 0

sessionLength -> (integer)

Specifies the Time to Live (TTL) in minutes for newly created user sessions.

Default: 60

sessionRenewDisabled -> (boolean)

Disables automatically extending a userâs session TTL on each request. By default, every request sets the sessionâs expiration time to five minutes from now. When disabled, sessions expire after the specified [session length](https://docs.influxdata.com/influxdb/v2/reference/config-options/#session-length) and the user is redirected to the login page, even if recently active.

Default: false

storageCacheMaxMemorySize -> (long)

Maximum size (in bytes) a shardâs cache can reach before it starts rejecting writes. Must be greater than storageCacheSnapShotMemorySize and lower than instanceâs total memory capacity. We recommend setting it to below 15% of the total memory capacity.

Default: 1073741824

storageCacheSnapshotMemorySize -> (long)

Size (in bytes) at which the storage engine will snapshot the cache and write it to a TSM file to make more memory available. Must not be greater than storageCacheMaxMemorySize.

Default: 26214400

storageCacheSnapshotWriteColdDuration -> (structure)

Duration at which the storage engine will snapshot the cache and write it to a new TSM file if the shard hasnât received writes or deletes.

Default: 10 minutes

durationType -> (string)

The type of duration for InfluxDB parameters.

value -> (long)

The value of duration for InfluxDB parameters.

storageCompactFullWriteColdDuration -> (structure)

Duration at which the storage engine will compact all TSM files in a shard if it hasnât received writes or deletes.

Default: 4 hours

durationType -> (string)

The type of duration for InfluxDB parameters.

value -> (long)

The value of duration for InfluxDB parameters.

storageCompactThroughputBurst -> (long)

Rate limit (in bytes per second) that TSM compactions can write to disk.

Default: 50331648

storageMaxConcurrentCompactions -> (integer)

Maximum number of full and level compactions that can run concurrently. A value of 0 results in 50% of runtime.GOMAXPROCS(0) used at runtime. Any number greater than zero limits compactions to that value. This setting does not apply to cache snapshotting.

Default: 0

storageMaxIndexLogFileSize -> (long)

Size (in bytes) at which an index write-ahead log (WAL) file will compact into an index file. Lower sizes will cause log files to be compacted more quickly and result in lower heap usage at the expense of write throughput.

Default: 1048576

storageNoValidateFieldSize -> (boolean)

Skip field size validation on incoming write requests.

Default: false

storageRetentionCheckInterval -> (structure)

Interval of retention policy enforcement checks. Must be greater than 0.

Default: 30 minutes

durationType -> (string)

The type of duration for InfluxDB parameters.

value -> (long)

The value of duration for InfluxDB parameters.

storageSeriesFileMaxConcurrentSnapshotCompactions -> (integer)

Maximum number of snapshot compactions that can run concurrently across all series partitions in a database.

Default: 0

storageSeriesIdSetCacheSize -> (long)

Size of the internal cache used in the TSI index to store previously calculated series results. Cached results are returned quickly rather than needing to be recalculated when a subsequent query with the same tag key/value predicate is executed. Setting this value to 0 will disable the cache and may decrease query performance.

Default: 100

storageWalMaxConcurrentWrites -> (integer)

Maximum number writes to the WAL directory to attempt at the same time. Setting this value to 0 results in number of processing units available x2.

Default: 0

storageWalMaxWriteDelay -> (structure)

Maximum amount of time a write request to the WAL directory will wait when the [maximum number of concurrent active writes to the WAL directory has been met](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-wal-max-concurrent-writes) . Set to 0 to disable the timeout.

Default: 10 minutes

durationType -> (string)

The type of duration for InfluxDB parameters.

value -> (long)

The value of duration for InfluxDB parameters.

uiDisabled -> (boolean)

Disable the InfluxDB user interface (UI). The UI is enabled by default.

Default: false