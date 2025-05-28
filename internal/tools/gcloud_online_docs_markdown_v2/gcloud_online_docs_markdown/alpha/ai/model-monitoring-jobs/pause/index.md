# gcloud alpha ai model-monitoring-jobs pause  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/pause](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/pause)*

**NAME**

: **gcloud alpha ai model-monitoring-jobs pause - pause a running Vertex AI model deployment monitoring job**

**SYNOPSIS**

: **`gcloud alpha ai model-monitoring-jobs pause` (`[MONITORING_JOB](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/pause#MONITORING_JOB)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/pause#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/pause#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Pause a running Vertex AI model deployment monitoring job.

**EXAMPLES**

: To pause a model deployment monitoring job `123` of project
`example` in region `us-central1`, run:

```
gcloud alpha ai model-monitoring-jobs pause 123 --project=example --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Monitoring job resource - The model deployment monitoring job to pause. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `monitoring_job` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MONITORING_JOB`**:
ID of the monitoring_job or fully qualified identifier for the monitoring_job.
To set the `name` attribute:

- provide the argument `monitoring_job` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the monitoring_job.
To set the `region` attribute:

- provide the argument `monitoring_job` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

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
gcloud ai model-monitoring-jobs pause
```

```
gcloud beta ai model-monitoring-jobs pause
```