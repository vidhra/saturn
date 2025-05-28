# gcloud spanner backup-schedules update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update)*

**NAME**

: **gcloud spanner backup-schedules update - update a Cloud Spanner backup schedule**

**SYNOPSIS**

: **`gcloud spanner backup-schedules update` (`[BACKUP_SCHEDULE](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#BACKUP_SCHEDULE)` : `[--database](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--database)`=`DATABASE` `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--instance)`=`INSTANCE`) (`[--cron](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--cron)`=`CRON` `[--encryption-type](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--encryption-type)`=`ENCRYPTION_TYPE` `[--retention-duration](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--retention-duration)`=`RETENTION_DURATION` `[--kms-keys](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--kms-keys)`=[`KMS_KEYS`,…]     | [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#--kms-project)`=`KMS_PROJECT`]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Spanner backup schedule.

**EXAMPLES**

: To update a Cloud Spanner backup schedule, run:

```
gcloud spanner backup-schedules update backup-schedule-id --instance=instance-id --database=database-id --cron="0 2 * * *" --retention-duration=2w --encryption-type=GOOGLE_DEFAULT_ENCRYPTION
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

: **--cron**

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
gcloud alpha spanner backup-schedules update
```

```
gcloud beta spanner backup-schedules update
```