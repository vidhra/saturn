# gcloud alpha bq tables update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update)*

**NAME**

: **gcloud alpha bq tables update - update a new BigQuery table**

**SYNOPSIS**

: **`gcloud alpha bq tables update` (`[TABLE](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update#TABLE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update#--dataset)`=`DATASET`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update#--description)`=`DESCRIPTION`] [`[--expiration](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update#--expiration)`=`EXPIRATION`] [`[--relax-columns](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update#--relax-columns)`=[`FIELD_NAME`,…]] [`[--add-columns](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update#--add-columns)`=[`FIELD_NAME`=`FIELD_TYPE`,…]     | `[--add-columns-file](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update#--add-columns-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new BigQuery table. Updates one or more attributes
of a table or view.

**EXAMPLES**

: The following command updates the description on a table with ID
`my-table` in `my-dataset`:

```
gcloud alpha bq tables update /projects/myproject/datasets/my-dataset/tables/my-table --description 'My New Table'
```

The following command changes the schema mode from `REQUIRED` to
`NULLABLE` on the `value` and `tags` columns in
a table with ID `my-other-table` in dataset
`my-other-dataset`:

```
gcloud alpha bq tables update my-other-table --dataset my-other-dataset --relax-columns name,tags
```

**POSITIONAL ARGUMENTS**

: **Table resource - The BigQuery table you want to update. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**--dataset**:
The id of the BigQuery dataset.
To set the `dataset` attribute:

- provide the argument `table` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.**

**FLAGS**

: **--description**:
Description of the table.

**--expiration**:
How long after creation should this table or view expire e.g. 1d, 2w etc.
See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats

**--relax-columns**:
A comma-separated list of field names in the current schema that should have
their mode changed from REQUIRED to NULLABLE.
For more details on updating and managing BigQuery schemas see: [https://cloud.google.com/bigquery/docs/managing-table-schemas](https://cloud.google.com/bigquery/docs/managing-table-schemas)

**--add-columns**

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

: This command uses the `bigquery/v2` API. The full documentation for
this API can be found at: [https://cloud.google.com/bigquery/](https://cloud.google.com/bigquery/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.