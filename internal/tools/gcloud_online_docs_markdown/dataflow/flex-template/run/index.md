# gcloud dataflow flex-template run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run)*

**NAME**

: **gcloud dataflow flex-template run - runs a job from the specified path**

**SYNOPSIS**

: **`gcloud dataflow flex-template run` `[JOB_NAME](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#JOB_NAME)` `[--template-file-gcs-location](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--template-file-gcs-location)`=`TEMPLATE_FILE_GCS_LOCATION` [`[--additional-experiments](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--additional-experiments)`=[`ADDITIONAL_EXPERIMENTS`,…]] [`[--additional-pipeline-options](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--additional-pipeline-options)`=[`ADDITIONAL_PIPELINE_OPTIONS`,…]] [`[--additional-user-labels](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--additional-user-labels)`=[`ADDITIONAL_USER_LABELS`,…]] [`[--dataflow-kms-key](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--dataflow-kms-key)`=`DATAFLOW_KMS_KEY`] [`[--disable-public-ips](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--disable-public-ips)`] [`[--enable-streaming-engine](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--enable-streaming-engine)`] [`[--flexrs-goal](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--flexrs-goal)`=`FLEXRS_GOAL`] [`[--launcher-machine-type](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--launcher-machine-type)`=`LAUNCHER_MACHINE_TYPE`] [`[--max-workers](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--max-workers)`=`MAX_WORKERS`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--network)`=`NETWORK`] [`[--num-workers](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--num-workers)`=`NUM_WORKERS`] [`[--parameters](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--parameters)`=[`PARAMETERS`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--region)`=`REGION_ID`] [`[--service-account-email](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--service-account-email)`=`SERVICE_ACCOUNT_EMAIL`] [`[--staging-location](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--staging-location)`=`STAGING_LOCATION`] [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--subnetwork)`=`SUBNETWORK`] [`[--temp-location](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--temp-location)`=`TEMP_LOCATION`] [`[--worker-machine-type](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--worker-machine-type)`=`WORKER_MACHINE_TYPE`] [[`[--[no-]update](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--[no-]update)` : `[--transform-name-mappings](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--transform-name-mappings)`=[`TRANSFORM_NAME_MAPPINGS`,…]]] [`[--worker-region](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--worker-region)`=`WORKER_REGION`     | `[--worker-zone](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--worker-zone)`=`WORKER_ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Runs a job from the specified flex template gcs path.

**EXAMPLES**

: To run a job from the flex template, run:

```
gcloud dataflow flex-template run my-job --template-file-gcs-location=gs://flex-template-path --region=europe-west1 --parameters=input="gs://input",output="gs://output-path" --max-workers=5
```

**POSITIONAL ARGUMENTS**

: **`JOB_NAME`**:
Unique name to assign to the job.

**REQUIRED FLAGS**

: **--template-file-gcs-location**:
Google Cloud Storage location of the flex template to run. (Must be a URL
beginning with 'gs://'.)

**OPTIONAL FLAGS**

: **--additional-experiments**:
Additional experiments to pass to the job. Example:
--additional-experiments=experiment1,experiment2=value2

**--additional-pipeline-options**:
Additional pipeline options to pass to the job. Example:
--additional-pipeline-options=option1=value1,option2=value2

**--additional-user-labels**:
Additional user labels to pass to the job. Example:
--additional-user-labels='key1=value1,key2=value2'

**--dataflow-kms-key**:
Cloud KMS key to protect the job resources.

**--disable-public-ips**:
Cloud Dataflow workers must not use public IP addresses. Overrides the default
`dataflow/disable_public_ips` property value for this command
invocation.

**--enable-streaming-engine**:
Enabling Streaming Engine for the streaming job. Overrides the default
`dataflow/enable_streaming_engine` property value for this command
invocation.

**--flexrs-goal**:
FlexRS goal for the flex template job. `FLEXRS_GOAL` must
be one of: `COST_OPTIMIZED`, `SPEED_OPTIMIZED`.

**--launcher-machine-type**:
The machine type to use for launching the job. The default isn1-standard-1.

**--max-workers**:
Maximum number of workers to run.

**--network**:
Compute Engine network for launching instances to run your pipeline.

**--num-workers**:
Initial number of workers to use.

**--parameters**:
Parameters to pass to the job.

**--region**:
Region ID of the job's regional endpoint. Defaults to 'us-central1'.

**--service-account-email**:
Service account to run the workers as.

**--staging-location**:
Default Google Cloud Storage location to stage local files.(Must be a URL
beginning with 'gs://'.)

**--subnetwork**:
Compute Engine subnetwork for launching instances to run your pipeline.

**--temp-location**:
Default Google Cloud Storage location to stage temporary files. If not set,
defaults to the value for --staging-location.(Must be a URL beginning with
'gs://'.)

**--worker-machine-type**:
Type of machine to use for workers. Defaults to server-specified.

**--[no-]update**:
Set this to true for streaming update jobs. Use `--update` to enable
and `--no-update` to disable.

**--transform-name-mappings**:
Transform name mappings for the streaming update job.

**--worker-region**

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
gcloud beta dataflow flex-template run
```