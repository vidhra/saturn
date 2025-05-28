# gcloud compute instances set-scheduling  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling)*

**NAME**

: **gcloud compute instances set-scheduling - set scheduling options for Compute Engine virtual machines**

**SYNOPSIS**

: **`gcloud compute instances set-scheduling` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#INSTANCE_NAME)` [`[--clear-min-node-cpu](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--clear-min-node-cpu)`] [`[--host-error-timeout-seconds](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--host-error-timeout-seconds)`=`HOST_ERROR_TIMEOUT_SECONDS`] [`[--local-ssd-recovery-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--local-ssd-recovery-timeout)`=`LOCAL_SSD_RECOVERY_TIMEOUT`] [`[--maintenance-policy](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--maintenance-policy)`=`MAINTENANCE_POLICY`] [`[--min-node-cpu](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--min-node-cpu)`=`MIN_NODE_CPU`] [`[--[no-]preemptible](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--[no-]preemptible)`] [`[--provisioning-model](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--provisioning-model)`=`PROVISIONING_MODEL`] [`[--[no-]restart-on-failure](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--[no-]restart-on-failure)`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--zone)`=`ZONE`] [`[--clear-discard-local-ssds-at-termination-timestamp](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--clear-discard-local-ssds-at-termination-timestamp)`     | `[--discard-local-ssds-at-termination-timestamp](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--discard-local-ssds-at-termination-timestamp)`=`DISCARD_LOCAL_SSDS_AT_TERMINATION_TIMESTAMP`] [`[--clear-instance-termination-action](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--clear-instance-termination-action)`     | `[--instance-termination-action](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--instance-termination-action)`=`INSTANCE_TERMINATION_ACTION`] [`[--clear-max-run-duration](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--clear-max-run-duration)`     | `[--max-run-duration](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--max-run-duration)`=`MAX_RUN_DURATION`] [`[--clear-node-affinities](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--clear-node-affinities)`     | `[--node](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--node)`=`NODE`     | `[--node-affinity-file](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--node-affinity-file)`=`PATH_TO_FILE`     | `[--node-group](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--node-group)`=`NODE_GROUP`] [`[--clear-termination-time](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--clear-termination-time)`     | `[--termination-time](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--termination-time)`=`TERMINATION_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `$gcloud compute instances set-scheduling` is used to update
scheduling options for VM instances. You can only call this method on a VM
instance that is stopped (a VM instance in a `TERMINATED` state).

**EXAMPLES**

: To set instance to be terminated during maintenance, run:

```
gcloud compute instances set-scheduling example-instance --maintenance-policy=TERMINATE --zone=us-central1-b
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--clear-min-node-cpu**:
Removes the min-node-cpu field from the instance. If specified, the instance
min-node-cpu will be cleared. The instance will not be overcommitted and utilize
the full CPU count assigned.

**--host-error-timeout-seconds**:
The timeout in seconds for host error detection. The value must be set with 30
second increments, with a range of 90 to 330 seconds. If unset, the default
behavior of the host error recovery is used.

**--local-ssd-recovery-timeout**:
Specifies the maximum amount of time a Local Ssd Vm should wait while recovery
of the Local Ssd state is attempted. Its value should be in between 0 and 168
hours with hour granularity and the default value being 1 hour.

**--maintenance-policy**:
Specifies the behavior of the VMs when their host machines undergo maintenance.
The default is MIGRATE. For more information, see [https://cloud.google.com/compute/docs/instances/host-maintenance-options](https://cloud.google.com/compute/docs/instances/host-maintenance-options).
`MAINTENANCE_POLICY` must be one of:

**`MIGRATE`**:
The instances should be migrated to a new host. This will temporarily impact the
performance of instances during a migration event.

**`TERMINATE`**:
The instances should be terminated.

**--min-node-cpu**:
Minimum number of virtual CPUs this instance will consume when running on a
sole-tenant node.

**--[no-]preemptible**:
If provided, instances will be preemptible and time-limited. Instances might be
preempted to free up resources for standard VM instances, and will only be able
to run for a limited amount of time. Preemptible instances can not be restarted
and will not migrate. Use `--preemptible` to enable and
`--no-preemptible` to disable.

**--provisioning-model**:
Specifies the provisioning model for your VM instances. This choice affects the
price, availability, and how long your VM instances can run.
`PROVISIONING_MODEL` must be one of:

**`RESERVATION_BOUND`**:
The VM instances run for the entire duration of their associated reservation.
You can only specify this provisioning model if you want your VM instances to
consume a specific reservation with either a calendar reservation mode or a
dense deployment type.

**`SPOT`**:
Compute Engine may stop a Spot VM instance whenever it needs capacity. Because
Spot VM instances don't have a guaranteed runtime, they come at a discounted
price.

**`STANDARD`**:
The default option. The STANDARD provisioning model gives you full control over
your VM instances' runtime.

**--[no-]restart-on-failure**:
The instances will be restarted if they are terminated by Compute Engine. This
does not affect terminations performed by the user. This option is mutually
exclusive with --preemptible. Use `--restart-on-failure` to enable
and `--no-restart-on-failure` to disable.

**--zone**:
Zone of the instance to operate on. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

**--clear-discard-local-ssds-at-termination-timestamp**

**--clear-instance-termination-action**

**--clear-max-run-duration**

**--clear-node-affinities**

**--clear-termination-time**

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
gcloud alpha compute instances set-scheduling
```

```
gcloud beta compute instances set-scheduling
```