# gcloud ai endpoints  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/endpoints](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints)*

**NAME**

: **gcloud ai endpoints - manage Vertex AI endpoints**

**SYNOPSIS**

: **`gcloud ai endpoints` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: An endpoint contains one or more deployed models, all of which must have the
same interface but may come from different models. An endpoint is to obtain
online prediction and explanation from one of its deployed models.
When you communicate with Vertex AI services, you identify a specific endpoint
that is deployed in the cloud using a combination of the current project, the
region, and the endpoint.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/create)`**:
Create a new Vertex AI endpoint.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/delete)`**:
Delete an existing Vertex AI endpoint.

**`[deploy-model](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/deploy-model)`**:
Deploy a model to an existing Vertex AI endpoint.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/describe)`**:
Describe an existing Vertex AI endpoint.

**`[direct-predict](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-predict)`**:
Run Vertex AI online direct prediction.

**`[direct-raw-predict](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-raw-predict)`**:
Run Vertex AI online direct raw prediction.

**`[explain](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/explain)`**:
Request an online explanation from an Vertex AI endpoint.

**`[list](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/list)`**:
List existing Vertex AI endpoints.

**`[predict](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/predict)`**:
Run Vertex AI online prediction.

**`[raw-predict](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/raw-predict)`**:
Run Vertex AI online raw prediction.

**`[stream-direct-predict](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/stream-direct-predict)`**:
Run Vertex AI online stream direct prediction.

**`[stream-direct-raw-predict](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/stream-direct-raw-predict)`**:
Run Vertex AI online stream direct raw prediction.

**`[stream-raw-predict](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/stream-raw-predict)`**:
Run Vertex AI online stream raw prediction.

**`[undeploy-model](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/undeploy-model)`**:
Undeploy a model from an existing Vertex AI endpoint.

**`[update](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/update)`**:
Update an existing Vertex AI endpoint.

**NOTES**

: These variants are also available:

```
gcloud alpha ai endpoints
```

```
gcloud beta ai endpoints
```