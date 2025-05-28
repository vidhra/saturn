# gcloud metastore services update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/update](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update)*

**NAME**

: **gcloud metastore services update - update a Dataproc Metastore service**

**SYNOPSIS**

: **`gcloud metastore services update` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--async)`] [`[--autoscaling-enabled](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--autoscaling-enabled)`] [`[--data-catalog-sync](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--data-catalog-sync)`] [`[--deletion-protection](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--deletion-protection)`] [`[--endpoint-protocol](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--endpoint-protocol)`=`ENDPOINT_PROTOCOL`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--port)`=`PORT`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--remove-labels)`=[`KEY`,…]] [`[--instance-size](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--instance-size)`=`INSTANCE_SIZE`     | `[--scaling-factor](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--scaling-factor)`=`SCALING_FACTOR`     | `[--tier](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--tier)`=`TIER`     | `[--max-scaling-factor](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--max-scaling-factor)`=`MAX_SCALING_FACTOR` `[--min-scaling-factor](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--min-scaling-factor)`=`MIN_SCALING_FACTOR`] [`[--kerberos-principal](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--kerberos-principal)`=`KERBEROS_PRINCIPAL` `[--keytab](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--keytab)`=`KEYTAB` `[--krb5-config](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--krb5-config)`=`KRB5_CONFIG`] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY` `[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[--scheduled-backup-configs-from-file](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--scheduled-backup-configs-from-file)`=`PATH_TO_FILE`     | `[--enable-scheduled-backup](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--enable-scheduled-backup)` `[--scheduled-backup-cron](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--scheduled-backup-cron)`=`SCHEDULED_BACKUP_CRON` `[--scheduled-backup-location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--scheduled-backup-location)`=`SCHEDULED_BACKUP_LOCATION`] [`[--update-auxiliary-versions-from-file](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--update-auxiliary-versions-from-file)`=`UPDATE_AUXILIARY_VERSIONS_FROM_FILE`     | `[--add-auxiliary-versions](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--add-auxiliary-versions)`=[`ADD_AUXILIARY_VERSIONS`,…] `[--clear-auxiliary-versions](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--clear-auxiliary-versions)`] [`[--update-hive-metastore-configs-from-file](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--update-hive-metastore-configs-from-file)`=`PATH_TO_FILE`     | `[--update-hive-metastore-configs](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--update-hive-metastore-configs)`=[`KEY`=`VALUE`,…] `[--clear-hive-metastore-configs](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--clear-hive-metastore-configs)`     | `[--remove-hive-metastore-configs](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#--remove-hive-metastore-configs)`=[`REMOVE_HIVE_METASTORE_CONFIGS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the metadata and/or configuration parameters of a Dataproc Metastore
service.
If run asynchronously with `--async`, exits after printing one
operation name that can be used to poll the status of the update via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To update a Dataproc Metastore service with the name
`my-metastore-service` to have the port number 8080, and add the two
labels, `env` and `foo`, run:

```
gcloud metastore services update my-metastore-service --port=8080 --update-labels=env=test,foo=bar
```

**POSITIONAL ARGUMENTS**

: **Service resource - Arguments and flags that specify the Dataproc Metastore
service you want to update. The arguments in this group can be used to specify
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--autoscaling-enabled**:
A boolean flag to determine whether Dataproc Metastore autoscaling should be
enabled, false if unspecified.
The default minimum and maximum scaling factors are 0.1 and 6.0, respectively.
The minimum and maximum scaling factors can be specified using
--min-scaling-factor and --max-scaling-factor.

**--data-catalog-sync**:
Boolean flag to determine whether or not Dataproc Metastore metadata sync to
Data Catalog is enabled, false if unspecified. Mutually exclusive with flag
`--encryption-kms-key`. Cannot be updated if the service uses
customer-managed encryption keys.

**--deletion-protection**:
Flag that enables delete protection on Dataproc Metastore instance to prevent
accidental deletions of the instance. Use --deletion-protection to enable and
--no-deletion-protection to disable.

**--endpoint-protocol**:
The protocol to use for the metastore service endpoint.
`ENDPOINT_PROTOCOL` must be one of:

**`grpc`**:
The modernized `GRPC` protocol.

**`thrift`**:
The legacy Apache `THRIFT` protocol.

**--port**:
The TCP port on which the Metastore service will listen.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--instance-size**

**--kerberos-principal**

**--maintenance-window-day**

**--scheduled-backup-configs-from-file**

**--update-auxiliary-versions-from-file**

**--update-hive-metastore-configs-from-file**

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
gcloud alpha metastore services update
```

```
gcloud beta metastore services update
```