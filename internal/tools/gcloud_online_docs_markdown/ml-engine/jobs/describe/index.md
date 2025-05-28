# gcloud ml-engine jobs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/describe](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/describe)*

**NAME**

: **gcloud ml-engine jobs describe - describe an AI Platform job**

**SYNOPSIS**

: **`gcloud ml-engine jobs describe` `[JOB](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/describe#JOB)` [`[--summarize](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/describe#--summarize)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an AI Platform job.

**EXAMPLES**

: To describe the AI Platform job named
``my-job``, run:

```
gcloud ml-engine jobs describe my-job
```

**POSITIONAL ARGUMENTS**

: **`JOB`**:
Name of the job.

**FLAGS**

: **--summarize**:
Summarize job output in a set of human readable tables instead of rendering the
entire resource as json or yaml. The tables currently rendered are:

- `Job Overview`: Overview of job including, jobId, status and create
time.
- `Training Input Summary`: Summary of input for a training job
including region, main training python module and scale tier.
- `Training Output Summary`: Summary of output for a training job
including the amount of ML units consumed by the job.
- `Training Output Trials`: Summary of hyperparameter trials run for a
hyperparameter tuning training job.
- `Predict Input Summary`: Summary of input for a prediction job
including region, model verion and output path.
- `Predict Output Summary`: Summary of output for a prediction job
including prediction count and output path.

This flag overrides the `--format` flag. If both are present on the
command line, a warning is displayed.

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
gcloud alpha ml-engine jobs describe
```

```
gcloud beta ml-engine jobs describe
```