# gcloud spanner backup-schedules delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/delete](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/delete)*

**NAME**

: **gcloud spanner backup-schedules delete - delete a Cloud Spanner backup schedule**

**SYNOPSIS**

: **`gcloud spanner backup-schedules delete` (`[BACKUP_SCHEDULE](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/delete#BACKUP_SCHEDULE)` : `[--database](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/delete#--database)`=`DATABASE` `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/delete#--instance)`=`INSTANCE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Cloud Spanner backup schedule.

**EXAMPLES**

: To delete a Cloud Spanner backup schedule, run:

```
gcloud spanner backup-schedules delete backup-schedule-id --instance=instance-id --database=database-id
```

**POSITIONAL ARGUMENTS**

: **Backup schedule resource - The Cloud Spanner backup schedule to delete. The
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
gcloud alpha spanner backup-schedules delete
```

```
gcloud beta spanner backup-schedules delete
```