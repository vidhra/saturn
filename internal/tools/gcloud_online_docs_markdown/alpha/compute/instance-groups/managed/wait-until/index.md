# gcloud alpha compute instance-groups managed wait-until  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until)*

**NAME**

: **gcloud alpha compute instance-groups managed wait-until - wait until the managed instance group reaches the desired state**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed wait-until` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until#NAME)` (`[--all-instances-config-effective](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until#--all-instances-config-effective)`     | `[--stable](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until#--stable)`     | `[--version-target-reached](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until#--version-target-reached)`) [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until#--timeout)`=`TIMEOUT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/wait-until#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Wait until the managed instance group reaches the desired
state.

**EXAMPLES**

: To wait until the managed instance group
``instance-group-1`` is stable, run:

```
gcloud alpha compute instance-groups managed wait-until --stable instance-group-1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--all-instances-config-effective**

**OPTIONAL FLAGS**

: **--timeout**:
Waiting time in seconds for the group to reach the desired state.

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
gcloud compute instance-groups managed wait-until
```

```
gcloud beta compute instance-groups managed wait-until
```