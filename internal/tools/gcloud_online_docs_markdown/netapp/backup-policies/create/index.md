# gcloud netapp backup-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create)*

**NAME**

: **gcloud netapp backup-policies create - create a Cloud NetApp Backup Policy**

**SYNOPSIS**

: **`gcloud netapp backup-policies create` (`[BACKUP_POLICY](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#BACKUP_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#--description)`=`DESCRIPTION`] [`[--enabled](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#--enabled)`=`ENABLED`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--daily-backup-limit](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#--daily-backup-limit)`=`DAILY_BACKUP_LIMIT` `[--monthly-backup-limit](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#--monthly-backup-limit)`=`MONTHLY_BACKUP_LIMIT` `[--weekly-backup-limit](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#--weekly-backup-limit)`=`WEEKLY_BACKUP_LIMIT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a Backup Policy for Cloud NetApp Volumes.

**EXAMPLES**

: The following command creates a Backup Policy named BACKUP_POLICY with all
possible arguments:

```
gcloud netapp backup-policies create BACKUP_POLICY --location=us-central1 --enabled=true --daily-backup-limit=3 --weekly-backup-limit=5 --monthly-backup-limit=2 --description="first backup policy" --labels=key1=val1
```

**POSITIONAL ARGUMENTS**

: **Backup policy resource - The Backup Policy to create The arguments in this group
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

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud beta netapp backup-policies create
```