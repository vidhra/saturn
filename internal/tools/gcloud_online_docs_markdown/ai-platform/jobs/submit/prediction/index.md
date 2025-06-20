# gcloud ai-platform jobs submit prediction  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction)*

**NAME**

: **gcloud ai-platform jobs submit prediction - start an AI Platform batch prediction job**

**SYNOPSIS**

: **`gcloud ai-platform jobs submit prediction` `[JOB](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#JOB)` `[--data-format](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--data-format)`=`DATA_FORMAT` `[--input-paths](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--input-paths)`=`INPUT_PATH`,[`[INPUT_PATH](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#INPUT_PATH)`,…] `[--output-path](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--output-path)`=`OUTPUT_PATH` `[--region](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--region)`=`REGION` (`[--model](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--model)`=`MODEL`     | `[--model-dir](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--model-dir)`=`MODEL_DIR`) [`[--batch-size](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--batch-size)`=`BATCH_SIZE`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-worker-count](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--max-worker-count)`=`MAX_WORKER_COUNT`] [`[--runtime-version](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--runtime-version)`=`RUNTIME_VERSION`] [`[--signature-name](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--signature-name)`=`SIGNATURE_NAME`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Start an AI Platform batch prediction job.

**POSITIONAL ARGUMENTS**

: **`JOB`**:
Name of the batch prediction job.

**REQUIRED FLAGS**

: **--data-format**:
Data format of the input files. `DATA_FORMAT` must be one
of:

**`text`**:
Text and JSON files; for text files, see
https://www.tensorflow.org/guide/datasets#consuming_text_data, for JSON files,
see [https://cloud.google.com/ai-platform/prediction/docs/overview#batch_prediction_input_data](https://cloud.google.com/ai-platform/prediction/docs/overview#batch_prediction_input_data)

**`tf-record`**:
TFRecord files; see [https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data](https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data)

**`tf-record-gzip`**:
GZIP-compressed TFRecord files.

**--input-paths**:
Cloud Storage paths to the instances to run prediction on.
Wildcards (`*`) accepted at the `end` of a path. More than
one path can be specified if multiple file patterns are needed. For example,

```
gs://my-bucket/instances*,gs://my-bucket/other-instances1
```

will match any objects whose names start with `instances` in
`my-bucket` as well as the `other-instances1` bucket,
while

```
gs://my-bucket/instance-dir/*
```

will match any objects in the `instance-dir` "directory" (since
directories aren't a first-class Cloud Storage concept) of
`my-bucket`.

**--output-path**:
Cloud Storage path to which to save the output. Example: gs://my-bucket/output.

**--region**:
The Compute Engine region to run the job in.

**--model**

**OPTIONAL FLAGS**

: **--batch-size**:
The number of records per batch. The service will buffer batch_size number of
records in memory before invoking TensorFlow. Defaults to 64 if not specified.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--max-worker-count**:
The maximum number of workers to be used for parallel processing. Defaults to 10
if not specified.

**--runtime-version**:
AI Platform runtime version for this job. Must be specified unless
--master-image-uri is specified instead. It is defined in documentation along
with the list of supported versions: [https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list)

**--signature-name**:
Name of the signature defined in the SavedModel to use for this job. Defaults to
DEFAULT_SERVING_SIGNATURE_DEF_KEY in
https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_constants,
which is "serving_default". Only applies to TensorFlow models.

**--version**:
Model version to be used.
This flag may only be given if --model is specified. If unspecified, the default
version of the model will be used. To list versions for a model, run

```
gcloud ai-platform versions list
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
gcloud alpha ai-platform jobs submit prediction
```

```
gcloud beta ai-platform jobs submit prediction
```