# gcloud compute snapshots delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete)*

**NAME**

: **gcloud compute snapshots delete - delete Compute Engine snapshots**

**SYNOPSIS**

: **`gcloud compute snapshots delete` `[SNAPSHOT_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete#SNAPSHOT_NAME)` [`[SNAPSHOT_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete#SNAPSHOT_NAME)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute snapshots delete` deletes one or more Compute Engine
snapshots.

**EXAMPLES**

: To delete Compute Engine snapshots with the names 'snapshot-1' and 'snapshot-2',
run:

```
gcloud compute snapshots delete snapshot-1 snapshot-2
```

To list all snapshots that were created before a specific date, use the --filter
flag with the `[gcloud compute snapshots
list](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/list)` command.

```
gcloud compute snapshots list --filter="creationTimestamp<'2017-01-01'"
```

For more information on how to use --filter with the list command, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters).

**POSITIONAL ARGUMENTS**

: **`SNAPSHOT_NAME` [`SNAPSHOT_NAME` …]**:
Names of the snapshots to delete.

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
gcloud alpha compute snapshots delete
```

```
gcloud beta compute snapshots delete
```