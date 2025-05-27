# gcloud container images list-tags  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags](https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags)*

**NAME**

: **gcloud container images list-tags - list tags and digests for the specified image**

**SYNOPSIS**

: **`gcloud container images list-tags` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags#IMAGE_NAME)` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags#--sort-by)`=[`FIELD`,…]; default="~timestamp"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The container images list-tags command of gcloud lists metadata about tags and
digests for the specified container image. Images must be hosted by the Google
Container Registry.

**EXAMPLES**

: List the tags in a specified image:

```
gcloud container images list-tags gcr.io/myproject/myimage
```

To receive the full, JSON-formatted output (with untruncated digests):

```
gcloud container images list-tags gcr.io/myproject/myimage --format=json
```

To list digests without corresponding tags:

```
gcloud container images list-tags gcr.io/myproject/myimage --filter="NOT tags:*"
```

To list images that have a tag with the value '30e5504145':

```
gcloud container images list-tags --filter="'tags:30e5504145'"
```

The last example encloses the filter expression in single quotes because the
value '30e5504145' could be interpreted as a number in scientific notation.

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME`**:
The name of the image to list tags for. The name format should be
*.gcr.io/PROJECT_ID/IMAGE_PATH.

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
`--limit`. The default is `~timestamp`.

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
gcloud alpha container images list-tags
```

```
gcloud beta container images list-tags
```