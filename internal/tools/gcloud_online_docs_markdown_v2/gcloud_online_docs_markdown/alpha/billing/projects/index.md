# gcloud alpha billing projects  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects)*

**NAME**

: **gcloud alpha billing projects - manage the billing account configuration of your projects**

**SYNOPSIS**

: **`gcloud alpha billing projects` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage the billing account configuration of your projects.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/describe)`**:
`(ALPHA)` Show detailed billing information for a project.

**`[link](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link)`**:
`(ALPHA)` Link a project with a billing account.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list)`**:
`(ALPHA)` List all active projects associated with the specified
billing account.

**`[unlink](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/unlink)`**:
`(ALPHA)` Unlink the account (if any) linked with a project.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud billing projects
```

```
gcloud beta billing projects
```