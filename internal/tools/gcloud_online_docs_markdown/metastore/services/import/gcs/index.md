# gcloud metastore services import gcs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs](https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs)*

**NAME**

: **gcloud metastore services import gcs - import metadata into a Dataproc Metastore service from Google Cloud Storage**

**SYNOPSIS**

: **`gcloud metastore services import gcs` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs#--location)`=`LOCATION`) `[--database-dump](https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs#--database-dump)`=`DATABASE_DUMP` `[--import-id](https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs#--import-id)`=`IMPORT_ID` [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs#--description)`=`DESCRIPTION`] [`[--dump-type](https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs#--dump-type)`=`DUMP_TYPE`; default="mysql"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import metadata into a Dataproc Metastore service from Google Cloud Storage.
If run asynchronously with `--async`, exits after printing the
operation name that can be used to poll the status of the export via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To import metadata with the name `my-import` and description
`testing description` into service `my-service` from a
database dump with uri `gs://database-dump` and database type
`mysql`, run:

```
gcloud metastore services import gcs my-service --import-id=my-import --description='testing description' --dump-type=mysql --database-dump=gs://database-dump
```

**POSITIONAL ARGUMENTS**

: **Service resource - Arguments and flags that specify the Dataproc Metastore
service you want to import. The arguments in this group can be used to specify
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

: **--database-dump**:
A Cloud Storage object URI that specifies a database dump from which to import
metadata. It must begin with `gs://`.

**--import-id**:
The ID of this metadata import.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
The description of this metadata import.

**--dump-type**:
The type of the database dump;. If unspecified, defaults to `mysql`.
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
gcloud alpha metastore services import gcs
```

```
gcloud beta metastore services import gcs
```