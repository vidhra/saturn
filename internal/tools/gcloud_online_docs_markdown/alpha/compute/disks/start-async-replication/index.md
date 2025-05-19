# gcloud alpha compute disks start-async-replication  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication)*

**NAME**

: **gcloud alpha compute disks start-async-replication - start asynchronous replication on a Compute Engine persistent disk**

**SYNOPSIS**

: **`gcloud alpha compute disks start-async-replication` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication#DISK_NAME)` `[--secondary-disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication#--secondary-disk)`=`SECONDARY_DISK` (`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication#--zone)`=`ZONE`) (`[--secondary-disk-region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication#--secondary-disk-region)`=`SECONDARY_DISK_REGION`     | `[--secondary-disk-zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication#--secondary-disk-zone)`=`SECONDARY_DISK_ZONE`) [`[--secondary-disk-project](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication#--secondary-disk-project)`=`SECONDARY_DISK_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute disks
start-async-replication` starts async replication on a Compute Engine
persistent disk. This command must be invoked on the primary disk and
`--secondary-disk` must be provided.

**EXAMPLES**

: Start replication from the primary disk 'my-disk-1' in zone us-east1-a to the
secondary disk 'my-disk-2' in zone us-west1-a:

```
gcloud alpha compute disks start-async-replication my-disk-1 --zone=us-east1-a --secondary-disk=my-disk-2 --secondary-disk-zone=us-west1-a
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to operate on.

**REQUIRED FLAGS**

: **--secondary-disk**:
Secondary disk for asynchronous replication. This flag is required when starting
replication.

**--region**

**--secondary-disk-region**

**SECONDARY DISK FLAGS**

: **--secondary-disk-project**:
Project of the secondary disk for asynchronous replication.

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
gcloud compute disks start-async-replication
```

```
gcloud beta compute disks start-async-replication
```