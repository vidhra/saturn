# gcloud netapp backup-vaults backups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/delete](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/delete)*

**NAME**

: **gcloud netapp backup-vaults backups delete - delete a Cloud NetApp Backup**

**SYNOPSIS**

: **`gcloud netapp backup-vaults backups delete` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/delete#BACKUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/delete#--async)`] [`[--backup-vault](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/delete#--backup-vault)`=`BACKUP_VAULT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Cloud NetApp Backup.

**EXAMPLES**

: The following command deletes a Backup named BACKUP inside a backup vault named
BACKUP_VAULT using the required arguments:

```
gcloud netapp backup-vaults backups delete BACKUP --location=us-central1 --backup-vault=BACKUP_VAULT
```

To delete a Backup named BACKUP asynchronously, run the following command:

```
gcloud netapp backup-vaults backups delete BACKUP --location=us-central1 --backup-vault=BACKUP_VAULT --async
```

**POSITIONAL ARGUMENTS**

: **Backup resource - The Backup to delete. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `backup_vault` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--backup-vault` on the command line.

This must be specified.

**`BACKUP`**:
ID of the backup or fully qualified identifier for the backup.
To set the `backup` attribute:

- provide the argument `backup` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the backup.
To set the `location` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**Backup vault resource - The Backup Vault that the Backup is stored in This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--backup-vault` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--backup-vault` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.

**--backup-vault**:
ID of the backup_vault or fully qualified identifier for the backup_vault.
To set the `backup_vault` attribute:

- provide the argument `--backup-vault` on the command line.**

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

: This variant is also available:

```
gcloud beta netapp backup-vaults backups delete
```