# gcloud alpha compute disk-settings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings)*

**NAME**

: **gcloud alpha compute disk-settings - read Compute Engine disk settings**

**SYNOPSIS**

: **`gcloud alpha compute disk-settings` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Disks settings allows the configuration of various
disk-related behavior.
At this time, only the access location is allowed to be configured.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings/describe)`**:
`(ALPHA)` Describe a Google Compute Engine disk setting.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings/update)`**:
`(ALPHA)` Update disk settings.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta compute disk-settings
```