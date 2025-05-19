# gcloud alpha billing projects unlink  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/unlink](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/unlink)*

**NAME**

: **gcloud alpha billing projects unlink - unlink the account (if any) linked with a project**

**SYNOPSIS**

: **`gcloud alpha billing projects unlink` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/unlink#PROJECT_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/unlink#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` This command unlinks a project from its associated billing
account. This action disables billing on the project. Any billable resources and
services in use in your project are stopped, and your application stops
functioning. Any costs accrued prior to disabling billing on the project are
charged to the previously associated billing account.
Note: To link a project to a different billing account, use the `billing
projects link` command. You do not need to unlink the project first.

**EXAMPLES**

: To unlink the project `my-project` from its linked billing account,
run:

```
gcloud alpha billing projects unlink my-project
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID`**:
Specify a project id.

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
gcloud billing projects unlink
```

```
gcloud beta billing projects unlink
```