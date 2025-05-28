# gcloud spanner backup-schedules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create)*

**NAME**

: **gcloud spanner backup-schedules create - create a Cloud Spanner backup schedule**

**SYNOPSIS**

: **`gcloud spanner backup-schedules create` (`[BACKUP_SCHEDULE](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#BACKUP_SCHEDULE)` : `[--database](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--database)`=`DATABASE` `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--instance)`=`INSTANCE`) `[--backup-type](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--backup-type)`=[`BACKUP_TYPE`] `[--cron](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--cron)`=`CRON` `[--retention-duration](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--retention-duration)`=`RETENTION_DURATION` [`[--encryption-type](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--encryption-type)`=`ENCRYPTION_TYPE` `[--kms-keys](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--kms-keys)`=[`KMS_KEYS`,…]     | [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#--kms-project)`=`KMS_PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Spanner backup schedule.

**EXAMPLES**

: To create a Cloud Spanner backup schedule, run:

```
gcloud spanner backup-schedules create backup-schedule-id --instance=instance-id --database=database-id --cron="0 2 * * *" --retention-duration=2w --backup-type=full-backup
```

**POSITIONAL ARGUMENTS**

: **Backup schedule resource - The Cloud Spanner backup schedule to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `backup_schedule` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP_SCHEDULE`**:
ID of the backup-schedule or fully qualified identifier for the backup-schedule.
To set the `backup-schedule` attribute:

- provide the argument `backup_schedule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--database**:
The Cloud Spanner database for the backup-schedule.
To set the `database` attribute:

- provide the argument `backup_schedule` on the command line with a
fully specified name;
- provide the argument `--database` on the command line.

**--instance**:
The Cloud Spanner instance for the backup-schedule.
To set the `instance` attribute:

- provide the argument `backup_schedule` on the command line with a
fully specified name;
- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

**REQUIRED FLAGS**

: **--backup-type**:
Type of backups created by this schedule.
Supported backup types:
`full-backup` A full backup stores the entire contents of the
database at a given version time.
`incremental-backup` An incremental backup contains only the data
that has changed since a previous backup.
`BACKUP_TYPE` must be one of: `full-backup`,
`incremental-backup`.

**--cron**:
Textual representation of the crontab. User can customize the backup frequency
and the backup version time using the cron expression. The version time must be
in UTC timzeone. The backup will contain an externally consistent copy of the
database at the version time. Allowed frequencies are 12 hour, 1 day, 1 week and
1 month. Examples of valid cron specifications: * `0 2/12 * * *` :
every 12 hours at (2, 14) hours past midnight in UTC. * `0 2,14 * * *` : every 12 hours at (2,14) hours past midnight in UTC. * `0 2 * * *` : once a day at 2 past midnight in UTC. * `0 2 * * 0` : once
a week every Sunday at 2 past midnight in UTC. * `0 2 8 * *` : once
a month on 8th day at 2 past midnight in UTC.

**--retention-duration**:
The retention duration of a backup that must be at least 6 hours and at most 366
days. The backup is eligible to be automatically deleted once the retention
period has elapsed.

**OPTIONAL FLAGS**

: **--encryption-type**:
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
gcloud alpha spanner backup-schedules create
```

```
gcloud beta spanner backup-schedules create
```