# gcloud compute instance-groups managed  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed)*

**NAME**

: **gcloud compute instance-groups managed - read and manipulate Compute Engine managed instance groups**

**SYNOPSIS**

: **`gcloud compute instance-groups managed` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate Compute Engine managed instance groups.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[all-instances-config](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config)`**:
Override instance template settings for all instances in a managed instance
group.

**`[instance-configs](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs)`**:
Manage instance-specific settings in a managed instance group.

**`[resize-requests](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests)`**:
List, create, delete, cancel, and describe ResizeRequests.

**`[rolling-action](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action)`**:
Manipulate rolling actions on Compute Engine managed instance groups.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[abandon-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances)`**:
Abandon instances owned by a managed instance group.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create)`**:
Create a Compute Engine managed instance group.

**`[create-instance](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create-instance)`**:
Create a new virtual machine instance in a managed instance group with a defined
name and optionally its stateful configuration.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete)`**:
Delete Compute Engine managed instance groups.

**`[delete-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete-instances)`**:
Delete instances that are managed by a managed instance group.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe)`**:
Display detailed information about an instance group.

**`[describe-instance](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe-instance)`**:
Describe an instance in a managed instance group.

**`[get-named-ports](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/get-named-ports)`**:
Lists the named ports for an instance group resource.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list)`**:
List Google Compute Engine managed instance groups.

**`[list-errors](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors)`**:
List errors produced by managed instances in a managed instance group.

**`[list-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances)`**:
List instances present in the managed instance group.

**`[recreate-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/recreate-instances)`**:
Recreate instances managed by a managed instance group.

**`[resize](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize)`**:
Set managed instance group size.

**`[resume-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances)`**:
Resume the suspended instances in a managed instance group.

**`[set-autoscaling](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling)`**:
Set autoscaling parameters of a managed instance group.

**`[set-instance-template](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template)`**:
Set the instance template for a managed instance group.

**`[set-named-ports](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports)`**:
Sets the list of named ports for an instance group.

**`[set-target-pools](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools)`**:
Set target pools of managed instance group.

**`[start-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/start-instances)`**:
Start the stopped instances in a managed instance group.

**`[stop-autoscaling](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/stop-autoscaling)`**:
Stop autoscaling a managed instance group.

**`[stop-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/stop-instances)`**:
Stop instances owned by a managed instance group.

**`[suspend-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/suspend-instances)`**:
Suspend instances owned by a managed instance group.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update)`**:
Update a Compute Engine managed instance group.

**`[update-autoscaling](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-autoscaling)`**:
Update autoscaling parameters of a managed instance group.

**`[update-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances)`**:
Immediately update selected instances in a Compute Engine managed instance
group.

**`[wait-until](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until)`**:
Wait until the managed instance group reaches the desired state.

**`[wait-until-stable](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable)`**:
`(DEPRECATED)` Waits until state of managed instance group is stable.

**NOTES**

: These variants are also available:

```
gcloud alpha compute instance-groups managed
```

```
gcloud beta compute instance-groups managed
```