# gcloud access-context-manager policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/delete](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/delete)*

**NAME**

: **gcloud access-context-manager policies delete - delete an access policy**

**SYNOPSIS**

: **`gcloud access-context-manager policies delete` [`[POLICY](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/delete#POLICY)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a given access policy.

**POSITIONAL ARGUMENTS**

: **Policy resource - The access policy you want to delete. This represents a Cloud
resource.

**[`POLICY`]**:
ID of the policy or fully qualified identifier for the policy.
To set the `policy` attribute:

- provide the argument `policy` on the command line;
- set the property `access_context_manager/policy`;
- automatically, if the current account belongs to an organization with exactly
one access policy..**

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

: These variants are also available:

```
gcloud alpha access-context-manager policies delete
```

```
gcloud beta access-context-manager policies delete
```