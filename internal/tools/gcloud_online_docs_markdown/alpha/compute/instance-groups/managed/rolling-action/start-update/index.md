# gcloud alpha compute instance-groups managed rolling-action start-update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update)*

**NAME**

: **gcloud alpha compute instance-groups managed rolling-action start-update - updates instances in a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed rolling-action start-update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#NAME)` `[--version](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--version)`=[`template`=`TEMPLATE`,[`name`=`NAME`],…] [`[--canary-version](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--canary-version)`=[`template`=`TEMPLATE`,`target-size`=`FIXED_OR_PERCENT`,[`name`=`NAME`],…]] [`[--type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--type)`=`TYPE`; default="proactive"] [`[--force](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--force)`] [`[--max-surge](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--max-surge)`=`MAX_SURGE`] [`[--max-unavailable](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--max-unavailable)`=`MAX_UNAVAILABLE`] [`[--min-ready](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--min-ready)`=`MIN_READY`] [`[--minimal-action](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--minimal-action)`=`MINIMAL_ACTION`] [`[--most-disruptive-allowed-action](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--most-disruptive-allowed-action)`=`MOST_DISRUPTIVE_ALLOWED_ACTION`] [`[--replacement-method](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--replacement-method)`=`REPLACEMENT_METHOD`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups managed
rolling-action start-update` updates instances in a managed instance
group, according to the given versions and the given update policy.
An instance template version can be either a global or regional resource.

**EXAMPLES**

: Running:

```
gcloud alpha compute instance-groups managed rolling-action start-update example-managed-instance-group \
--version='template=example-global-instance-template'
```

Sets the group's instance template version to a global instance template
resource 'example-global-instance-template'.
To use a regional instance template, specify the full or partial URL of the
template.
Running:

```
gcloud alpha compute instance-groups managed rolling-action start-update example-managed-instance-group \
--version='template=projects/example-project/regions/us-central1/instanceTemplates/example-regional-instance-template'
```

Sets the group's instance template version to a regional instance template
resource 'example-regional-instance-template'.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--version**:
Original instance template resource to be used. Each version has the following
format: template=TEMPLATE,[name=NAME]

**COMMONLY USED FLAGS**

: **--canary-version**:
New instance template resource to be used. Each version has the following
format: template=TEMPLATE,target-size=FIXED_OR_PERCENT,[name=NAME]

**--type**:
Desired update type. `TYPE` must be one of:

**`opportunistic`**:
Do not proactively replace VMs. Create new VMs and delete old ones on resizes of
the group and when you target specific VMs to be updated or recreated.

**`proactive`**:
Replace instances proactively.

**OTHER FLAGS**

: **--force**:
If set, accepts any original or new version configurations without validation.

**--max-surge**:
Maximum additional number of instances that can be created during the update
process. This can be a fixed number (e.g. 5) or a percentage of size to the
managed instance group (e.g. 10%). Defaults to 0 if the managed instance group
has stateful configuration, or to the number of zones in which it operates
otherwise.

**--max-unavailable**:
Maximum number of instances that can be unavailable during the update process.
This can be a fixed number (e.g. 5) or a percentage of size to the managed
instance group (e.g. 10%). Defaults to the number of zones in which the managed
instance group operates.

**--min-ready**:
Minimum time for which a newly created instance should be ready to be considered
available. For example `10s` for 10 seconds. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--minimal-action**:
Use this flag to minimize disruption as much as possible or to apply a more
disruptive action than is strictly necessary. The MIG performs at least this
action on each instance while updating. If the update requires a more disruptive
action than the one specified here, then the more disruptive action is
performed. If you omit this flag, the update uses the
``minimal-action`` value from the MIG's update
policy, unless it is not set in which case the default is
``replace``.
`MINIMAL_ACTION` must be one of:

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

**`refresh`**:
Apply the new configuration without stopping VMs, if possible. For example, use
``refresh`` to apply changes that only affect metadata or additional disks.

**`restart`**:
Apply the new configuration without replacing VMs, if possible. For example,
stopping VMs and starting them again is sufficient to apply changes to machine
type.

**`replace`**:
Replace old VMs according to the --replacement-method flag.

**--replacement-method**:
Type of replacement method. Specifies what action will be taken to update
instances. Defaults to ``recreate`` if the managed instance group has stateful
configuration, or to ``substitute`` otherwise.
`REPLACEMENT_METHOD` must be one of:

**`recreate`**:
Recreate instances and preserve the instance names. The instance IDs and
creation timestamps might change.

**`substitute`**:
Delete old instances and create instances with new names.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instance-groups managed rolling-action start-update
```

```
gcloud beta compute instance-groups managed rolling-action start-update
```