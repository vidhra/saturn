# gcloud sql export csv  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/export/csv](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv)*

**NAME**

: **gcloud sql export csv - exports data from a Cloud SQL instance to a CSV file**

**SYNOPSIS**

: **`gcloud sql export csv` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#INSTANCE)` `[URI](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#URI)` `[--query](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#--query)`=`QUERY` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#--async)`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#--database)`=`DATABASE`,[`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#DATABASE)`,…], `[-d](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#-d)` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#DATABASE)`,[`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#DATABASE)`,…]] [`[--escape](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#--escape)`=`ESCAPE`] [`[--fields-terminated-by](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#--fields-terminated-by)`=`FIELDS_TERMINATED_BY`] [`[--lines-terminated-by](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#--lines-terminated-by)`=`LINES_TERMINATED_BY`] [`[--offload](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#--offload)`] [`[--quote](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#--quote)`=`QUOTE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/export/csv#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Exports data from a Cloud SQL instance to a Google Cloud Storage bucket as a
plain text file with one line per row and comma-separated fields.

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**`URI`**:
The path to the file in Google Cloud Storage where the export will be stored.
The URI is in the form gs://bucketName/fileName. If the file already exists, the
operation fails. If the filename ends with .gz, the contents are compressed.

**REQUIRED FLAGS**

: **--query**:
A SQL SELECT query (e.g., SELECT * FROM table) that specifies the data to
export. WARNING: While in-transit, the query might be processed in intermediate
locations other than the location of the target instance.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--database**:
Database(s) from which the export is made. Information on requirements can be
found here: [https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances/export#exportContext.databases](https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances/export#exportContext.databases)

**--escape**:
Specifies the character that should appear before a data character that needs to
be escaped. The value of this argument has to be a character in Hex ASCII Code.
For example, "22" represents double quotes. This flag is only available for
MySQL and Postgres. If this flag is not provided, double quotes character will
be used as the default value.

**--fields-terminated-by**:
Specifies the character that splits column values. The value of this argument
has to be a character in Hex ASCII Code. For example, "2C" represents a comma.
This flag is only available for MySQL and Postgres. If this flag is not
provided, a comma character will be used as the default value.

**--lines-terminated-by**:
Specifies the character that split line records. The value of this argument has
to be a character in Hex ASCII Code. For example, "0A" represents a new line.
This flag is only available for MySQL. If this flag is not provided, a new line
character will be used as the default value.

**--offload**:
Offload an export to a temporary instance. Doing so reduces strain on source
instances and allows other operations to be performed while the export is in
progress.

**--quote**:
Specifies the character that encloses values from columns that have string data
type. The value of this argument has to be a character in Hex ASCII Code. For
example, "22" represents double quotes. This flag is only available for MySQL
and Postgres. If this flag is not provided, double quotes character will be used
as the default value.

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
gcloud alpha sql export csv
```

```
gcloud beta sql export csv
```