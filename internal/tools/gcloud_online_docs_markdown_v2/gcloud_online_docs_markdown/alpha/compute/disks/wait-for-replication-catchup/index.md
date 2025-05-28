# gcloud alpha compute disks wait-for-replication-catchup  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup)*

**NAME**

: **gcloud alpha compute disks wait-for-replication-catchup - provides the operation id for the asynchronous replication of a Compute Engine persistent disk-pair that can be used to wait for the replication to catch up**

**SYNOPSIS**

: **`gcloud alpha compute disks wait-for-replication-catchup` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup#DISK_NAME)` [`[--max-wait-duration](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup#--max-wait-duration)`=`MAX_WAIT_DURATION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute disks
wait-for-replication-catchup` fetches the operation id that can be used to
track the status of async replication for a Compute Engine persistent disk-pair.
The operation id can be used to wait for the replication to catch up. This
command can be invoked only on the primary disk.

**EXAMPLES**

: Note: The max-wait-duration is optional. If not specified, the default value
would be picked up from the API. Wait for replication catchup can only be
invoked on the primary scope. To wait for the replication catchup for the
primary disk 'my-disk-1' in zone 'us-east1-a' under project 'my-project1' to
catch up with the secondary disk 'my-disk-2' in zone 'us-west1-a' in any
project, the following command can be used (with custom wait duration of 20s):

```
gcloud alpha compute disks wait-for-replication-catchup my-disk-1 --zone=us-east1-a --project=my-project1 --max-wait-duration=20s
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to operate on.

**FLAGS**

: **--max-wait-duration**:
Maximum duration to wait for the replication catchup.

**--region**

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
allowlist.