# gcloud memorystore backup-collections backups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/describe](https://cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/describe)*

**NAME**

: **gcloud memorystore backup-collections backups describe - describe backups**

**SYNOPSIS**

: **`gcloud memorystore backup-collections backups describe` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/describe#BACKUP)` : `[--backup-collection](https://cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/describe#--backup-collection)`=`BACKUP_COLLECTION` `[--location](https://cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a backup

**EXAMPLES**

: To describe the backup, run:

```
gcloud memorystore backup-collections backups describe
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Instance backup resource name using the form:
`projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}`
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP`**:
ID of the backup or fully qualified identifier for the backup.
To set the `backup` attribute:

- provide the argument `backup` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--backup-collection**:
The backupCollection id of the backup resource.
To set the `backup-collection` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--backup-collection` on the command line.

**--location**:
The location id of the backup resource.
To set the `location` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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

: This command uses the `memorystore/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/memorystore/](https://cloud.google.com/memorystore/)

**NOTES**

: These variants are also available:

```
gcloud alpha memorystore backup-collections backups describe
```

```
gcloud beta memorystore backup-collections backups describe
```