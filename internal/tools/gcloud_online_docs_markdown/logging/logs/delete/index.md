# gcloud logging logs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/logs/delete](https://cloud.google.com/sdk/gcloud/reference/logging/logs/delete)*

**NAME**

: **gcloud logging logs delete - delete all entries from a log in the global `_Default` log bucket**

**SYNOPSIS**

: **`gcloud logging logs delete` `[LOG_NAME](https://cloud.google.com/sdk/gcloud/reference/logging/logs/delete#LOG_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/logs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete all entries from a log in the global `_Default` log bucket.
With no entries, the log will not appear in the list of your project's logs.
However, you can write new entries to the log.

**EXAMPLES**

: To delete all entries from log 'my-log' in the global `_Default` log
bucket:

```
gcloud logging logs delete my-log
```

**POSITIONAL ARGUMENTS**

: **`LOG_NAME`**:
Log name.

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
gcloud alpha logging logs delete
```

```
gcloud beta logging logs delete
```