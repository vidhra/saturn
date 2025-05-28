# gcloud alpha billing projects list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list)*

**NAME**

: **gcloud alpha billing projects list - list all active projects associated with the specified billing account**

**SYNOPSIS**

: **`gcloud alpha billing projects list` ([`[ACCOUNT_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list#ACCOUNT_ID)`] `[--billing-account](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list#--billing-account)`=`ACCOUNT_ID`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha billing projects list` ACCOUNT_ID
-- lists all active projects, for the specified billing account id.

**EXAMPLES**

: To list projects linked to billing account `0X0X0X-0X0X0X-0X0X0X`,
run:

```
gcloud alpha billing projects list 0X0X0X-0X0X0X-0X0X0X
```

**POSITIONAL ARGUMENTS**

: **Exactly one of these must be specified:

**[`ACCOUNT_ID`]**:
(DEPRECATED) Specify a billing account ID. Billing account IDs are of the form
`0X0X0X-0X0X0X-0X0X0X`. To see available IDs, run `$ [gcloud billing accounts
list](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/list)`.
The `ACCOUNT_ID` argument has been renamed
`--billing-account`.

**--billing-account**:
Specify a billing account ID. Billing account IDs are of the form
`0X0X0X-0X0X0X-0X0X0X`. To see available IDs, run `$ [gcloud billing accounts
list](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/list)`.**

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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

: This command uses the `cloudbilling/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/billing/v1/getting-started](https://cloud.google.com/billing/v1/getting-started)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud billing projects list
```

```
gcloud beta billing projects list
```