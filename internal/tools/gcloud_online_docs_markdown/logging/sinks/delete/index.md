# gcloud logging sinks delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/sinks/delete](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/delete)*

**NAME**

: **gcloud logging sinks delete - delete a sink**

**SYNOPSIS**

: **`gcloud logging sinks delete` `[SINK_NAME](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/delete#SINK_NAME)` [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/delete#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/delete#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/delete#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/delete#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a sink and halt the export of log entries associated with that sink.
Deleting a sink does not affect log entries already exported through the deleted
sink, and will not affect other sinks that are exporting the same log(s).

**EXAMPLES**

: To delete a sync 'my-bq-sync':

```
gcloud logging sinks delete my-bq-sink
```

**POSITIONAL ARGUMENTS**

: **`SINK_NAME`**:
The name of the sink to delete.

**FLAGS**

: **--billing-account**

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
gcloud alpha logging sinks delete
```

```
gcloud beta logging sinks delete
```