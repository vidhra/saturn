# gcloud sql databases delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/databases/delete](https://cloud.google.com/sdk/gcloud/reference/sql/databases/delete)*

**NAME**

: **gcloud sql databases delete - deletes a Cloud SQL database**

**SYNOPSIS**

: **`gcloud sql databases delete` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/databases/delete#DATABASE)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/databases/delete#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/databases/delete#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/databases/delete#INSTANCE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/databases/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: For MySQL, also deletes all files in the database directory.

**POSITIONAL ARGUMENTS**

: **`DATABASE`**:
Cloud SQL database name.

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
gcloud alpha sql databases delete
```

```
gcloud beta sql databases delete
```