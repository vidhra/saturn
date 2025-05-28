# gcloud storage operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/operations/describe](https://cloud.google.com/sdk/gcloud/reference/storage/operations/describe)*

**NAME**

: **gcloud storage operations describe - get configuration and latest storage operation details**

**SYNOPSIS**

: **`gcloud storage operations describe` `[OPERATION_NAME](https://cloud.google.com/sdk/gcloud/reference/storage/operations/describe#OPERATION_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get details about a specific storage operation.

**EXAMPLES**

: To describe an operation "C894F35J" on bucket "my-bucket", run:

```
gcloud storage operations describe projects/_/buckets/my-bucket/operations/C894F35J
```

**POSITIONAL ARGUMENTS**

: **`OPERATION_NAME`**:
The operation name including the Cloud Storage bucket and operation ID.

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
gcloud alpha storage operations describe
```