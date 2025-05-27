# gcloud dataflow snapshots create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/create](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/create)*

**NAME**

: **gcloud dataflow snapshots create - creates a snapshot for a Cloud Dataflow job**

**SYNOPSIS**

: **`gcloud dataflow snapshots create` `[--job-id](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/create#--job-id)`=`JOB_ID` `[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/create#--region)`=`REGION_ID` [`[--snapshot-sources](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/create#--snapshot-sources)`=`SNAPSHOT_SOURCES`] [`[--snapshot-ttl](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/create#--snapshot-ttl)`=`DURATION`; default="7d"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a snapshot for a Cloud Dataflow job.

**EXAMPLES**

: To create a Cloud Dataflow snapshot with sources for a running job, run:

```
gcloud dataflow snapshots create --job-id=JOB_ID --region=JOB_REGION --snapshot-sources=true --snapshot-ttl=7d
```

**REQUIRED FLAGS**

: **--job-id**:
The job ID to snapshot.

**--region**:
The region ID of the snapshot and job's regional endpoint.

**OPTIONAL FLAGS**

: **--snapshot-sources**:
If true, snapshots will also be created for the Cloud Pub/Sub sources of the
Cloud Dataflow job.

**--snapshot-ttl**:
Time to live for the snapshot.

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
gcloud alpha dataflow snapshots create
```

```
gcloud beta dataflow snapshots create
```