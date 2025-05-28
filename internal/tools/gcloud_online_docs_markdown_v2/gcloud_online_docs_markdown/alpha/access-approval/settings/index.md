# gcloud alpha access-approval settings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings)*

**NAME**

: **gcloud alpha access-approval settings - manage Access Approval settings**

**SYNOPSIS**

: **`gcloud alpha access-approval settings` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Access Approval settings can be set on projects, folders,
or organizations. The settings apply hierarchically. For example, enabling
Access Approval at the organization level enables it for all folders and
projects under the organization.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/delete)`**:
`(ALPHA)` Delete Access Approval settings.

**`[get](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/get)`**:
`(ALPHA)` Get Access Approval settings.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/update)`**:
`(ALPHA)` Update Access Approval settings.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-approval settings
```

```
gcloud beta access-approval settings
```