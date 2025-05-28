# gcloud metastore services create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/create](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create)*

**NAME**

: **gcloud metastore services create - create a Dataproc Metastore service**

**SYNOPSIS**

: **`gcloud metastore services create` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--async)`] [`[--autoscaling-enabled](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--autoscaling-enabled)`] [`[--data-catalog-sync](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--data-catalog-sync)`] [`[--database-type](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--database-type)`=`DATABASE_TYPE`; default="mysql"] [`[--deletion-protection](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--deletion-protection)`] [`[--encryption-kms-key](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--encryption-kms-key)`=`ENCRYPTION_KMS_KEY`] [`[--endpoint-protocol](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--endpoint-protocol)`=`ENDPOINT_PROTOCOL`; default="thrift"] [`[--hive-metastore-version](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--hive-metastore-version)`=`HIVE_METASTORE_VERSION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--port](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--port)`=`PORT`; default=9083] [`[--release-channel](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--release-channel)`=`RELEASE_CHANNEL`; default="stable"] [`[--auxiliary-versions](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--auxiliary-versions)`=[`AUXILIARY_VERSIONS`,…]     | `[--auxiliary-versions-from-file](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--auxiliary-versions-from-file)`=`AUXILIARY_VERSIONS_FROM_FILE`] [`[--consumer-subnetworks](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--consumer-subnetworks)`=[`CONSUMER_SUBNETWORKS`,…]     | `[--network](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--network)`=`NETWORK`     | `[--network-config-from-file](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--network-config-from-file)`=`NETWORK_CONFIG_FROM_FILE`] [`[--hive-metastore-configs](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--hive-metastore-configs)`=[`KEY`=`VALUE`,…]     | `[--hive-metastore-configs-from-file](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--hive-metastore-configs-from-file)`=`PATH_TO_FILE`] [`[--instance-size](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--instance-size)`=`INSTANCE_SIZE`     | `[--scaling-factor](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--scaling-factor)`=`SCALING_FACTOR`     | `[--tier](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--tier)`=`TIER`     | `[--max-scaling-factor](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--max-scaling-factor)`=`MAX_SCALING_FACTOR` `[--min-scaling-factor](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--min-scaling-factor)`=`MIN_SCALING_FACTOR`] [`[--kerberos-principal](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--kerberos-principal)`=`KERBEROS_PRINCIPAL` `[--keytab](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--keytab)`=`KEYTAB` `[--krb5-config](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--krb5-config)`=`KRB5_CONFIG`] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY` `[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[--scheduled-backup-configs-from-file](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--scheduled-backup-configs-from-file)`=`PATH_TO_FILE`     | `[--enable-scheduled-backup](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--enable-scheduled-backup)` `[--scheduled-backup-cron](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--scheduled-backup-cron)`=`SCHEDULED_BACKUP_CRON` `[--scheduled-backup-location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#--scheduled-backup-location)`=`SCHEDULED_BACKUP_LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Dataproc Metastore service with the given name and configurations.
If run asynchronously with `--async`, exits after printing one
operation name that can be used to poll the status of the creation via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To create a Dataproc Metastore service with the name
`my-metastore-service` in location `us-central` using a
non default port 9090, run:

```
gcloud metastore services create my-metastore-service --location=us-central1 --port=9090
```

To create a Dataproc Metastore service with the name
`my-metastore-service` in location `us-central` using a
non default network foo, run:

```
gcloud metastore services create my-metastore-service --location=us-central1 --network=foo
```

**POSITIONAL ARGUMENTS**

: **Service resource - Arguments and flags that specify the Dataproc Metastore
service you want to create. The arguments in this group can be used to specify
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
A boolean flag to determine whether Dataproc Metastore metadata sync to Data
Catalog should be enabled, false if unspecified. Mutually exclusive with flag
`--encryption-kms-key`.

**--database-type**:
The type of database the Dataproc Metastore service will store data in.
`DATABASE_TYPE` must be one of:

**`mysql`**:
`MYSQL` database type is a Dataproc Metastore service backed by MySQL
CloudSQL.

**`spanner`**:
`SPANNER` database type is a Dataproc Metastore service backed by
Cloud Spanner.

**--deletion-protection**:
Flag that enables delete protection on Dataproc Metastore instance to prevent
accidental deletions of the instance. Use --deletion-protection to enable.

**--encryption-kms-key**

**--endpoint-protocol**:
The protocol to use for the metastore service endpoint. If unspecified, defaults
to `THRIFT`. `ENDPOINT_PROTOCOL` must be one
of:

**`grpc`**:
The modernized `GRPC` protocol.

**`thrift`**:
The legacy Apache `THRIFT` protocol.

**--hive-metastore-version**:
The Hive metastore schema version. The supported versions of a location are
listed via:

```
gcloud metastore locations describe
```

If unspecified, the default version chosen by the server will be used.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--port**:
The TCP port on which the Metastore service will listen. If unspecified, the
default port 9083 will be used.

**--release-channel**:
The release channel of the service. `RELEASE_CHANNEL` must
be one of:

**`canary`**:
The `CANARY` release channel contains the newest features, which may
be unstable and subject to unresolved issues with no known workarounds. Services
using the `CANARY` release channel are not subject to any SLAs.

**`stable`**:
The `STABLE` release channel contains features that are considered
stable and have been validated for production use.

**--auxiliary-versions**

**--consumer-subnetworks**

**--hive-metastore-configs**

**--instance-size**

**--kerberos-principal**

**--maintenance-window-day**

**--scheduled-backup-configs-from-file**

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
gcloud alpha metastore services create
```

```
gcloud beta metastore services create
```