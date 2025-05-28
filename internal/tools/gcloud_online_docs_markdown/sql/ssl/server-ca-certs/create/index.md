# gcloud sql ssl server-ca-certs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/create](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/create)*

**NAME**

: **gcloud sql ssl server-ca-certs create - create a server CA cert for a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql ssl server-ca-certs create` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/create#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/create#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/create#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/create#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a server CA cert for a Cloud SQL instance.

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
gcloud alpha sql ssl server-ca-certs create
```

```
gcloud beta sql ssl server-ca-certs create
```