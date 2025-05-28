# gcloud sql ssl client-certs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/delete](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/delete)*

**NAME**

: **gcloud sql ssl client-certs delete - delete a client certificate for a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql ssl client-certs delete` `[COMMON_NAME](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/delete#COMMON_NAME)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/delete#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/delete#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/delete#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a client certificate for a Cloud SQL instance.

**POSITIONAL ARGUMENTS**

: **`COMMON_NAME`**:
User supplied name. Constrained to `[a-zA-Z.-_ ]+`.

**REQUIRED FLAGS**

: **--instance**:
Cloud SQL instance ID.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha sql ssl client-certs delete
```

```
gcloud beta sql ssl client-certs delete
```