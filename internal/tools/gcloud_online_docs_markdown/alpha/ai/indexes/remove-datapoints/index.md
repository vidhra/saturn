# gcloud alpha ai indexes remove-datapoints  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/indexes/remove-datapoints](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/indexes/remove-datapoints)*

**NAME**

: **gcloud alpha ai indexes remove-datapoints - remove data points from the specified index**

**SYNOPSIS**

: **`gcloud alpha ai indexes remove-datapoints` (`[INDEX](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/indexes/remove-datapoints#INDEX)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/indexes/remove-datapoints#--region)`=`REGION`) (`[--datapoint-ids](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/indexes/remove-datapoints#--datapoint-ids)`=[`DATAPOINT_IDS`,…]     | `[--datapoints-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/indexes/remove-datapoints#--datapoints-from-file)`=`DATAPOINTS_FROM_FILE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/indexes/remove-datapoints#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To remove data points from an index `123`, run:

```
gcloud alpha ai indexes remove-datapoints 123 --datapoint-ids=example1,example2 --project=example --region=us-central1
```

Or put datapoint ids in a JSON file and run:

```
gcloud alpha ai indexes remove-datapoints 123 --datapoints-from-file=example.json --project=example --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Index resource - Index to remove data points from. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `index` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INDEX`**:
ID of the index or fully qualified identifier for the index.
To set the `name` attribute:

- provide the argument `index` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the index.
To set the `region` attribute:

- provide the argument `index` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**REQUIRED FLAGS**

: **--datapoint-ids**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud ai indexes remove-datapoints
```

```
gcloud beta ai indexes remove-datapoints
```