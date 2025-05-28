# gcloud sql export tde  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/export/tde](https://cloud.google.com/sdk/gcloud/reference/sql/export/tde)*

**NAME**

: **gcloud sql export tde - export a TDE certificate from a Cloud SQL for SQL Server instance**

**SYNOPSIS**

: **`gcloud sql export tde` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/export/tde#INSTANCE)` (`[--cert-path](https://cloud.google.com/sdk/gcloud/reference/sql/export/tde#--cert-path)`=`CERT_PATH` `[--certificate](https://cloud.google.com/sdk/gcloud/reference/sql/export/tde#--certificate)`=`CERTIFICATE` `[--pvk-path](https://cloud.google.com/sdk/gcloud/reference/sql/export/tde#--pvk-path)`=`PVK_PATH` (`[--prompt-for-pvk-password](https://cloud.google.com/sdk/gcloud/reference/sql/export/tde#--prompt-for-pvk-password)` | `[--pvk-password](https://cloud.google.com/sdk/gcloud/reference/sql/export/tde#--pvk-password)`=`PVK_PASSWORD`)) [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/export/tde#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/export/tde#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Exports a TDE certificate from a Cloud SQL instance to a Google Cloud Storage
bucket. This is only supported for SQL Server.

**EXAMPLES**

: To export a TDE certificate with the name `foo` and private key
password `my-pvk-password` in the Cloud SQL instance
`my-instance` to certificate path `my-bucket/my-cert.cert`
and private key path `my-bucket/my-key.pvk`, run:

```
gcloud sql export tde my-instance --certificate=foo --cert-path=gs://my-bucket/my-cert.cert --pvk-path=gs://my-bucket/my-key.pvk --pvk-password=my-pvk-password
```

To export a TDE certificate with the name `foo` and private key
password `my-pvk-password` in the Cloud SQL instance
`my-instance` and prompting for the private key password, run:

```
gcloud sql export tde my-instance --certificate=foo --cert-path=gs://my-bucket/my-cert.cert --pvk-path=gs://my-bucket/my-key.pvk --prompt-for-pvk-password
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**REQUIRED FLAGS**

: **--cert-path**

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
gcloud alpha sql export tde
```

```
gcloud beta sql export tde
```