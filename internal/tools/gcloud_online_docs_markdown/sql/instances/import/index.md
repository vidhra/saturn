# gcloud sql instances import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/import](https://cloud.google.com/sdk/gcloud/reference/sql/instances/import)*

**NAME**

: **gcloud sql instances import - imports data into a Cloud SQL instance from Google Cloud Storage**

**SYNOPSIS**

: **`gcloud sql instances import` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/import#INSTANCE)` `[URI](https://cloud.google.com/sdk/gcloud/reference/sql/instances/import#URI)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/import#--async)`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/sql/instances/import#--database)`=`DATABASE`, `[-d](https://cloud.google.com/sdk/gcloud/reference/sql/instances/import#-d)` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/import#DATABASE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Imports data into a Cloud SQL instance from Google
Cloud Storage.
This command is deprecated and will be removed in version 205.0.0. Use `[gcloud sql import sql](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql)`
instead.
Note: authorization is required. For more information on importing data into
Google Cloud SQL see [https://cloud.google.com/sql/docs/import-export/importing](https://cloud.google.com/sql/docs/import-export/importing).
Cloud SQL supports importing CSV files and SQL dump files from both MySQL and
PostgreSQL. For more information on how to create these export formats, see [https://cloud.google.com/sql/docs/mysql/import-export/creating-sqldump-csv](https://cloud.google.com/sql/docs/mysql/import-export/creating-sqldump-csv)

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**`URI`**:
Path to the MySQL dump file in Google Cloud Storage from which the import is
made. The URI is in the form gs://bucketName/fileName. Compressed gzip files
(.gz) are also supported.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--database**:
Database to which the import is made. The database needs to be created before
importing. If not set, it is assumed that the database is specified in the file
to be imported. If your SQL dump file includes a database statement, it will
override the database set in this flag.

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

**NOTES**

: These variants are also available:

```
gcloud alpha sql instances import
```

```
gcloud beta sql instances import
```