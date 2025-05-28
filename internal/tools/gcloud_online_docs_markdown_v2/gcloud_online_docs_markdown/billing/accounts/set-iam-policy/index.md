# gcloud billing accounts set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/billing/accounts/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/set-iam-policy)*

**NAME**

: **gcloud billing accounts set-iam-policy - set the IAM policy for a Cloud Billing account**

**SYNOPSIS**

: **`gcloud billing accounts set-iam-policy` `[ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/set-iam-policy#ACCOUNT)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/billing/accounts/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud billing accounts set-iam-policy` sets the IAM policy for a
Cloud Billing account given an account ID and a JSON or YAML file that describes
the IAM policy.
Note: Setting the IAM policy for a Cloud Billing account replaces existing IAM
bindings for that account.

**EXAMPLES**

: The following command reads an IAM policy defined in the JSON file
`policy.json` and sets it for a Billing account ID
`123456-789876-543210`:

```
gcloud billing accounts set-iam-policy 123456-789876-543210 policy.json
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for policy file format and content details.

**POSITIONAL ARGUMENTS**

: **Account resource - The Cloud Billing account for which to display the IAM
policy. This represents a Cloud resource.
This must be specified.

**`ACCOUNT`**:
ID of the account or fully qualified identifier for the account.
To set the `account` attribute:

- provide the argument `account` on the command line.**

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

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
gcloud alpha billing accounts set-iam-policy
```

```
gcloud beta billing accounts set-iam-policy
```