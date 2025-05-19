# gcloud access-context-manager cloud-bindings list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/list](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/list)*

**NAME**

: **gcloud access-context-manager cloud-bindings list - list cloud access bindings under an organization**

**SYNOPSIS**

: **`gcloud access-context-manager cloud-bindings list` [`[--organization](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/list#--organization)`=`ORGANIZATION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List cloud access bindings.

**EXAMPLES**

: To list cloud access bindings, run:

```
gcloud access-context-manager cloud-bindings list
```

This command prints a list of Google Cloud user access bindings,
`gcpUserAccessBindings`, in YAML format. By default, the binding is
printed in the following format:

```
---
accessLevels:
- accessPolicies/9522/accessLevels/device_trusted
dryRunAccessLevels:
- accessPolicies/9522/accessLevels/specific_location
groupKey: a3dad
name: organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N
sessionSettings:
  sessionLength: 57600s
  sessionLengthEnabled: true
  sessionReauthMethod: LOGIN
```

Or

```
---
accessLevels:
- accessPolicies/9522/accessLevels/device_trusted
dryRunAccessLevels:
- accessPolicies/9522/accessLevels/specific_location
groupKey: a3dad
name: organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N
scopedAccessSettings:
- activeSettings:
    accessLevels:
    - accessPolicies/9522/accessLevels/device_trusted
  dryRunSettings:
    accessLevels:
    - accessPolicies/9522/accessLevels/specific_location
  scope:
    clientScope:
      restrictedClientApplication:
        clientId: 123.apps.googleusercontent.com
- activeSettings:
    accessLevels:
    - accessPolicies/9522/accessLevels/device_trusted
  dryRunSettings:
    accessLevels:
    - accessPolicies/9522/accessLevels/specific_location
  scope:
    clientScope:
      restrictedClientApplication:
        name: Cloud Console
- activeSettings:
    sessionSettings:
      sessionLength: 57600s
      sessionLengthEnabled: true
      sessionReauthMethod: LOGIN
  scope:
    clientScope:
      restrictedClientApplication:
        clientId: 123.apps.googleusercontent.com
sessionSettings:
  sessionLength: 57600s
  sessionLengthEnabled: true
  sessionReauthMethod: LOGIN
```

**FLAGS**

: **--organization**

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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

: This variant is also available:

```
gcloud alpha access-context-manager cloud-bindings list
```