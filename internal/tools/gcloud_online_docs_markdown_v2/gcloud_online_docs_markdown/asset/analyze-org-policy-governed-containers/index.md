# gcloud asset analyze-org-policy-governed-containers  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers)*

**NAME**

: **gcloud asset analyze-org-policy-governed-containers - analyze organization policies governed containers under a scope**

**SYNOPSIS**

: **`gcloud asset analyze-org-policy-governed-containers` `[--constraint](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers#--constraint)`=`CONSTRAINT` `[--scope](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers#--scope)`=`SCOPE` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Analyze organization policies governed containers under a scope.

**EXAMPLES**

: To list 10 containers governed by a constraint in an organization, run:

```
gcloud asset analyze-org-policy-governed-containers --scope=organizations/YOUR_ORG_ID --constraint=YOUR_CONSTRAINT_NAME --limit=10
```

**REQUIRED FLAGS**

: **--constraint**:
The name of the constraint to analyze organization policies for. The response
only contains analyzed organization policies for the provided constraint.
Example:

- organizations/{ORGANIZATION_NUMBER}/customConstraints/{CUSTOM_CONSTRAINT_NAME}
for a user-defined custom constraint.

**--scope**:
Scope can only be an organization. The analysis is limited to the Cloud
organization policies and containers within this scope. The caller must be
granted the `cloudasset.assets.searchAllResources` permission on the
desired scope.
The allowed values are:

- `organizations/{ORGANIZATION_NUMBER}` (e.g.
``organizations/123456``)

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

**NOTES**

: These variants are also available:

```
gcloud alpha asset analyze-org-policy-governed-containers
```

```
gcloud beta asset analyze-org-policy-governed-containers
```