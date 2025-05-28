# gcloud spanner databases restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore)*

**NAME**

: **gcloud spanner databases restore - restore a Cloud Spanner database**

**SYNOPSIS**

: **`gcloud spanner databases restore` (`[--destination-database](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--destination-database)`=`DESTINATION_DATABASE` : `[--destination-instance](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--destination-instance)`=`DESTINATION_INSTANCE`) (`[--source-backup](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--source-backup)`=`SOURCE_BACKUP` : `[--source-instance](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--source-instance)`=`SOURCE_INSTANCE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--async)`] [`[--encryption-type](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--encryption-type)`=`ENCRYPTION_TYPE` `[--kms-keys](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--kms-keys)`=[`KMS_KEYS`,…]     | [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#--kms-project)`=`KMS_PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Restores from a backup to a new Cloud Spanner database.

**EXAMPLES**

: To restore a backup, run:

```
gcloud spanner databases restore --source-backup=BACKUP_ID --source-instance=SOURCE_INSTANCE --destination-database=DATABASE --destination-instance=INSTANCE_NAME
```

To restore a backup using relative names, run:

```
gcloud spanner databases restore --source-backup=projects/PROJECT_ID/instances/SOURCE_INSTANCE_ID/backups/BACKUP_ID --destination-database=projects/PROJECT_ID/instances/SOURCE_INSTANCE_ID/databases/DATABASE_ID
```

**REQUIRED FLAGS**

: **Database resource - TEXT The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--destination-database` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--destination-database**:
ID of the database or fully qualified identifier for the database.
To set the `database` attribute:

- provide the argument `--destination-database` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--destination-instance**:
The Cloud Spanner instance for the database.
To set the `instance` attribute:

- provide the argument `--destination-database` on the command line
with a fully specified name;
- provide the argument `--destination-instance` on the command line;
- set the property `spanner/instance`.**

**Backup resource - TEXT The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--source-backup` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--source-backup**:
ID of the backup or fully qualified identifier for the backup.
To set the `backup` attribute:

- provide the argument `--source-backup` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--source-instance**:
The Cloud Spanner instance for the backup.
To set the `instance` attribute:

- provide the argument `--source-backup` on the command line with a
fully specified name;
- provide the argument `--source-instance` on the command line;
- set the property `spanner/instance`.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--encryption-type**:
The encryption type of the restored database.
`ENCRYPTION_TYPE` must be one of:

**`customer-managed-encryption`**:
Use the provided Cloud KMS key for encryption. If this option is selected,
kms-key must be set.

**`google-default-encryption`**:
Use Google default encryption.

**`use-config-default-or-backup-encryption`**:
Use the default encryption configuration if one exists, otherwise use the same
encryption configuration as the backup.

**KMS key name group
At most one of these can be specified:

**Key resource - Cloud KMS key(s) to be used to restore the Cloud Spanner
database. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `kms-project` attribute:

- provide the argument `--kms-keys` on the command line with a fully
specified name.

To set the `kms-location` attribute:

- provide the argument `--kms-keys` on the command line with a fully
specified name.

To set the `kms-keyring` attribute:

- provide the argument `--kms-keys` on the command line with a fully
specified name.

**--kms-keys**:
IDs of the keys or fully qualified identifiers for the keys.
To set the `kms-key` attribute:

- provide the argument `--kms-keys` on the command line.**

**--kms-key****

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

: These variants are also available:

```
gcloud alpha spanner databases restore
```

```
gcloud beta spanner databases restore
```