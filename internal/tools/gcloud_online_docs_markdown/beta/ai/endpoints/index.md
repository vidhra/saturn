# gcloud beta ai endpoints  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints)*

**NAME**

: **gcloud beta ai endpoints - manage Vertex AI endpoints**

**SYNOPSIS**

: **`gcloud beta ai endpoints` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` An endpoint contains one or more deployed models, all of
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

**`[create](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create)`**:
`(BETA)` Create a new Vertex AI endpoint.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/delete)`**:
`(BETA)` Delete an existing Vertex AI endpoint.

**`[deploy-model](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/deploy-model)`**:
`(BETA)` Deploy a model to an existing Vertex AI endpoint.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/describe)`**:
`(BETA)` Describe an existing Vertex AI endpoint.

**`[direct-predict](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/direct-predict)`**:
`(BETA)` Run Vertex AI online direct prediction.

**`[direct-raw-predict](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/direct-raw-predict)`**:
`(BETA)` Run Vertex AI online direct raw prediction.

**`[explain](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/explain)`**:
`(BETA)` Request an online explanation from an Vertex AI endpoint.

**`[list](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/list)`**:
`(BETA)` List existing Vertex AI endpoints.

**`[predict](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/predict)`**:
`(BETA)` Run Vertex AI online prediction.

**`[raw-predict](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/raw-predict)`**:
`(BETA)` Run Vertex AI online raw prediction.

**`[stream-direct-predict](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-direct-predict)`**:
`(BETA)` Run Vertex AI online stream direct prediction.

**`[stream-direct-raw-predict](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-direct-raw-predict)`**:
`(BETA)` Run Vertex AI online stream direct raw prediction.

**`[stream-raw-predict](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict)`**:
`(BETA)` Run Vertex AI online stream raw prediction.

**`[undeploy-model](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model)`**:
`(BETA)` Undeploy a model from an existing Vertex AI endpoint.

**`[update](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update)`**:
`(BETA)` Update an existing Vertex AI endpoint.

**NOTES**

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud ai endpoints
```

```
gcloud alpha ai endpoints
```