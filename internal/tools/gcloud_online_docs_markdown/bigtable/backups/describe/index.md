# gcloud bigtable backups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/describe](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/describe)*

**NAME**

: **gcloud bigtable backups describe - retrieves information about a backup**

**SYNOPSIS**

: **`gcloud bigtable backups describe` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/describe#BACKUP)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/describe#--cluster)`=`CLUSTER` `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/describe#--instance)`=`INSTANCE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieves information about a backup.

**EXAMPLES**

: To describe a backup, run:

```
gcloud bigtable backups describe BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Cloud Bigtable backup to describe. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP`**:
ID of the backup or fully qualified identifier for the backup.
To set the `backup` attribute:

- provide the argument `backup` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
Name of the Cloud Bigtable cluster.
To set the `cluster` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line.

**--instance**:
Name of the Cloud Bigtable instance.
To set the `instance` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.**

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

: This command uses the `bigtableadmin/v2` API. The full documentation
for this API can be found at: [https://cloud.google.com/bigtable/](https://cloud.google.com/bigtable/)

**NOTES**

: These variants are also available:

```
gcloud alpha bigtable backups describe
```

```
gcloud beta bigtable backups describe
```