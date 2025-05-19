# gcloud backup-dr backup-plan-associations delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plan-associations/delete](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plan-associations/delete)*

**NAME**

: **gcloud backup-dr backup-plan-associations delete - delete the specified backup plan association**

**SYNOPSIS**

: **`gcloud backup-dr backup-plan-associations delete` (`[BACKUP_PLAN_ASSOCIATION](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plan-associations/delete#BACKUP_PLAN_ASSOCIATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plan-associations/delete#--location)`=`LOCATION` `[--workload-project](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plan-associations/delete#--workload-project)`=`WORKLOAD_PROJECT`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plan-associations/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plan-associations/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the specified backup plan association.

**EXAMPLES**

: To delete a backup plan association `sample-bpa` in project
`sample-project` and location `us-central1` , run:

```
gcloud backup-dr backup-plan-associations delete sample-bpa --project=sample-project --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Backup Plan Association resource - Name of the backup plan association to
delete. The arguments in this group can be used to specify the attributes of
this resource.
This must be specified.

**`BACKUP_PLAN_ASSOCIATION`**:
ID of the Backup Plan Association or fully qualified identifier for the Backup
Plan Association.
To set the `name` attribute:

- provide the argument `backup_plan_association` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Backup Plan Association.
To set the `location` attribute:

- provide the argument `backup_plan_association` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.

**--workload-project**:
Cloud project id for the Backup Plan Association.
To set the `workload-project` attribute:

- provide the argument `backup_plan_association` on the command line
with a fully specified name;
- provide the argument `--workload-project` on the command line;
- provide the argument `--project` on the command line;
- set the property `core/project`.**

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

: Delete a specific backup plan association

**NOTES**

: This variant is also available:

```
gcloud alpha backup-dr backup-plan-associations delete
```