# gcloud alpha compute instance-groups managed suspend-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances)*

**NAME**

: **gcloud alpha compute instance-groups managed suspend-instances - suspend instances owned by a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed suspend-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances#NAME)` `[--instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances#INSTANCE)`,…] [`[--force](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances#--force)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/suspend-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups managed
suspend-instances` suspends one or more instances from a managed instance
group, thereby reducing the targetSize and increasing the targetSuspendedSize of
the group.
The command returns the operation status per instance, which might be
``FAIL``,
``SUCCESS``, or
``MEMBER_NOT_FOUND``.
``MEMBER_NOT_FOUND`` is returned only for
regional groups when the gcloud command-line tool wasn't able to resolve the
zone from the instance name.

**EXAMPLES**

: To suspend an instance from a managed instance group in the us-central1-a zone,
run:

```
gcloud alpha compute instance-groups managed suspend-instances example-managed-instance-group --zone=us-central1-a --instances=example-instance
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--instances**:
Names of instances to suspend.

**OPTIONAL FLAGS**

: **--force**:
Immediately suspend the specified instances, skipping the initial delay, if one
is specified in the standby policy.

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
gcloud compute instance-groups managed suspend-instances
```

```
gcloud beta compute instance-groups managed suspend-instances
```