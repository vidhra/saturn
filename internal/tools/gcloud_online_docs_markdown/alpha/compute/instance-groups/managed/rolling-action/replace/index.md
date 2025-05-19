# gcloud alpha compute instance-groups managed rolling-action replace  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace)*

**NAME**

: **gcloud alpha compute instance-groups managed rolling-action replace - replaces instances in a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed rolling-action replace` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace#NAME)` [`[--max-surge](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace#--max-surge)`=`MAX_SURGE`] [`[--max-unavailable](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace#--max-unavailable)`=`MAX_UNAVAILABLE`] [`[--min-ready](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace#--min-ready)`=`MIN_READY`] [`[--replacement-method](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace#--replacement-method)`=`REPLACEMENT_METHOD`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Deletes the existing instance and creates a new instance
from the target template. The Updater creates a brand new instance with all new
instance properties, such as new internal and external IP addresses.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**FLAGS**

: **--max-surge**:
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
gcloud compute instance-groups managed rolling-action replace
```

```
gcloud beta compute instance-groups managed rolling-action replace
```