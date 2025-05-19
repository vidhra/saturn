# gcloud alpha compute instance-groups managed set-standby-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-standby-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-standby-policy)*

**NAME**

: **gcloud alpha compute instance-groups managed set-standby-policy - set the standby policy for a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed set-standby-policy` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-standby-policy#NAME)` [`[--initial-delay](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-standby-policy#--initial-delay)`=`INITIAL_DELAY`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-standby-policy#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-standby-policy#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-standby-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups managed
set-standby-policy` sets the fields in the standby policy for a managed
instance group. The standby policy dictates the behaviour of standby (stopped
and suspended) instances

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**FLAGS**

: **--initial-delay**:
Initialization delay before stopping or suspending instances in this managed
instance group. For example: 5m or 300s. See `[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)`
for information on duration formats.

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
allowlist.