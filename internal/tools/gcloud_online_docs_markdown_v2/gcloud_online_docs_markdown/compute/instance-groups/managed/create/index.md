# gcloud compute instance-groups managed create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create)*

**NAME**

: **gcloud compute instance-groups managed create - create a Compute Engine managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#NAME)` `[--size](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--size)`=`SIZE` `[--template](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--template)`=`TEMPLATE` [`[--base-instance-name](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--base-instance-name)`=`BASE_INSTANCE_NAME`] [`[--default-action-on-vm-failure](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--default-action-on-vm-failure)`=`ACTION_ON_VM_FAILURE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--description)`=`DESCRIPTION`] [`[--[no-]force-update-on-repair](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--[no-]force-update-on-repair)`] [`[--initial-delay](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--initial-delay)`=`INITIAL_DELAY`] [`[--instance-redistribution-type](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--instance-redistribution-type)`=`TYPE`] [`[--instance-selection](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--instance-selection)`=`name`=`NAME`,`machine-type`=`MACHINE_TYPE`[,`machine-type`=`MACHINE_TYPE`…][,`rank`=`RANK`]] [`[--instance-selection-machine-types](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--instance-selection-machine-types)`=[`MACHINE_TYPE`,…]] [`[--list-managed-instances-results](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--list-managed-instances-results)`=`MODE`] [`[--standby-policy-initial-delay](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--standby-policy-initial-delay)`=`STANDBY_POLICY_INITIAL_DELAY`] [`[--standby-policy-mode](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--standby-policy-mode)`=`STANDBY_POLICY_MODE`] [`[--stateful-disk](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--stateful-disk)`=[`auto-delete`=`AUTO-DELETE`],[`device-name`=`DEVICE-NAME`]] [`[--stateful-external-ip](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--stateful-external-ip)`=[`enabled`],[`auto-delete`=`AUTO-DELETE`],[`interface-name`=`INTERFACE-NAME`]] [`[--stateful-internal-ip](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--stateful-internal-ip)`=[`enabled`],[`auto-delete`=`AUTO-DELETE`],[`interface-name`=`INTERFACE-NAME`]] [`[--stopped-size](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--stopped-size)`=`STOPPED_SIZE`] [`[--suspended-size](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--suspended-size)`=`SUSPENDED_SIZE`] [`[--target-distribution-shape](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--target-distribution-shape)`=`SHAPE`] [`[--target-pool](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--target-pool)`=[`TARGET_POOL`,…]] [`[--zones](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--zones)`=`ZONE`,[`[ZONE](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#ZONE)`,…]] [`[--health-check](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--health-check)`=`HEALTH_CHECK`     | `[--http-health-check](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--http-health-check)`=`HTTP_HEALTH_CHECK`     | `[--https-health-check](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--https-health-check)`=`HTTPS_HEALTH_CHECK`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--zone)`=`ZONE`] [`[--update-policy-max-surge](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--update-policy-max-surge)`=`MAX_SURGE` `[--update-policy-max-unavailable](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--update-policy-max-unavailable)`=`MAX_UNAVAILABLE` `[--update-policy-minimal-action](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--update-policy-minimal-action)`=`UPDATE_POLICY_MINIMAL_ACTION` `[--update-policy-most-disruptive-action](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--update-policy-most-disruptive-action)`=`UPDATE_POLICY_MOST_DISRUPTIVE_ACTION` `[--update-policy-replacement-method](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--update-policy-replacement-method)`=`UPDATE_POLICY_REPLACEMENT_METHOD` `[--update-policy-type](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--update-policy-type)`=`UPDATE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed create` creates a Compute
Engine managed instance group.

**EXAMPLES**

: Running:

```
gcloud compute instance-groups managed create example-managed-instance-group --zone=us-central1-a --template=example-global-instance-template --size=1
```

will create a managed instance group called 'example-managed-instance-group' in
the ``us-central1-a`` zone with a global
instance template resource 'example-global-instance-template'.
To use a regional instance template, specify the full or partial URL of the
template.
Running:

```
gcloud compute instance-groups managed create example-managed-instance-group --zone=us-central1-a --template=projects/example-project/regions/us-central1/instanceTemplates/example-regional-instance-template --size=1
```

will create a managed instance group called 'example-managed-instance-group' in
the ``us-central1-a`` zone with a regional
instance template resource 'example-regional-instance-template'.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to create.

**REQUIRED FLAGS**

: **--size**:
Initial number of instances you want in this group.

**--template**:
Specifies the instance template to use when creating new instances. An instance
template is either a global or regional resource.

**OPTIONAL FLAGS**

: **--base-instance-name**:
Base name to use for the Compute Engine instances that will be created with the
managed instance group. If not provided base instance name will be the prefix of
instance group name.

**--default-action-on-vm-failure**:
Specifies the action that a MIG performs on a failed or an unhealthy VM. A VM is
marked as unhealthy when the application running on that VM fails a health
check. By default, the value of the flag is set to
``repair``.
`ACTION_ON_VM_FAILURE` must be one of:

**`do-nothing`**:
MIG does not repair a failed or an unhealthy VM.

**`repair`**:
MIG automatically repairs a failed or an unhealthy VM.

**--description**:
An optional description for this group.

**--[no-]force-update-on-repair**:
Specifies whether to apply the group's latest configuration when repairing a VM.
If you updated the group's instance template or per-instance configurations
after the VM was created, then these changes are applied when VM is repaired. If
this flag is disabled with
``-no-force-update-on-repair``, then updates
are applied in accordance with the group's update policy type. By default, this
flag is disabled. Use `--force-update-on-repair` to enable and
`--no-force-update-on-repair` to disable.

**--initial-delay**:
Specifies the number of seconds that a new VM takes to initialize and run its
startup script. During a VM's initial delay period, the MIG ignores unsuccessful
health checks because the VM might be in the startup process. This prevents the
MIG from prematurely recreating a VM. If the health check receives a healthy
response during the initial delay, it indicates that the startup process is
complete and the VM is ready. The value of initial delay must be between 0 and
3600 seconds. The default value is 0. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

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
Use this argument multiple times to attach more disks.

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
External IPs considered stateful by the instance group. Managed instance groups
preserve stateful IPs on VM autohealing, update, and recreate events.
Use this argument multiple times to make more external IPs stateful.
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
Internal IPs considered stateful by the instance group. Managed instance groups
preserve stateful IPs on VM autohealing, update, and recreate events.
Use this argument multiple times to make more internal IPs stateful.
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

**--target-pool**:
Specifies any target pools you want the instances of this managed instance group
to be part of.

**--zones**:
If this flag is specified a regional managed instance group will be created. The
managed instance group will be in the same region as specified zones and will
spread instances in it between specified zones.
All zones must belong to the same region. You may specify --region flag but it
must be the region to which zones belong. This flag is mutually exclusive with
--zone flag.

**--health-check**

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

: These variants are also available:

```
gcloud alpha compute instance-groups managed create
```

```
gcloud beta compute instance-groups managed create
```