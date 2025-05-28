# gcloud sql backups patch  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/backups/patch](https://cloud.google.com/sdk/gcloud/reference/sql/backups/patch)*

**NAME**

: **gcloud sql backups patch - update the Final backup of a Cloud SQL project**

**SYNOPSIS**

: **`gcloud sql backups patch` `[NAME](https://cloud.google.com/sdk/gcloud/reference/sql/backups/patch#NAME)` (`[--backup-description](https://cloud.google.com/sdk/gcloud/reference/sql/backups/patch#--backup-description)`=`BACKUP_DESCRIPTION` `[--expiry-time](https://cloud.google.com/sdk/gcloud/reference/sql/backups/patch#--expiry-time)`=`EXPIRY_TIME`     | `[--ttl-days](https://cloud.google.com/sdk/gcloud/reference/sql/backups/patch#--ttl-days)`=`TTL_DAYS`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/backups/patch#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the Final backup of a Cloud SQL project.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The NAME of the backup. To find the NAME, run the following command: $ [gcloud sql backups list](https://cloud.google.com/sdk/gcloud/reference/sql/backups/list)
--filter=type:FINAL instance:{instance}.

**REQUIRED FLAGS**

: **--backup-description**

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
gcloud alpha sql backups patch
```

```
gcloud beta sql backups patch
```