# gcloud alpha access-context-manager policies set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/set-iam-policy)*

**NAME**

: **gcloud alpha access-context-manager policies set-iam-policy - set IAM policy for an access policy**

**SYNOPSIS**

: **`gcloud alpha access-context-manager policies set-iam-policy` [`[POLICY](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/set-iam-policy#POLICY)`] `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Sets the IAM policy for a access policy, given access
policy ID and a file encoded in JSON or YAML that contains the IAM policy.

**EXAMPLES**

: The following command reads an IAM policy defined in a JSON file
`policy.json` and sets it for the access policy with the ID
`accessPolicies/1234`:

```
gcloud alpha access-context-manager policies set-iam-policy accessPolicies/1234 policy.json
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**POSITIONAL ARGUMENTS**

: **Policy resource - The access policy to set the IAM policy for. This represents a
Cloud resource.

**[`POLICY`]**:
ID of the policy or fully qualified identifier for the policy.
To set the `policy` attribute:

- provide the argument `policy` on the command line;
- set the property `access_context_manager/policy`;
- automatically, if the current account belongs to an organization with exactly
one access policy..**

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

: This command uses the `accesscontextmanager/v1alpha` API. The full
documentation for this API can be found at: [https://cloud.google.com/access-context-manager/docs/reference/rest/](https://cloud.google.com/access-context-manager/docs/reference/rest/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-context-manager policies set-iam-policy
```

```
gcloud beta access-context-manager policies set-iam-policy
```