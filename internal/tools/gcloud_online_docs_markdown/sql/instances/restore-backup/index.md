# gcloud sql instances restore-backup  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/restore-backup](https://cloud.google.com/sdk/gcloud/reference/sql/instances/restore-backup)*

**NAME**

: **gcloud sql instances restore-backup - restores a backup of a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql instances restore-backup` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/restore-backup#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/restore-backup#--async)`] [`[--backup-id](https://cloud.google.com/sdk/gcloud/reference/sql/instances/restore-backup#--backup-id)`=`BACKUP_ID`] [`[--backup-instance](https://cloud.google.com/sdk/gcloud/reference/sql/instances/restore-backup#--backup-instance)`=`BACKUP_INSTANCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/restore-backup#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: DEPRECATED: This command is deprecated and will be removed. Use 'gcloud beta sql
backups restore' instead.

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID that will be restored.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--backup-id**:
The ID of the backup run to restore from.

**--backup-instance**:
The ID of the instance that the backup was taken from.

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
gcloud alpha sql instances restore-backup
```

```
gcloud beta sql instances restore-backup
```