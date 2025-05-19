# gcloud alpha compute instance-groups managed delete-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances)*

**NAME**

: **gcloud alpha compute instance-groups managed delete-instances - delete instances that are managed by a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed delete-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances#NAME)` `[--instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances#INSTANCE)`,…] [`[--skip-instances-on-validation-error](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances#--skip-instances-on-validation-error)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups managed
delete-instances` is used to delete one or more instances from a managed
instance group. Once the instances are deleted, the size of the group is
automatically reduced to reflect the changes.
The command returns the operation status per instance, which might be
``FAIL``,
``SUCCESS``,
``SKIPPED``, or
``MEMBER_NOT_FOUND``.
``MEMBER_NOT_FOUND`` is returned only for
regional groups when the gcloud command-line tool wasn't able to resolve the
zone from the instance name. ``SKIPPED`` is
returned only when the `--skip-instances-on-validation-error` flag is
used and the instance is not a member of the group or is already being deleted
or abandoned.
If you want to keep the underlying virtual machines but still remove them from
the managed instance group, use the abandon-instances command instead.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--instances**:
Names of instances to delete.

**OPTIONAL FLAGS**

: **--skip-instances-on-validation-error**:
Specifies whether the request should proceed even if the request includes
instances that are not members of the group or that are already being deleted or
abandoned. By default, if you omit this flag and such an instance is specified
in the request, the operation fails. The operation always fails if the request
contains a badly formatted instance name or a reference to an instance that
exists in a zone or region other than the group's zone or region.

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
gcloud compute instance-groups managed delete-instances
```

```
gcloud beta compute instance-groups managed delete-instances
```