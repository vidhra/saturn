# gcloud dataproc batches submit spark  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark)*

**NAME**

: **gcloud dataproc batches submit spark - submit a Spark batch job**

**SYNOPSIS**

: **`gcloud dataproc batches submit spark` (`[--class](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--class)`=`MAIN_CLASS`     | `[--jar](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--jar)`=`MAIN_JAR`) [`[--archives](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--archives)`=[`ARCHIVE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--async)`] [`[--batch](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--batch)`=`BATCH`] [`[--container-image](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--container-image)`=`CONTAINER_IMAGE`] [`[--deps-bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--deps-bucket)`=`DEPS_BUCKET`] [`[--files](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--files)`=[`FILE`,…]] [`[--history-server-cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--history-server-cluster)`=`HISTORY_SERVER_CLUSTER`] [`[--jars](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--jars)`=[`JAR`,…]] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--labels)`=[`KEY`=`VALUE`,…]] [`[--metastore-service](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--metastore-service)`=`METASTORE_SERVICE`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--properties)`=[`PROPERTY`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--region)`=`REGION`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--request-id)`=`REQUEST_ID`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--service-account)`=`SERVICE_ACCOUNT`] [`[--staging-bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--staging-bucket)`=`STAGING_BUCKET`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--tags)`=[`TAGS`,…]] [`[--ttl](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--ttl)`=`TTL`] [`[--user-workload-authentication-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--user-workload-authentication-type)`=`USER_WORKLOAD_AUTHENTICATION_TYPE`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--version)`=`VERSION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--network)`=`NETWORK`     | `[--subnet](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--subnet)`=`SUBNET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#GCLOUD-WIDE-FLAGS) …`] [-- `[JOB_ARG](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#JOB_ARG)` …]**

**DESCRIPTION**

: Submit a Spark batch job.

**EXAMPLES**

: To submit a Spark job, run:

```
gcloud dataproc batches submit spark --region=us-central1 --jar=my_jar.jar --deps-bucket=gs://my-bucket -- ARG1 ARG2
```

To submit a Spark job that runs a specific class of a jar, run:

```
gcloud dataproc batches submit spark --region=us-central1 --class=org.my.main.Class --jars=my_jar1.jar,my_jar2.jar --deps-bucket=gs://my-bucket -- ARG1 ARG2
```

To submit a Spark job that runs a jar installed on the cluster, run:

```
gcloud dataproc batches submit spark --region=us-central1 --class=org.apache.spark.examples.SparkPi --deps-bucket=gs://my-bucket --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar -- 15
```

**POSITIONAL ARGUMENTS**

: **[-- `JOB_ARG` …]**:
Arguments to pass to the driver.
The '--' argument must be specified between gcloud specific args on the left and
JOB_ARG on the right.

**REQUIRED FLAGS**

: **--class**

**OPTIONAL FLAGS**

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
gcloud beta dataproc batches submit spark
```