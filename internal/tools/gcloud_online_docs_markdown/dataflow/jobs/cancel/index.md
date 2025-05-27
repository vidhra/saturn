# gcloud dataflow jobs cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/cancel](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/cancel)*

**NAME**

: **gcloud dataflow jobs cancel - cancels all jobs that match the command line arguments**

**SYNOPSIS**

: **`gcloud dataflow jobs cancel` `[JOB_ID](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/cancel#JOB_ID)` [`[JOB_ID](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/cancel#JOB_ID)` …] [`[--force](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/cancel#--force)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/cancel#--region)`=`REGION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancels all jobs that match the command line arguments.

**POSITIONAL ARGUMENTS**

: **`JOB_ID` [`JOB_ID` …]**:
Job IDs to operate on.

**FLAGS**

: **--force**:
Forcibly cancels a Dataflow job. Regular cancel must have been attempted at
least 30 minutes prior for a job to be force cancelled.

**--region**:
Region ID of the jobs' regional endpoint. Defaults to 'us-central1'.

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
gcloud beta dataflow jobs cancel
```