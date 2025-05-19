# gcloud alpha ai-platform versions update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update)*

**NAME**

: **gcloud alpha ai-platform versions update - update an AI Platform version**

**SYNOPSIS**

: **`gcloud alpha ai-platform versions update` (`[VERSION](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#VERSION)` : `[--model](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#--model)`=`MODEL`) [`[--config](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#--config)`=`YAML_FILE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#--description)`=`DESCRIPTION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#--region)`=`REGION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--bigquery-table-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#--bigquery-table-name)`=`BIGQUERY_TABLE_NAME` `[--sampling-percentage](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#--sampling-percentage)`=`SAMPLING_PERCENTAGE`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an AI Platform version.

**POSITIONAL ARGUMENTS**

: **Version resource - The AI Platform model to update. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `version` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`VERSION`**:
ID of the version or fully qualified identifier for the version.
To set the `version` attribute:

- provide the argument `version` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--model**:
Model for the version.
To set the `model` attribute:

- provide the argument `version` on the command line with a fully
specified name;
- provide the argument `--model` on the command line.**

**FLAGS**

: **--config**:
Path to a YAML configuration file containing configuration parameters for the [version](https://cloud.google.com/ml/reference/rest/v1/projects.models.versions)
to create.
The file is in YAML format. Note that not all attributes of a version are
configurable; available attributes (with example values) are:

```
description: A free-form description of the version.
manualScaling:
  nodes: 10  # The number of nodes to allocate for this model.
autoScaling:
  minNodes: 0  # The minimum number of nodes to allocate for this model.
  maxNodes: 1  # The maxinum number of nodes to allocate for this model.
requestLoggingconfig:
  bigqueryTableName: someTable  # Fully qualified BigQuery table name.
  samplingPercentage: 0.5  # Percentage of requests to be logged.
```

The name of the version must always be specified via the required VERSION
argument.
Only one of manualScaling or autoScaling can be specified. If both are specified
in same yaml file, an error will be returned.
Labels cannot currently be set in the config.yaml; please use the command-line
flags to alter them.
If an option is specified both in the configuration file and via command-line
arguments, the command-line arguments override the configuration file.

**--description**:
Description of the version.

**--region**:
Google Cloud region of the regional endpoint to use for this command. For the
global endpoint, the region needs to be specified as `global`.
Learn more about regional endpoints and see a list of available regions: [https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints)
`REGION` must be one of: `global`,
`asia-east1`, `asia-northeast1`,
`asia-southeast1`, `australia-southeast1`,
`europe-west1`, `europe-west2`, `europe-west3`,
`europe-west4`, `northamerica-northeast1`,
`us-central1`, `us-east1`, `us-east4`,
`us-west1`.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--bigquery-table-name**

**--clear-labels**

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
gcloud ai-platform versions update
```

```
gcloud beta ai-platform versions update
```