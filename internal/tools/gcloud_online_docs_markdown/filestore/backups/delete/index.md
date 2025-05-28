# gcloud filestore backups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/backups/delete](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/delete)*

**NAME**

: **gcloud filestore backups delete - delete a Filestore backup**

**SYNOPSIS**

: **`gcloud filestore backups delete` `[BACKUP](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/delete#BACKUP)` `[--region](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/delete#--region)`=`REGION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Filestore backup.
This command can fail for the following reasons:

- The backup specified does not exist.
- The active account does not have permission to delete the given backup.

**EXAMPLES**

: The following command deletes a backup with the name 'my-backup' in the region
us-central1:

```
gcloud filestore backups delete my-backup --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`BACKUP`**:
Arguments and flags that specify the Filestore backup you want to delete.

**REQUIRED FLAGS**

: **--region**:
Compute region (e.g. us-central1) for the backup.

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

**API REFERENCE**

: This command uses the `file/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/filestore/](https://cloud.google.com/filestore/)

**NOTES**

: These variants are also available:

```
gcloud alpha filestore backups delete
```

```
gcloud beta filestore backups delete
```