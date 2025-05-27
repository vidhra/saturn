# gcloud dataflow yaml run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run](https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run)*

**NAME**

: **gcloud dataflow yaml run - runs a job from the specified path**

**SYNOPSIS**

: **`gcloud dataflow yaml run` `[JOB_NAME](https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run#JOB_NAME)` (`[--yaml-pipeline](https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run#--yaml-pipeline)`=`YAML_PIPELINE`     | `[--yaml-pipeline-file](https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run#--yaml-pipeline-file)`=`YAML_PIPELINE_FILE`) [`[--jinja-variables](https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run#--jinja-variables)`=`JSON_OBJECT`] [`[--pipeline-options](https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run#--pipeline-options)`=[`OPTIONS`=`VALUE`;`[OPTION](https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run#OPTION)`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run#--region)`=`REGION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/yaml/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Runs a job from the specified YAML description or Cloud Storage path.

**EXAMPLES**

: To run a job from YAML, run:

```
gcloud dataflow yaml run my-job --yaml-pipeline-file=gs://yaml-path --region=europe-west1
```

**POSITIONAL ARGUMENTS**

: **`JOB_NAME`**:
Unique name to assign to the job.

**REQUIRED FLAGS**

: **--yaml-pipeline**

**OPTIONAL FLAGS**

: **--jinja-variables**:
Jinja2 variables to be used in reifying the yaml.

**--pipeline-options**:
Pipeline options to pass to the job.

**--region**:
Region ID of the job's regional endpoint. Defaults to 'us-central1'.

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

: This variant is also available:

```
gcloud beta dataflow yaml run
```