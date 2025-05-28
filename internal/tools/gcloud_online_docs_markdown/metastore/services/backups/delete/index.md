# gcloud metastore services backups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/delete](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/delete)*

**NAME**

: **gcloud metastore services backups delete - delete a service backup**

**SYNOPSIS**

: **`gcloud metastore services backups delete` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/delete#BACKUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/delete#--location)`=`LOCATION` `[--service](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/delete#--service)`=`SERVICE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a backup.
If run asynchronously with `--async`, exits after printing an
operation name that can be used to poll the status of the deletion via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To delete a backup named `my-backup` from the service
`my-service`, run:

```
gcloud metastore services backups delete my-backup --service=my-service
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Backup to delete. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
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

**--location**:
The location of the Dataproc Metastore service.
If not specified, will use `default` metastore/location.
To set the `location` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `metastore/location`.

**--service**:
The identifier of the Dataproc Metastore service
To set the `service` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--service` on the command line.**

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

**API REFERENCE**

: This command uses the `metastore/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataproc-metastore/docs](https://cloud.google.com/dataproc-metastore/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha metastore services backups delete
```

```
gcloud beta metastore services backups delete
```