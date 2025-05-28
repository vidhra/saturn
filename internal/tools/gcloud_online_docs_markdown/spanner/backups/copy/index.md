# gcloud spanner backups copy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy)*

**NAME**

: **gcloud spanner backups copy - copies a backup of a Cloud Spanner database**

**SYNOPSIS**

: **`gcloud spanner backups copy` (`[--destination-backup](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--destination-backup)`=`DESTINATION_BACKUP` : `[--destination-instance](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--destination-instance)`=`DESTINATION_INSTANCE`) (`[--expiration-date](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--expiration-date)`=`EXPIRATION_DATE`     | `[--retention-period](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--retention-period)`=`RETENTION_PERIOD`) (`[--source-backup](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--source-backup)`=`SOURCE_BACKUP` : `[--source-instance](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--source-instance)`=`SOURCE_INSTANCE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--async)`] [`[--encryption-type](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--encryption-type)`=`ENCRYPTION_TYPE` `[--kms-keys](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--kms-keys)`=[`KMS_KEYS`,…]     | [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#--kms-project)`=`KMS_PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/copy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Copies a backup of a Cloud Spanner database.

**EXAMPLES**

: To copy a backup within the same project, run:

```
gcloud spanner backups copy --source-instance=SOURCE_INSTANCE_ID --source-backup=SOURCE_BACKUP_ID --destination-instance=DESTINATION_INSTANCE_ID --destination-backup=DESTINATION_BACKUP_ID --expiration-date=2020-03-29T10:49:41Z
```

To copy a backup to a different project, run:

```
gcloud spanner backups copy --source-backup=projects/SOURCE_PROJECT_ID/instances/SOURCE_INSTANCE_ID/backups/SOURCE_BACKUP_ID --destination-backup=projects/DESTINATION_PROJECT_ID/instances/DESTINATION_INSTANCE_ID/backups/DESTINATION_BACKUP_ID --expiration-date=2020-03-29T10:49:41Z
```

**REQUIRED FLAGS**

: **Backup resource - TEXT The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--destination-backup` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--destination-backup**:
ID of the backup or fully qualified identifier for the backup.
To set the `backup` attribute:

- provide the argument `--destination-backup` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--destination-instance**:
The Cloud Spanner instance for the backup.
To set the `instance` attribute:

- provide the argument `--destination-backup` on the command line with
a fully specified name;
- provide the argument `--destination-instance` on the command line;
- set the property `spanner/instance`.**

**--expiration-date**

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
The encryption type of the copied backup.
`ENCRYPTION_TYPE` must be one of:

**`customer-managed-encryption`**:
Use the provided Cloud KMS key for encryption. If this option is selected,
kms-key must be set.

**`google-default-encryption`**:
Use Google default encryption.

**`use-config-default-or-backup-encryption`**:
Use the default encryption configuration if one exists. otherwise use the same
encryption configuration as the source backup.

**KMS key name group
At most one of these can be specified:

**Key resource - Cloud KMS key(s) to be used to copy the Cloud Spanner backup.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
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
gcloud alpha spanner backups copy
```

```
gcloud beta spanner backups copy
```