# gcloud alpha compute instance-groups managed update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update)*

**NAME**

: **gcloud alpha compute instance-groups managed update - update a Compute Engine managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#NAME)` [`[--action-on-vm-failed-health-check](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--action-on-vm-failed-health-check)`=`ACTION_ON_FAILED_HEALTH_CHECK`] [`[--default-action-on-vm-failure](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--default-action-on-vm-failure)`=`ACTION_ON_VM_FAILURE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--description)`=`DESCRIPTION`] [`[--[no-]force-update-on-repair](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--[no-]force-update-on-repair)`] [`[--instance-redistribution-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--instance-redistribution-type)`=`TYPE`] [`[--instance-selection](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--instance-selection)`=`name`=`NAME`,`machine-type`=`MACHINE_TYPE`[,`machine-type`=`MACHINE_TYPE`…][,`rank`=`RANK`]] [`[--instance-selection-machine-types](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--instance-selection-machine-types)`=[`MACHINE_TYPE`,…]] [`[--list-managed-instances-results](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--list-managed-instances-results)`=`MODE`] [`[--remove-instance-selections](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--remove-instance-selections)`=[`INSTANCE_SELECTION_NAME`,…]] [`[--remove-instance-selections-all](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--remove-instance-selections-all)`] [`[--remove-stateful-disks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--remove-stateful-disks)`=`DEVICE_NAME`,[`[DEVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#DEVICE_NAME)`,…]] [`[--remove-stateful-external-ips](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--remove-stateful-external-ips)`=`INTERFACE_NAME`,[…]] [`[--remove-stateful-internal-ips](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--remove-stateful-internal-ips)`=`INTERFACE_NAME`,[…]] [`[--size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--size)`=`SIZE`] [`[--standby-policy-initial-delay](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--standby-policy-initial-delay)`=`STANDBY_POLICY_INITIAL_DELAY`] [`[--standby-policy-mode](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--standby-policy-mode)`=`STANDBY_POLICY_MODE`] [`[--stateful-disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--stateful-disk)`=[`auto-delete`=`AUTO-DELETE`],[`device-name`=`DEVICE-NAME`]] [`[--stateful-external-ip](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--stateful-external-ip)`=[`enabled`],[`auto-delete`=`AUTO-DELETE`],[`interface-name`=`INTERFACE-NAME`]] [`[--stateful-internal-ip](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--stateful-internal-ip)`=[`enabled`],[`auto-delete`=`AUTO-DELETE`],[`interface-name`=`INTERFACE-NAME`]] [`[--stopped-size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--stopped-size)`=`STOPPED_SIZE`] [`[--suspended-size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--suspended-size)`=`SUSPENDED_SIZE`] [`[--target-distribution-shape](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--target-distribution-shape)`=`SHAPE`] [`[--clear-autohealing](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--clear-autohealing)`     | `[--initial-delay](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--initial-delay)`=`INITIAL_DELAY` `[--health-check](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--health-check)`=`HEALTH_CHECK`     | `[--http-health-check](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--http-health-check)`=`HTTP_HEALTH_CHECK`     | `[--https-health-check](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--https-health-check)`=`HTTPS_HEALTH_CHECK`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--zone)`=`ZONE`] [`[--update-policy-max-surge](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--update-policy-max-surge)`=`MAX_SURGE` `[--update-policy-max-unavailable](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--update-policy-max-unavailable)`=`MAX_UNAVAILABLE` `[--update-policy-min-ready](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--update-policy-min-ready)`=`MIN_READY` `[--update-policy-minimal-action](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--update-policy-minimal-action)`=`UPDATE_POLICY_MINIMAL_ACTION` `[--update-policy-most-disruptive-action](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--update-policy-most-disruptive-action)`=`UPDATE_POLICY_MOST_DISRUPTIVE_ACTION` `[--update-policy-replacement-method](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--update-policy-replacement-method)`=`UPDATE_POLICY_REPLACEMENT_METHOD` `[--update-policy-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#--update-policy-type)`=`UPDATE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Compute Engine managed instance group.
`gcloud alpha compute instance-groups managed update` allows you to
specify or modify the description and group policies for an existing managed
instance group, including the group's update policy and optional autohealing and
stateful policies
The group's update policy defines how an updated VM configuration is applied to
existing VMs in the group. For more information, see [Applying new
configurations]
(https://cloud.google.com/compute/docs/instance-groups/updating-migs) to VMs in
a MIG.
A stateful policy defines which resources should be preserved across the group.
When instances in the group are recreated, stateful resources are preserved.
This command allows you to update stateful resources, specifically to add or
remove stateful disks.
When updating the autohealing policy, you can specify the health check, initial
delay, or both. If either field is unspecified, its value won't be modified. If
`--health-check` is specified, the health check monitors the health
of your application. Whenever the health check signal for an instance becomes
`UNHEALTHY`, the autohealer recreates the instance.
If no health check exists, instance autohealing is triggered only by instance
status: if an instance is not `RUNNING`, the group recreates it.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to update.

**FLAGS**

: **--action-on-vm-failed-health-check**:
Specifies the action that a MIG performs on an unhealthy VM. A VM is marked as
unhealthy when the application running on that VM fails a health check. By
default, the value of the flag is set to
``default-action``.
`ACTION_ON_FAILED_HEALTH_CHECK` must be one of:

**`default-action`**:
(Default) MIG uses the same action configured for the defaultActionOnFailure
field.

**`do-nothing`**:
MIG does not repair an unhealthy VM.

**`repair`**:
MIG automatically repairs an unhealthy VM by recreating it.

**--default-action-on-vm-failure**:
Specifies the action that a MIG performs on a failed VM. If the value of the
onFailedHealthCheck field is `DEFAULT_ACTION`, then the same action
also applies to the VMs on which your application fails a health check. By
default, the value of the flag is set to
``repair``.
`ACTION_ON_VM_FAILURE` must be one of:

**`repair`**:
(Default) MIG automatically repairs a failed VM by recreating it.

**`do-nothing`**:
MIG does not repair a failed VM.

**`delete`**:
MIG deletes a failed VM. Deleting the VM decreases the target size of the MIG.

**--description**:
An optional description for this group. To clear the description, set the value
to an empty string.

**--[no-]force-update-on-repair**:
Specifies whether to apply the group's latest configuration when repairing a VM.
If you updated the group's instance template or per-instance configurations
after the VM was created, then these changes are applied when VM is repaired. If
this flag is disabled with
``-no-force-update-on-repair``, then updates
are applied in accordance with the group's update policy type. By default, this
flag is disabled. Use `--force-update-on-repair` to enable and
`--no-force-update-on-repair` to disable.

**--instance-redistribution-type**:
Specifies the type of the instance redistribution policy. An instance
redistribution type lets you enable or disable automatic instance redistribution
across zones to meet the group's target distribution shape.
An instance redistribution type can be specified only for a non-autoscaled
regional managed instance group. By default it is set to
``proactive``.
`TYPE` must be one of:

**`none`**:
The managed instance group does not redistribute instances across zones.

**`proactive`**:
The managed instance group proactively redistributes instances to meet its
target distribution.

**--instance-selection**:
Named selection of machine types with an optional rank. For example,
`--instance-selection="name=instance-selection-1,machine-type=e2-standard-8,machine-type=t2d-standard-8,rank=0"`

**--instance-selection-machine-types**:
Machine types that are used to create VMs in the managed instance group. If not
provided, the machine type specified in the instance template is used.

**--list-managed-instances-results**:
Pagination behavior for the group's listManagedInstances API method. This flag
does not affect the group's gcloud or console list-instances behavior. By
default it is set to ``pageless``.
`MODE` must be one of:

**`pageless`**:
Pagination is disabled for the group's listManagedInstances API method.
maxResults and pageToken query parameters are ignored and all instances are
returned in a single response.

**`paginated`**:
Pagination is enabled for the group's listManagedInstances API method.
maxResults and pageToken query parameters are respected.

**--remove-instance-selections**:
Remove specific instance selections from the instance flexibility policy.

**--remove-instance-selections-all**:
Remove all instance selections from the instance flexibility policy.

**--remove-stateful-disks**:
Remove stateful configuration for the specified disks.

**--remove-stateful-external-ips**:
Remove stateful configuration for the specified interfaces for external IPs.

**--remove-stateful-internal-ips**:
Remove stateful configuration for the specified interfaces for internal IPs.

**--size**:
Target number of running instances in managed instance group.

**--standby-policy-initial-delay**:
Specifies the number of seconds that the MIG should wait before suspending or
stopping a VM. The initial delay gives the initialization script the time to
prepare your VM for a quick scale out.

**--standby-policy-mode**:
Defines how a MIG resumes or starts VMs from a standby pool when the group
scales out. The default mode is ``manual``.
`STANDBY_POLICY_MODE` must be one of:

**`manual`**:
MIG does not automatically resume or start VMs in the standby pool when the
group scales out.

**`scale-out-pool`**:
MIG automatically resumes or starts VMs in the standby pool when the group
scales out, and replenishes the standby pool afterwards.

**--stateful-disk**:
Disks considered stateful by the instance group. Managed instance groups
preserve and reattach stateful disks on VM autohealing, update, and recreate
events.
Use this argument multiple times to update more disks.
If a stateful disk with the given device name already exists in the current
instance configuration, its properties will be replaced by the newly provided
ones. Otherwise, a new stateful disk definition will be added to the instance
configuration.

**`device-name`**:
(Required) Device name of the disk to mark stateful.

**`auto-delete`**:
(Optional) Specifies the auto deletion policy of the stateful disk. The
following options are available:

- ``never``: (Default) Never delete this disk.
Instead, detach the disk when its instance is deleted.
- ``on-permanent-instance-deletion``: Delete the
stateful disk when the instance that it's attached to is permanently deleted
from the group; for example, when the instance is deleted manually or when the
group size is decreased.

**--stateful-external-ip**:
Managed instance groups preserve stateful IPs on VM autohealing, update, and
recreate events.
Use this argument multiple times to update more IPs.
If a stateful external IP with the given interface name already exists in the
current instance configuration, its properties are replaced by the newly
provided ones. Otherwise, a new stateful external IP definition is added to the
instance configuration.
At least one of the following is required:

**`enabled`**:
Marks the IP address as stateful. The network interface named
``nic0`` is assumed by default when
``interface-name`` is not specified. This flag
can be omitted when ``interface-name`` is
provided explicitly.

**`interface-name`**:
Marks the IP address from this network interface as stateful. This flag can be
omitted when ``enabled`` is provided.
Additional arguments:

**`auto-delete`**:
(Optional) Prescribes what should happen to an associated static Address
resource when a VM instance is permanently deleted. Regardless of the value of
the delete rule, stateful IP addresses are always preserved on instance
autohealing, update, and recreation operations. The following options are
available:

- ``never``: (Default) Never delete the static IP
address. Instead, unassign the address when its instance is permanently deleted
and keep the address reserved.
- ``on-permanent-instance-deletion``: Delete the
static IP address reservation when the instance that it's assigned to is
permanently deleted from the instance group; for example, when the instance is
deleted manually or when the group size is decreased.

**--stateful-internal-ip**:
Managed instance groups preserve stateful IPs on VM autohealing, update, and
recreate events.
Use this argument multiple times to update more IPs.
If a stateful internal IP with the given interface name already exists in the
current instance configuration, its properties are replaced by the newly
provided ones. Otherwise, a new stateful internal IP definition is added to the
instance configuration.
At least one of the following is required:

**`enabled`**:
Marks the IP address as stateful. The network interface named
``nic0`` is assumed by default when
``interface-name`` is not specified. This flag
can be omitted when ``interface-name`` is
provided explicitly.

**`interface-name`**:
Marks the IP address from this network interface as stateful. This flag can be
omitted when ``enabled`` is provided.
Additional arguments:

**`auto-delete`**:
(Optional) Prescribes what should happen to an associated static Address
resource when a VM instance is permanently deleted. Regardless of the value of
the delete rule, stateful IP addresses are always preserved on instance
autohealing, update, and recreation operations. The following options are
available:

- ``never``: (Default) Never delete the static IP
address. Instead, unassign the address when its instance is permanently deleted
and keep the address reserved.
- ``on-permanent-instance-deletion``: Delete the
static IP address reservation when the instance that it's assigned to is
permanently deleted from the instance group; for example, when the instance is
deleted manually or when the group size is decreased.

**--stopped-size**:
Specifies the target size of stopped VMs in the group.

**--suspended-size**:
Specifies the target size of suspended VMs in the group.

**--target-distribution-shape**:
Specifies how a regional managed instance group distributes its instances across
zones within the region. The default shape is
``even``. `SHAPE` must be
one of:

**`any`**:
The group picks zones for creating VM instances to fulfill the requested number
of VMs within present resource constraints and to maximize utilization of unused
zonal reservations. Recommended for batch workloads that do not require high
availability.

**`any-single-zone`**:
The group schedules all instances within a single zone. The zone is chosen based
on hardware support, current resources availability, and matching reservations.
The group might not be able to create the requested number of VMs in case of
zonal resource availability constraints. Recommended for workloads requiring
extensive communication between VMs.

**`balanced`**:
The group prioritizes acquisition of resources, scheduling VMs in zones where
resources are available while distributing VMs as evenly as possible across
selected zones to minimize the impact of zonal failure. Recommended for highly
available serving or batch workloads that do not require autoscaling.

**`even`**:
The group schedules VM instance creation and deletion to achieve and maintain an
even number of managed instances across the selected zones. The distribution is
even when the number of managed instances does not differ by more than 1 between
any two zones. Recommended for highly available serving workloads.

**--clear-autohealing**

**--region**

**--update-policy-max-surge**

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
gcloud compute instance-groups managed update
```

```
gcloud beta compute instance-groups managed update
```