# gcloud ai-platform versions set-default  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai-platform/versions/set-default](https://cloud.google.com/sdk/gcloud/reference/ai-platform/versions/set-default)*

**NAME**

: **gcloud ai-platform versions set-default - sets an existing AI Platform version as the default for its model**

**SYNOPSIS**

: **`gcloud ai-platform versions set-default` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/ai-platform/versions/set-default#VERSION)` `[--model](https://cloud.google.com/sdk/gcloud/reference/ai-platform/versions/set-default#--model)`=`MODEL` [`[--region](https://cloud.google.com/sdk/gcloud/reference/ai-platform/versions/set-default#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai-platform/versions/set-default#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets an existing AI Platform version as the default for its model.
`gcloud ai-platform versions set-default` sets an existing AI
Platform version as the default for its model. Only one version may be the
default for a given version.

**POSITIONAL ARGUMENTS**

: **`VERSION`**:
Name of the model version.

**REQUIRED FLAGS**

: **--model**:
Name of the model.

**OPTIONAL FLAGS**

: **--region**:
Google Cloud region of the regional endpoint to use for this command. For the
global endpoint, the region needs to be specified as `global`.
Learn more about regional endpoints and see a list of available regions: [https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints)
`REGION` must be one of: `global`,
`asia-east1`, `asia-northeast1`,
`asia-southeast1`, `australia-southeast1`,
`europe-west1`, `europe-west2`, `europe-west3`,
`europe-west4`, `northamerica-northeast1`,
`us-central1`, `us-east1`, `us-east4`,
`us-west1`.

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
gcloud alpha ai-platform versions set-default
```

```
gcloud beta ai-platform versions set-default
```