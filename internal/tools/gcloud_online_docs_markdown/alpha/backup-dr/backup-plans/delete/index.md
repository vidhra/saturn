# gcloud alpha backup-dr backup-plans delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plans/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plans/delete)*

**NAME**

: **gcloud alpha backup-dr backup-plans delete - deletes a Backup Plan**

**SYNOPSIS**

: **`gcloud alpha backup-dr backup-plans delete` (`[BACKUP_PLAN](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plans/delete#BACKUP_PLAN)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plans/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plans/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plans/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Deletes a Backup Plan.

**EXAMPLES**

: To delete a backup plan `sample-backup-plan` in project
`sample-project` and location `us-central1` , run:

```
gcloud alpha backup-dr backup-plans delete sample-backup-plan --project=sample-project --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Backup Plan resource - Name of the backup plan to delete The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `backup_plan` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP_PLAN`**:
ID of the Backup Plan or fully qualified identifier for the Backup Plan.
To set the `name` attribute:

- provide the argument `backup_plan` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Backup Plan.
To set the `location` attribute:

- provide the argument `backup_plan` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

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

**BRIEF**

: Deletes a specific backup plan

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud backup-dr backup-plans delete
```