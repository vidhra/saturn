# gcloud compute instance-groups managed update-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances)*

**NAME**

: **gcloud compute instance-groups managed update-instances - immediately update selected instances in a Compute Engine managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed update-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances#NAME)` (`[--all-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances#--all-instances)`     | `[--instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances#INSTANCE)`,…]) [`[--minimal-action](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances#--minimal-action)`=`MINIMAL_ACTION`; default="none"] [`[--most-disruptive-allowed-action](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances#--most-disruptive-allowed-action)`=`MOST_DISRUPTIVE_ALLOWED_ACTION`; default="replace"] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: When using a managed instance group, it's possible that your intended
specification for a VM is different from the current state of that VM. For
example, this can happen due to changes to the group's target instance template.
This command enables you to initiate the update process on the given set of
instances instantly, thus when your Managed Instance Group is stable you can be
sure that all the changes were applied.
`gcloud compute instance-groups managed update-instances` allows you
to specify the least and the most disruptive actions that can be performed while
updating the instances. This way you can reduce the risk of rolling out too many
changes at once. Possible actions are: `none`, `refresh`,
`restart` and `replace`. The level of disruption to the
instance is ordered as: `none` < `refresh` <
`restart` < `replace`.
The command returns the operation status per instance, which might be
``FAIL``,
``SUCCESS``, or
``MEMBER_NOT_FOUND``.
``MEMBER_NOT_FOUND`` is returned only for
regional groups when the gcloud command-line tool wasn't able to resolve the
zone from the instance name.

**EXAMPLES**

: To update instances `instance-1`, `instance-2` in
`my-group`, with `minimal-action=none` and
`most-disruptive-allowed-action=restart`, run:

```
gcloud compute instance-groups managed update-instances my-group --instances=instance-1,instance2 --minimal-action=none --most-disruptive-allowed-action=restart
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--all-instances**

**OPTIONAL FLAGS**

: **--minimal-action**:
Use this flag to minimize disruption as much as possible or to apply a more
disruptive action than is strictly necessary. The MIG performs at least this
action on each instance while updating. If the update requires a more disruptive
action than the one specified here, then the more disruptive action is
performed. If you omit this flag, the update uses the
``minimal-action`` value from the MIG's update
policy, unless it is not set in which case the default is
``replace``.
`MINIMAL_ACTION` must be one of:

**`none`**:
No action

**`refresh`**:
Apply the new configuration without stopping VMs, if possible. For example, use
``refresh`` to apply changes that only affect metadata or additional disks.

**`restart`**:
Apply the new configuration without replacing VMs, if possible. For example,
stopping VMs and starting them again is sufficient to apply changes to machine
type.

**`replace`**:
Replace old VMs according to the --replacement-method flag.

**--most-disruptive-allowed-action**:
Use this flag to prevent an update if it requires more disruption than you can
afford. At most, the MIG performs the specified action on each instance while
updating. If the update requires a more disruptive action than the one specified
here, then the update fails and no changes are made. If you omit this flag, the
update uses the
``most-disruptive-allowed-action`` value from
the MIG's update policy, unless it is not set in which case the default is
``replace``.
`MOST_DISRUPTIVE_ALLOWED_ACTION` must be one of:

**`none`**:
No action

**`refresh`**:
Apply the new configuration without stopping VMs, if possible. For example, use
``refresh`` to apply changes that only affect metadata or additional disks.

**`restart`**:
Apply the new configuration without replacing VMs, if possible. For example,
stopping VMs and starting them again is sufficient to apply changes to machine
type.

**`replace`**:
Replace old VMs according to the --replacement-method flag.

**--region**

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
gcloud alpha compute instance-groups managed update-instances
```

```
gcloud beta compute instance-groups managed update-instances
```