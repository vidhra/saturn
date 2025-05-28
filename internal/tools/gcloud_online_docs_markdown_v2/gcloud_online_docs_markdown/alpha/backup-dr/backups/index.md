# gcloud alpha backup-dr backups  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups)*

**NAME**

: **gcloud alpha backup-dr backups - manage Backup and DR backups**

**SYNOPSIS**

: **`gcloud alpha backup-dr backups` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage Backup and DR backups.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[restore](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/restore)`**:
`(ALPHA)` Manage restore operations for resources.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/delete)`**:
`(ALPHA)` Delete the specified Backup.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/describe)`**:
`(ALPHA)` Show details of the backup.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/list)`**:
`(ALPHA)` List Backups.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/update)`**:
`(ALPHA)` Update the specified Backup.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud backup-dr backups
```