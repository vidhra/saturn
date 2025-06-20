# gcloud ml-engine jobs stream-logs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/stream-logs](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/stream-logs)*

**NAME**

: **gcloud ml-engine jobs stream-logs - show logs from a running AI Platform job**

**SYNOPSIS**

: **`gcloud ml-engine jobs stream-logs` `[JOB](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/stream-logs#JOB)` [`[--allow-multiline-logs](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/stream-logs#--allow-multiline-logs)`] [`[--polling-interval](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/stream-logs#--polling-interval)`=`POLLING_INTERVAL`; default=60] [`[--task-name](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/stream-logs#--task-name)`=`TASK_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml-engine/jobs/stream-logs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show logs from a running AI Platform job.

**EXAMPLES**

: To show the logs from running the AI Platform job
``my-job``, run:

```
gcloud ml-engine jobs stream-logs my-job
```

**POSITIONAL ARGUMENTS**

: **`JOB`**:
Name of the job.

**FLAGS**

: **--allow-multiline-logs**:
Output multiline log messages as single records.

**--polling-interval**:
Number of seconds to wait between efforts to fetch the latest log messages.
Overrides the default `ml_engine/polling_interval` property value for
this command invocation.

**--task-name**:
If set, display only the logs for this particular task.

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
gcloud alpha ml-engine jobs stream-logs
```

```
gcloud beta ml-engine jobs stream-logs
```