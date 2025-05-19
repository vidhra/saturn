# gcloud alpha ai-platform versions create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create)*

**NAME**

: **gcloud alpha ai-platform versions create - create a new AI Platform version**

**SYNOPSIS**

: **`gcloud alpha ai-platform versions create` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#VERSION)` `[--model](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--model)`=`MODEL` [`[--accelerator](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--async)`] [`[--config](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--config)`=`CONFIG`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--description)`=`DESCRIPTION`] [`[--explanation-method](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--explanation-method)`=`EXPLANATION_METHOD`] [`[--framework](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--framework)`=`FRAMEWORK`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--machine-type)`=`MACHINE_TYPE`] [`[--num-integral-steps](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--num-integral-steps)`=`NUM_INTEGRAL_STEPS`; default=50] [`[--num-paths](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--num-paths)`=`NUM_PATHS`; default=50] [`[--origin](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--origin)`=`ORIGIN`] [`[--python-version](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--python-version)`=`PYTHON_VERSION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--region)`=`REGION`] [`[--runtime-version](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--runtime-version)`=`RUNTIME_VERSION`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--staging-bucket](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--staging-bucket)`=`STAGING_BUCKET`] [`[--args](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--args)`=[`ARG`,…] `[--command](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--command)`=[`COMMAND`,…] `[--env-vars](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--env-vars)`=[`KEY`=`VALUE`,…] `[--image](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--image)`=`IMAGE` `[--ports](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--ports)`=[`ARG`,…]] [`[--health-route](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--health-route)`=`HEALTH_ROUTE` `[--predict-route](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--predict-route)`=`PREDICT_ROUTE`] [`[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--max-nodes)`=`MAX_NODES` `[--metric-targets](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--metric-targets)`=[`METRIC-NAME`=`TARGET`,…] `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--min-nodes)`=`MIN_NODES`] [`[--package-uris](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--package-uris)`=[`PACKAGE_URI`,…] `[--prediction-class](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#--prediction-class)`=`PREDICTION_CLASS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Creates a new version of an AI Platform model.
For more details on managing AI Platform models and versions see [https://cloud.google.com/ai-platform/prediction/docs/managing-models-jobs](https://cloud.google.com/ai-platform/prediction/docs/managing-models-jobs)

**EXAMPLES**

: To create an AI Platform version model with the version ID 'versionId' and with
the name 'model-name', run:

```
gcloud alpha ai-platform versions create versionId --model=model-name
```

**POSITIONAL ARGUMENTS**

: **`VERSION`**:
Name of the model version.

**REQUIRED FLAGS**

: **--model**:
Name of the model.

**OPTIONAL FLAGS**

: **--accelerator**:
Manage the accelerator config for GPU serving. When deploying a model with
Compute Engine Machine Types, a GPU accelerator may also be selected.

**`type`**:
The type of the accelerator. Choices are 'nvidia-tesla-a100',
'nvidia-tesla-k80', 'nvidia-tesla-p100', 'nvidia-tesla-p4', 'nvidia-tesla-t4',
'nvidia-tesla-v100'.

**`count`**:
The number of accelerators to attach to each machine running the job. If not
specified, the default value is 1. Your model must be specially designed to
accommodate more than 1 accelerator per machine. To configure how many replicas
your model has, set the `manualScaling` or `autoScaling`
parameters.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--config**:
Path to a YAML configuration file containing configuration parameters for the [Version](https://cloud.google.com/ai-platform/prediction/docs/reference/rest/v1/projects.models.versions)
to create.
The file is in YAML format. Note that not all attributes of a version are
configurable; available attributes (with example values) are:

```
description: A free-form description of the version.
deploymentUri: gs://path/to/source
runtimeVersion: '2.1'
#  Set only one of either manualScaling or autoScaling.
manualScaling:
  nodes: 10  # The number of nodes to allocate for this model.
autoScaling:
  minNodes: 0  # The minimum number of nodes to allocate for this model.
labels:
  user-defined-key: user-defined-value
```

The name of the version must always be specified via the required VERSION
argument.
Only one of manualScaling or autoScaling can be specified. If both are specified
in same yaml file an error will be returned.
If an option is specified both in the configuration file and via command-line
arguments, the command-line arguments override the configuration file.

**--description**:
Description of the version.

**--explanation-method**:
Enable explanations and select the explanation method to use.
The valid options are: integrated-gradients: Use Integrated Gradients.
sampled-shapley: Use Sampled Shapley. xrai: Use XRAI.
`EXPLANATION_METHOD` must be one of:
`integrated-gradients`, `sampled-shapley`,
`xrai`.

**--framework**:
ML framework used to train this version of the model. If not specified, defaults
to 'tensorflow'. `FRAMEWORK` must be one of:
`scikit-learn`, `tensorflow`, `xgboost`.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--machine-type**:
Type of machine on which to serve the model. Currently only applies to online
prediction. For available machine types, see [https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-prediction#available_machine_types](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-prediction#available_machine_types).

**--num-integral-steps**:
Number of integral steps for Integrated Gradients. Only valid when
`--explanation-method=integrated-gradients` or
`--explanation-method=xrai` is specified.

**--num-paths**:
Number of paths for Sampled Shapley. Only valid when
`--explanation-method=sampled-shapley` is specified.

**--origin**:
Location of `model/` "directory" (see
https://cloud.google.com/ai-platform/prediction/docs/deploying-models#upload-model).
This overrides `deploymentUri` in the `--config` file. If
this flag is not passed, `deploymentUri` `must` be
specified in the file from `--config`.
Can be a Cloud Storage (`gs://`) path or local file path (no prefix).
In the latter case the files will be uploaded to Cloud Storage and a
`--staging-bucket` argument is required.

**--python-version**:
Version of Python used when creating the version. Choices are 3.7, 3.5, and 2.7.
However, this value must be compatible with the chosen runtime version for the
job.
Must be used with a compatible runtime version:

- 3.7 is compatible with runtime versions 1.15 and later.
- 3.5 is compatible with runtime versions 1.4 through 1.14.
- 2.7 is compatible with runtime versions 1.15 and earlier.

**--region**:
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

**--runtime-version**:
AI Platform runtime version for this job. Must be specified unless
--master-image-uri is specified instead. It is defined in documentation along
with the list of supported versions: [https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list)

**--service-account**:
Specifies the service account for resource access control.

**--staging-bucket**:
Bucket in which to stage training archives.
Required only if a file upload is necessary (that is, other flags include local
paths) and no other flags implicitly specify an upload path.

**--args**

**--health-route**

**--max-nodes**

**--package-uris**

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
gcloud ai-platform versions create
```

```
gcloud beta ai-platform versions create
```