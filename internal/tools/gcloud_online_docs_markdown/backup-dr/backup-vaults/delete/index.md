# gcloud backup-dr backup-vaults delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete)*

**NAME**

: **gcloud backup-dr backup-vaults delete - delete the specified Backup Vault**

**SYNOPSIS**

: **`gcloud backup-dr backup-vaults delete` (`[BACKUP_VAULT](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete#BACKUP_VAULT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete#--location)`=`LOCATION`) [`[--allow-missing](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete#--allow-missing)`] [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete#--async)`] [`[--ignore-backup-plan-references](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete#--ignore-backup-plan-references)`] [`[--ignore-inactive-datasources](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete#--ignore-inactive-datasources)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the specified Backup Vault.

**EXAMPLES**

: To delete a backup vault ``BACKUP_VAULT`` in
location ``MY_LOCATION``, run:

```
gcloud backup-dr backup-vaults delete BACKUP_VAULT --location=MY_LOCATION
```

To override restrictions against the deletion of a backup vault
``BACKUP_VAULT`` containing inactive
datasources in location ``MY_LOCATION``, run:

```
gcloud backup-dr backup-vaults delete BACKUP_VAULT --location=MY_LOCATION --ignore-inactive-datasources
```

To override restrictions against the deletion of a backup vault
``BACKUP_VAULT`` containing backup plan
references in location ``MY_LOCATION``, run:

```
gcloud backup-dr backup-vaults delete BACKUP_VAULT --location=MY_LOCATION --ignore-backup-plan-references
```

**POSITIONAL ARGUMENTS**

: **Backup Vault resource - Name of the backup vault to delete. Before you delete,
take a look at the prerequisites [here](https://cloud.google.com/backup-disaster-recovery/docs/configuration/decommission).
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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

: **--allow-missing**:
Allow idempotent deletion of backup vault. The request will still succeed in
case the backup vault does not exist.

**--no-async**:
Wait for the operation in progress to complete.

**--ignore-backup-plan-references**:
If set, the following restrictions against deletion of the backup vault instance
can be overridden: * deletion of a backup vault instance being actively
referenced by a backup plan.

**--ignore-inactive-datasources**:
If set, the following restrictions against deletion of the backup vault instance
can be overridden: * deletion of a backup vault instance containing no
backups,but still contains empty datasources.

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

: Deletes a specific backup vault

**NOTES**

: This variant is also available:

```
gcloud alpha backup-dr backup-vaults delete
```