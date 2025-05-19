# gcloud alpha billing accounts projects link  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects/link](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects/link)*

**NAME**

: **gcloud alpha billing accounts projects link - link a project with a billing account**

**SYNOPSIS**

: **`gcloud alpha billing accounts projects link` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects/link#PROJECT_ID)` (`[--account-id](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects/link#--account-id)`=`ACCOUNT_ID`     | `[--billing-account](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects/link#--billing-account)`=`ACCOUNT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects/link#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `(DEPRECATED)` The `[gcloud alpha
billing accounts projects](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects)` group has been moved to `gcloud
billing projects`. Please use the new, shorter commands instead.
This command links a billing account to a project.
If the specified billing account is open, this enables billing on the project.

**EXAMPLES**

: To link a billing account `0X0X0X-0X0X0X-0X0X0X` with a project
`my-project`, run:

```
gcloud alpha billing accounts projects link my-project --billing-account=0X0X0X-0X0X0X-0X0X0X
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

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.