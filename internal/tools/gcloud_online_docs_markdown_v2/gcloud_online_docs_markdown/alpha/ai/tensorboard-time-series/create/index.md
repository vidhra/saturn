# gcloud alpha ai tensorboard-time-series create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create)*

**NAME**

: **gcloud alpha ai tensorboard-time-series create - create a new Vertex AI Tensorboard time series**

**SYNOPSIS**

: **`gcloud alpha ai tensorboard-time-series create` (`[TENSORBOARD_RUN](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#TENSORBOARD_RUN)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#--region)`=`REGION` `[--tensorboard-experiment-id](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#--tensorboard-experiment-id)`=`TENSORBOARD_EXPERIMENT_ID` `[--tensorboard-id](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#--tensorboard-id)`=`TENSORBOARD_ID`) `[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#--display-name)`=`DISPLAY_NAME` `[--type](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#--type)`=`TYPE` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#--description)`=`DESCRIPTION`] [`[--plugin-data](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#--plugin-data)`=`PLUGIN_DATA`] [`[--plugin-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#--plugin-name)`=`PLUGIN_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new Vertex AI Tensorboard time series.

**EXAMPLES**

: To create a Tensorboard Time Series in Tensorboard `12345`,
Tensorboard Experiment `my-tensorboard-experiment, and in Tensorboard Run`my-tensorboard-run`, with the display name`my tensorboard
time series`and type Scalar:

```
gcloud alpha ai tensorboard-time-series create my-tensorboard-run --tensorboard-experiment-id=my-tensorboard-experiment --tensorboard-id=12345 --display-name="my tensorboard time series" --type=SCALAR
```

You may also provide a description:

```
gcloud alpha ai tensorboard-time-series create my-tensorboard-run --tensorboard-experiment-id=my-tensorboard-experiment --tensorboard-id=12345 --display-name="my tensorboard time series" --type=SCALAR --description="my description"
```

To create a Tensorboard Time Series in Tensorboard`12345`,
Tensorboard Experiment`my-tensorboard-experiment, Tensorboard Run
`my-tensorboard-run`, region `us-central1`, and project
`my-project`:

```
gcloud alpha ai tensorboard-time-series create projects/my-project/locations/us-central1/tensorboards/12345/experiments/my-tensorboard-experiment/runs/my-tensorboard-run --display-name="my tensorboard time series" --type=SCALAR
```

**POSITIONAL ARGUMENTS**

: **Tensorboard run resource - The Tensorboard run to create a Tensorboard time
series. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `tensorboard_run` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TENSORBOARD_RUN`**:
ID of the tensorboard_run or fully qualified identifier for the tensorboard_run.
To set the `name` attribute:

- provide the argument `tensorboard_run` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the tensorboard_run.
To set the `region` attribute:

- provide the argument `tensorboard_run` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.

**--tensorboard-experiment-id**:
ID of the tensorboard experiment for the tensorboard_run.
To set the `tensorboard-experiment-id` attribute:

- provide the argument `tensorboard_run` on the command line with a
fully specified name;
- provide the argument `--tensorboard-experiment-id` on the command
line.

**--tensorboard-id**:
ID of the tensorboard for the tensorboard_run.
To set the `tensorboard-id` attribute:

- provide the argument `tensorboard_run` on the command line with a
fully specified name;
- provide the argument `--tensorboard-id` on the command line.**

**REQUIRED FLAGS**

: **--display-name**:
Display name of the tensorboard-time-series.

**--type**:
Value type of the tensorboard-time-series. `TYPE` must be
one of:

**`blob-sequence`**:
Used for tensorboard-time-series that is a list of blob sequences. E.g. set of
sample images with labels over epochs/time.

**`scalar`**:
Used for tensorboard-time-series that is a list of scalars. E.g. accuracy of a
model over epochs/time.

**`tensor`**:
Used for tensorboard-time-series that is a list of tensors. E.g. histograms of
weights of layer in a model over epoch/time.

**OPTIONAL FLAGS**

: **--description**:
Description of the tensorboard-time-series.

**--plugin-data**:
Plugin data of the tensorboard-time-series.

**--plugin-name**:
Plugin name of the tensorboard-time-series.

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
gcloud beta ai tensorboard-time-series create
```