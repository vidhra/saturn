# gcloud artifacts sbom list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list)*

**NAME**

: **gcloud artifacts sbom list - list SBOM file references**

**SYNOPSIS**

: **`gcloud artifacts sbom list` [`[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list#--location)`=`LOCATION`] [`[--dependency](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list#--dependency)`=`DEPENDENCY`     | `[--resource](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list#--resource)`=`RESOURCE`     | `[--resource-prefix](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list#--resource-prefix)`=`RESOURCE_PREFIX`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list#--sort-by)`=[`FIELD`,…]; default=`"occ.create_time"`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List SBOM file references.

**EXAMPLES**

: To list SBOM file references:

```
gcloud artifacts sbom list
```

To list SBOM file references related to the image with the tag
"us-east1-docker.pkg.dev/project/repo/my-image:1.0":

```
gcloud artifacts sbom list --resource="us-east1-docker.pkg.dev/project/repo/my-image:1.0"
```

To list SBOM file references related to the image with the digest
"us-east1-docker.pkg.dev/project/repo/my-image@sha256:88b205d7995332e10e836514fbfd59ecaf8976fc15060cd66e85cdcebe7fb356":

```
gcloud artifacts sbom list --resource="us-east1-docker.pkg.dev/project/repo/my-image@sha256:88b205d7995332e10e836514fbfd59ecaf8976fc15060cd66e85cdcebe7fb356"
```

To list SBOM file references related to the images with the resource path prefix
"us-east1-docker.pkg.dev/project/repo":

```
gcloud artifacts sbom list --resource-prefix="us-east1-docker.pkg.dev/project/repo"
```

To list SBOM file references generated when the images were pushed to Artifact
Registry and related to the installed package dependency "perl":

```
gcloud artifacts sbom list --dependency="perl"
```

**FLAGS**

: **--location**:
If specified, all requests to Artifact Analysis for occurrences will go to
location specified

**--dependency**

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
`--limit`. The default is `occ.create_time`.

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