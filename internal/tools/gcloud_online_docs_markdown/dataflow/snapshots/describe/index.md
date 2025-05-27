# gcloud dataflow snapshots describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/describe](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/describe)*

**NAME**

: **gcloud dataflow snapshots describe - describe a Cloud Dataflow snapshot**

**SYNOPSIS**

: **`gcloud dataflow snapshots describe` `[SNAPSHOT_ID](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/describe#SNAPSHOT_ID)` `[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/describe#--region)`=`REGION_ID` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/snapshots/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud Dataflow snapshot.

**EXAMPLES**

: To see details about a Cloud Dataflow snapshot, run:

```
gcloud dataflow snapshots describe SNAPSHOT_ID --region=SNAPSHOT_REGION
```

**POSITIONAL ARGUMENTS**

: **`SNAPSHOT_ID`**:
ID of the Cloud Dataflow snapshot.

**REQUIRED FLAGS**

: **--region**:
Region ID of the snapshot regional endpoint.

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
gcloud alpha dataflow snapshots describe
```

```
gcloud beta dataflow snapshots describe
```