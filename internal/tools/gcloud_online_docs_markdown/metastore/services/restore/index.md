# gcloud metastore services restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore](https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore)*

**NAME**

: **gcloud metastore services restore - restore a Dataproc Metastore service**

**SYNOPSIS**

: **`gcloud metastore services restore` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore#--location)`=`LOCATION`) (`[--backup](https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore#--backup)`=`BACKUP`     | `[--backup-location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore#--backup-location)`=`BACKUP_LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore#--async)`] [`[--restore-type](https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore#--restore-type)`=`RESTORE_TYPE`; default="metadata-only"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Restore a Dataproc Metastore service from the given backup or backup-location
If run asynchronously with `--async`, exits after printing an
operation name that can be used to poll the status of the creation via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To restore a Dataproc Metastore service with the name `my-service`
from the backup `my-backup` with a `FULL` restore type,
run:

```
gcloud metastore services restore my-service --backup=my-backup --restore-type=full
```

To restore a Dataproc Metastore service with the name `my-service`
from the backup-location `gs://gcs_bucket` with a `FULL`
restore type, run:

```
gcloud metastore services restore my-service --backup-location=gs://gcs_bucket --restore-type=full
```

**POSITIONAL ARGUMENTS**

: **Service resource - Arguments and flags that specify the Dataproc Metastore
service you want to restore. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `service` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataproc Metastore service.
If not specified, will use `default` metastore/location.
To set the `location` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `metastore/location`.**

**REQUIRED FLAGS**

: **--backup**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--restore-type**:
The type of restore to perform. `RESTORE_TYPE` must be one
of:

**`full`**:
The service's metadata and configuration are restored.

**`metadata-only`**:
Only the service's metadata is restored.

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
gcloud alpha metastore services restore
```

```
gcloud beta metastore services restore
```