# gcloud alpha compute instance-groups managed rolling-action  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action)*

**NAME**

: **gcloud alpha compute instance-groups managed rolling-action - manipulate rolling actions on Compute Engine managed instance groups**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed rolling-action` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate Compute Engine managed instance groups.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[replace](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/replace)`**:
`(ALPHA)` Replaces instances in a managed instance group.

**`[restart](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/restart)`**:
`(ALPHA)` Restarts instances in a managed instance group.

**`[start-update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/start-update)`**:
`(ALPHA)` Updates instances in a managed instance group.

**`[stop-proactive-update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action/stop-proactive-update)`**:
`(ALPHA)` Stop the proactive update process of managed instance
group.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instance-groups managed rolling-action
```

```
gcloud beta compute instance-groups managed rolling-action
```