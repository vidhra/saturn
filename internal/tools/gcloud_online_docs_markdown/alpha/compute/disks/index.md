# gcloud alpha compute disks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks)*

**NAME**

: **gcloud alpha compute disks - read and manipulate Compute Engine disks**

**SYNOPSIS**

: **`gcloud alpha compute disks` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate Compute Engine disks.
For more information about disks, see the [disks documentation](https://cloud.google.com/compute/docs/disks/).
See also: [Disks
API](https://cloud.google.com/compute/docs/reference/rest/v1/disks).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[bulk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/bulk)`**:
`(ALPHA)` Manipulate multiple Compute Engine disks with single
command executions.

**`[config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/config)`**:
`(ALPHA)` Manage Compute Engine disk configurations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-iam-policy-binding)`**:
`(ALPHA)` Add IAM policy binding to a Compute Engine disk.

**`[add-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-labels)`**:
`(ALPHA)` Add labels to Google Compute Engine persistent disks.

**`[add-resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-resource-policies)`**:
`(ALPHA)` Add resource policies to a Compute Engine disk.

**`[convert](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/convert)`**:
`(ALPHA)` Convert a Compute Engine Persistent Disk volume to a
Hyperdisk volume.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create)`**:
`(ALPHA)` Create Compute Engine persistent disks.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/delete)`**:
`(ALPHA)` Delete a Compute Engine disk.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/describe)`**:
`(ALPHA)` Describe a Compute Engine disk.

**`[get-async-replication-status](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/get-async-replication-status)`**:
`(ALPHA)` Retrieves the status of asynchronous replication for a
Compute Engine persistent disk-pair.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/get-iam-policy)`**:
`(ALPHA)` Get the IAM policy for a Compute Engine disk.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/list)`**:
`(ALPHA)` List Google Compute Engine disks.

**`[move](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/move)`**:
`(ALPHA)` Move a disk between zones.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-iam-policy-binding)`**:
`(ALPHA)` Remove IAM policy binding from a Compute Engine disk.

**`[remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-labels)`**:
`(ALPHA)` Remove labels from Google Compute Engine persistent disks.

**`[remove-resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-resource-policies)`**:
`(ALPHA)` Remove resource policies from a Compute Engine disk.

**`[resize](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize)`**:
`(ALPHA)` Resize a disk or disks.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/set-iam-policy)`**:
`(ALPHA)` Set the IAM policy for a Compute Engine disk.

**`[snapshot](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/snapshot)`**:
`(ALPHA)` Create snapshots of Compute Engine persistent disks.

**`[start-async-replication](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication)`**:
`(ALPHA)` Start asynchronous replication on a Compute Engine
persistent disk.

**`[stop-async-replication](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/stop-async-replication)`**:
`(ALPHA)` Stop async replication on a Compute Engine persistent disk.

**`[stop-group-async-replication](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/stop-group-async-replication)`**:
`(ALPHA)` Consistently stops a group of asynchronously replicating
disks.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update)`**:
`(ALPHA)` Update a Compute Engine persistent disk.

**`[wait-for-replication-catchup](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup)`**:
`(ALPHA)` Provides the operation id for the asynchronous replication
of a Compute Engine persistent disk-pair that can be used to wait for the
replication to catch up.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute disks
```

```
gcloud beta compute disks
```