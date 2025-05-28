# gcloud logging metrics update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/metrics/update](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/update)*

**NAME**

: **gcloud logging metrics update - update the definition of a logs-based metric**

**SYNOPSIS**

: **`gcloud logging metrics update` `[METRIC_NAME](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/update#METRIC_NAME)` (`[--config-from-file](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/update#--config-from-file)`=`PATH_TO_FILE`     | `[--bucket-name](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/update#--bucket-name)`=`BUCKET_NAME` `[--description](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/update#--description)`=`DESCRIPTION` `[--log-filter](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/update#--log-filter)`=`LOG_FILTER`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the description or the filter expression of an existing logs-based
metric.

**EXAMPLES**

: To update the description of a metric called high_severity_count, run:

```
gcloud logging metrics update high_severity_count --description="Count of high-severity log entries."
```

To update the filter expression of the metric, run:

```
gcloud logging metrics update high_severity_count --log-filter="severity >= WARNING"
```

Detailed information about filters can be found at: [https://cloud.google.com/logging/docs/view/logging-query-language](https://cloud.google.com/logging/docs/view/logging-query-language)
For advanced features such as user-defined labels and distribution metrics,
update using a config file:

```
gcloud logging metrics update high_severity_count --config-from-file=$PATH_TO_FILE
```

The config file should be in YAML format. Detailed information about how to
configure metrics can be found at: [https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric](https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric).
Any top-level fields in the LogMetric definition that aren't specified in the
config file will not be updated in the metric.
To update the bucket associated with a bucket log-based metric, run:

```
gcloud logging metrics update my-bucket-metric --bucket-name="NEW_BUCKET_NAME"
```

**POSITIONAL ARGUMENTS**

: **`METRIC_NAME`**:
The name of the log-based metric to update.

**REQUIRED FLAGS**

: **--config-from-file**

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
gcloud alpha logging metrics update
```

```
gcloud beta logging metrics update
```