# gcloud alpha ai model-garden models list-deployment-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/list-deployment-config](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/list-deployment-config)*

**NAME**

: **gcloud alpha ai model-garden models list-deployment-config - list the machine specifications supported by and verified for a model in Model Garden**

**SYNOPSIS**

: **`gcloud alpha ai model-garden models list-deployment-config` `[--model](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/list-deployment-config#--model)`=`MODEL` [`[--hugging-face-access-token](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/list-deployment-config#--hugging-face-access-token)`=`HUGGING_FACE_ACCESS_TOKEN`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/list-deployment-config#--filter)`=`EXPRESSION`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/list-deployment-config#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/list-deployment-config#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To list the supported machine specifications for
`google/gemma2@gemma-2-9b`, run:

```
gcloud ai model-garden models list-deployment-config --model=google/gemma2@gemma-2-9b
```

To list the supported machine specifications for a Hugging Face model
`meta-llama/Meta-Llama-3-8B`, run:

```
gcloud ai model-garden models list-deployment-config --model=meta-llama/Meta-Llama-3-8B
```

**REQUIRED FLAGS**

: **--model**:
The model to be deployed. If it is a Model Garden model, it should be in the
format of `{publisher_name}/{model_name}@{model_version_name}, e.g.`google/gemma2@gemma-2-2b`. If it is a Hugging Face model, it should
be in the convention of Hugging Face models, e.g.`meta-llama/Meta-Llama-3-8B`.`

**FLAGS**

: **--hugging-face-access-token**:
The access token from Hugging Face needed to read the model artifacts of gated
models in order to generate the deployment configs. It is only needed when the
Hugging Face model to deploy is gated and not verified by Model Garden. You can
use the `gcloud ai alpha/beta model-garden models list` command to
find out which ones are verified by Model Garden.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta ai model-garden models list-deployment-config
```