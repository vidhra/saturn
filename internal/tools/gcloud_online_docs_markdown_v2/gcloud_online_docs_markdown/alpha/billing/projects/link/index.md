# gcloud alpha billing projects link  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link)*

**NAME**

: **gcloud alpha billing projects link - link a project with a billing account**

**SYNOPSIS**

: **`gcloud alpha billing projects link` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link#PROJECT_ID)` (`[--account-id](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link#--account-id)`=`ACCOUNT_ID`     | `[--billing-account](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link#--billing-account)`=`ACCOUNT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` This command sets or updates the billing account associated
with a project.
Billing is enabled on a project when the project is linked to a valid, active
Cloud Billing account. The billing account accrues charges for the usage of
resources in all of the linked projects. If the project is already linked to a
billing account, this command moves the project to the billing account you
specify, updating the billing account that is linked to the project.
Note that associating a project with a closed billing account has the same
effect as disabling billing on the project: any paid resources in use by the
project are shut down, and your application stops functioning. Unless you want
to disable billing, you should always specify a valid, active Cloud Billing
account when you run this command. Learn how to confirm the status of a Cloud
Billing account at [https://cloud.google.com/billing/docs/how-to/verify-billing-enabled#billing_account_status](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled#billing_account_status)

**EXAMPLES**

: To link a billing account `0X0X0X-0X0X0X-0X0X0X` with a project
`my-project`, run:

```
gcloud alpha billing projects link my-project --billing-account=0X0X0X-0X0X0X-0X0X0X
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID`**:
Specify a project id.

**REQUIRED FLAGS**

: **--account-id**

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
gcloud billing projects link
```

```
gcloud beta billing projects link
```