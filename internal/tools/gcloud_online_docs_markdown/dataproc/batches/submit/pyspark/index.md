# gcloud dataproc batches submit pyspark  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark)*

**NAME**

: **gcloud dataproc batches submit pyspark - submit a PySpark batch job**

**SYNOPSIS**

: **`gcloud dataproc batches submit pyspark` `[MAIN_PYTHON_FILE](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#MAIN_PYTHON_FILE)` [`[--archives](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--archives)`=[`ARCHIVE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--async)`] [`[--batch](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--batch)`=`BATCH`] [`[--container-image](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--container-image)`=`CONTAINER_IMAGE`] [`[--deps-bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--deps-bucket)`=`DEPS_BUCKET`] [`[--files](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--files)`=[`FILE`,…]] [`[--history-server-cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--history-server-cluster)`=`HISTORY_SERVER_CLUSTER`] [`[--jars](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--jars)`=[`JAR`,…]] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--labels)`=[`KEY`=`VALUE`,…]] [`[--metastore-service](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--metastore-service)`=`METASTORE_SERVICE`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--properties)`=[`PROPERTY`=`VALUE`,…]] [`[--py-files](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--py-files)`=[`PY`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--region)`=`REGION`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--request-id)`=`REQUEST_ID`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--service-account)`=`SERVICE_ACCOUNT`] [`[--staging-bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--staging-bucket)`=`STAGING_BUCKET`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--tags)`=[`TAGS`,…]] [`[--ttl](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--ttl)`=`TTL`] [`[--user-workload-authentication-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--user-workload-authentication-type)`=`USER_WORKLOAD_AUTHENTICATION_TYPE`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--version)`=`VERSION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--network)`=`NETWORK`     | `[--subnet](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#--subnet)`=`SUBNET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#GCLOUD-WIDE-FLAGS) …`] [-- `[JOB_ARG](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark#JOB_ARG)` …]**

**DESCRIPTION**

: Submit a PySpark batch job.

**EXAMPLES**

: To submit a PySpark batch job called "my-batch" that runs "my-pyspark.py", run:

```
gcloud dataproc batches submit pyspark my-pyspark.py --batch=my-batch --deps-bucket=gs://my-bucket --region=us-central1 --py-files='path/to/my/python/script.py'
```

**POSITIONAL ARGUMENTS**

: **`MAIN_PYTHON_FILE`**:
URI of the main Python file to use as the Spark driver. Must be a
``.py`` file.

**[-- `JOB_ARG` …]**:
Arguments to pass to the driver.
The '--' argument must be specified between gcloud specific args on the left and
JOB_ARG on the right.

**FLAGS**

: **--archives**:
Archives to be extracted into the working directory. Supported file types: .jar,
.tar, .tar.gz, .tgz, and .zip.

**--async**:
Return immediately without waiting for the operation in progress to complete.

**--batch**:
The ID of the batch job to submit. The ID must contain only lowercase letters
(a-z), numbers (0-9) and hyphens (-). The length of the name must be between 4
and 63 characters. If this argument is not provided, a random generated UUID
will be used.

**--container-image**:
Optional custom container image to use for the batch/session runtime
environment. If not specified, a default container image will be used. The value
should follow the container image naming format:
{registry}/{repository}/{name}:{tag}, for example,
gcr.io/my-project/my-image:1.2.3

**--deps-bucket**:
A Cloud Storage bucket to upload workload dependencies.

**--files**:
Files to be placed in the working directory.

**--history-server-cluster**:
Spark History Server configuration for the batch/session job. Resource name of
an existing Dataproc cluster to act as a Spark History Server for the workload
in the format: "projects/{project_id}/regions/{region}/clusters/{cluster_name}".

**--jars**:
Comma-separated list of jar files to be provided to the classpaths.

**--kms-key**:
Cloud KMS key to use for encryption.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--metastore-service**:
Name of a Dataproc Metastore service to be used as an external metastore in the
format: "projects/{project-id}/locations/{region}/services/{service-name}".

**--properties**:
Specifies configuration properties for the workload. See [Dataproc
Serverless for Spark documentation](https://cloud.google.com/dataproc-serverless/docs/concepts/properties) for the list of supported properties.

**--py-files**:
Comma-separated list of Python scripts to be passed to the PySpark framework.
Supported file types: ``.py``,
``.egg`` and
``.zip.``

**Region resource - Dataproc region to use. Each Dataproc region constitutes an
independent resource namespace constrained to deploying instances into Compute
Engine zones inside the region. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--region` on the command line with a fully
specified name;
- set the property `dataproc/region` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--region**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**--request-id**:
A unique ID that identifies the request. If the service receives two batch
create requests with the same request_id, the second request is ignored and the
operation that corresponds to the first batch created and stored in the backend
is returned. Recommendation: Always set this value to a UUID. The value must
contain only letters (a-z, A-Z), numbers (0-9), underscores (`), and
hyphens (-). The maximum length is 40 characters.`

**--service-account**:
The IAM service account to be used for a batch/session job.

**--staging-bucket**:
The Cloud Storage bucket to use to store job dependencies, config files, and job
driver console output. If not specified, the default [staging bucket]
(https://cloud.google.com/dataproc-serverless/docs/concepts/buckets) is used.

**--tags**:
Network tags for traffic control.

**--ttl**:
The duration after the workload will be unconditionally terminated, for example,
'20m' or '1h'. Run [gcloud
topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats.

**--user-workload-authentication-type**:
Whether to use END_USER_CREDENTIALS or SERVICE_ACCOUNT to run the workload.

**--version**:
Optional runtime version. If not specified, a default version will be used.

**--network**

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
gcloud beta dataproc batches submit pyspark
```