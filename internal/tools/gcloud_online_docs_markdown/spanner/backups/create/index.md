# gcloud spanner backups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create)*

**NAME**

: **gcloud spanner backups create - creates a backup of a Cloud Spanner database**

**SYNOPSIS**

: **`gcloud spanner backups create` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#BACKUP)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--instance)`=`INSTANCE`) `[--database](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--database)`=`DATABASE` (`[--expiration-date](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--expiration-date)`=`EXPIRATION_DATE`     | `[--retention-period](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--retention-period)`=`RETENTION_PERIOD`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--async)`] [`[--version-time](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--version-time)`=`TIMESTAMP`] [`[--encryption-type](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--encryption-type)`=`ENCRYPTION_TYPE` `[--kms-keys](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--kms-keys)`=[`KMS_KEYS`,…]     | [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#--kms-project)`=`KMS_PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a backup of a Cloud Spanner database.

**EXAMPLES**

: To create a backup asynchronously, run:

```
gcloud spanner backups create BACKUP_ID --instance=INSTANCE_NAME --database=DATABASE --expiration-date=2020-03-29T10:49:41Z --async
```

To create a backup synchronously, run:

```
gcloud spanner backups create BACKUP_ID --instance=INSTANCE_NAME --database=DATABASE --retention-period=2w
```

**POSITIONAL ARGUMENTS**

: **Backup resource - The Cloud Spanner backup to create. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**--instance**:
The Cloud Spanner instance for the backup.
To set the `instance` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

**REQUIRED FLAGS**

: **--database**:
ID of the database from which the backup will be created.

**--expiration-date**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--version-time**:
The backup will contain an externally consistent copy of the database at the
timestamp specified by `--version-time`. If
`--version-time` is not specified, the system will use the creation
time of the backup.

**--encryption-type**:
The encryption type of the backup. `ENCRYPTION_TYPE` must
be one of:

**`customer-managed-encryption`**:
Use the provided Cloud KMS key for encryption. If this option is selected,
kms-key must be set.

**`google-default-encryption`**:
Use Google default encryption.

**`use-database-encryption`**:
Use the same encryption configuration as the database.

**KMS key name group
At most one of these can be specified:

**Key resource - Cloud KMS key(s) to be used to create the Cloud Spanner backup.
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
gcloud alpha spanner backups create
```

```
gcloud beta spanner backups create
```