# gcloud ml-engine operations wait  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml-engine/operations/wait](https://cloud.google.com/sdk/gcloud/reference/ml-engine/operations/wait)*

**NAME**

: **gcloud ml-engine operations wait - wait for an AI Platform operation to complete**

**SYNOPSIS**

: **`gcloud ml-engine operations wait` `[OPERATION](https://cloud.google.com/sdk/gcloud/reference/ml-engine/operations/wait#OPERATION)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/ml-engine/operations/wait#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml-engine/operations/wait#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Wait for an AI Platform operation to complete.
Given an operation ID, this command polls the operation and blocks until it
completes. At completion, the operation message is printed (which includes the
operation response).

**POSITIONAL ARGUMENTS**

: **`OPERATION`**:
Name of the operation.

**FLAGS**

: **--region**:
Google Cloud region of the regional endpoint to use for this command. If
unspecified, the command uses the global endpoint of the AI Platform Training
and Prediction API.
Learn more about regional endpoints and see a list of available regions: [https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints)
`REGION` must be one of: `asia-east1`,
`asia-northeast1`, `asia-southeast1`,
`australia-southeast1`, `europe-west1`,
`europe-west2`, `europe-west3`, `europe-west4`,
`northamerica-northeast1`, `us-central1`,
`us-east1`, `us-east4`, `us-west1`.

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
gcloud alpha ml-engine operations wait
```

```
gcloud beta ml-engine operations wait
```