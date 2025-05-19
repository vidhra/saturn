# gcloud alpha compute instance-groups  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups)*

**NAME**

: **gcloud alpha compute instance-groups - read and manipulate Compute Engine instance groups**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate Compute Engine instance groups.
To accommodate the differences between managed and unmanaged instances, some
commands (such as `delete`) are in the managed or unmanaged
subgroups.
For more information about instance groups, see the [instance groups
documentation](https://cloud.google.com/compute/docs/instance-groups/).
See also: [Instance
groups API](https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroups).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[managed](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed)`**:
`(ALPHA)` Read and manipulate Compute Engine managed instance groups.

**`[unmanaged](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/unmanaged)`**:
`(ALPHA)` Read and manipulate Compute Engine unmanaged instance
group.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/describe)`**:
`(ALPHA)` Display detailed information about an instance group.

**`[get-named-ports](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/get-named-ports)`**:
`(ALPHA)` Lists the named ports for an instance group resource.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list)`**:
`(ALPHA)` List Google Compute Engine instance groups.

**`[list-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances)`**:
`(ALPHA)` List instances present in the instance group.

**`[set-named-ports](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/set-named-ports)`**:
`(ALPHA)` Sets the list of named ports for an instance group.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instance-groups
```

```
gcloud beta compute instance-groups
```