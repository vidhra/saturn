# gcloud netapp backup-vaults backups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create)*

**NAME**

: **gcloud netapp backup-vaults backups create - create a Cloud NetApp Backup**

**SYNOPSIS**

: **`gcloud netapp backup-vaults backups create` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create#BACKUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create#--async)`] [`[--backup-vault](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create#--backup-vault)`=`BACKUP_VAULT`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--source-snapshot](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create#--source-snapshot)`=`SOURCE_SNAPSHOT`] [`[--source-volume](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create#--source-volume)`=`SOURCE_VOLUME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud NetApp Backup.

**EXAMPLES**

: The following command creates a Backup named BACKUP attached to a Backup Vault
named BACKUP_VAULT, and a source volume named SOURCE_VOL asynchronously using
the specified arguments:

```
gcloud netapp backup-vaults backups create BACKUP --location=LOCATION --async --backup-vault=BACKUP_VAULT --source-volume=SOURCE_VOL
```

**POSITIONAL ARGUMENTS**

: **Backup resource - The Backup to create The arguments in this group can be used
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

**--description**:
A description of the Cloud NetApp Backup Vault

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**Snapshot resource - The full name of the Source Snapshot that the Backup is
based on', Format:
`projects/{project_id}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}`
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--source-snapshot` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--source-snapshot` on the command line with a
fully specified name;
- set the property `netapp/location`.

To set the `volume` attribute:

- provide the argument `--source-snapshot` on the command line with a
fully specified name.

**--source-snapshot**:
ID of the snapshot or fully qualified identifier for the snapshot.
To set the `snapshot` attribute:

- provide the argument `--source-snapshot` on the command line.**

**Volume resource - The full name of the Source Volume that the Backup is based
on', Format:
`projects/{projects_id}/locations/{location}/volumes/{volume_id}`
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--source-volume` on the command line with a
fully specified name;
- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--source-volume` on the command line with a
fully specified name;
- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.

**--source-volume**:
ID of the volume or fully qualified identifier for the volume.
To set the `volume` attribute:

- provide the argument `--source-volume` on the command line;
- provide the argument `--volume` on the command line.**

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
gcloud beta netapp backup-vaults backups create
```