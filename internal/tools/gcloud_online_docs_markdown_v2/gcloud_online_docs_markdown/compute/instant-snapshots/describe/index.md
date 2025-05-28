# gcloud compute instant-snapshots describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/describe](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/describe)*

**NAME**

: **gcloud compute instant-snapshots describe - describe a Compute Engine instant snapshot**

**SYNOPSIS**

: **`gcloud compute instant-snapshots describe` `[INSTANT_SNAPSHOT_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/describe#INSTANT_SNAPSHOT_NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/describe#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/describe#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instant-snapshots describe` displays all data
associated with a Compute Engine instant snapshot in a project.

**EXAMPLES**

: To describe the instant snapshot 'instant-snapshot-1' in zone 'us-east1-a', run:

```
gcloud compute instant-snapshots describe instant-snapshot-1 --zone=us-east1-a
```

**POSITIONAL ARGUMENTS**

: **`INSTANT_SNAPSHOT_NAME`**:
Name of the instant snapshot to describe.

**FLAGS**

: **--region**

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
gcloud alpha compute instant-snapshots describe
```

```
gcloud beta compute instant-snapshots describe
```