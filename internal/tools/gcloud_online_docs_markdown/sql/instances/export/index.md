# gcloud sql instances export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/export](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export)*

**NAME**

: **gcloud sql instances export - exports data from a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql instances export` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#INSTANCE)` `[URI](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#URI)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#--async)`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#--database)`=`DATABASE`,[`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#DATABASE)`,…], `[-d](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#-d)` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#DATABASE)`,[`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#DATABASE)`,…]] [`[--table](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#--table)`=`TABLE`,[`[TABLE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#TABLE)`,…], `[-t](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#-t)` `[TABLE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#TABLE)`,[`[TABLE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#TABLE)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Exports data from a Cloud SQL instance.
This command is deprecated and will be removed in version 205.0.0. Use `[gcloud sql export sql](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql)`
instead.
Exports data from a Cloud SQL instance to a Google Cloud Storage bucket as a
MySQL dump file.

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**`URI`**:
The path to the file in Google Cloud Storage where the export will be stored.
The URI is in the form gs://bucketName/fileName. If the file already exists, the
operation fails. If the filename ends with .gz, the contents are compressed.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--database**:
Database(s) from which the export is made. Information on requirements can be
found here: [https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances/export#exportContext.databases](https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances/export#exportContext.databases)

**--table**:
Tables to export from the specified database. If you specify tables, specify one
and only one database. For Postgres instances, only one table can be exported at
a time.

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
gcloud alpha sql instances export
```

```
gcloud beta sql instances export
```