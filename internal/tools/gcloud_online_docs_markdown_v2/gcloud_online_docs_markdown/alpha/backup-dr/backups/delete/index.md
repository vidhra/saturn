# gcloud alpha backup-dr backups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/delete)*

**NAME**

: **gcloud alpha backup-dr backups delete - delete the specified Backup**

**SYNOPSIS**

: **`gcloud alpha backup-dr backups delete` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/delete#BACKUP)` : `[--backup-vault](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/delete#--backup-vault)`=`BACKUP_VAULT` `[--data-source](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/delete#--data-source)`=`DATA_SOURCE` `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Delete the specified Backup.

**EXAMPLES**

: To delete a backup `sample-backup` in backup vault
`sample-vault`, data source `sample-ds`, project
`sample-project` and location `us-central1` , run:

```
gcloud alpha backup-dr backups delete sample-backup --backup-vault=sample-vault --data-source=sample-ds --project=sample-project --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Name of the backup to delete. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP`**:
ID of the Backup or fully qualified identifier for the Backup.
To set the `name` attribute:

- provide the argument `backup` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--backup-vault**:
The ID of the Backup Vault.
To set the `backup-vault` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--backup-vault` on the command line.

**--data-source**:
The ID of the Data Source.
To set the `data-source` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--data-source` on the command line.

**--location**:
The location of the Backup.
To set the `location` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

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

**BRIEF**

: Deletes a specific backup

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud backup-dr backups delete
```