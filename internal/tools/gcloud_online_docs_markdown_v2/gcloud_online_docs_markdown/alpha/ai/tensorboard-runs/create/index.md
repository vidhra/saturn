# gcloud alpha ai tensorboard-runs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create)*

**NAME**

: **gcloud alpha ai tensorboard-runs create - create a new Vertex AI Tensorboard run**

**SYNOPSIS**

: **`gcloud alpha ai tensorboard-runs create` (`[TENSORBOARD_EXPERIMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create#TENSORBOARD_EXPERIMENT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create#--region)`=`REGION` `[--tensorboard-id](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create#--tensorboard-id)`=`TENSORBOARD_ID`) `[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create#--display-name)`=`DISPLAY_NAME` `[--tensorboard-run-id](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create#--tensorboard-run-id)`=`TENSORBOARD_RUN_ID` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new Vertex AI Tensorboard run.

**EXAMPLES**

: To create a Tensorboard Run `my-tensorboard-run` in Tensorboard
`12345` and Tensorboard Experiment `my-tensorboard-experiment,
with the display name`my tensorboard run`:

```
gcloud alpha ai tensorboard-runs create my-tensorboard-experiment --tensorboard-run-id=my-tensorboard-run --tensorboard-id=12345 --display-name="my tensorboard run"
```

You may also provide a description and/or labels:

```
gcloud alpha ai tensorboard-runs create my-tensorboard-experiment --tensorboard-run-id=my-tensorboard-run --tensorboard-id=12345 --description="my description" --labels="label1=value1" --labels="label2=value2"
```

To create a Tensorboard Run`my-tensorboard-run`in Tensorboard`12345`, Tensorboard Experiment`my-tensorboard-experiment,
region `us-central1`, and project `my-project`:

```
gcloud alpha ai tensorboard-runs create projects/my-project/locations/us-central1/tensorboards/12345/experiments/my-tensorboard-experiment --tensorboard-run-id=my-tensorboard-run
```

**POSITIONAL ARGUMENTS**

: **Tensorboard experiment resource - The Tensorboard experiment to create a
Tensorboard run. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--display-name**:
Display name of the tensorboard-run.

**--tensorboard-run-id**:
ID of the Tensorboard run.

**OPTIONAL FLAGS**

: **--description**:
Description of the tensorboard-run.

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
gcloud beta ai tensorboard-runs create
```