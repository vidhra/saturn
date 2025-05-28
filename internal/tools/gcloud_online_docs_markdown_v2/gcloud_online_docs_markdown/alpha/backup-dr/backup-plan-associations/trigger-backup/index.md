# gcloud alpha backup-dr backup-plan-associations trigger-backup  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/trigger-backup](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/trigger-backup)*

**NAME**

: **gcloud alpha backup-dr backup-plan-associations trigger-backup - create an on-demand backup for a resource**

**SYNOPSIS**

: **`gcloud alpha backup-dr backup-plan-associations trigger-backup` (`[BACKUP_PLAN_ASSOCIATION](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/trigger-backup#BACKUP_PLAN_ASSOCIATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/trigger-backup#--location)`=`LOCATION` `[--workload-project](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/trigger-backup#--workload-project)`=`WORKLOAD_PROJECT`) `[--backup-rule-id](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/trigger-backup#--backup-rule-id)`=`BACKUP_RULE_ID` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/trigger-backup#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/trigger-backup#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create an on-demand backup for a resource. Trigger an on
demand backup for the given backup rule.

**EXAMPLES**

: To trigger an on demand backup for a backup plan association
`sample-bpa` in project `sample-project` and location
`us-central1` with backup rule `sample-backup-rule`, run:

```
gcloud alpha backup-dr backup-plan-associations trigger-backup sample-bpa --project=sample-project --location=us-central1 --backup-rule-id=sample-backup-rule
```

**POSITIONAL ARGUMENTS**

: **Backup Plan Association resource - Name of an existing backup plan association
to use for creating an on-demand backup. The arguments in this group can be used
to specify the attributes of this resource.
This must be specified.

**`BACKUP_PLAN_ASSOCIATION`**:
ID of the Backup Plan Association or fully qualified identifier for the Backup
Plan Association.
To set the `name` attribute:

- provide the argument `BACKUP_PLAN_ASSOCIATION` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Backup Plan Association.
To set the `location` attribute:

- provide the argument `BACKUP_PLAN_ASSOCIATION` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.

**--workload-project**:
Cloud project id for the Backup Plan Association.
To set the `workload-project` attribute:

- provide the argument `BACKUP_PLAN_ASSOCIATION` on the command line
with a fully specified name;
- provide the argument `--workload-project` on the command line;
- provide the argument `--project` on the command line;
- set the property `core/project`.**

**REQUIRED FLAGS**

: **--backup-rule-id**:
Name of an existing backup rule to use for creating an on-demand backup.

**OPTIONAL FLAGS**

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

: Create an on-demand backup.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud backup-dr backup-plan-associations trigger-backup
```