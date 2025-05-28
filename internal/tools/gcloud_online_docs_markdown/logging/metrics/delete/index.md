# gcloud logging metrics delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/metrics/delete](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/delete)*

**NAME**

: **gcloud logging metrics delete - delete a logs-based metric**

**SYNOPSIS**

: **`gcloud logging metrics delete` `[METRIC_NAME](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/delete#METRIC_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/metrics/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a logs-based metric called high_severity_count.

**EXAMPLES**

: To delete a metric called high_severity_count, run:

```
gcloud logging metrics delete high_severity_count
```

**POSITIONAL ARGUMENTS**

: **`METRIC_NAME`**:
The name of the metric to delete.

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
gcloud alpha logging metrics delete
```

```
gcloud beta logging metrics delete
```