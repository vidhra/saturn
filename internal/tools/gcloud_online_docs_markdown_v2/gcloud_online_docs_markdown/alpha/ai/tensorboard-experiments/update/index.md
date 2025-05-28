# gcloud alpha ai tensorboard-experiments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update)*

**NAME**

: **gcloud alpha ai tensorboard-experiments update - update an existing Vertex AI Tensorboard experiment**

**SYNOPSIS**

: **`gcloud alpha ai tensorboard-experiments update` (`[TENSORBOARD_EXPERIMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update#TENSORBOARD_EXPERIMENT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update#--region)`=`REGION` `[--tensorboard-id](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update#--tensorboard-id)`=`TENSORBOARD_ID`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update#--display-name)`=`DISPLAY_NAME`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an existing Vertex AI Tensorboard experiment.

**EXAMPLES**

: To update a Tensorboard Experiment `my-tensorboard-experiment` in
Tensorboard `12345`, region `us-central1`, and project
`my-project`, with the display name `updated display
name`:

```
gcloud alpha ai tensorboard-experiments update projects/my-project/locations/us-central1/tensorboards/12345/experiments/my-tensorboard-experiment --display-name="updated display name"
```

Or with flags:

```
gcloud alpha ai tensorboard-experiments update my-tensorboard-experiment --tensorboard-id=12345 --display-name="updated display name"
```

**POSITIONAL ARGUMENTS**

: **Tensorboard experiment resource - The Tensorboard experiment to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `tensorboard_experiment` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TENSORBOARD_EXPERIMENT`**:
ID of the tensorboard_experiment or fully qualified identifier for the
tensorboard_experiment.
To set the `name` attribute:

- provide the argument `tensorboard_experiment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the tensorboard_experiment.
To set the `region` attribute:

- provide the argument `tensorboard_experiment` on the command line
with a fully specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.

**--tensorboard-id**:
ID of the tensorboard for the tensorboard_experiment.
To set the `tensorboard-id` attribute:

- provide the argument `tensorboard_experiment` on the command line
with a fully specified name;
- provide the argument `--tensorboard-id` on the command line.**

**FLAGS**

: **--description**:
Description of the tensorboard experiment.

**--display-name**:
Display name of the tensorboard experiment.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
allowlist. This variant is also available:

```
gcloud beta ai tensorboard-experiments update
```