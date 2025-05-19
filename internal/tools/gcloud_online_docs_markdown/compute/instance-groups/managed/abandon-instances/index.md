# gcloud compute instance-groups managed abandon-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances)*

**NAME**

: **gcloud compute instance-groups managed abandon-instances - abandon instances owned by a managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed abandon-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances#NAME)` `[--instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances#INSTANCE)`,…] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed abandon-instances` abandons
one or more instances from a managed instance group, thereby reducing the
targetSize of the group. Once instances have been abandoned, the currentSize of
the group is automatically reduced as well to reflect the change.
Abandoning an instance does not reboot or delete the underlying virtual machine
instances, but just removes the instances from the instance group. If you would
like to delete the underlying instances, use the `delete-instances`
command instead.
The command returns the operation status per instance, which might be
``FAIL``,
``SUCCESS``, or
``MEMBER_NOT_FOUND``.
``MEMBER_NOT_FOUND`` is returned only for
regional groups when the gcloud command-line tool wasn't able to resolve the
zone from the instance name.
For a more detailed overview of how abandoning instances from a managed instance
group works, see [Abandoning
instances from a MIG](https://cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances).

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--instances**:
Names of instances to abandon.

**OPTIONAL FLAGS**

: **--region**

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
gcloud alpha compute instance-groups managed abandon-instances
```

```
gcloud beta compute instance-groups managed abandon-instances
```