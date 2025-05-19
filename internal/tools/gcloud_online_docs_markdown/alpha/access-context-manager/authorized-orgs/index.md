# gcloud alpha access-context-manager authorized-orgs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs)*

**NAME**

: **gcloud alpha access-context-manager authorized-orgs - manage Access Context Manager authorized organizations descriptions**

**SYNOPSIS**

: **`gcloud alpha access-context-manager authorized-orgs` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` An authorized organizations description describes a list of
organizations (1) that have been authorized to use certain asset (for example,
device) data owned by different organizations at the enforcement points, or (2)
with certain asset (for example, device) have been authorized to access the
resources in another organization at the enforcement points.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs/create)`**:
`(ALPHA)` Create a new authorized organizations description.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs/delete)`**:
`(ALPHA)` Delete an authorized organizations description.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs/describe)`**:
`(ALPHA)` Show details about an authorized organizations description.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs/list)`**:
`(ALPHA)` List authorized organizations descriptions.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs/update)`**:
`(ALPHA)` Update the organizations for an existing authorized
organizations description.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud access-context-manager authorized-orgs
```