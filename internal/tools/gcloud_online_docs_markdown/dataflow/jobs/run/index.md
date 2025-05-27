# gcloud dataflow jobs run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run)*

**NAME**

: **gcloud dataflow jobs run - runs a job from the specified path**

**SYNOPSIS**

: **`gcloud dataflow jobs run` `[JOB_NAME](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#JOB_NAME)` `[--gcs-location](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--gcs-location)`=`GCS_LOCATION` [`[--additional-experiments](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--additional-experiments)`=[`ADDITIONAL_EXPERIMENTS`,…]] [`[--additional-user-labels](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--additional-user-labels)`=[`ADDITIONAL_USER_LABELS`,…]] [`[--dataflow-kms-key](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--dataflow-kms-key)`=`DATAFLOW_KMS_KEY`] [`[--disable-public-ips](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--disable-public-ips)`] [`[--enable-streaming-engine](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--enable-streaming-engine)`] [`[--max-workers](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--max-workers)`=`MAX_WORKERS`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--network)`=`NETWORK`] [`[--num-workers](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--num-workers)`=`NUM_WORKERS`] [`[--parameters](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--parameters)`=[`PARAMETERS`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--region)`=`REGION_ID`] [`[--service-account-email](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--service-account-email)`=`SERVICE_ACCOUNT_EMAIL`] [`[--staging-location](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--staging-location)`=`STAGING_LOCATION`] [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--subnetwork)`=`SUBNETWORK`] [`[--worker-machine-type](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--worker-machine-type)`=`WORKER_MACHINE_TYPE`] [[`[--[no-]update](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--[no-]update)` : `[--transform-name-mappings](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--transform-name-mappings)`=[`TRANSFORM_NAME_MAPPINGS`,…]]] [`[--worker-region](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--worker-region)`=`WORKER_REGION`     | `[--worker-zone](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--worker-zone)`=`WORKER_ZONE`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Runs a job from the specified path.

**POSITIONAL ARGUMENTS**

: **`JOB_NAME`**:
The unique name to assign to the job.

**REQUIRED FLAGS**

: **--gcs-location**:
The Google Cloud Storage location of the job template to run. (Must be a URL
beginning with 'gs://'.)

**OPTIONAL FLAGS**

: **--additional-experiments**:
Additional experiments to pass to the job. These experiments are appended to any
experiments already set by the template.

**--additional-user-labels**:
Additional user labels to pass to the job. Example:
--additional-user-labels='key1=value1,key2=value2'

**--dataflow-kms-key**:
The Cloud KMS key to protect the job resources.

**--disable-public-ips**:
The Cloud Dataflow workers must not use public IP addresses. Overrides the
default `dataflow/disable_public_ips` property value for this command
invocation.

**--enable-streaming-engine**:
Enabling Streaming Engine for the streaming job. Overrides the default
`dataflow/enable_streaming_engine` property value for this command
invocation.

**--max-workers**:
The maximum number of workers to run.

**--network**:
The Compute Engine network for launching instances to run your pipeline.

**--num-workers**:
The initial number of workers to use.

**--parameters**:
The parameters to pass to the job.

**--region**:
Region ID of the job's regional endpoint. Defaults to 'us-central1'.

**--service-account-email**:
The service account to run the workers as.

**--staging-location**:
The Google Cloud Storage location to stage temporary files. (Must be a URL
beginning with 'gs://'.)

**--subnetwork**:
The Compute Engine subnetwork for launching instances to run your pipeline.

**--worker-machine-type**:
The type of machine to use for workers. Defaults to server-specified.

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
gcloud beta dataflow jobs run
```