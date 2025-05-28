# gcloud billing accounts add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/billing/accounts/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/add-iam-policy-binding)*

**NAME**

: **gcloud billing accounts add-iam-policy-binding - add an IAM policy binding to a Cloud Billing account**

**SYNOPSIS**

: **`gcloud billing accounts add-iam-policy-binding` `[ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/add-iam-policy-binding#ACCOUNT)` `[--member](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/add-iam-policy-binding#--role)`=`ROLE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add an IAM policy binding to the IAM policy of a Cloud Billing account. A
binding consists of a member and a role.

**EXAMPLES**

: To add someone@example.com as a Billing Account Administrator for billing
account 123456-789876-543210, run:

```
gcloud billing accounts add-iam-policy-binding 123456-789876-543210 --member='user:someone@example.com' --role='roles/billing.admin'
```

**POSITIONAL ARGUMENTS**

: **Account resource - Name of the Cloud Billing account for which to add the IAM
policy binding. This represents a Cloud resource.
This must be specified.

**`ACCOUNT`**:
ID of the account or fully qualified identifier for the account.
To set the `account` attribute:

- provide the argument `account` on the command line.**

**REQUIRED FLAGS**

: **--member**:
The principal to add the binding for. Should be of the form
`user|group|serviceAccount:email` or `domain:domain`.
Examples: `user:test-user@gmail.com`,
`group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.
Some resources also accept the following special values:

- `allUsers` - Special identifier that represents anyone who is on the
internet, with or without a Google account.
- `allAuthenticatedUsers` - Special identifier that represents anyone
who is authenticated with a Google account or a service account.

**--role**:
Role name to assign to the principal. The role name is the complete path of a
predefined role, such as `roles/logging.viewer`, or the role ID for a
custom role, such as
`organizations/{ORGANIZATION_ID}/roles/logging.viewer`.

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
for this API can be found at: [https://cloud.google.com/billing/docs/apis](https://cloud.google.com/billing/docs/apis)

**NOTES**

: These variants are also available:

```
gcloud alpha billing accounts add-iam-policy-binding
```

```
gcloud beta billing accounts add-iam-policy-binding
```