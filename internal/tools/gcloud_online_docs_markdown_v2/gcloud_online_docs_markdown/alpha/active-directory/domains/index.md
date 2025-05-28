# gcloud alpha active-directory domains  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains)*

**NAME**

: **gcloud alpha active-directory domains - manage Managed Microsoft AD domains**

**SYNOPSIS**

: **`gcloud alpha active-directory domains` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage Managed Microsoft AD domains.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[backups](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups)`**:
`(ALPHA)` Managed Microsoft AD Backups.

**`[migration](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration)`**:
`(ALPHA)` Manage Managed Microsoft AD domains.

**`[sql-integrations](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/sql-integrations)`**:
`(ALPHA)` Discover Cloud SQL integrations with Managed Microsoft AD
domains.

**`[trusts](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts)`**:
`(ALPHA)` Manage Managed Microsoft AD domains.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/create)`**:
`(ALPHA)` Create a Managed Microsoft AD domain.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/delete)`**:
`(ALPHA)` Delete a managed Microsoft Active Directory domain.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/describe)`**:
`(ALPHA)` Describe a Managed Microsoft AD domain.

**`[describe-ldaps-settings](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/describe-ldaps-settings)`**:
`(ALPHA)` Describe the LDAPS settings of a Managed Microsoft AD
domain.

**`[extend-schema](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/extend-schema)`**:
`(ALPHA)` Initiate schema extension for a Managed Microsoft AD
domain.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/get-iam-policy)`**:
`(ALPHA)` Describe the IAM policy for a Managed Microsoft AD domain.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/list)`**:
`(ALPHA)` List Managed Microsoft AD domains.

**`[reset-admin-password](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/reset-admin-password)`**:
`(ALPHA)` Reset the admin password for a Managed Microsoft AD domain.

**`[restore](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/restore)`**:
`(ALPHA)` Restore a domain from the specified backup.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/set-iam-policy)`**:
`(ALPHA)` Set the IAM policy for a Managed Microsoft AD domain.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update)`**:
`(ALPHA)` Update a Managed Microsoft AD domain.

**`[update-ldaps-settings](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings)`**:
`(ALPHA)` Update the LDAPS settings for a domain.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud active-directory domains
```

```
gcloud beta active-directory domains
```