# gcloud bigtable backups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/update](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/update)*

**NAME**

: **gcloud bigtable backups update - update a backup, only supported for the following fields: --expiration-date and --retention-period**

**SYNOPSIS**

: **`gcloud bigtable backups update` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/update#BACKUP)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/update#--cluster)`=`CLUSTER` `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/update#--instance)`=`INSTANCE`) [`[--hot-to-standard-time](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/update#--hot-to-standard-time)`=`HOT_TO_STANDARD_TIME`] [`[--expiration-date](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/update#--expiration-date)`=`EXPIRATION_DATE`     | `[--retention-period](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/update#--retention-period)`=`RETENTION_PERIOD`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a backup, only supported for the following fields: --expiration-date and
--retention-period.

**EXAMPLES**

: To update the expire time of backup 'BACKUP_NAME' to 7 days from now, run:

```
gcloud bigtable backups update BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME --retention-period=7d
```

To update the hot-to-standard time of backup 'BACKUP_NAME' to
'2019-03-31T10:49:41Z', run:

```
gcloud bigtable backups update BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME --hot-to-standard-time=2019-03-31T10:49:41Z
```

To update the hot-to-standard time of backup 'BACKUP_NAME' to 7 days from now,
run:

```
gcloud bigtable backups update BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME --hot-to-standard-time=+P7d
```

To clear the hot-to-standard time of backup 'BACKUP_NAME', run:

```
gcloud bigtable backups update BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME --hot-to-standard-time=''
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Cloud Bigtable backup to update. The arguments in this group
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

**FLAGS**

: **--hot-to-standard-time**:
Time at which a hot backup will be converted to a standard backup; must be at
least 24 hours from backup creation time. Only applies for hot backups. See
`$ [gcloud topic
datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on date/time formats. See `$ [gcloud bigtable backups
describe](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/describe)` for creation time.

**--expiration-date**

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
gcloud alpha bigtable backups update
```

```
gcloud beta bigtable backups update
```