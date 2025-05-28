# gcloud netapp backup-policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update)*

**NAME**

: **gcloud netapp backup-policies update - update a Cloud NetApp Volumes Backup Policies**

**SYNOPSIS**

: **`gcloud netapp backup-policies update` (`[BACKUP_POLICY](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#BACKUP_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--description)`=`DESCRIPTION`] [`[--enabled](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--enabled)`=`ENABLED`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--remove-labels)`=[`KEY`,…]] [`[--daily-backup-limit](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--daily-backup-limit)`=`DAILY_BACKUP_LIMIT` `[--monthly-backup-limit](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--monthly-backup-limit)`=`MONTHLY_BACKUP_LIMIT` `[--weekly-backup-limit](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#--weekly-backup-limit)`=`WEEKLY_BACKUP_LIMIT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a Backup Policy

**EXAMPLES**

: The following command updates a Backup Policy named BACKUP_POLICY with all
possible arguments

```
gcloud netapp backup-policies update BACKUP_POLICY --location=us-central1 --enabled=True --daily-backup-limit=5 --weekly-backup-limit=3 --monthly-backup-limit=2
```

To update a Backup Policy named BACKUP_POLICY asynchronously, run the following
command:

```
gcloud netapp backup-policies update BACKUP_POLICY --async --location=us-central1 --enabled=True --daily-backup-limit=5 --weekly-backup-limit=3 --monthly-backup-limit=2
```

**POSITIONAL ARGUMENTS**

: **Backup policy resource - The Backup Policy to update The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `backup_policy` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP_POLICY`**:
ID of the backup_policy or fully qualified identifier for the backup_policy.
To set the `backup_policy` attribute:

- provide the argument `backup_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the backup_policy.
To set the `location` attribute:

- provide the argument `backup_policy` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description of the Cloud NetApp Backup Policy

**--enabled**:
The Boolean value indiciating whether backups are made automatically according
to the schedules. If enabled, this will be applied to all volumes that have this
backup policy attached and enforced on the volume level. If not specified, the
default is true.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--daily-backup-limit**

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

: This variant is also available:

```
gcloud beta netapp backup-policies update
```