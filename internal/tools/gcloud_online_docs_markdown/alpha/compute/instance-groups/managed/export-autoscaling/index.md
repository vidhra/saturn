# gcloud alpha compute instance-groups managed export-autoscaling  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/export-autoscaling](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/export-autoscaling)*

**NAME**

: **gcloud alpha compute instance-groups managed export-autoscaling - export autoscaling parameters of a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed export-autoscaling` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/export-autoscaling#NAME)` `[--autoscaling-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/export-autoscaling#--autoscaling-file)`=`PATH` [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/export-autoscaling#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/export-autoscaling#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/export-autoscaling#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups managed
export-autoscaling` exports the autoscaling parameters of the specified
managed instance group.
Autoscalers can use one or more autoscaling signals. Information on using
multiple autoscaling signals can be found here: [https://cloud.google.com/compute/docs/autoscaler/multiple-signals](https://cloud.google.com/compute/docs/autoscaler/multiple-signals)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--autoscaling-file**:
Path of the file to which autoscaling configuration will be written.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta compute instance-groups managed export-autoscaling
```