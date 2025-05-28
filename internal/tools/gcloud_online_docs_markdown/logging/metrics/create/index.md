# gcloud logging metrics create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/metrics/create](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/create)*

**NAME**

: **gcloud logging metrics create - create a logs-based metric**

**SYNOPSIS**

: **`gcloud logging metrics create` `[METRIC_NAME](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/create#METRIC_NAME)` (`[--config-from-file](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/create#--config-from-file)`=`PATH_TO_FILE`     | [`[--description](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/create#--description)`=`DESCRIPTION` `[--log-filter](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/create#--log-filter)`=`LOG_FILTER` : `[--bucket-name](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/create#--bucket-name)`=`BUCKET_NAME`]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a logs-based metric to count the number of log entries that match a
filter expression. Logs-based metrics can also be used to extract values from
logs and create a distribution of the values.

**EXAMPLES**

: To create a metric that counts the number of log entries with a severity level
higher than WARNING, run:

```
gcloud logging metrics create high_severity_count --description="Number of high severity log entries" --log-filter="severity > WARNING"
```

Detailed information about filters can be found at: [https://cloud.google.com/logging/docs/view/logging-query-language](https://cloud.google.com/logging/docs/view/logging-query-language)
To create a metric that uses advanced features like distribution or user-defined
labels, run:

```
gcloud logging metrics create my_metric --config-from-file=$PATH_TO_FILE
```

The config file can be in YAML or JSON format. Detailed information about how to
configure metrics can be found at: [https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric](https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric).
To create a bucket log-based metric, run:

```
gcloud logging metrics create my_bucket_metric --description="DESCRIPTION" --log-filter="LOG_FILTER" --bucket-name="BUCKET_NAME"
```

**POSITIONAL ARGUMENTS**

: **`METRIC_NAME`**:
The name of the new metric.

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
gcloud alpha logging metrics create
```

```
gcloud beta logging metrics create
```