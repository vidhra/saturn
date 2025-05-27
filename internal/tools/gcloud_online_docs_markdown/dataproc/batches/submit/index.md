# gcloud dataproc batches submit  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit)*

**NAME**

: **gcloud dataproc batches submit - submit a Dataproc batch job**

**SYNOPSIS**

: **`gcloud dataproc batches submit` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#COMMAND)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--async)`] [`[--batch](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--batch)`=`BATCH`] [`[--container-image](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--container-image)`=`CONTAINER_IMAGE`] [`[--history-server-cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--history-server-cluster)`=`HISTORY_SERVER_CLUSTER`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--labels)`=[`KEY`=`VALUE`,…]] [`[--metastore-service](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--metastore-service)`=`METASTORE_SERVICE`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--properties)`=[`PROPERTY`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--region)`=`REGION`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--request-id)`=`REQUEST_ID`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--service-account)`=`SERVICE_ACCOUNT`] [`[--staging-bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--staging-bucket)`=`STAGING_BUCKET`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--tags)`=[`TAGS`,…]] [`[--ttl](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--ttl)`=`TTL`] [`[--user-workload-authentication-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--user-workload-authentication-type)`=`USER_WORKLOAD_AUTHENTICATION_TYPE`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--version)`=`VERSION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--network)`=`NETWORK`     | `[--subnet](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--subnet)`=`SUBNET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Submit a Dataproc batch job.

**EXAMPLES**

: To submit a PySpark job, run:

```
gcloud dataproc batches submit pyspark my-pyspark.py --region='us-central1' --deps-bucket=gs://my-bucket --py-files='path/to/my/python/scripts'
```

To submit a Spark job, run:

```
gcloud dataproc batches submit spark --region='us-central1' --deps-bucket=gs://my-bucket --jar='my_jar.jar' -- ARG1 ARG2
```

To submit a Spark-R job, run:

```
gcloud dataproc batches submit spark-r my-main-r.r --region='us-central1' --deps-bucket=gs://my-bucket -- ARG1 ARG2
```

To submit a Spark-Sql job, run:

```
gcloud dataproc batches submit spark-sql 'my-sql-script.sql' --region='us-central1' --deps-bucket=gs://my-bucket --vars='variable=value'
```

**FLAGS**

: **--async**:
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

**--history-server-cluster**:
Spark History Server configuration for the batch/session job. Resource name of
an existing Dataproc cluster to act as a Spark History Server for the workload
in the format: "projects/{project_id}/regions/{region}/clusters/{cluster_name}".

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

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[pyspark](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark)`**:
Submit a PySpark batch job.

**`[spark](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark)`**:
Submit a Spark batch job.

**`[spark-r](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-r)`**:
Submit a Spark R batch job.

**`[spark-sql](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql)`**:
Submit a Spark SQL batch job.

**NOTES**

: This variant is also available:

```
gcloud beta dataproc batches submit
```