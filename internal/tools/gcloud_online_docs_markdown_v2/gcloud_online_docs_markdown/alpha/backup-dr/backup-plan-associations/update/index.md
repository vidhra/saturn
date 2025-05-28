# gcloud alpha backup-dr backup-plan-associations update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/update](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/update)*

**NAME**

: **gcloud alpha backup-dr backup-plan-associations update - update a specific backup plan within a backup plan association**

**SYNOPSIS**

: **`gcloud alpha backup-dr backup-plan-associations update` (`[BACKUP_PLAN_ASSOCIATION](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/update#BACKUP_PLAN_ASSOCIATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/update#--location)`=`LOCATION` `[--workload-project](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/update#--workload-project)`=`WORKLOAD_PROJECT`) `[--backup-plan](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/update#--backup-plan)`=`BACKUP_PLAN` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a specific backup plan within a backup plan
association.

**EXAMPLES**

: To update backup plan association `sample-bpa` in project
`sample-project` and location `us-central1` with backup
plan `sample-backup-plan` in the same project and location, run:

```
gcloud alpha backup-dr backup-plan-associations update sample-bpa --project=sample-project --location=us-central1 --backup-plan=sample-backup-plan
```

To update backup plan association `sample-bpa-uri` with backup plan
`sample-backup-plan-uri` (using full URIs), run:

```
gcloud alpha backup-dr backup-plan-associations update sample-bpa-uri --backup-plan=sample-backup-plan-uri
```

To update backup plan association `sample-bpa` in location
`us-central1` with backup plan `sample-backup-plan-uri`,
run:

```
gcloud alpha backup-dr backup-plan-associations update sample-bpa --location=us-central1 --backup-plan=sample-backup-plan-uri
```

To update backup plan association `sample-bpa` in project
`workload-project` and location `us-central1` with backup
plan `sample-backup-plan` in project `sample-project`,
run:

```
gcloud alpha backup-dr backup-plan-associations update sample-bpa --workload-project=workload-project --location=us-central1 --backup-plan=sample-backup-plan --project=sample-project
```

**POSITIONAL ARGUMENTS**

: **Backup Plan Association resource - Backup plan association to be updated. To
update backup plan associations in a project that's different from the backup
plan, use the --workload-project flag. The arguments in this group can be used
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

: **Backup Plan resource - Name of the specific backup plan to be applied to the
backup plan association. E.g.,
projects/sample-project/locations/us-central1/backupPlans/sample-backup-plan
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--backup-plan` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--backup-plan` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

This must be specified.

**--backup-plan**:
ID of the Backup Plan or fully qualified identifier for the Backup Plan.
To set the `name` attribute:

- provide the argument `--backup-plan` on the command line.**

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

: Update a specific backup plan within a backup plan association.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.