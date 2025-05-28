# gcloud ai custom-jobs stream-logs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/stream-logs](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/stream-logs)*

**NAME**

: **gcloud ai custom-jobs stream-logs - show stream logs from a running custom job**

**SYNOPSIS**

: **`gcloud ai custom-jobs stream-logs` (`[CUSTOM_JOB](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/stream-logs#CUSTOM_JOB)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/stream-logs#--region)`=`REGION`) [`[--allow-multiline-logs](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/stream-logs#--allow-multiline-logs)`] [`[--polling-interval](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/stream-logs#--polling-interval)`=`POLLING_INTERVAL`; default=60] [`[--task-name](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/stream-logs#--task-name)`=`TASK_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/stream-logs#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To stream logs of custom job ``123`` under
project ``example`` in region
``us-central1``, run:

```
gcloud ai custom-jobs stream-logs 123 --project=example --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Custom job resource - The custom job to fetch stream log. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `custom_job` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CUSTOM_JOB`**:
ID of the custom job or fully qualified identifier for the custom job.
To set the `name` attribute:

- provide the argument `custom_job` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the custom job.
To set the `region` attribute:

- provide the argument `custom_job` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**FLAGS**

: **--allow-multiline-logs**:
Output multiline log messages as single records.

**--polling-interval**:
Number of seconds to wait between efforts to fetch the latest log messages.

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
gcloud alpha ai custom-jobs stream-logs
```

```
gcloud beta ai custom-jobs stream-logs
```