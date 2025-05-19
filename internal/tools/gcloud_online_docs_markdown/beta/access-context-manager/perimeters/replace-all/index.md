# gcloud beta access-context-manager perimeters replace-all  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/replace-all](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/replace-all)*

**NAME**

: **gcloud beta access-context-manager perimeters replace-all - replace all existing service perimeters**

**SYNOPSIS**

: **`gcloud beta access-context-manager perimeters replace-all` [`[POLICY](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/replace-all#POLICY)`] `[--source-file](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/replace-all#--source-file)`=`SOURCE_FILE` [`[--etag](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/replace-all#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/replace-all#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Replace all existing service perimeter in specified access
policy with service perimeters specified in a file.

**EXAMPLES**

: To replace all perimeters within a policy, using etag:

```
gcloud beta access-context-manager perimeters replace-all my-policy-number --source-file=path-to-file-containing-all-replacement-service-perimeters.yaml --etag=optional-latest-etag-of-policy
```

To replace all perimeters within a policy, without using etag:

```
gcloud beta access-context-manager perimeters replace-all my-policy-number --source-file=path-to-file-containing-all-replacement-service-perimeters.yaml
```

**POSITIONAL ARGUMENTS**

: **Policy resource - The access policy that contains the perimeters you want to
replace. This represents a Cloud resource.

**[`POLICY`]**:
ID of the policy or fully qualified identifier for the policy.
To set the `policy` attribute:

- provide the argument `policy` on the command line;
- set the property `access_context_manager/policy`;
- automatically, if the current account belongs to an organization with exactly
one access policy..**

**REQUIRED FLAGS**

: **--source-file**:
Path to a file containing a list of service perimeters.
An service perimeter file is a YAML-formatted list of service perimeters, which
are YAML objects representing a Condition as described in the API reference. For
example:

```
- name: my_perimeter
  title: My Perimeter
  description: Perimeter for foo.
  perimeterType: PERIMETER_TYPE_REGULAR
  status:
    resources:
    - projects/0123456789
    accessLevels:
    - accessPolicies/my_policy/accessLevels/my_level
    restrictedServices:
    - storage.googleapis.com
```

For more information about the alpha version, see: [https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters](https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters)
For other versions, see: [https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)

**OPTIONAL FLAGS**

: **--etag**:
An etag which specifies the version of the Access Policy. Only etags that
represent the latest version of the Access Policy will be accepted.

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
gcloud access-context-manager perimeters replace-all
```

```
gcloud alpha access-context-manager perimeters replace-all
```