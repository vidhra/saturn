# gcloud sql backups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/backups/create](https://cloud.google.com/sdk/gcloud/reference/sql/backups/create)*

**NAME**

: **gcloud sql backups create - creates a backup of a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql backups create` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/backups/create#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/backups/create#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/backups/create#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/backups/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/sql/backups/create#--description)`=`DESCRIPTION`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/sql/backups/create#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/backups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a backup of a Cloud SQL instance.

**REQUIRED FLAGS**

: **--instance**:
Cloud SQL instance ID.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A friendly description of the backup.

**--location**:
Choose where to store your backup. Backups are stored in the closest
multi-region location to you by default. Only customize if needed.

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
gcloud alpha sql backups create
```

```
gcloud beta sql backups create
```