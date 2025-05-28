# gcloud transfer operations pause  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/operations/pause](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/pause)*

**NAME**

: **gcloud transfer operations pause - pause a currently running transfer operation**

**SYNOPSIS**

: **`gcloud transfer operations pause` `[NAME](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/pause#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/pause#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Pause a currently running transfer operation.

**EXAMPLES**

: To pause an operation, run:

```
gcloud transfer operations pause OPERATION-NAME
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the paused transfer operation you want to cancel.

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

: This variant is also available:

```
gcloud alpha transfer operations pause
```