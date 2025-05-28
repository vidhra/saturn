# gcloud spanner rows update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/rows/update](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/update)*

**NAME**

: **gcloud spanner rows update - update a row in a Cloud Spanner database**

**SYNOPSIS**

: **`gcloud spanner rows update` `[--data](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/update#--data)`=[`COLUMN_NAME`=`VALUE`,…] `[--table](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/update#--table)`=`TABLE` (`[--database](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/update#--database)`=`DATABASE` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/update#--instance)`=`INSTANCE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update a row with SingerId=1,SingName=abc in table Singers under my-database
and my-instance, run:

```
gcloud spanner rows update --table=Singers --database=my-database --instance=my-instance --data=SingerId=1,SingerName=abc
```

```
gcloud spanner rows update --table=Singers --database=my-database --instance=my-instance --flags-file=path/to/file.yaml
```

**REQUIRED FLAGS**

: **--data**:
The column names and values for the row being updated. For complicated input
values, such as arrays, use the `--flags-file` flag. See $ [gcloud topic flags-file](https://cloud.google.com/sdk/gcloud/reference/topic/flags-file) for
more information.

**--table**:
The Cloud Spanner table name.

**Database resource - The Cloud Spanner database in which to update a row. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--database` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--database**:
ID of the database or fully qualified identifier for the database.
To set the `database` attribute:

- provide the argument `--database` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--instance**:
The Cloud Spanner instance for the database.
To set the `instance` attribute:

- provide the argument `--database` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

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
gcloud alpha spanner rows update
```

```
gcloud beta spanner rows update
```