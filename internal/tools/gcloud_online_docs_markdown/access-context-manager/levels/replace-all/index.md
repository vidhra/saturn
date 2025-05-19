# gcloud access-context-manager levels replace-all  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/replace-all](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/replace-all)*

**NAME**

: **gcloud access-context-manager levels replace-all - replace all existing access levels**

**SYNOPSIS**

: **`gcloud access-context-manager levels replace-all` [`[POLICY](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/replace-all#POLICY)`] `[--source-file](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/replace-all#--source-file)`=`SOURCE_FILE` [`[--etag](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/replace-all#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/replace-all#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Replace all existing access level in specified access policy with access levels
specified in a file.

**EXAMPLES**

: To replace all levels within a policy, using etag:

```
gcloud access-context-manager levels replace-all my-policy-number --source-file=path-to-file-containing-all-replacement-access-levels.yaml --etag=optional-latest-etag-of-policy
```

To replace all levels within a policy, without using etag:

```
gcloud access-context-manager levels replace-all my-policy-number --source-file=path-to-file-containing-all-replacement-access-levels.yaml
```

**POSITIONAL ARGUMENTS**

: **Policy resource - The access policy that contains the levels you want to
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
Path to a file containing a list of access levels.
An access level file is a YAML-formatted list of access levels, which are YAML
objects representing a Basic or Custom level as described in the API reference.
For example:

```
- name: accessPolicies/my_policy/accessLevels/my_level
  title: My Basic Level
  description: Basic level for foo.
  basic:
    combiningFunction: AND
    conditions:
    - ipSubnetworks:
      - 192.168.100.14/24
      - 2001:db8::/48
    - members
      - user1:user1@example.com
- name: accessPolicies/my_policy/accessLevels/my_other_level
  title: My Other Custom Level
  description: Custom level for bar.
  custom:
    expr:
      expression: "origin.region_code in ['US', 'CA']"
```

For more information about the alpha version, see: [https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels](https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels)
For other versions, see: [https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels)

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

: These variants are also available:

```
gcloud alpha access-context-manager levels replace-all
```

```
gcloud beta access-context-manager levels replace-all
```