# gcloud sql export bak  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/export/bak](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak)*

**NAME**

: **gcloud sql export bak - export data from a Cloud SQL instance to a BAK file**

**SYNOPSIS**

: **`gcloud sql export bak` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#INSTANCE)` `[URI](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#URI)` `[--database](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#--database)`=`DATABASE`,[`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#DATABASE)`,…], `[-d](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#-d)` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#DATABASE)`,[`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#DATABASE)`,…] [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#--async)`] [`[--bak-type](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#--bak-type)`=`BAK_TYPE`; default="FULL"] [`[--differential-base](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#--differential-base)`] [`[--export-log-end-time](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#--export-log-end-time)`=`EXPORT_LOG_END_TIME`] [`[--export-log-start-time](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#--export-log-start-time)`=`EXPORT_LOG_START_TIME`] [`--stripe_count`=`STRIPE_COUNT`] [`[--[no-]striped](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#--[no-]striped)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/export/bak#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export data from a Cloud SQL instance to a Google Cloud Storage bucket as a BAK
backup file. This is only supported for SQL Server.

**EXAMPLES**

: To export data from the database `my-database` in the Cloud SQL
instance `my-instance` to a BAK file
`my-bucket/my-export.bak`, run:

```
gcloud sql export bak my-instance gs://my-bucket/my-export.bak --database=my-database
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**`URI`**:
The path to the file in Google Cloud Storage where the export will be stored.
The URI is in the form gs://bucketName/fileName. If the file already exists, the
operation fails.

**REQUIRED FLAGS**

: **--database**:
Database from which the export is made. Information on requirements can be found
here: [https://cloud.google.com/sql/docs/sqlserver/admin-api/v1beta4/instances/export#exportContext.databases](https://cloud.google.com/sql/docs/sqlserver/admin-api/v1beta4/instances/export#exportContext.databases)

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bak-type**:
Type of bak file that will be exported, FULL or DIFF. SQL Server only.
`BAK_TYPE` must be one of: `FULL`,
`DIFF`, `TLOG`.

**--differential-base**:
Whether the bak file export can be used as differential base for future
differential backup. SQL Server only

**--export-log-end-time**:
Optional flag. The end time of the transaction log files that are included in
the export file. Use this flag to export transaction logs for Cloud SQL for SQL
Server only. Format: YYYY-MM-DDTHH:MM:SSZ, UTC timezone only.

**--export-log-start-time**:
Optional flag. The start time of the transaction log files that are included in
the export file. Use this flag to export transaction logs for Cloud SQL for SQL
Server only. Format: YYYY-MM-DDTHH:MM:SSZ, UTC timezone only.

**--stripe_count**:
Specifies the number of stripes to use for SQL Server exports.

**--[no-]striped**:
Whether SQL Server export should be striped. Use `--striped` to
enable and `--no-striped` to disable.

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
gcloud alpha sql export bak
```

```
gcloud beta sql export bak
```