# gcloud sql instances delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete](https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete)*

**NAME**

: **gcloud sql instances delete - deletes a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql instances delete` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete#--async)`] [`[--enable-final-backup](https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete#--enable-final-backup)`] [`[--final-backup-description](https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete#--final-backup-description)`=`FINAL_BACKUP_DESCRIPTION`] [`[--final-backup-expiry-time](https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete#--final-backup-expiry-time)`=`FINAL_BACKUP_EXPIRY_TIME`     | `[--final-backup-retention-days](https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete#--final-backup-retention-days)`=`FINAL_BACKUP_RETENTION_DAYS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes a Cloud SQL instance.

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--enable-final-backup**:
Enables the final backup to be taken at the time of instance deletion.

**--final-backup-description**:
Provides description for the final backup going to be taken.

**--final-backup-expiry-time**

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
gcloud alpha sql instances delete
```

```
gcloud beta sql instances delete
```