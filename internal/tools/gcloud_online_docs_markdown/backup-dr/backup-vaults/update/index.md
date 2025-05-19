# gcloud backup-dr backup-vaults update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update)*

**NAME**

: **gcloud backup-dr backup-vaults update - update a Backup and DR backup vault**

**SYNOPSIS**

: **`gcloud backup-dr backup-vaults update` (`[BACKUP_VAULT](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update#BACKUP_VAULT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update#--location)`=`LOCATION`) [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update#--async)`] [`[--backup-min-enforced-retention](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update#--backup-min-enforced-retention)`=`BACKUP_MIN_ENFORCED_RETENTION`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update#--description)`=`DESCRIPTION`] [`[--effective-time](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update#--effective-time)`=`EFFECTIVE_TIME`] [`[--force-update](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update#--force-update)`] [`[--unlock-backup-min-enforced-retention](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update#--unlock-backup-min-enforced-retention)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Backup and DR backup vault.

**EXAMPLES**

: To update a backup vault BACKUP_VAULT in location MY_LOCATION with one update
field, run:

```
gcloud backup-dr backup-vaults update BACKUP_VAULT --location=MY_LOCATION --effective-time="2024-03-22"
```

To update a backup vault BACKUP_VAULT in location MY_LOCATION with multiple
update fields, run:

```
gcloud backup-dr backup-vaults update BACKUP_VAULT --location=MY_LOCATION --backup-min-enforced-retention="400000s" --description="Updated backup vault"
```

**POSITIONAL ARGUMENTS**

: **Backup Vault resource - Name of the existing backup vault to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `backup_vault` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP_VAULT`**:
ID of the Backup Vault or fully qualified identifier for the Backup Vault.
To set the `name` attribute:

- provide the argument `backup_vault` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Backup Vault.
To set the `location` attribute:

- provide the argument `backup_vault` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--no-async**:
Wait for the operation in progress to complete.

**--backup-min-enforced-retention**:
Backups will be kept for this minimum period before they can be deleted. Once
the effective time is reached, the enforced retention period cannot be decreased
or removed. The value must be specified in relative time format (e.g. p1d, p1m,
p1m1d).

**--description**:
Optional description for the backup vault (2048 characters or less).

**--effective-time**:
The time at which the enforced retention period becomes locked. This flag is
mutually exclusive with --unlock-backup-min-enforced-retention.

**--force-update**:
If set, allow update to extend the minimum enforced retention for backup vault.
This overrides the restriction against conflicting retention periods. This
conflict may occur when the expiration schedule defined by the associated backup
plan is shorter than the minimum retention set by the backup vault.

**--unlock-backup-min-enforced-retention**:
Removes the lock on the backup minimum enforced retention period, and resets the
effective time. When unlocked, the enforced retention period can be changed at
any time. This flag is mutually exclusive with --effective-time.

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

: This command uses the backupdr/v1 API. The full documentation for this API can
be found at: [https://cloud.google.com/backup-disaster-recovery](https://cloud.google.com/backup-disaster-recovery)

**BRIEF**

: Updates a Backup and DR backup vault.

**NOTES**

: This variant is also available:

```
gcloud alpha backup-dr backup-vaults update
```