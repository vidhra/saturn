# gcloud alpha ai models upload  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload)*

**NAME**

: **gcloud alpha ai models upload - upload a new model**

**SYNOPSIS**

: **`gcloud alpha ai models upload` `[--container-image-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-image-uri)`=`CONTAINER_IMAGE_URI` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--display-name)`=`DISPLAY_NAME` [`[--artifact-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--artifact-uri)`=`ARTIFACT_URI`] [`[--container-args](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-args)`=[`ARG`,…]] [`[--container-command](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-command)`=[`COMMAND`,…]] [`[--container-deployment-timeout-seconds](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-deployment-timeout-seconds)`=`CONTAINER_DEPLOYMENT_TIMEOUT_SECONDS`] [`[--container-env-vars](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-env-vars)`=[`KEY`=`VALUE`,…]] [`[--container-grpc-ports](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-grpc-ports)`=[`PORT`,…]] [`[--container-health-probe-exec](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-health-probe-exec)`=[`HEALTH_PROBE_EXEC`,…]] [`[--container-health-probe-period-seconds](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-health-probe-period-seconds)`=`CONTAINER_HEALTH_PROBE_PERIOD_SECONDS`] [`[--container-health-probe-timeout-seconds](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-health-probe-timeout-seconds)`=`CONTAINER_HEALTH_PROBE_TIMEOUT_SECONDS`] [`[--container-health-route](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-health-route)`=`CONTAINER_HEALTH_ROUTE`] [`[--container-ports](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-ports)`=[`PORT`,…]] [`[--container-predict-route](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-predict-route)`=`CONTAINER_PREDICT_ROUTE`] [`[--container-shared-memory-size-mb](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-shared-memory-size-mb)`=`CONTAINER_SHARED_MEMORY_SIZE_MB`] [`[--container-startup-probe-exec](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-startup-probe-exec)`=[`STARTUP_PROBE_EXEC`,…]] [`[--container-startup-probe-period-seconds](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-startup-probe-period-seconds)`=`CONTAINER_STARTUP_PROBE_PERIOD_SECONDS`] [`[--container-startup-probe-timeout-seconds](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--container-startup-probe-timeout-seconds)`=`CONTAINER_STARTUP_PROBE_TIMEOUT_SECONDS`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--description)`=`DESCRIPTION`] [`[--explanation-metadata-file](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--explanation-metadata-file)`=`EXPLANATION_METADATA_FILE`] [`[--explanation-method](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--explanation-method)`=`EXPLANATION_METHOD`] [`[--explanation-modality](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--explanation-modality)`=`EXPLANATION_MODALITY`; default=`"MODALITY_UNSPECIFIED"`] [`[--explanation-nearest-neighbor-search-config-file](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--explanation-nearest-neighbor-search-config-file)`=`EXPLANATION_NEAREST_NEIGHBOR_SEARCH_CONFIG_FILE`] [`[--explanation-neighbor-count](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--explanation-neighbor-count)`=`EXPLANATION_NEIGHBOR_COUNT`] [`[--explanation-path-count](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--explanation-path-count)`=`EXPLANATION_PATH_COUNT`] [`[--explanation-query](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--explanation-query)`=`EXPLANATION_QUERY`; default="PRECISE"] [`[--explanation-step-count](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--explanation-step-count)`=`EXPLANATION_STEP_COUNT`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--labels)`=[`KEY`=`VALUE`,…]] [`[--model-id](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--model-id)`=`MODEL_ID`] [`[--parent-model](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--parent-model)`=`PARENT_MODEL`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--region)`=`REGION`] [`[--smooth-grad-noise-sigma](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--smooth-grad-noise-sigma)`=`SMOOTH_GRAD_NOISE_SIGMA`] [`[--smooth-grad-noise-sigma-by-feature](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--smooth-grad-noise-sigma-by-feature)`=[`KEY`=`VALUE`,…]] [`[--smooth-grad-noisy-sample-count](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--smooth-grad-noisy-sample-count)`=`SMOOTH_GRAD_NOISY_SAMPLE_COUNT`] [`[--uris](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--uris)`=[`URIS`,…]] [`[--version-aliases](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--version-aliases)`=[`VERSION_ALIASES`,…]] [`[--version-description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#--version-description)`=`VERSION_DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/upload#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To upload a model under project `example` in region
`us-central1`, run:

```
gcloud alpha ai models upload --container-image-uri="gcr.io/example/my-image" --description=example-model --display-name=my-model --artifact-uri='gs://bucket/path' --project=example --region=us-central1
```

**REQUIRED FLAGS**

: **--container-image-uri**:
URI of the Model serving container file in the Container Registry (e.g.
gcr.io/myproject/server:latest).

**--display-name**:
Display name of the model.

**OPTIONAL FLAGS**

: **--artifact-uri**:
Path to the directory containing the Model artifact and any of its supporting
files.

**--container-args**:
Comma-separated arguments passed to the command run by the container image. If
not specified and no `--command` is provided, the container image's
default command is used.

**--container-command**:
Entrypoint for the container image. If not specified, the container image's
default entrypoint is run.

**--container-deployment-timeout-seconds**:
Deployment timeout in seconds.

**--container-env-vars**:
List of key-value pairs to set as environment variables.

**--container-grpc-ports**:
Container ports to receive grpc requests at. Must be a number between 1 and
65535, inclusive.

**--container-health-probe-exec**:
Exec specifies the action to take. Used by health probe. An example of this
argument would be ["cat", "/tmp/healthy"].

**--container-health-probe-period-seconds**:
How often (in seconds) to perform the health probe. Default to 10 seconds.
Minimum value is 1.

**--container-health-probe-timeout-seconds**:
Number of seconds after which the health probe times out. Defaults to 1 second.
Minimum value is 1.

**--container-health-route**:
HTTP path to send health checks to inside the container.

**--container-ports**:
Container ports to receive http requests at. Must be a number between 1 and
65535, inclusive.

**--container-predict-route**:
HTTP path to send prediction requests to inside the container.

**--container-shared-memory-size-mb**:
The amount of the VM memory to reserve as the shared memory for the model in
megabytes.

**--container-startup-probe-exec**:
Exec specifies the action to take. Used by startup probe. An example of this
argument would be ["cat", "/tmp/healthy"].

**--container-startup-probe-period-seconds**:
How often (in seconds) to perform the startup probe. Default to 10 seconds.
Minimum value is 1.

**--container-startup-probe-timeout-seconds**:
Number of seconds after which the startup probe times out. Defaults to 1 second.
Minimum value is 1.

**--description**:
Description of the model.

**--explanation-metadata-file**:
Path to a local JSON file that contains the metadata describing the Model's
input and output for explanation.

**--explanation-method**:
Method used for explanation. Accepted values are
`integrated-gradients`, `xrai` and
`sampled-shapley`.

**--explanation-modality**:
Preset option specifying the modality of the uploaded model, which automatically
configures the distance measurement and feature normalization for the underlying
example index and queries. Accepted values are `IMAGE`,
`TEXT` and `TABULAR`. Should be used only when the
explanation method is `examples`.

**--explanation-nearest-neighbor-search-config-file**:
Path to a local JSON file that contains the configuration for the generated
index, the semantics are the same as metadata and should match
NearestNeighborSearchConfig. If you specify this parameter, no need to use
`explanation-modality` and `explanation-query` for preset.
Should be used only when the explanation method is `examples`.
An example of a JSON config file:

```
{
"contentsDeltaUri": "",
"config": {
    "dimensions": 50,
    "approximateNeighborsCount": 10,
    "distanceMeasureType": "SQUARED_L2_DISTANCE",
    "featureNormType": "NONE",
    "algorithmConfig": {
        "treeAhConfig": {
            "leafNodeEmbeddingCount": 1000,
            "leafNodesToSearchPercent": 100
        }
    }
  }
}
```

**--explanation-neighbor-count**:
The number of items to return when querying for examples. Should be used only
when the explanation method is `examples`.

**--explanation-path-count**:
Number of feature permutations to consider when approximating the Shapley values
for explanation.

**--explanation-query**:
Preset option controlling parameters for query speed-precision trade-off.
Accepted values are `PRECISE` and `FAST`. Should be used
only when the explanation method is `examples`.

**--explanation-step-count**:
Number of steps to approximate the path integral for explanation.

**--labels**:
Labels with user-defined metadata to organize your Models.
Label keys and values can be no longer than 64 characters (Unicode codepoints),
can only contain lowercase letters, numeric characters, underscores and dashes.
International characters are allowed.
See [https://goo.gl/xmQnxf](https://goo.gl/xmQnxf) for more
information and examples of labels.

**--model-id**:
ID to use for the uploaded Model, which will become the final component of the
model resource name.

**--parent-model**:
Resource name of the model into which to upload the version. Only specify this
field when uploading a new version.
Value should be provided in format:
projects/``PROJECT_ID``/locations/``REGION``/models/``PARENT_MODEL_ID``

**Region resource - Cloud region to upload model. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--region` on the command line with a fully
specified name;
- set the property `ai/region` with a fully specified name;
- choose one from the prompted list of available regions with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--region**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**--smooth-grad-noise-sigma**:
Single float value used to add noise to all the features for explanation. Only
applicable to explanation method `integrated-gradients` or
`xrai`.

**--smooth-grad-noise-sigma-by-feature**:
Noise sigma by features for explanation. Noise sigma represents the standard
deviation of the gaussian kernel that will be used to add noise to interpolated
inputs prior to computing gradients. Only applicable to explanation method
`integrated-gradients` or `xrai`.

**--smooth-grad-noisy-sample-count**:
Number of gradient samples used for approximation at explanation. Only
applicable to explanation method `integrated-gradients` or
`xrai`.

**--uris**:
Cloud Storage bucket paths where training data is stored. Should be used only
when the explanation method is `examples`.

**--version-aliases**:
Aliases used to reference a model version instead of auto-generated version ID.
The aliases mentioned in the flag will replace the aliases set in the model.

**--version-description**:
Description of the model version.

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
gcloud ai models upload
```

```
gcloud beta ai models upload
```