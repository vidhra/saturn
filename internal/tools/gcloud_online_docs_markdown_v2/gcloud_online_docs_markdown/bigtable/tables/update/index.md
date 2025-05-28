# gcloud bigtable tables update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update)*

**NAME**

: **gcloud bigtable tables update - update an existing Cloud Bigtable table**

**SYNOPSIS**

: **`gcloud bigtable tables update` (`[TABLE](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#TABLE)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--instance)`=`INSTANCE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--async)`] [`[--deletion-protection](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--deletion-protection)`] [`[--row-key-schema-pre-encoded-bytes](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--row-key-schema-pre-encoded-bytes)`] [`[--automated-backup-retention-period](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--automated-backup-retention-period)`=`AUTOMATED_BACKUP_RETENTION_PERIOD`     | `[--disable-automated-backup](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--disable-automated-backup)`     | `[--enable-automated-backup](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--enable-automated-backup)`] [`[--change-stream-retention-period](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--change-stream-retention-period)`=`CHANGE_STREAM_RETENTION_PERIOD`     | `[--clear-change-stream-retention-period](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--clear-change-stream-retention-period)`] [`[--clear-row-key-schema](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--clear-row-key-schema)`     | `[--row-key-schema-definition-file](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#--row-key-schema-definition-file)`=`ROW_KEY_SCHEMA_DEFINITION_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/tables/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing new Cloud Bigtable table with the specified configuration.

**EXAMPLES**

: To enable deletion protection, run:

```
gcloud bigtable tables update my-table --instance=my-instance --deletion-protection
```

To disable deletion protection, run:

```
gcloud bigtable tables update my-table --instance=my-instance --no-deletion-protection
```

To enable a change stream with a retention period of 1 day, or to update your
table's change stream retention period to 1 day, run:

```
gcloud bigtable tables update my-table --instance=my-instance --change-stream-retention-period=1d
```

To disable a change stream, run:

```
gcloud bigtable tables update my-table --instance=my-instance --clear-change-stream-retention-period
```

To enable the default automated backup policy on a table, or update a table to
use the default policy (retention_period=7d, frequency=1d), run:

```
gcloud bigtable tables update my-table --instance=my-instance --enable-automated-backup
```

To disable automated backup: run:

```
gcloud bigtable tables update my-table --instance=my-instance --disable-automated-backup
```

To enable or update a custom automated backup policy and configure it to retain
backups for 30 days, run:

```
gcloud bigtable tables update my-table --instance=my-instance --automated-backup-retention_period=30d
```

**POSITIONAL ARGUMENTS**

: **Table resource - Cloud Bigtable table to update. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `table` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TABLE`**:
ID of the table or fully qualified identifier for the table.
To set the `table` attribute:

- provide the argument `table` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Name of the Cloud Bigtable instance.
To set the `instance` attribute:

- provide the argument `table` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--deletion-protection**:
Once specified, the table is deletion protected.

**--row-key-schema-pre-encoded-bytes**:
By default, Base64 encoding is applied to all binary fields in the YAML/JSON
file (for example, `encoding.delimitedBytes.delimiter`).
Use this to indicate that all binary fields are already encoded in the YAML/JSON
file and should not be encoded again.
This field is only used when `row-key-schema-definition-file` is set.
It is ignored if `clear-row-key-schema` is set.

**--automated-backup-retention-period**

**--change-stream-retention-period**

**--clear-row-key-schema**

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
gcloud alpha bigtable tables update
```

```
gcloud beta bigtable tables update
```