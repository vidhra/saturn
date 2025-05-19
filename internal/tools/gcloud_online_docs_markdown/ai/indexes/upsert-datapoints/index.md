# gcloud ai indexes upsert-datapoints  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/indexes/upsert-datapoints](https://cloud.google.com/sdk/gcloud/reference/ai/indexes/upsert-datapoints)*

**NAME**

: **gcloud ai indexes upsert-datapoints - upsert data points into the specified index**

**SYNOPSIS**

: **`gcloud ai indexes upsert-datapoints` (`[INDEX](https://cloud.google.com/sdk/gcloud/reference/ai/indexes/upsert-datapoints#INDEX)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/ai/indexes/upsert-datapoints#--region)`=`REGION`) `[--datapoints-from-file](https://cloud.google.com/sdk/gcloud/reference/ai/indexes/upsert-datapoints#--datapoints-from-file)`=`DATAPOINTS_FROM_FILE` [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/ai/indexes/upsert-datapoints#--update-mask)`=[`UPDATE_MASK_PATH`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/indexes/upsert-datapoints#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To upsert datapoints into an index '123', run:

```
gcloud ai indexes upsert-datapoints 123 --datapoints-from-file=example.json --project=example --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Index resource - Index to upsert data points from. The arguments in this group
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

: **--datapoints-from-file**:
Path to a local JSON file that contains the data points that need to be added to
the index.

**OPTIONAL FLAGS**

: **--update-mask**:
Update mask is used to specify the fields to be overwritten in the datapoints by
the update. The fields specified in the update_mask are relative to each
IndexDatapoint inside datapoints, not the full request.
Updatable fields:

- Use --update-mask=`all_restricts` to update both
`restricts` and `numeric_restricts`.

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
gcloud alpha ai indexes upsert-datapoints
```

```
gcloud beta ai indexes upsert-datapoints
```