# gcloud sql export sql  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/export/sql](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql)*

**NAME**

: **gcloud sql export sql - exports data from a Cloud SQL instance to a SQL file**

**SYNOPSIS**

: **`gcloud sql export sql` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#INSTANCE)` `[URI](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#URI)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#--async)`] [`[--clean](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#--clean)`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#--database)`=`DATABASE`,[`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#DATABASE)`,…], `[-d](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#-d)` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#DATABASE)`,[`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#DATABASE)`,…]] [`[--if-exists](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#--if-exists)`] [`[--offload](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#--offload)`] [`[--parallel](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#--parallel)`] [`[--table](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#--table)`=`TABLE`,[`[TABLE](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#TABLE)`,…], `[-t](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#-t)` `[TABLE](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#TABLE)`,[`[TABLE](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#TABLE)`,…]] [`[--threads](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#--threads)`=`THREADS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Exports data from a Cloud SQL instance to a Google Cloud Storage bucket as a SQL
dump file.
NOTE: Certain roles and permissions are required to export data to Google Cloud
Storage. For more information on exporting data from Google Cloud SQL see [Export
from Cloud SQL to a SQL dump file](https://cloud.google.com/sql/docs/mysql/import-export/import-export-sql#gcloud).

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

**--clean**:
Include SQL statements (DROP <object>) required to drop database objects
prior to import; corresponds to the clean flag for pg_dump. Only applies to
PostgreSQL non-parallel exports.

**--database**:
Database(s) from which the export is made. Information on requirements can be
found here: [https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances/export#exportContext.databases](https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances/export#exportContext.databases)

**--if-exists**:
Include an SQL statement (IF EXISTS) with each drop statement produced by the
clean flag; corresponds to the if-exists flag for pg_dump. Only applies to
PostgreSQL non-parallel exports.

**--offload**:
Offload an export to a temporary instance. Doing so reduces strain on source
instances and allows other operations to be performed while the export is in
progress.

**--parallel**:
Perform a parallel export. This flag is only applicable to MySQL and Postgres.

**--table**:
Tables to export from the specified database. If you specify tables, specify one
and only one database. For PostgreSQL instances, only one table can be exported
at a time.

**--threads**:
Specifies the number of threads to use for the parallel export. If
`--parallel` is specified and this flag is not provided, Cloud SQL
uses a default thread count to optimize performance.

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
gcloud alpha sql export sql
```

```
gcloud beta sql export sql
```