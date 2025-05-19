# gcloud alpha ai-platform local predict  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict)*

**NAME**

: **gcloud alpha ai-platform local predict - run prediction locally**

**SYNOPSIS**

: **`gcloud alpha ai-platform local predict` `[--model-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict#--model-dir)`=`MODEL_DIR` (`[--json-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict#--json-instances)`=`JSON_INSTANCES`     | `[--json-request](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict#--json-request)`=`JSON_REQUEST`     | `[--text-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict#--text-instances)`=`TEXT_INSTANCES`) [`[--framework](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict#--framework)`=`FRAMEWORK`] [`[--signature-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict#--signature-name)`=`SIGNATURE_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha ai-platform local predict`
performs prediction locally with the given instances. It requires the [TensorFlow SDK](https://www.tensorflow.org/install) be installed
locally. The output format mirrors `[gcloud ai-platform
predict](https://cloud.google.com/sdk/gcloud/reference/ai-platform/predict)` (online prediction).
You cannot use this command with custom prediction routines.

**REQUIRED FLAGS**

: **--model-dir**:
Path to the model.

**--json-instances**

**OPTIONAL FLAGS**

: **--framework**:
ML framework used to train this version of the model. If not specified, defaults
to 'tensorflow'. `FRAMEWORK` must be one of:
`scikit-learn`, `tensorflow`, `xgboost`.

**--signature-name**:
Name of the signature defined in the SavedModel to use for this job. Defaults to
DEFAULT_SERVING_SIGNATURE_DEF_KEY in
https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_constants,
which is "serving_default". Only applies to TensorFlow models.

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
allowlist. These variants are also available:

```
gcloud ai-platform local predict
```

```
gcloud beta ai-platform local predict
```