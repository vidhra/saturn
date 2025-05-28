# gcloud billing  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/billing](https://cloud.google.com/sdk/gcloud/reference/billing)*

**NAME**

: **gcloud billing - manage billing accounts and associate them with projects**

**SYNOPSIS**

: **`gcloud billing` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/billing#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/billing#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage billing accounts and associate them with projects.

**EXAMPLES**

: To list billing accounts associated with the current user, run:

```
gcloud billing accounts list
```

To link one of the billing accounts `0X0X0X-0X0X0X-0X0X0X` with a
project `my-project`, run:

```
gcloud billing projects link my-project --billing-account 0X0X0X-0X0X0X-0X0X0X
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[accounts](https://cloud.google.com/sdk/gcloud/reference/billing/accounts)`**:
Manage billing accounts.

**`[budgets](https://cloud.google.com/sdk/gcloud/reference/billing/budgets)`**:
Manage the budgets of your billing accounts.

**`[projects](https://cloud.google.com/sdk/gcloud/reference/billing/projects)`**:
Manage the billing account configuration of your projects.

**NOTES**

: These variants are also available:

```
gcloud alpha billing
```

```
gcloud beta billing
```