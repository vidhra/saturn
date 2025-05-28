# gcloud filestore backups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update)*

**NAME**

: **gcloud filestore backups update - update a Filestore backup**

**SYNOPSIS**

: **`gcloud filestore backups update` `[BACKUP](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update#BACKUP)` `[--region](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update#--region)`=`REGION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update#--description)`=`DESCRIPTION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the metadata of a Filestore backup.
This command can fail for the following reasons:

- The backup specified does not exist.
- The active account does not have permission to update the given backup.

**EXAMPLES**

: The following command updates the Filestore Backup named 'my-backup' in region
us-central1 to change the description to 'A new description.'

```
gcloud filestore backups update my-backup --region=us-central1 --description="A new description."
```

**POSITIONAL ARGUMENTS**

: **`BACKUP`**:
Arguments and flags that specify the Filestore backup you want to update.

**REQUIRED FLAGS**

: **--region**:
Compute region (e.g. us-central1) for the backup.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the backup.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud alpha filestore backups update
```

```
gcloud beta filestore backups update
```