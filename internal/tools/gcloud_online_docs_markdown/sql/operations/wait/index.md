# gcloud sql operations wait  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/operations/wait](https://cloud.google.com/sdk/gcloud/reference/sql/operations/wait)*

**NAME**

: **gcloud sql operations wait - waits for one or more operations to complete**

**SYNOPSIS**

: **`gcloud sql operations wait` `[OPERATION](https://cloud.google.com/sdk/gcloud/reference/sql/operations/wait#OPERATION)` [`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/sql/operations/wait#OPERATION)` …] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/sql/operations/wait#--timeout)`=`TIMEOUT`; default=300] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/operations/wait#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Waits for one or more operations to complete.

**POSITIONAL ARGUMENTS**

: **`OPERATION` [`OPERATION` …]**:
An identifier that uniquely identifies the operation.

**FLAGS**

: **--timeout**:
Maximum number of seconds to wait for an operation to complete. By default, wait
for 300s. Set to `unlimited` to wait indefinitely.

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
gcloud alpha sql operations wait
```

```
gcloud beta sql operations wait
```