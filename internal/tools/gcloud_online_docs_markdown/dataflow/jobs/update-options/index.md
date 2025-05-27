# gcloud dataflow jobs update-options  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options)*

**NAME**

: **gcloud dataflow jobs update-options - update pipeline options on-the-fly for running Dataflow jobs**

**SYNOPSIS**

: **`gcloud dataflow jobs update-options` `[JOB_ID](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options#JOB_ID)` [`[--max-num-workers](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options#--max-num-workers)`=`MAX_NUM_WORKERS`] [`[--min-num-workers](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options#--min-num-workers)`=`MIN_NUM_WORKERS`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options#--region)`=`REGION_ID`] [`[--unset-worker-utilization-hint](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options#--unset-worker-utilization-hint)`] [`[--worker-utilization-hint](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options#--worker-utilization-hint)`=`WORKER_UTILIZATION_HINT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can modify properties of running Dataflow jobs. Currently, only
updating autoscaling settings for Streaming Engine jobs is supported.
Adjust the autoscaling settings for Streaming Engine Dataflow jobs by providing
at-least one of --min-num-workers or --max-num-workers or
--worker-utilization-hint (or all 3), or --unset-worker-utilization-hint (which
cannot be run at the same time as --worker-utilization-hint but works with the
others). Allow a few minutes for the changes to take effect.
Note that autoscaling settings can only be modified on-the-fly for Streaming
Engine jobs. Attempts to modify batch job or Streaming Appliance jobs will fail.

**EXAMPLES**

: Modify autoscaling settings to scale between 5-10 workers:

```
gcloud dataflow jobs update-options --min-num-workers=5 --max-num-workers=10
```

Require a job to use at least 2 workers:

```
gcloud dataflow jobs update-options --min-num-workers=2
```

Require a job to use at most 20 workers:

```
gcloud dataflow jobs update-options --max-num-workers=20
```

Adjust the hint of target worker utilization to 70% for horizontal autoscaling:

```
gcloud dataflow jobs update-options --worker-utilization-hint=0.7
```

"Unset" worker utilization hint so that horizontal scaling will rely on its
default CPU utilization target:

```
gcloud dataflow jobs update-options --unset-worker-utilization-hint
```

**POSITIONAL ARGUMENTS**

: **`JOB_ID`**:
Job ID to operate on.

**FLAGS**

: **--max-num-workers**:
Upper-bound for autoscaling, between 1-1000. Only supported for streaming-engine
jobs.

**--min-num-workers**:
Lower-bound for autoscaling, between 1-1000. Only supported for streaming-engine
jobs.

**--region**:
Region ID of the job's regional endpoint. Defaults to 'us-central1'.

**--unset-worker-utilization-hint**:
Unset --worker-utilization-hint. This causes the job autoscaling to fall back to
internal tunings if they exist, or otherwise use the default hint value.

**--worker-utilization-hint**:
Target CPU utilization for autoscaling, ranging from 0.1 to 0.9. Only supported
for streaming-engine jobs with autoscaling enabled.

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

: This variant is also available:

```
gcloud beta dataflow jobs update-options
```