# gcloud alpha ai endpoints  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints)*

**NAME**

: **gcloud alpha ai endpoints - manage Vertex AI endpoints**

**SYNOPSIS**

: **`gcloud alpha ai endpoints` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` An endpoint contains one or more deployed models, all of
which must have the same interface but may come from different models. An
endpoint is to obtain online prediction and explanation from one of its deployed
models.
When you communicate with Vertex AI services, you identify a specific endpoint
that is deployed in the cloud using a combination of the current project, the
region, and the endpoint.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/create)`**:
`(ALPHA)` Create a new Vertex AI endpoint.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/delete)`**:
`(ALPHA)` Delete an existing Vertex AI endpoint.

**`[deploy-model](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model)`**:
`(ALPHA)` Deploy a model to an existing Vertex AI endpoint.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/describe)`**:
`(ALPHA)` Describe an existing Vertex AI endpoint.

**`[direct-predict](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/direct-predict)`**:
`(ALPHA)` Run Vertex AI online direct prediction.

**`[direct-raw-predict](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/direct-raw-predict)`**:
`(ALPHA)` Run Vertex AI online direct raw prediction.

**`[explain](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/explain)`**:
`(ALPHA)` Request an online explanation from an Vertex AI endpoint.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/list)`**:
`(ALPHA)` List existing Vertex AI endpoints.

**`[predict](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/predict)`**:
`(ALPHA)` Run Vertex AI online prediction.

**`[raw-predict](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/raw-predict)`**:
`(ALPHA)` Run Vertex AI online raw prediction.

**`[stream-direct-predict](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/stream-direct-predict)`**:
`(ALPHA)` Run Vertex AI online stream direct prediction.

**`[stream-direct-raw-predict](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/stream-direct-raw-predict)`**:
`(ALPHA)` Run Vertex AI online stream direct raw prediction.

**`[stream-raw-predict](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/stream-raw-predict)`**:
`(ALPHA)` Run Vertex AI online stream raw prediction.

**`[undeploy-model](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/undeploy-model)`**:
`(ALPHA)` Undeploy a model from an existing Vertex AI endpoint.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/update)`**:
`(ALPHA)` Update an existing Vertex AI endpoint.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud ai endpoints
```

```
gcloud beta ai endpoints
```