# gcloud access-context-manager perimeters dry-run enforce-all  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/enforce-all](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/enforce-all)*

**NAME**

: **gcloud access-context-manager perimeters dry-run enforce-all - enforces the dry-run mode configuration for all Service Perimeters**

**SYNOPSIS**

: **`gcloud access-context-manager perimeters dry-run enforce-all` [`[--etag](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/enforce-all#--etag)`=`etag`] [`[--policy](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/enforce-all#--policy)`=`policy`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/enforce-all#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: An enforce operation on a Service Perimeter involves copying its dry-run mode
configuration (`spec`) to that Service Perimeter's enforcement mode
configration (`status`). This command performs this operation for
`all` Service Perimeters in the user's Access Policy.
Note: Only Service Perimeters with an explicit dry-run mode configuration are
affected by this operation. The overall operation succeeds once the dry-run
configurations of all such Service Perimeters have been enforced. If the
operation fails for any given Service Perimeter, it will cause the entire
operation to be aborted.

**EXAMPLES**

: To enforce the dry-run mode configurations for all Service Perimeter in an
Access Policy, run the following command:

```
gcloud access-context-manager perimeters dry-run enforce-all
```

**FLAGS**

: **--etag**:
The etag for the version of the Access Policy that this operation is to be
performed on. If, at the time of the operation, the etag for the Access Policy
stored in Access Context Manager is different from the specified etag, then the
commit operation will not be performed and the call will fail. If etag is not
provided, the operation will be performed as if a valid etag is provided.

**--policy**:
The parent Access Policy which owns all Service Perimeters in scope for the
commit operation.

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

: These variants are also available:

```
gcloud alpha access-context-manager perimeters dry-run enforce-all
```

```
gcloud beta access-context-manager perimeters dry-run enforce-all
```