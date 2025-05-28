# gcloud run services logs read  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/services/logs/read](https://cloud.google.com/sdk/gcloud/reference/run/services/logs/read)*

**NAME**

: **gcloud run services logs read - read logs for a Cloud Run service**

**SYNOPSIS**

: **`gcloud run services logs read` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/run/services/logs/read#SERVICE)` [`[--freshness](https://cloud.google.com/sdk/gcloud/reference/run/services/logs/read#--freshness)`=`FRESHNESS`; default="1d"] [`[--log-filter](https://cloud.google.com/sdk/gcloud/reference/run/services/logs/read#--log-filter)`=`LOG_FILTER`] [`[--order](https://cloud.google.com/sdk/gcloud/reference/run/services/logs/read#--order)`=`ORDER`; default="desc"] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/services/logs/read#--region)`=`REGION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/run/services/logs/read#--limit)`=`LIMIT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/services/logs/read#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud run services logs read reads log entries. Log entries matching
`--log-filter` are returned according to the specified --order. If
the log entries come from multiple logs, then entries from different logs might
be intermingled in the results.

**EXAMPLES**

: To read log entries from for a Cloud Run Service, run:

```
gcloud run services logs read my-service
```

To read log entries with severity ERROR or higher, run:

```
gcloud run services logs read my-service --log-filter="severity>=ERROR"
```

To read log entries written in a specific time window, run:

```
gcloud run services logs read my-service --log-filter='timestamp<="2015-05-31T23:59:59Z" AND
 timestamp>="2015-05-31T00:00:00Z"'
```

To read up to 10 log entries in your service payloads that include the word
`SearchText` and format the output in `JSON` format, run:

```
gcloud run services logs read my-service --log-filter="textPayload:SearchText" --limit=10 --format=json
```

Detailed information about filters can be found at: [https://cloud.google.com/logging/docs/view/advanced_filters](https://cloud.google.com/logging/docs/view/advanced_filters)

**POSITIONAL ARGUMENTS**

: **`SERVICE`**:
Name for a Cloud Run service.

**FLAGS**

: **--freshness**:
Return entries that are not older than this value. Works only with DESC ordering
and filters without a timestamp. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--log-filter**:
Filter expression that specifies the log entries to return. Detailed information
about filters can be found at: [https://cloud.google.com/logging/docs/view/logging-query-language](https://cloud.google.com/logging/docs/view/logging-query-language)

**--order**:
Ordering of returned log entries based on timestamp field.
`ORDER` must be one of: `desc`,
`asc`.

**--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

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
gcloud alpha run services logs read
```

```
gcloud beta run services logs read
```