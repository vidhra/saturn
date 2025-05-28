# gcloud healthcare datasets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/datasets/update](https://cloud.google.com/sdk/gcloud/reference/healthcare/datasets/update)*

**NAME**

: **gcloud healthcare datasets update - update a Cloud Healthcare API dataset**

**SYNOPSIS**

: **`gcloud healthcare datasets update` (`[DATASET](https://cloud.google.com/sdk/gcloud/reference/healthcare/datasets/update#DATASET)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/datasets/update#--location)`=`LOCATION`) [`[--time-zone](https://cloud.google.com/sdk/gcloud/reference/healthcare/datasets/update#--time-zone)`=`TIME_ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/datasets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Healthcare API dataset.

**EXAMPLES**

: To update the dataset 'test-dataset', run:

```
gcloud healthcare datasets update test-dataset --time-zone=PDT
```

**POSITIONAL ARGUMENTS**

: **Dataset resource - Cloud Healthcare API dataset you want to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `dataset` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DATASET`**:
ID of the dataset or fully qualified identifier for the dataset.
To set the `dataset` attribute:

- provide the argument `dataset` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `dataset` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**FLAGS**

: **--time-zone**:
Default timezone used by this dataset.

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

: This command uses the `healthcare/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/healthcare](https://cloud.google.com/healthcare)

**NOTES**

: These variants are also available:

```
gcloud alpha healthcare datasets update
```

```
gcloud beta healthcare datasets update
```