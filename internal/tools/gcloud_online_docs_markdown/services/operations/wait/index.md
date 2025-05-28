# gcloud services operations wait  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/operations/wait](https://cloud.google.com/sdk/gcloud/reference/services/operations/wait)*

**NAME**

: **gcloud services operations wait - waits for an operation to complete for a given operation name**

**SYNOPSIS**

: **`gcloud services operations wait` `[OPERATION](https://cloud.google.com/sdk/gcloud/reference/services/operations/wait#OPERATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/operations/wait#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command will block until an operation has been marked as complete.

**EXAMPLES**

: To wait on an operation named `operations/abc` to complete, run:

```
gcloud services operations wait operations/abc
```

**POSITIONAL ARGUMENTS**

: **`OPERATION`**:
The name of the operation on which to wait.

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
gcloud alpha services operations wait
```

```
gcloud beta services operations wait
```