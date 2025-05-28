# gcloud sql import csv  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/import/csv](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv)*

**NAME**

: **gcloud sql import csv - imports data into a Cloud SQL instance from a CSV file**

**SYNOPSIS**

: **`gcloud sql import csv` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#INSTANCE)` `[URI](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#URI)` `[--database](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--database)`=`DATABASE`, `[-d](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#-d)` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#DATABASE)` `[--table](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--table)`=`TABLE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--async)`] [`[--columns](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--columns)`=`COLUMNS`,[`[COLUMNS](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#COLUMNS)`,…]] [`[--escape](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--escape)`=`ESCAPE`] [`[--fields-terminated-by](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--fields-terminated-by)`=`FIELDS_TERMINATED_BY`] [`[--lines-terminated-by](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--lines-terminated-by)`=`LINES_TERMINATED_BY`] [`[--quote](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--quote)`=`QUOTE`] [`[--user](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--user)`=`USER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Imports data into a Cloud SQL instance from a plain text file in a Google Cloud
Storage bucket with one line per row and comma-separated fields.

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**`URI`**:
Path to the CSV file in Google Cloud Storage from which the import is made. The
URI is in the form `gs://bucketName/fileName`. Compressed gzip files
(.gz) are also supported.

**REQUIRED FLAGS**

: **--database**:
The database (for example, guestbook) to which the import is made.

**--table**:
The database table to import csv file into.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--columns**:
The columns to import from csv file. These correspond to actual database columns
to import. If not set, all columns from csv file are imported to corresponding
database columns.

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

**--quote**:
Specifies the character that encloses values from columns that have string data
type. The value of this argument has to be a character in Hex ASCII Code. For
example, "22" represents double quotes. This flag is only available for MySQL
and Postgres. If this flag is not provided, double quotes character will be used
as the default value.

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
gcloud alpha sql import csv
```

```
gcloud beta sql import csv
```