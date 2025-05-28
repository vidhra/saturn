# gcloud beta ai model-garden models list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list](https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list)*

**NAME**

: **gcloud beta ai model-garden models list - list the publisher models in Model Garden**

**SYNOPSIS**

: **`gcloud beta ai model-garden models list` [`[--can-deploy-hugging-face-models](https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list#--can-deploy-hugging-face-models)`] [`[--full-resource-name](https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list#--full-resource-name)`] [`[--model-filter](https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list#--model-filter)`=`MODEL_FILTER`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list#--limit)`=`LIMIT`; default=1000] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` This command lists either all models in Model Garden or all
Hugging Face models supported by Model Garden.
Note: Since the number of Hugging Face models is large, the default limit is set
to 500 with a page size of 100 when listing supported Hugging Face models. To
override the limit or page size, specify the --limit or --page-size flags,
respectively. To list all models in Model Garden, use
`--limit=unlimited`.

**FLAGS**

: **--can-deploy-hugging-face-models**:
Whether to only list Hugging Face models that can be deployed.

**--full-resource-name**:
Whether to return the full resource name of the model.

**--model-filter**:
Filter to apply to the model names or the display names of the list of models.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `1000`. This flag
interacts with other flags that are applied in this order:
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

: This command is currently in beta and might change without notice. This variant
is also available:

```
gcloud alpha ai model-garden models list
```