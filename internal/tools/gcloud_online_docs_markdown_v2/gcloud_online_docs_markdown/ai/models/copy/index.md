# gcloud ai models copy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/models/copy](https://cloud.google.com/sdk/gcloud/reference/ai/models/copy)*

**NAME**

: **gcloud ai models copy - copy a model**

**SYNOPSIS**

: **`gcloud ai models copy` `[--source-model](https://cloud.google.com/sdk/gcloud/reference/ai/models/copy#--source-model)`=`SOURCE_MODEL` [`[--kms-key-name](https://cloud.google.com/sdk/gcloud/reference/ai/models/copy#--kms-key-name)`=`KMS_KEY_NAME`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/ai/models/copy#--region)`=`REGION`] [`[--destination-model-id](https://cloud.google.com/sdk/gcloud/reference/ai/models/copy#--destination-model-id)`=`DESTINATION_MODEL_ID`     | `[--destination-parent-model](https://cloud.google.com/sdk/gcloud/reference/ai/models/copy#--destination-parent-model)`=`DESTINATION_PARENT_MODEL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/models/copy#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To copy a model `123` of project `example` from region
`us-central1` to region `europe-west4`, run:

```
gcloud ai models copy --source-model=projects/example/locations/us-central1/models/123 --region=projects/example/locations/europe-west4
```

**REQUIRED FLAGS**

: **--source-model**:
The resource name of the Model to copy. That Model must be in the same Project.
Format: `projects/{project}/locations/{location}/models/{model}`.

**OPTIONAL FLAGS**

: **--kms-key-name**:
The Cloud KMS resource identifier of the customer managed encryption key used to
protect the resource. Has the form:
`projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`.
The key needs to be in the same region as the destination region of the model to
be copied.

**Region resource - Cloud region to copy the model into. This represents a Cloud
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

**--destination-model-id**

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
gcloud alpha ai models copy
```

```
gcloud beta ai models copy
```