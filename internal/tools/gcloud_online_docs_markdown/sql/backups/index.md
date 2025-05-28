# gcloud sql backups  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/backups](https://cloud.google.com/sdk/gcloud/reference/sql/backups)*

**NAME**

: **gcloud sql backups - provide commands for working with backups of Cloud SQL instances**

**SYNOPSIS**

: **`gcloud sql backups` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/sql/backups#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/backups#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Provide commands for working with backups of Cloud SQL instances including
listing and getting information about backups for a Cloud SQL instance.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/sql/backups/create)`**:
Creates a backup of a Cloud SQL instance.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/sql/backups/delete)`**:
Delete a backup of a Cloud SQL instance.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/sql/backups/describe)`**:
Retrieves information about a backup.

**`[list](https://cloud.google.com/sdk/gcloud/reference/sql/backups/list)`**:
Lists all backups associated with the project or a given instance.

**`[patch](https://cloud.google.com/sdk/gcloud/reference/sql/backups/patch)`**:
Update the Final backup of a Cloud SQL project.

**`[restore](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore)`**:
Restores a backup of a Cloud SQL instance.

**NOTES**

: These variants are also available:

```
gcloud alpha sql backups
```

```
gcloud beta sql backups
```