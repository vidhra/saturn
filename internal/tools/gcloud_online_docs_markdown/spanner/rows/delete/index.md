# gcloud spanner rows delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/rows/delete](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/delete)*

**NAME**

: **gcloud spanner rows delete - delete a row in a Cloud Spanner database**

**SYNOPSIS**

: **`gcloud spanner rows delete` `[--keys](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/delete#--keys)`=[`KEY`,…] `[--table](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/delete#--table)`=`TABLE` (`[--database](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/delete#--database)`=`DATABASE` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/delete#--instance)`=`INSTANCE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/rows/delete#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To delete a row with primary keys of SingerId=1,SingName=abc in table Singers
under my-database and my-instance, run:

```
gcloud spanner rows delete --table=Singers --database=my-database --instance=my-instance --keys=1,abc
```

**REQUIRED FLAGS**

: **--keys**:
The primary key values of the row to delete.

**--table**:
The Cloud Spanner table name.

**Database resource - The Cloud Spanner database in which to delete a row. The
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
gcloud alpha spanner rows delete
```

```
gcloud beta spanner rows delete
```