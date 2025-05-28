# gcloud bms volumes  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bms/volumes](https://cloud.google.com/sdk/gcloud/reference/bms/volumes)*

**NAME**

: **gcloud bms volumes - manage bare metal volumes in Bare Metal Solution**

**SYNOPSIS**

: **`gcloud bms volumes` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/bms/volumes#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/bms/volumes#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bms/volumes#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage bare metal volumes in Bare Metal Solution.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[luns](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/luns)`**:
Manage bare metal logical unit numbers (LUNs) in Bare Metal Solution.

**`[snapshots](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshots)`**:
Manage snapshots for Bare Metal Solution volumes.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/describe)`**:
Describe a Bare Metal Solution volume.

**`[list](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/list)`**:
List Bare Metal Solution volumes in a project.

**`[rename](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/rename)`**:
Rename a Bare Metal Solution volume.

**`[restore](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/restore)`**:
Restore a Bare Metal Solution boot volume from an existing snapshot.

**`[snapshot](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshot)`**:
Create a snapshot of a Bare Metal Solution boot volume.

**`[update](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/update)`**:
Update a Bare Metal Solution volume.

**NOTES**

: This variant is also available:

```
gcloud alpha bms volumes
```