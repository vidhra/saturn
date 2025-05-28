# gcloud access-context-manager perimeters dry-run list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/list](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/list)*

**NAME**

: **gcloud access-context-manager perimeters dry-run list - list the effective dry-run configuration across all Service Perimeters**

**SYNOPSIS**

: **`gcloud access-context-manager perimeters dry-run list` [`[--policy](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/list#--policy)`=`policy`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: By default, only the Service Perimeter name, title, type and the dry-run mode
configuration (as `spec`) is displayed.
Note: For Service Perimeters without an explicit dry-run mode configuration, the
enforcement mode configuration is used as the dry-run mode configuration,
resulting in no audit logs being generated.

**EXAMPLES**

: To list the dry-run mode configuration across all Service Perimeter:

```
gcloud access-context-manager perimeters dry-run list
```

Output:

```
name: perimeter_1*
spec:
  resources:
  - projects/123
  - projects/456
  restrictedServices:
  - storage.googleapis.com
title: Perimeter 1
---
name: perimeter_2
spec:
  resources:
  - projects/789
  restrictedServices:
  - bigquery.googleapis.com
  vpcAccessibleServices:
    allowedServices:
    - bigquery.googleapis.com
    enableRestriction: true
title: Perimeter 2
```

**FLAGS**

: **--policy**:
Policy resource - The access policy you want to list the effective dry-run
configuration for. This represents a Cloud resource.

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
gcloud alpha access-context-manager perimeters dry-run list
```

```
gcloud beta access-context-manager perimeters dry-run list
```