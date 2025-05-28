# gcloud compute instance-groups managed instance-configs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete)*

**NAME**

: **gcloud compute instance-groups managed instance-configs delete - delete per-instance configs from a managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed instance-configs delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete#NAME)` `[--instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete#INSTANCE)`,…] [`[--instance-update-minimal-action](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete#--instance-update-minimal-action)`=`INSTANCE_UPDATE_MINIMAL_ACTION`; default="none"] [`[--no-update-instance](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete#--update-instance)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed instance-configs delete`
deletes one or more per-instance configs from a Google Compute Engine managed
instance group.
Changes are applied immediately to the corresponding instances, by performing
the necessary action (for example, REFRESH), unless overridden by providing the
``--no-update-instance`` flag.

**EXAMPLES**

: To delete the per-instance config from
``my-instance``, run:

```
gcloud compute instance-groups managed instance-configs delete my-group --region=europe-west4 --instances=my-instance
```

This removes all metadata and detaches all disks that were defined in the
per-instance config (except for disks that are also defined in the instance
template, which remain attached).

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to delete.

**REQUIRED FLAGS**

: **--instances**:
Names of instances to delete instance-configs from.

**OPTIONAL FLAGS**

: **--instance-update-minimal-action**:
Perform at least this action on the instance while updating, if
`--update-instance` is set to `true`.
`INSTANCE_UPDATE_MINIMAL_ACTION` must be one of:

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

**--update-instance**:
Apply the configuration changes immediately to the instance. If you disable this
flag, the managed instance group will apply the configuration update when you
next recreate or update the instance.
Example: say you have an instance with a disk attached to it and you created a
stateful configuration for the disk. If you decide to delete the stateful
configuration for the disk and you provide this flag, the group immediately
refreshes the instance and removes the stateful configuration for the disk.
Similarly if you have attached a new disk or changed its definition, with this
flag the group immediately refreshes the instance with the new configuration.
Enabled by default, use `--no-update-instance` to disable.

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
gcloud alpha compute instance-groups managed instance-configs delete
```

```
gcloud beta compute instance-groups managed instance-configs delete
```