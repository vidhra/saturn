# gcloud logging read  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/read](https://cloud.google.com/sdk/gcloud/reference/logging/read)*

**NAME**

: **gcloud logging read - read log entries**

**SYNOPSIS**

: **`gcloud logging read` [`[LOG_FILTER](https://cloud.google.com/sdk/gcloud/reference/logging/read#LOG_FILTER)`] [`[--freshness](https://cloud.google.com/sdk/gcloud/reference/logging/read#--freshness)`=`FRESHNESS`; default="1d"] [`[--order](https://cloud.google.com/sdk/gcloud/reference/logging/read#--order)`=`ORDER`; default="desc"] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/read#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/read#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/read#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/read#--project)`=`PROJECT_ID`] [`[--resource-names](https://cloud.google.com/sdk/gcloud/reference/logging/read#--resource-names)`=[`RESOURCE`,…]     | `[--bucket](https://cloud.google.com/sdk/gcloud/reference/logging/read#--bucket)`=`BUCKET` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/read#--location)`=`LOCATION` `[--view](https://cloud.google.com/sdk/gcloud/reference/logging/read#--view)`=`VIEW`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/logging/read#--limit)`=`LIMIT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/read#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud logging read reads log entries. Log entries matching
`log-filter` are returned in order of decreasing timestamps,
most-recent entries first. If the log entries come from multiple logs, then
entries from different logs might be intermingled in the results.

**EXAMPLES**

: To read log entries from Google Compute Engine instances, run:

```
gcloud logging read "resource.type=gce_instance"
```

To read log entries with severity ERROR or higher, run:

```
gcloud logging read "severity>=ERROR"
```

To read log entries written in a specific time window, run:

```
gcloud logging read 'timestamp<="2015-05-31T23:59:59Z" AND
 timestamp>="2015-05-31T00:00:00Z"'
```

To read up to 10 log entries in your project's syslog log from Compute Engine
instances containing payloads that include the word `SyncAddress` and
format the output in `JSON` format, run:

```
gcloud logging read "resource.type=gce_instance AND logName=projects/[PROJECT_ID]/logs/syslog AND textPayload:SyncAddress" --limit=10 --format=json
```

To read a log entry from a folder, run:

```
gcloud logging read "resource.type=global" --folder=[FOLDER_ID] --limit=1
```

To read a log entry from a global log bucket, run:

```
gcloud logging read --bucket=<bucket-id> --location=[LOCATION] --limit=1
```

To read a log entry from the global `_Required` log bucket using the
bucket's `_Default` log view:

```
gcloud logging read "" --bucket=_Required --location=global --view=_Default --limit=1
```

To read a log entry from a log bucket using the bucket's `_AllLogs`
log view:

```
gcloud logging read "" --bucket=[BUCKET_ID] --location=[LOCATION] --view=_AllLogs --limit=1
```

To read a log entry from a log bucket using a custom log view that you have
created for the bucket:

```
gcloud logging read "" --bucket=[BUCKET_ID] --location=[LOCATION] --view=[VIEW_ID] --limit=1
```

To read log entries from multiple resources, specify them as a comma-delimeted
sequence with --resource-names. Each resource name can be specified either as a
top-level resource (e.g., projects/[PROJECT_ID], folders/[FOLDER_ID], etc.) or
as a Log View resource (e.g.,
projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_NAME]/views/[VIEW_ID]).

```
gcloud logging read "" --resource-names=[RESOURCE-1],[RESOURCE-2]
```

**POSITIONAL ARGUMENTS**

: **[`LOG_FILTER`]**:
Filter expression that specifies the log entries to return. Detailed information
about filters can be found at: [https://cloud.google.com/logging/docs/view/logging-query-language](https://cloud.google.com/logging/docs/view/logging-query-language)

**FLAGS**

: **--freshness**:
Return entries that are not older than this value. Works only with DESC ordering
and filters without a timestamp. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--order**:
Ordering of returned log entries based on timestamp field.
`ORDER` must be one of: `desc`,
`asc`.

**--billing-account**

**--resource-names**

**LIST COMMAND FLAGS**

: **--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha logging read
```

```
gcloud beta logging read
```