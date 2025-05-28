# gcloud spanner backups update-metadata  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/backups/update-metadata](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/update-metadata)*

**NAME**

: **gcloud spanner backups update-metadata - updates the metadata of a Cloud Spanner a backup**

**SYNOPSIS**

: **`gcloud spanner backups update-metadata` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/update-metadata#BACKUP)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/update-metadata#--instance)`=`INSTANCE`) (`[--expiration-date](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/update-metadata#--expiration-date)`=`EXPIRATION_DATE`     | `[--retention-period](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/update-metadata#--retention-period)`=`RETENTION_PERIOD`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/update-metadata#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the metadata of a Cloud Spanner a backup.

**EXAMPLES**

: To update the backup metadata with an exact expiration date, run:

```
gcloud spanner backups update-metadata BACKUP_ID --instance=INSTANCE_NAME --expiration-date=2020-03-29T10:49:41Z
```

To update the backup metadata with a retention period, run:

```
gcloud spanner backups update-metadata BACKUP_ID --instance=INSTANCE_NAME --retention-period=2w
```

**POSITIONAL ARGUMENTS**

: **Backup resource - The Cloud Spanner backup to update. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**--instance**:
The name of the Cloud Spanner instance.
To set the `instance` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

**REQUIRED FLAGS**

: **--expiration-date**

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
gcloud alpha spanner backups update-metadata
```

```
gcloud beta spanner backups update-metadata
```