# gcloud dataproc jobs submit spark-r  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r)*

**NAME**

: **gcloud dataproc jobs submit spark-r - submit a SparkR job to a cluster**

**SYNOPSIS**

: **`gcloud dataproc jobs submit spark-r` `[R_FILE](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#R_FILE)` (`[--cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--cluster)`=`CLUSTER`     | `[--cluster-labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--cluster-labels)`=[`KEY`=`VALUE`,…]) [`[--archives](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--archives)`=[`ARCHIVE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--async)`] [`[--bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--bucket)`=`BUCKET`] [`[--driver-log-levels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--driver-log-levels)`=[`PACKAGE`=`LEVEL`,…]] [`[--driver-required-memory-mb](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--driver-required-memory-mb)`=`DRIVER_REQUIRED_MEMORY_MB`] [`[--driver-required-vcores](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--driver-required-vcores)`=`DRIVER_REQUIRED_VCORES`] [`[--files](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--files)`=[`FILE`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-failures-per-hour](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--max-failures-per-hour)`=`MAX_FAILURES_PER_HOUR`] [`[--max-failures-total](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--max-failures-total)`=`MAX_FAILURES_TOTAL`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--properties)`=[`PROPERTY`=`VALUE`,…]] [`[--properties-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--properties-file)`=`PROPERTIES_FILE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#GCLOUD-WIDE-FLAGS) …`] [-- `[JOB_ARGS](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r#JOB_ARGS)` …]**

**DESCRIPTION**

: Submit a SparkR job to a cluster.

**EXAMPLES**

: To submit a SparkR job with a local script, run:

```
gcloud dataproc jobs submit spark-r --cluster=my-cluster my_script.R
```

To submit a Spark job that runs a script already on the cluster, run:

```
gcloud dataproc jobs submit spark-r --cluster=my-cluster file:///…/my_script.R -- gs://my_bucket/data.csv
```

**POSITIONAL ARGUMENTS**

: **`R_FILE`**:
Main .R file to run as the driver.

**[-- `JOB_ARGS` …]**:
Arguments to pass to the driver.
The '--' argument must be specified between gcloud specific args on the left and
JOB_ARGS on the right.

**REQUIRED FLAGS**

: **--cluster**

**OPTIONAL FLAGS**

: **--archives**:
Comma separated list of archives to be extracted into the working directory of
each executor. Must be one of the following file formats: .zip, .tar, .tar.gz,
or .tgz.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bucket**:
The Cloud Storage bucket to stage files in. Defaults to the cluster's configured
bucket.

**--driver-log-levels**:
List of key value pairs to configure driver logging, where key is a package and
value is the log4j log level. For example: root=FATAL,com.example=INFO

**--driver-required-memory-mb**:
The memory allocation requested by the job driver in megabytes (MB) for
execution on the driver node group (it is used only by clusters with a driver
node group).

**--driver-required-vcores**:
The vCPU allocation requested by the job driver for execution on the driver node
group (it is used only by clusters with a driver node group).

**--files**:
Comma separated list of files to be placed in the working directory of both the
app driver and executors.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--max-failures-per-hour**:
Specifies the maximum number of times a job can be restarted per hour in event
of failure. Default is 0 (no retries after job failure).

**--max-failures-total**:
Specifies the maximum total number of times a job can be restarted after the job
fails. Default is 0 (no retries after job failure).

**--properties**:
List of key value pairs to configure SparkR. For a list of available properties,
see: [https://spark.apache.org/docs/latest/configuration.html#available-properties](https://spark.apache.org/docs/latest/configuration.html#available-properties).

**--properties-file**:
Path to a local file or a file in a Cloud Storage bucket containing
configuration properties for the job. The client machine running this command
must have read permission to the file.
Specify properties in the form of property=value in the text file. For example:

```
# Properties to set for the job:
  key1=value1
  key2=value2
  # Comment out properties not used.
  # key3=value3
```

If a property is set in both `--properties` and
`--properties-file`, the value defined in `--properties`
takes precedence.

**--region**:
Dataproc region to use. Each Dataproc region constitutes an independent resource
namespace constrained to deploying instances into Compute Engine zones inside
the region. Overrides the default `dataproc/region` property value
for this command invocation.

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
gcloud alpha dataproc jobs submit spark-r
```

```
gcloud beta dataproc jobs submit spark-r
```