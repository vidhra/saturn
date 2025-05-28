# gcloud sql ssl-certs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/ssl-certs/create](https://cloud.google.com/sdk/gcloud/reference/sql/ssl-certs/create)*

**NAME**

: **gcloud sql ssl-certs create - creates an SSL certificate for a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql ssl-certs create` `[COMMON_NAME](https://cloud.google.com/sdk/gcloud/reference/sql/ssl-certs/create#COMMON_NAME)` `[CERT_FILE](https://cloud.google.com/sdk/gcloud/reference/sql/ssl-certs/create#CERT_FILE)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/ssl-certs/create#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/ssl-certs/create#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/ssl-certs/create#INSTANCE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/ssl-certs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Creates an SSL certificate for a Cloud SQL instance.
`gcloud sql ssl-certs` is deprecated. Use `[gcloud sql ssl
client-certs](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs)` instead.

**POSITIONAL ARGUMENTS**

: **`COMMON_NAME`**:
User supplied name. Constrained to `[a-zA-Z.-_ ]+`.

**`CERT_FILE`**:
Location of file which the private key of the created ssl-cert will be written
to.

**REQUIRED FLAGS**

: **--instance**:
Cloud SQL instance ID.

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
gcloud alpha sql ssl-certs create
```

```
gcloud beta sql ssl-certs create
```