# gcloud dataproc jobs submit flink  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink)*

**NAME**

: **gcloud dataproc jobs submit flink - submit a Flink job to a cluster**

**SYNOPSIS**

: **`gcloud dataproc jobs submit flink` (`[--class](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--class)`=`MAIN_CLASS`     | `[--jar](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--jar)`=`MAIN_JAR`) (`[--cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--cluster)`=`CLUSTER`     | `[--cluster-labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--cluster-labels)`=[`KEY`=`VALUE`,…]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--async)`] [`[--bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--bucket)`=`BUCKET`] [`[--driver-log-levels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--driver-log-levels)`=[`PACKAGE`=`LEVEL`,…]] [`[--driver-required-memory-mb](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--driver-required-memory-mb)`=`DRIVER_REQUIRED_MEMORY_MB`] [`[--driver-required-vcores](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--driver-required-vcores)`=`DRIVER_REQUIRED_VCORES`] [`[--jars](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--jars)`=[`JAR`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-failures-per-hour](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--max-failures-per-hour)`=`MAX_FAILURES_PER_HOUR`] [`[--max-failures-total](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--max-failures-total)`=`MAX_FAILURES_TOTAL`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--properties)`=[`PROPERTY`=`VALUE`,…]] [`[--properties-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--properties-file)`=`PROPERTIES_FILE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--region)`=`REGION`] [`[--savepoint](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#--savepoint)`=`SAVEPOINT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#GCLOUD-WIDE-FLAGS) …`] [-- `[JOB_ARGS](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink#JOB_ARGS)` …]**

**DESCRIPTION**

: Submit a Flink job to a cluster.

**EXAMPLES**

: To submit a Flink job that runs the main class of a jar, run:

```
gcloud dataproc jobs submit flink --cluster=my-cluster --region=us-central1 --jar=my_jar.jar -- arg1 arg2
```

To submit a Flink job that runs a specific class as an entrypoint:

```
gcloud dataproc jobs submit flink --cluster=my-cluster --region=us-central1 --class=org.my.main.Class --jars=my_jar.jar -- arg1 arg2
```

To submit a Flink job that runs a jar that is on the cluster, run:

```
gcloud dataproc jobs submit flink --cluster=my-cluster --region=us-central1 --jar=/usr/lib/flink/examples/streaming/TopSpeedWindowing.jar
```

**POSITIONAL ARGUMENTS**

: **[-- `JOB_ARGS` …]**:
The job arguments to pass.
The '--' argument must be specified between gcloud specific args on the left and
JOB_ARGS on the right.

**REQUIRED FLAGS**

: **--class**

**--cluster**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bucket**:
The Cloud Storage bucket to stage files in. Defaults to the cluster's configured
bucket.

**--driver-log-levels**:
List of package to log4j log level pairs to configure driver logging. For
example: root=FATAL,com.example=INFO.

**--driver-required-memory-mb**:
The memory allocation requested by the job driver in megabytes (MB) for
execution on the driver node group (it is used only by clusters with a driver
node group).

**--driver-required-vcores**:
The vCPU allocation requested by the job driver for execution on the driver node
group (it is used only by clusters with a driver node group).

**--jars**:
Comma-separated list of jar files to provide to the task manager classpaths.

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
List of key=value pairs to configure Flink. For a list of available properties,
see: [https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/config/](https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/config/).

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

**--savepoint**:
HCFS URI of the savepoint that is used to refer to the state of the previously
stopped job. The new job will resume previous state from there.

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
gcloud alpha dataproc jobs submit flink
```

```
gcloud beta dataproc jobs submit flink
```