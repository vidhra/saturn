# gcloud alpha active-directory domains trusts  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts)*

**NAME**

: **gcloud alpha active-directory domains trusts - manage Managed Microsoft AD domains**

**SYNOPSIS**

: **`gcloud alpha active-directory domains trusts` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage Managed Microsoft AD domains.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts/create)`**:
`(ALPHA)` Create a Microsoft Active Directory Trust between a Managed
Microsoft AD domain and another domain.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts/delete)`**:
`(ALPHA)` Delete an Active Directory Trust between a Managed
Microsoft AD domain and a target domain.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts/update)`**:
`(ALPHA)` Update target DNS IP addresses for a Managed Microsoft AD
trust.

**`[validate-state](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts/validate-state)`**:
`(ALPHA)` Validate the state of a Managed Microsoft AD trust.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud active-directory domains trusts
```

```
gcloud beta active-directory domains trusts
```