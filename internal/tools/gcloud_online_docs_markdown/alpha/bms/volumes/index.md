# gcloud alpha bms volumes  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes)*

**NAME**

: **gcloud alpha bms volumes - manage bare metal volumes in Bare Metal Solution**

**SYNOPSIS**

: **`gcloud alpha bms volumes` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage bare metal volumes in Bare Metal Solution.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[luns](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/luns)`**:
`(ALPHA)` Manage bare metal logical unit numbers (LUNs) in Bare Metal
Solution.

**`[snapshots](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/snapshots)`**:
`(ALPHA)` Manage snapshots for Bare Metal Solution volumes.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/describe)`**:
`(ALPHA)` Describe a Bare Metal Solution volume.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/list)`**:
`(ALPHA)` List Bare Metal Solution volumes in a project.

**`[rename](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/rename)`**:
`(ALPHA)` Rename a Bare Metal Solution volume.

**`[restore](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/restore)`**:
`(ALPHA)` Restore a Bare Metal Solution boot volume from an existing
snapshot.

**`[snapshot](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/snapshot)`**:
`(ALPHA)` Create a snapshot of a Bare Metal Solution boot volume.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update)`**:
`(ALPHA)` Update a Bare Metal Solution volume.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud bms volumes
```