# gcloud ai-platform operations cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai-platform/operations/cancel](https://cloud.google.com/sdk/gcloud/reference/ai-platform/operations/cancel)*

**NAME**

: **gcloud ai-platform operations cancel - cancel an AI Platform operation**

**SYNOPSIS**

: **`gcloud ai-platform operations cancel` `[OPERATION](https://cloud.google.com/sdk/gcloud/reference/ai-platform/operations/cancel#OPERATION)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/ai-platform/operations/cancel#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai-platform/operations/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancel an AI Platform operation.

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
gcloud alpha ai-platform operations cancel
```

```
gcloud beta ai-platform operations cancel
```