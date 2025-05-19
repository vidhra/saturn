# gcloud alpha bq datasets delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bq/datasets/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/datasets/delete)*

**NAME**

: **gcloud alpha bq datasets delete - delete a BigQuery dataset**

**SYNOPSIS**

: **`gcloud alpha bq datasets delete` `[DATASET](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/datasets/delete#DATASET)` [`[--remove-tables](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/datasets/delete#--remove-tables)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/datasets/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Delete a BigQuery dataset.

**EXAMPLES**

: The following command deletes a dataset with ID `my-dataset`

```
gcloud alpha bq datasets delete my-dataset
```

**POSITIONAL ARGUMENTS**

: **Dataset resource - The BigQuery dataset you want to delete. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `dataset` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DATASET`**:
ID of the dataset or fully qualified identifier for the dataset.
To set the `dataset` attribute:

- provide the argument `dataset` on the command line.**

**FLAGS**

: **--remove-tables**:
Remove the dataset even if it contains one or more tables. Tables will be
removed before deleteing dataset.

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