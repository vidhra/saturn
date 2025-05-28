# gcloud alpha compute instance-groups managed update-autoscaling  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling)*

**NAME**

: **gcloud alpha compute instance-groups managed update-autoscaling - update autoscaling parameters of a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed update-autoscaling` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#NAME)` [`[--clear-scale-down-control](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--clear-scale-down-control)`] [`[--cpu-utilization-predictive-method](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--cpu-utilization-predictive-method)`=`CPU_UTILIZATION_PREDICTIVE_METHOD`] [`[--max-num-replicas](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--max-num-replicas)`=`MAX_NUM_REPLICAS`] [`[--min-num-replicas](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--min-num-replicas)`=`MIN_NUM_REPLICAS`] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--mode)`=`MODE`] [`[--clear-scale-in-control](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--clear-scale-in-control)`     | `[--scale-in-control](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--scale-in-control)`=[`max-scaled-in-replicas`=`MAX-SCALED-IN-REPLICAS`],[`max-scaled-in-replicas-percent`=`MAX-SCALED-IN-REPLICAS-PERCENT`],[`time-window`=`TIME-WINDOW`]] [`[--disable-schedule](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--disable-schedule)`=`SCHEDULE_NAME`     | `[--enable-schedule](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--enable-schedule)`=`SCHEDULE_NAME`     | `[--remove-schedule](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--remove-schedule)`=`SCHEDULE_NAME`     | `[--set-schedule](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--set-schedule)`=`SCHEDULE_NAME`     | `[--update-schedule](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--update-schedule)`=`SCHEDULE_NAME`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--zone)`=`ZONE`] [`[--schedule-cron](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--schedule-cron)`=`CRON_EXPRESSION` `[--schedule-description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--schedule-description)`=`DESCRIPTION` `[--schedule-duration-sec](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--schedule-duration-sec)`=`DURATION` `[--schedule-min-required-replicas](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--schedule-min-required-replicas)`=`MIN_REQUIRED_REPLICAS` `[--schedule-time-zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#--schedule-time-zone)`=`TIME_ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups managed
update-autoscaling` updates autoscaling parameters of specified managed
instance group.
Autoscalers can use one or more autoscaling signals. Information on using
multiple autoscaling signals can be found here: [https://cloud.google.com/compute/docs/autoscaler/multiple-signals](https://cloud.google.com/compute/docs/autoscaler/multiple-signals)
In contrast to `[gcloud
alpha compute instance-groups managed set-autoscaling](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autoscaling)`, this command
`only` updates specified fields. For instance:

```
gcloud alpha compute instance-groups managed update-autoscaling --mode only-scale-out
```

would change the `mode` field of the autoscaler policy, but leave the
rest of the settings intact.

**EXAMPLES**

: To update an existing instance group:

```
gcloud alpha compute instance-groups managed update-autoscaling --mode=only-scale-out
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**FLAGS**

: **--clear-scale-down-control**:
If specified, the scale-down-control field will be cleared. Using this flag will
remove any configuration set by the now-deprecated
`--scale-down-control` flag. This is only useful if the MIG
configuration had scale-down-control set in the past.

**--cpu-utilization-predictive-method**:
Indicates whether to use a predictive algorithm when scaling based on CPU.
`CPU_UTILIZATION_PREDICTIVE_METHOD` must be one of:

**`none`**:
(Default) No predictions are made when calculating the number of VM instances.

**`optimize-availability`**:
Predictive autoscaling predicts the future values of the scaling metric and
scales the group in advance to ensure that new VM instances are ready in time to
cover the predicted peak.

**`standard`**:
Standard predictive autoscaling predicts the future values of the scaling metric
and then scales the group to ensure that new VM instances are ready in time to
cover the predicted peak.

**--max-num-replicas**:
Maximum number of replicas Autoscaler can set.

**--min-num-replicas**:
Minimum number of replicas Autoscaler can set.

**--mode**:
Set the mode of an autoscaler for a managed instance group.
You can turn off or restrict a group's autoscaler activities without affecting
your autoscaler configuration. The autoscaler configuration persists while the
activities are turned off or restricted, and the activities resume when the
autoscaler is turned on again or when the restrictions are lifted.
`MODE` must be one of:

**`off`**:
Turns off autoscaling, while keeping the new configuration.

**`on`**:
Permits autoscaling to scale out and in (default for new autoscalers).

**`only-scale-out`**:
Permits autoscaling to scale only out and not in.

**`only-up`**:
(DEPRECATED) Permits autoscaling to scale only out and not in.
Value `only-up` is deprecated. Use `--mode only-scale-out`
instead.

**--clear-scale-in-control**

**--disable-schedule**

**--region**

**--schedule-cron**:
Start time of the scaling schedule in cron format.
This is when the autoscaler starts creating new VMs, if the group's current size
is less than the minimum required instances. Set the start time to allow enough
time for new VMs to boot and initialize. For example if your workload takes 10
minutes from VM creation to start serving then set the start time 10 minutes
earlier than the time you need VMs to be ready.

**--schedule-description**:
A verbose description of the scaling schedule.

**--schedule-duration-sec**:
How long should the scaling schedule be active, measured in seconds.
Minimum duration is 5 minutes. A scaling schedule is active from its start time
and for its configured duration. During this time, the autoscaler scales the
group to have at least as many VMs as defined by the minimum required instances.
After the configured duration, if there is no need to maintain capacity, the
autoscaler starts removing instances after the usual stabilization period and
after scale-in controls (if configured). For more information, see [Delays
in scaling in](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#delays_in_scaling_in) and [Scale-in
controls](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#scale-in_controls). This ensures you don't accidentally lose capacity immediately
after the scaling schedule ends.

**--schedule-min-required-replicas**:
How many VMs the autoscaler should provision for the duration of this scaling
schedule.
Autoscaler provides at least this number of instances when the scaling schedule
is active. A managed instance group can have more VMs if there are other scaling
schedules active with more required instances or if another signal (for example,
scaling based on CPU) requires more instances to meet its target.
This configuration does not change autoscaling minimum and maximum instance
limits which are always in effect. Autoscaler does not create more than the
maximum number of instances configured for a group.

**--schedule-time-zone**:
Name of the timezone that the scaling schedule's start time is in.
It should be provided as a name from the IANA tz database (for example
Europe/Paris or UTC). It automatically adjusts for daylight savings time (DST).
If no time zone is provided, UTC is used as a default.
See [https://en.wikipedia.org/wiki/List_of_tz_database_time_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
for the list of valid timezones.

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
gcloud compute instance-groups managed update-autoscaling
```

```
gcloud beta compute instance-groups managed update-autoscaling
```