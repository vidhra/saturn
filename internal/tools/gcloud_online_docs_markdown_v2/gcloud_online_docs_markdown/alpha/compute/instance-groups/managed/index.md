# gcloud alpha compute instance-groups managed  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed)*

**NAME**

: **gcloud alpha compute instance-groups managed - read and manipulate Compute Engine managed instance groups**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate Compute Engine managed instance groups.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[all-instances-config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config)`**:
`(ALPHA)` Override instance template settings for all instances in a
managed instance group.

**`[instance-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/instance-configs)`**:
`(ALPHA)` Manage instance-specific settings in a managed instance
group.

**`[resize-requests](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests)`**:
`(ALPHA)` List, create, delete, cancel, and describe ResizeRequests.

**`[rolling-action](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action)`**:
`(ALPHA)` Manipulate rolling actions on Compute Engine managed
instance groups.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[abandon-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/abandon-instances)`**:
`(ALPHA)` Abandon instances owned by a managed instance group.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/create)`**:
`(ALPHA)` Create a Compute Engine managed instance group.

**`[create-instance](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/create-instance)`**:
`(ALPHA)` Create a new virtual machine instance in a managed instance
group with a defined name and optionally its stateful configuration.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete)`**:
`(ALPHA)` Delete Compute Engine managed instance groups.

**`[delete-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances)`**:
`(ALPHA)` Delete instances that are managed by a managed instance
group.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/describe)`**:
`(ALPHA)` Display detailed information about an instance group.

**`[describe-instance](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/describe-instance)`**:
`(ALPHA)` Describe an instance in a managed instance group.

**`[export-autoscaling](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/export-autoscaling)`**:
`(ALPHA)` Export autoscaling parameters of a managed instance group.

**`[get-named-ports](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/get-named-ports)`**:
`(ALPHA)` Lists the named ports for an instance group resource.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/list)`**:
`(ALPHA)` List Google Compute Engine managed instance groups.

**`[list-errors](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/list-errors)`**:
`(ALPHA)` List errors produced by managed instances in a managed
instance group.

**`[list-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/list-instances)`**:
`(ALPHA)` List instances present in the managed instance group.

**`[recreate-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/recreate-instances)`**:
`(ALPHA)` Recreate instances managed by a managed instance group.

**`[resize](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize)`**:
`(ALPHA)` Set managed instance group size.

**`[resume-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resume-instances)`**:
`(ALPHA)` Resume the suspended instances in a managed instance group.

**`[set-autohealing](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing)`**:
`(ALPHA)` `(DEPRECATED)` Set autohealing policy for
managed instance group.

**`[set-autoscaling](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autoscaling)`**:
`(ALPHA)` Set autoscaling parameters of a managed instance group.

**`[set-instance-template](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-instance-template)`**:
`(ALPHA)` Set the instance template for a managed instance group.

**`[set-named-ports](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-named-ports)`**:
`(ALPHA)` Sets the list of named ports for an instance group.

**`[set-standby-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-standby-policy)`**:
`(ALPHA)` Set the standby policy for a managed instance group.

**`[set-target-pools](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-target-pools)`**:
`(ALPHA)` Set target pools of managed instance group.

**`[start-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/start-instances)`**:
`(ALPHA)` Start the stopped instances in a managed instance group.

**`[stop-autoscaling](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-autoscaling)`**:
`(ALPHA)` Stop autoscaling a managed instance group.

**`[stop-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances)`**:
`(ALPHA)` Stop instances owned by a managed instance group.

**`[suspend-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances)`**:
`(ALPHA)` Suspend instances owned by a managed instance group.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update)`**:
`(ALPHA)` Update a Compute Engine managed instance group.

**`[update-autoscaling](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling)`**:
`(ALPHA)` Update autoscaling parameters of a managed instance group.

**`[update-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-instances)`**:
`(ALPHA)` Immediately update selected instances in a Compute Engine
managed instance group.

**`[wait-until](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until)`**:
`(ALPHA)` Wait until the managed instance group reaches the desired
state.

**`[wait-until-stable](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until-stable)`**:
`(ALPHA)` `(DEPRECATED)` Waits until state of managed
instance group is stable.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instance-groups managed
```

```
gcloud beta compute instance-groups managed
```