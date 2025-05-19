# gcloud alpha ai tensorboard-experiments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create)*

**NAME**

: **gcloud alpha ai tensorboard-experiments create - create a new Vertex AI Tensorboard experiment**

**SYNOPSIS**

: **`gcloud alpha ai tensorboard-experiments create` (`[TENSORBOARD](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create#TENSORBOARD)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create#--region)`=`REGION`) `[--tensorboard-experiment-id](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create#--tensorboard-experiment-id)`=`TENSORBOARD_EXPERIMENT_ID` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new Vertex AI Tensorboard experiment.

**EXAMPLES**

: To create a Tensorboard Experiment in a Tensorboard `12345`, with the
display name `my tensorboard experiment`:

```
gcloud alpha ai tensorboard-experiments create 12345 --tensorboard-experiment-id=my-tensorboard-experiment --display-name="my tensorboard experiment"
```

You may also provide a description and/or labels:

```
gcloud alpha ai tensorboard-experiments create 12345 --tensorboard-experiment-id=my-tensorboard-experiment --description="my description" --labels="label1=value1" --labels="label2=value2"
```

To create a Tensorboard Experiment `my-tensorboard-experiment` in a
Tensorboard `12345`, region `us-central1`, and project
`my-project`:

```
gcloud alpha ai tensorboard-experiments create projects/my-project/locations/us-central1/tensorboards/12345 --tensorboard-experiment-id=my-tensorboard-experiment
```

**POSITIONAL ARGUMENTS**

: **Tensorboard resource - The tensorboard to create a Tensorboard experiment. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `tensorboard` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TENSORBOARD`**:
ID of the tensorboard or fully qualified identifier for the tensorboard.
To set the `name` attribute:

- provide the argument `tensorboard` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the tensorboard.
To set the `region` attribute:

- provide the argument `tensorboard` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**REQUIRED FLAGS**

: **--tensorboard-experiment-id**:
Id of the Tensorboard experiment.

**OPTIONAL FLAGS**

: **--description**:
Description of the tensorboard-experiment.

**--display-name**:
Display name of the tensorboard-experiment.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud beta ai tensorboard-experiments create
```