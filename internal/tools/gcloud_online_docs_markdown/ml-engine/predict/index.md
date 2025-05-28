# gcloud ml-engine predict  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict](https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict)*

**NAME**

: **gcloud ml-engine predict - run AI Platform online prediction**

**SYNOPSIS**

: **`gcloud ml-engine predict` `[--model](https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict#--model)`=`MODEL` (`[--json-instances](https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict#--json-instances)`=`JSON_INSTANCES`     | `[--json-request](https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict#--json-request)`=`JSON_REQUEST`     | `[--text-instances](https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict#--text-instances)`=`TEXT_INSTANCES`) [`[--region](https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict#--region)`=`REGION`] [`[--signature-name](https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict#--signature-name)`=`SIGNATURE_NAME`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml-engine/predict#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud ml-engine predict` sends a prediction request to AI Platform
for the given instances. This command will read up to 100 instances, though the
service itself will accept instances up to the payload limit size (currently,
1.5MB). If you are predicting on more instances, you should use batch prediction
via

```
gcloud ml-engine jobs submit prediction.
```

**REQUIRED FLAGS**

: **--model**:
Name of the model.

**--json-instances**

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

**--signature-name**:
Name of the signature defined in the SavedModel to use for this job. Defaults to
DEFAULT_SERVING_SIGNATURE_DEF_KEY in
https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_constants,
which is "serving_default". Only applies to TensorFlow models.

**--version**:
Model version to be used.
If unspecified, the default version of the model will be used. To list model
versions run

```
gcloud ml-engine versions list
```

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
gcloud alpha ml-engine predict
```

```
gcloud beta ml-engine predict
```