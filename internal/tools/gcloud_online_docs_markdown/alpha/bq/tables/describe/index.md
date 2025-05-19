# gcloud alpha bq tables describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/describe)*

**NAME**

: **gcloud alpha bq tables describe - describe a BigQuery table**

**SYNOPSIS**

: **`gcloud alpha bq tables describe` (`[TABLE](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/describe#TABLE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/describe#--dataset)`=`DATASET`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe a BigQuery table.

**EXAMPLES**

: The following command fetches details about a table with ID
`my-table`

```
gcloud alpha bq tables describe my-table
```

**POSITIONAL ARGUMENTS**

: **Table resource - The BigQuery table you want to describe. The arguments in this
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