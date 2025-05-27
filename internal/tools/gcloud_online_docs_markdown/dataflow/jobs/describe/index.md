# gcloud dataflow jobs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/describe](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/describe)*

**NAME**

: **gcloud dataflow jobs describe - outputs the Job object resulting from the Get API**

**SYNOPSIS**

: **`gcloud dataflow jobs describe` `[JOB_ID](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/describe#JOB_ID)` [`[--full](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/describe#--full)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/describe#--region)`=`REGION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: By default this will display the Summary view which includes:

- Project ID
- Regional Endpoint
- Job ID
- Job Name
- Job Type (Batch vs. Streaming)
- Job Create Time
- Job Status (Running, Done, Cancelled, Failed)
- Job Status Time

Notable values that are only in the full view:

- Environment (staging Jars, information about workers, etc.)
- Steps from the workflow graph

**POSITIONAL ARGUMENTS**

: **`JOB_ID`**:
Job ID to operate on.

**FLAGS**

: **--full**:
Retrieve the full Job rather than the summary view

**--region**:
Region ID of the job's regional endpoint. Defaults to 'us-central1'.

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
gcloud beta dataflow jobs describe
```