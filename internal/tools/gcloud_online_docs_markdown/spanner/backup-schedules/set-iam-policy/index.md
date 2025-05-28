# gcloud spanner backup-schedules set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/set-iam-policy)*

**NAME**

: **gcloud spanner backup-schedules set-iam-policy - set the IAM policy for a Cloud Spanner backup schedule**

**SYNOPSIS**

: **`gcloud spanner backup-schedules set-iam-policy` (`[BACKUP_SCHEDULE](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/set-iam-policy#BACKUP_SCHEDULE)` : `[--database](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/set-iam-policy#--database)`=`DATABASE` `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/set-iam-policy#--instance)`=`INSTANCE`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Set the IAM policy for a Cloud Spanner backup schedule given a backup schedule
ID and a file encoded in JSON or YAML that contains the IAM policy.

**EXAMPLES**

: The following command reads an IAM policy defined in a JSON file
`policy.json` and sets it for a Cloud Spanner backup schedule:

```
gcloud spanner backup-schedules set-iam-policy backup-schedule-id --instance=instance-id --database=database-id policy.json
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**POSITIONAL ARGUMENTS**

: **BackupSchedule resource - The Cloud Spanner backup schedule to set the IAM
policy for. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `backup_schedule` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP_SCHEDULE`**:
ID of the backupSchedule or fully qualified identifier for the backupSchedule.
To set the `backup_schedule` attribute:

- provide the argument `backup_schedule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--database**:
The name of the Cloud Spanner database.
To set the `database` attribute:

- provide the argument `backup_schedule` on the command line with a
fully specified name;
- provide the argument `--database` on the command line.

**--instance**:
The name of the Cloud Spanner instance.
To set the `instance` attribute:

- provide the argument `backup_schedule` on the command line with a
fully specified name;
- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

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

: This command uses the `spanner/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/spanner/](https://cloud.google.com/spanner/)

**NOTES**

: These variants are also available:

```
gcloud alpha spanner backup-schedules set-iam-policy
```

```
gcloud beta spanner backup-schedules set-iam-policy
```