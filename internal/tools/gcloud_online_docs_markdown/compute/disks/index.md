# gcloud compute disks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/disks](https://cloud.google.com/sdk/gcloud/reference/compute/disks)*

**NAME**

: **gcloud compute disks - read and manipulate Compute Engine disks**

**SYNOPSIS**

: **`gcloud compute disks` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/disks#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/disks#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/disks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate Compute Engine disks.
For more information about disks, see the [disks documentation](https://cloud.google.com/compute/docs/disks/).
See also: [Disks
API](https://cloud.google.com/compute/docs/reference/rest/v1/disks).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[bulk](https://cloud.google.com/sdk/gcloud/reference/compute/disks/bulk)`**:
Manipulate multiple Compute Engine disks with single command executions.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/compute/disks/add-iam-policy-binding)`**:
Add IAM policy binding to a Compute Engine disk.

**`[add-labels](https://cloud.google.com/sdk/gcloud/reference/compute/disks/add-labels)`**:
Add labels to Google Compute Engine persistent disks.

**`[add-resource-policies](https://cloud.google.com/sdk/gcloud/reference/compute/disks/add-resource-policies)`**:
Add resource policies to a Compute Engine disk.

**`[convert](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert)`**:
Convert a Compute Engine Persistent Disk volume to a Hyperdisk volume.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/disks/create)`**:
Create Compute Engine persistent disks.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/disks/delete)`**:
Delete a Compute Engine disk.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/disks/describe)`**:
Describe a Compute Engine disk.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/compute/disks/get-iam-policy)`**:
Get the IAM policy for a Compute Engine disk.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/disks/list)`**:
List Google Compute Engine disks.

**`[move](https://cloud.google.com/sdk/gcloud/reference/compute/disks/move)`**:
Move a disk between zones.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-iam-policy-binding)`**:
Remove IAM policy binding from a Compute Engine disk.

**`[remove-labels](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels)`**:
Remove labels from Google Compute Engine persistent disks.

**`[remove-resource-policies](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-resource-policies)`**:
Remove resource policies from a Compute Engine disk.

**`[resize](https://cloud.google.com/sdk/gcloud/reference/compute/disks/resize)`**:
Resize a disk or disks.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/compute/disks/set-iam-policy)`**:
Set the IAM policy for a Compute Engine disk.

**`[snapshot](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot)`**:
Create snapshots of Compute Engine persistent disks.

**`[start-async-replication](https://cloud.google.com/sdk/gcloud/reference/compute/disks/start-async-replication)`**:
Start asynchronous replication on a Compute Engine persistent disk.

**`[stop-async-replication](https://cloud.google.com/sdk/gcloud/reference/compute/disks/stop-async-replication)`**:
Stop async replication on a Compute Engine persistent disk.

**`[stop-group-async-replication](https://cloud.google.com/sdk/gcloud/reference/compute/disks/stop-group-async-replication)`**:
Consistently stops a group of asynchronously replicating disks.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update)`**:
Update a Compute Engine persistent disk.

**NOTES**

: These variants are also available:

```
gcloud alpha compute disks
```

```
gcloud beta compute disks
```