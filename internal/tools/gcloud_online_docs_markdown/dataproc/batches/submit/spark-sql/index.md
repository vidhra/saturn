# gcloud dataproc batches submit spark-sql  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql)*

**NAME**

: **gcloud dataproc batches submit spark-sql - submit a Spark SQL batch job**

**SYNOPSIS**

: **`gcloud dataproc batches submit spark-sql` `[SQL_SCRIPT](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#SQL_SCRIPT)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--async)`] [`[--batch](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--batch)`=`BATCH`] [`[--container-image](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--container-image)`=`CONTAINER_IMAGE`] [`[--deps-bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--deps-bucket)`=`DEPS_BUCKET`] [`[--history-server-cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--history-server-cluster)`=`HISTORY_SERVER_CLUSTER`] [`[--jars](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--jars)`=[`JAR`,…]] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--labels)`=[`KEY`=`VALUE`,…]] [`[--metastore-service](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--metastore-service)`=`METASTORE_SERVICE`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--properties)`=[`PROPERTY`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--region)`=`REGION`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--request-id)`=`REQUEST_ID`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--service-account)`=`SERVICE_ACCOUNT`] [`[--staging-bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--staging-bucket)`=`STAGING_BUCKET`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--tags)`=[`TAGS`,…]] [`[--ttl](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--ttl)`=`TTL`] [`[--user-workload-authentication-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--user-workload-authentication-type)`=`USER_WORKLOAD_AUTHENTICATION_TYPE`] [`[--vars](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--vars)`=[`NAME`=`VALUE`,…]] [`[--version](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--version)`=`VERSION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--network)`=`NETWORK`     | `[--subnet](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#--subnet)`=`SUBNET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Submit a Spark SQL batch job.

**EXAMPLES**

: To submit a Spark SQL job running "my-sql-script.sql" and upload it to
"gs://my-bucket", run:

```
gcloud dataproc batches submit spark-sql my-sql-script.sql --deps-bucket=gs://my-bucket --region=us-central1 --vars="NAME=VALUE,NAME2=VALUE2"
```

**POSITIONAL ARGUMENTS**

: **`SQL_SCRIPT`**:
URI of the script that contains Spark SQL queries to execute.

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

**--deps-bucket**:
A Cloud Storage bucket to upload workload dependencies.

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

**--vars**:
Mapping of query variable names to values (equivalent to the Spark SQL command:
SET name="value";).

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
gcloud beta dataproc batches submit spark-sql
```