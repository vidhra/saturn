# gcloud compute instance-groups  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups)*

**NAME**

: **gcloud compute instance-groups - read and manipulate Compute Engine instance groups**

**SYNOPSIS**

: **`gcloud compute instance-groups` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate Compute Engine instance groups.
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

**`[managed](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed)`**:
Read and manipulate Compute Engine managed instance groups.

**`[unmanaged](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged)`**:
Read and manipulate Compute Engine unmanaged instance group.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/describe)`**:
Display detailed information about an instance group.

**`[get-named-ports](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/get-named-ports)`**:
Lists the named ports for an instance group resource.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/list)`**:
List Google Compute Engine instance groups.

**`[list-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/list-instances)`**:
List instances present in the instance group.

**`[set-named-ports](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/set-named-ports)`**:
Sets the list of named ports for an instance group.

**NOTES**

: These variants are also available:

```
gcloud alpha compute instance-groups
```

```
gcloud beta compute instance-groups
```