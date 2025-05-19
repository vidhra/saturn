# gcloud alpha alloydb backups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/backups/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/backups/delete)*

**NAME**

: **gcloud alpha alloydb backups delete - deletes an AlloyDB backup within a given project**

**SYNOPSIS**

: **`gcloud alpha alloydb backups delete` `[BACKUP](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/backups/delete#BACKUP)` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/backups/delete#--region)`=`REGION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/backups/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/backups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Deletes an AlloyDB backup within a given project.

**EXAMPLES**

: To delete a backup, run:

```
gcloud alpha alloydb backups delete my-backup --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`BACKUP`**:
AlloyDB backup ID

**REQUIRED FLAGS**

: **--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud alloydb backups delete
```

```
gcloud beta alloydb backups delete
```