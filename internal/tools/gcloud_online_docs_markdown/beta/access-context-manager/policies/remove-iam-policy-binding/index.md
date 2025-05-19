# gcloud beta access-context-manager policies remove-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/remove-iam-policy-binding)*

**NAME**

: **gcloud beta access-context-manager policies remove-iam-policy-binding - remove IAM policy binding for an access policy**

**SYNOPSIS**

: **`gcloud beta access-context-manager policies remove-iam-policy-binding` [`[POLICY](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/remove-iam-policy-binding#POLICY)`] `[--member](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/remove-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/remove-iam-policy-binding#--role)`=`ROLE` [`[--all](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/remove-iam-policy-binding#--all)`     | `[--condition](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/remove-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/remove-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/remove-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Removes a policy binding to the IAM policy of an access
policy, given an access policy ID and the binding.

**EXAMPLES**

: To remove an IAM policy binding for the role of
``roles/editor`` for the user
'test-user@gmail.com' on the access policy 'accessPolicies/123', run:

```
gcloud beta access-context-manager policies remove-iam-policy-binding accessPolicies/123 --member='user:test-user@gmail.com' --role='roles/editor'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Policy resource - The access policy to remove the IAM binding. This represents a
Cloud resource.

**[`POLICY`]**:
ID of the policy or fully qualified identifier for the policy.
To set the `policy` attribute:

- provide the argument `policy` on the command line;
- set the property `access_context_manager/policy`;
- automatically, if the current account belongs to an organization with exactly
one access policy..**

**REQUIRED FLAGS**

: **--member**:
The principal to remove the binding for. Should be of the form
`user|group|serviceAccount:email` or `domain:domain`.
Examples: `user:test-user@gmail.com`,
`group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.
Deleted principals have an additional `deleted:` prefix and a
`?uid=UID` suffix, where ``UID`` is
a unique identifier for the principal. Example:
`deleted:user:test-user@gmail.com?uid=123456789012345678901`.
Some resources also accept the following special values:

- `allUsers` - Special identifier that represents anyone who is on the
internet, with or without a Google account.
- `allAuthenticatedUsers` - Special identifier that represents anyone
who is authenticated with a Google account or a service account.

**--role**:
The role to remove the principal from.

**OPTIONAL FLAGS**

: **--all**

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

: This command uses the `accesscontextmanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/access-context-manager/docs/reference/rest/](https://cloud.google.com/access-context-manager/docs/reference/rest/)

**NOTES**

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud access-context-manager policies remove-iam-policy-binding
```

```
gcloud alpha access-context-manager policies remove-iam-policy-binding
```