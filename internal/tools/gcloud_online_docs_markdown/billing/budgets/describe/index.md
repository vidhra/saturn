# gcloud billing budgets describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/billing/budgets/describe](https://cloud.google.com/sdk/gcloud/reference/billing/budgets/describe)*

**NAME**

: **gcloud billing budgets describe - describe a budget**

**SYNOPSIS**

: **`gcloud billing budgets describe` (`[BUDGET](https://cloud.google.com/sdk/gcloud/reference/billing/budgets/describe#BUDGET)` : `[--billing-account](https://cloud.google.com/sdk/gcloud/reference/billing/budgets/describe#--billing-account)`=`BILLING_ACCOUNT`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/billing/budgets/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a budget.

**EXAMPLES**

: To describe the budget 'abc' in account '123', run:

```
gcloud billing budgets describe "billingAccounts/123/budgets/abc"
```

Alternatively, you can run:

```
gcloud billing budgets describe abc --billing-account=123
```

**POSITIONAL ARGUMENTS**

: **Budget resource - Billing budget to describe. The arguments in this group can be
used to specify the attributes of this resource.
This must be specified.

**`BUDGET`**:
ID of the budget or fully qualified identifier for the budget.
To set the `budget` attribute:

- provide the argument `budget` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--billing-account**:
The billing account.
To set the `billing-account` attribute:

- provide the argument `budget` on the command line with a fully
specified name;
- provide the argument `--billing-account` on the command line.**

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

**API REFERENCE**

: This command uses the `billingbudgets/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/billing/docs/how-to/budget-api-overview](https://cloud.google.com/billing/docs/how-to/budget-api-overview)

**NOTES**

: These variants are also available:

```
gcloud alpha billing budgets describe
```

```
gcloud beta billing budgets describe
```