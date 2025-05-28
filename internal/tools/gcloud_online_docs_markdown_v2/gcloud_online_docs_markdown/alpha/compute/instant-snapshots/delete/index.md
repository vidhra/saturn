# gcloud alpha compute instant-snapshots delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots/delete)*

**NAME**

: **gcloud alpha compute instant-snapshots delete - delete a Compute Engine instant snapshot**

**SYNOPSIS**

: **`gcloud alpha compute instant-snapshots delete` `[INSTANT_SNAPSHOT_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots/delete#INSTANT_SNAPSHOT_NAME)` [`[INSTANT_SNAPSHOT_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots/delete#INSTANT_SNAPSHOT_NAME)` …] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots/delete#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots/delete#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instant-snapshots delete`
deletes a Compute Engine instant snapshot. A disk can be deleted only if it is
not attached to any virtual machine instances.

**EXAMPLES**

: To delete Compute Engine instant snapshots with the names 'instant-snapshot-1'
and 'instant-snapshot-2', run:

```
gcloud alpha compute instant-snapshots delete instant-snapshot-1 instant-snapshot-2
```

To list all instant snapshots that were created before a specific date, use the
--filter flag with the `[gcloud alpha
compute instant-snapshots list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots/list)` command.

```
gcloud alpha compute instant-snapshots list --filter="creationTimestamp<'2017-01-01'"
```

For more information on how to use --filter with the list command, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters).

**POSITIONAL ARGUMENTS**

: **`INSTANT_SNAPSHOT_NAME` [`INSTANT_SNAPSHOT_NAME` …]**:
Names of the instant snapshots to delete.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instant-snapshots delete
```

```
gcloud beta compute instant-snapshots delete
```