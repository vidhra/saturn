# gcloud bigtable instances tables describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/describe](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/describe)*

**NAME**

: **gcloud bigtable instances tables describe - retrieve information about a table**

**SYNOPSIS**

: **`gcloud bigtable instances tables describe` (`[TABLE](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/describe#TABLE)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/describe#--instance)`=`INSTANCE`) [`[--view](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/describe#--view)`=`VIEW`; default="schema"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieve information about a table.

**EXAMPLES**

: To describe a table, run:

```
gcloud bigtable instances tables describe TABLE_NAME --instance=INSTANCE_NAME
```

**POSITIONAL ARGUMENTS**

: **Table resource - Cloud Bigtable table to describe. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `table` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TABLE`**:
ID of the table or fully qualified identifier for the table.
To set the `table` attribute:

- provide the argument `table` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Name of the Cloud Bigtable instance.
To set the `instance` attribute:

- provide the argument `table` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.**

**FLAGS**

: **--view**:
The view to be applied to the returned table's fields.
`VIEW` must be one of:

**`encryption`**:
Only populates `name` and fields related to the table's encryption
status.

**`full`**:
Populates all fields.

**`name`**:
Only populates `name`.

**`replication`**:
Only populates `name` and fields related to the table's replication.

**`schema`**:
Only populates `name` and fields related to the table's schema.

**`stats`**:
Only populates `name` and fields related to the table's statistics
(e.g. TableStats and ColumnFamilyStats).

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

: This command uses the `bigtableadmin/v2` API. The full documentation
for this API can be found at: [https://cloud.google.com/bigtable/](https://cloud.google.com/bigtable/)

**NOTES**

: These variants are also available:

```
gcloud alpha bigtable instances tables describe
```

```
gcloud beta bigtable instances tables describe
```