# gcloud alpha billing  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/billing](https://cloud.google.com/sdk/gcloud/reference/alpha/billing)*

**NAME**

: **gcloud alpha billing - manage billing accounts and associate them with projects**

**SYNOPSIS**

: **`gcloud alpha billing` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/billing#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/billing#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage billing accounts and associate them with projects.

**EXAMPLES**

: To list billing accounts associated with the current user, run:

```
gcloud alpha billing accounts list
```

To link one of the billing accounts `0X0X0X-0X0X0X-0X0X0X` with a
project `my-project`, run:

```
gcloud alpha billing projects link my-project --billing-account 0X0X0X-0X0X0X-0X0X0X
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[accounts](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts)`**:
`(ALPHA)` Manage billing accounts.

**`[budgets](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/budgets)`**:
`(ALPHA)` Manage the budgets of your billing accounts.

**`[projects](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects)`**:
`(ALPHA)` Manage the billing account configuration of your projects.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud billing
```

```
gcloud beta billing
```