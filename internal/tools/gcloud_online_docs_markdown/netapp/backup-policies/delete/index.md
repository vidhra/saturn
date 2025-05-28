# gcloud netapp backup-policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/delete](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/delete)*

**NAME**

: **gcloud netapp backup-policies delete - delete a Cloud NetApp Volumes Backup Policy**

**SYNOPSIS**

: **`gcloud netapp backup-policies delete` (`[BACKUP_POLICY](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/delete#BACKUP_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Backup Policy

**EXAMPLES**

: The following command deletes a Backup Policy instance named BACKUP_POLICY in
the default netapp/location

```
gcloud netapp backup-policies delete BACKUP_POLICY
```

To delete a Backup Policy named BACKUP_POLICY asynchronously, run the following
command:

```
gcloud netapp backup-policies delete BACKUP_POLICY --async
```

**POSITIONAL ARGUMENTS**

: **Backup policy resource - The Backup Policy to delete The arguments in this group
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
gcloud beta netapp backup-policies delete
```