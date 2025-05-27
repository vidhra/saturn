# gcloud dataflow snapshots list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/list](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/list)*

**NAME**

: **gcloud dataflow snapshots list - list all Cloud Dataflow snapshots in a project in the specified region, optionally filtered by job ID**

**SYNOPSIS**

: **`gcloud dataflow snapshots list` `[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/list#--region)`=`REGION_ID` [`[--job-id](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/list#--job-id)`=`JOB_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List all Cloud Dataflow snapshots in a project in the specified region,
optionally filtered by job ID.

**EXAMPLES**

: To list all Cloud Dataflow snapshots in the us-central1 region, run:

```
gcloud dataflow snapshots list --region=us-central1
```

To list all Cloud Dataflow snapshots for a job, run:

```
gcloud dataflow snapshots list --job-id=JOB_ID --region=JOB_REGION
```

**REQUIRED FLAGS**

: **--region**:
The region ID of the snapshot and job's regional endpoint.

**OPTIONAL FLAGS**

: **--job-id**:
The job ID to use to filter the snapshots list.

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
gcloud alpha dataflow snapshots list
```

```
gcloud beta dataflow snapshots list
```