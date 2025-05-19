# gcloud alpha compute disks get-async-replication-status  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/get-async-replication-status](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/get-async-replication-status)*

**NAME**

: **gcloud alpha compute disks get-async-replication-status - retrieves the status of asynchronous replication for a Compute Engine persistent disk-pair**

**SYNOPSIS**

: **`gcloud alpha compute disks get-async-replication-status` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/get-async-replication-status#DISK_NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/get-async-replication-status#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/get-async-replication-status#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/get-async-replication-status#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute disks
get-async-replication-status` fetches the current status of async
replication on a Compute Engine persistent disk-pair. This command can be
invoked on either the primary disk or the secondary-disk but the scope
respective to the disk must be provided.

**EXAMPLES**

: Replication status can be fetched by using either the primary or the secondary
disk. To get the current replication status of the disk-pair with the primary
disk 'primary-disk-1' in zone 'us-east1-a', and project 'my-project1' and the
secondary disk 'secondary-disk-1' in zone 'us-west1-a', and the project
'my-project2', the following commands can be used:

```
gcloud alpha compute disks get-async-replication-status primary-disk-1 --zone=us-east1-a --project=my-project1 or
gcloud alpha compute disks get-async-replication-status secondary-disk-1 --zone=us-west1-a --project=my-project2
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to operate on.

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
allowlist.