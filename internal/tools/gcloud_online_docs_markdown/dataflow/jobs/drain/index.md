# gcloud dataflow jobs drain  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/drain](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/drain)*

**NAME**

: **gcloud dataflow jobs drain - drains all jobs that match the command line arguments**

**SYNOPSIS**

: **`gcloud dataflow jobs drain` `[JOB_ID](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/drain#JOB_ID)` [`[JOB_ID](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/drain#JOB_ID)` …] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/drain#--region)`=`REGION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/drain#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Once Drain is triggered, the pipeline will stop accepting new inputs. The input
watermark will be advanced to infinity. Elements already in the pipeline will
continue to be processed. Drained jobs can safely be cancelled.

**POSITIONAL ARGUMENTS**

: **`JOB_ID` [`JOB_ID` …]**:
Job IDs to operate on.

**FLAGS**

: **--region**:
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
gcloud beta dataflow jobs drain
```