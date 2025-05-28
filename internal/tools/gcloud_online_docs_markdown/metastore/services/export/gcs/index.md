# gcloud metastore services export gcs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs](https://cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs)*

**NAME**

: **gcloud metastore services export gcs - export metadata from a Dataproc Metastore service to Google Cloud Storage**

**SYNOPSIS**

: **`gcloud metastore services export gcs` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs#--location)`=`LOCATION`) `[--destination-folder](https://cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs#--destination-folder)`=`DESTINATION_FOLDER` [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs#--async)`] [`[--dump-type](https://cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs#--dump-type)`=`DUMP_TYPE`; default="mysql"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export metadata from a Dataproc Metastore service to Google Cloud Storage.
If run asynchronously with `--async`, exits after printing the
operation name that can be used to poll the status of the export via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To export metadata from a Dataproc Metastore service with the name
`my-metastore-service` in location `us-central1` to the
destination folder `gs://my-bucket/destination-folder`, run:

```
gcloud metastore services export gcs my-metastore-service --location=us-central1 --destination-folder=gs://my-bucket/destination-folder
```

**POSITIONAL ARGUMENTS**

: **Service resource - Arguments and flags that specify the Dataproc Metastore
service you want to export. The arguments in this group can be used to specify
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

: **--destination-folder**:
A Cloud Storage URI of a folder that metadata is exported to, in the format
`gs://<bucket_name>/<path_inside_bukcet>`. A sub-folder
containing exported files will be created below it.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--dump-type**:
The type of the database dump. If unspecified, defaults to `mysql`.
`DUMP_TYPE` must be one of:

**`avro`**:
Database dump contains AVRO files.

**`mysql`**:
Database dump is a MYSQL dump file.

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
gcloud alpha metastore services export gcs
```

```
gcloud beta metastore services export gcs
```