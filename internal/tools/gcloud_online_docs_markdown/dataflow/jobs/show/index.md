# gcloud dataflow jobs show  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/show](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/show)*

**NAME**

: **gcloud dataflow jobs show - shows a short description of the given job**

**SYNOPSIS**

: **`gcloud dataflow jobs show` `[JOB_ID](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/show#JOB_ID)` [`[--environment](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/show#--environment)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/show#--region)`=`REGION_ID`] [`[--steps](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/show#--steps)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/show#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Shows a short description of the given job.

**POSITIONAL ARGUMENTS**

: **`JOB_ID`**:
Job ID to operate on.

**FLAGS**

: **--environment**:
If present, the environment will be listed.

**--region**:
Region ID of the job's regional endpoint. Defaults to 'us-central1'.

**--steps**:
If present, the steps will be listed.

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
gcloud beta dataflow jobs show
```