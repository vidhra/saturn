# gcloud sql import sql  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/import/sql](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql)*

**NAME**

: **gcloud sql import sql - imports data into a Cloud SQL instance from a SQL dump file**

**SYNOPSIS**

: **`gcloud sql import sql` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#INSTANCE)` `[URI](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#URI)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#--async)`] [`[--clean](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#--clean)`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#--database)`=`DATABASE`, `[-d](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#-d)` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#DATABASE)`] [`[--if-exists](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#--if-exists)`] [`[--parallel](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#--parallel)`] [`[--threads](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#--threads)`=`THREADS`] [`[--user](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#--user)`=`USER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/import/sql#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud sql import sql imports data into a Cloud SQL instance from a SQL dump
file in Google Cloud Storage.
NOTE: Certain roles and permissions are required to import data into Google
Cloud SQL. For more information on importing data into Google Cloud SQL see [Import
a SQL dump file](https://cloud.google.com/sql/docs/mysql/import-export/import-export-sql#gcloud_1).
For detailed help on importing data into Cloud SQL, refer to this guide: [https://cloud.google.com/sql/docs/mysql/import-export/importing](https://cloud.google.com/sql/docs/mysql/import-export/importing)

**EXAMPLES**

: To import data from a SQL dump file into a database, `testdb`, on the
specified Cloud SQL instance `test-instance-1`, run:

```
gcloud sql import sql test-instance-1 gs://test-bucket/test-file.sql.gz --database=testdb
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**`URI`**:
Path to the MySQL dump file in Google Cloud Storage from which the import is
made. The URI is in the form `gs://bucketName/fileName`. Compressed
gzip files (.gz) are also supported.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--clean**:
Option to clean (DROP) database objects before recreating them. corresponds to
the clean flag for pg_restore. Only applies if --parallel is set. PostgreSQL
only.

**--database**:
Database to which the import is made. The database needs to be created before
importing. If not set, it is assumed that the database is specified in the file
to be imported. If your SQL dump file includes a database statement, it will
override the database set in this flag.

**--if-exists**:
Include an SQL statement (IF EXISTS) with each DROP statement produced by
--clean; corresponds to the if-exists flag for pg_restore. Only applies if
--parallel is set. PostgreSQL only.

**--parallel**:
Perform a parallel import. This flag is only applicable to MySQL and Postgres.

**--threads**:
Specifies the number of threads to use for the parallel import. If
`--parallel` is specified and this flag is not provided, Cloud SQL
uses a default thread count to optimize performance.

**--user**:
PostgreSQL user for this import operation.

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
gcloud alpha sql import sql
```

```
gcloud beta sql import sql
```