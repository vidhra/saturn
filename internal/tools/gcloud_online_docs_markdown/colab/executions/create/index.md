# gcloud colab executions create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/colab/executions/create](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create)*

**NAME**

: **gcloud colab executions create - create an execution**

**SYNOPSIS**

: **`gcloud colab executions create` (`[--display-name](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--display-name)`=`DISPLAY_NAME` `[--gcs-output-uri](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--gcs-output-uri)`=`GCS_OUTPUT_URI` `[--notebook-runtime-template](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--notebook-runtime-template)`=`NOTEBOOK_RUNTIME_TEMPLATE` (`[--direct-content](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--direct-content)`=`DIRECT_CONTENT` | [`[--dataform-repository-name](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--dataform-repository-name)`=`DATAFORM_REPOSITORY_NAME` : `[--commit-sha](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--commit-sha)`=`COMMIT_SHA`] | [`[--gcs-notebook-uri](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--gcs-notebook-uri)`=`GCS_NOTEBOOK_URI` : `[--generation](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--generation)`=`GENERATION`]) (`[--service-account](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--service-account)`=`SERVICE_ACCOUNT` | `[--user-email](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--user-email)`=`USER_EMAIL`) : `[--execution-timeout](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--execution-timeout)`=`EXECUTION_TIMEOUT`; default="24h") [`[--async](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--async)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/colab/executions/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a notebook execution to be used on a Colab Enterprise runtime.

**EXAMPLES**

: To create an execution of a notebook file with Cloud Storage URI
`gs://my-bucket/my-notebook.ipynb`, with an execution job display
name `my-execution`, compute configured from runtime template
`my-runtime-template-id`, running with service account
`my-service-account@my-project.iam.gserviceaccount.com`, with results
uploaded to Cloud Storage bucket `gs://my-bucket/results`, and in
region `us-central1` run:

```
gcloud colab executions create --display-name=my-execution --runtime-template=my-runtime-template-id --gcs-notebook-uri=gs://my-bucket/my-notebook.ipynb --service-account=my-service-account@my-project.iam.gserviceaccount.com --gcs-output-uri=gs://my-bucket/results --region=us-central1
```

**REQUIRED FLAGS**

: **--display-name**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**Region resource - Cloud region to create. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--region` on the command line with a fully
specified name;
- set the property `colab/region` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--region**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `--region` on the command line;
- set the property `colab/region`.**

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
gcloud beta colab executions create
```