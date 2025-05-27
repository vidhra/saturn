# gcloud dataproc jobs submit hadoop  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop)*

**NAME**

: **gcloud dataproc jobs submit hadoop - submit a Hadoop job to a cluster**

**SYNOPSIS**

: **`gcloud dataproc jobs submit hadoop` (`[--class](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--class)`=`MAIN_CLASS`     | `[--jar](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--jar)`=`MAIN_JAR`) (`[--cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--cluster)`=`CLUSTER`     | `[--cluster-labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--cluster-labels)`=[`KEY`=`VALUE`,…]) [`[--archives](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--archives)`=[`ARCHIVE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--async)`] [`[--bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--bucket)`=`BUCKET`] [`[--driver-log-levels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--driver-log-levels)`=[`PACKAGE`=`LEVEL`,…]] [`[--driver-required-memory-mb](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--driver-required-memory-mb)`=`DRIVER_REQUIRED_MEMORY_MB`] [`[--driver-required-vcores](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--driver-required-vcores)`=`DRIVER_REQUIRED_VCORES`] [`[--files](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--files)`=[`FILE`,…]] [`[--jars](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--jars)`=[`JAR`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-failures-per-hour](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--max-failures-per-hour)`=`MAX_FAILURES_PER_HOUR`] [`[--max-failures-total](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--max-failures-total)`=`MAX_FAILURES_TOTAL`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--properties)`=[`PROPERTY`=`VALUE`,…]] [`[--properties-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--properties-file)`=`PROPERTIES_FILE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#GCLOUD-WIDE-FLAGS) …`] [-- `[JOB_ARGS](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#JOB_ARGS)` …]**

**DESCRIPTION**

: Submit a Hadoop job to a cluster.

**EXAMPLES**

: To submit a Hadoop job that runs the main class of a jar, run:

```
gcloud dataproc jobs submit hadoop --cluster=my-cluster --jar=my_jar.jar -- arg1 arg2
```

To submit a Hadoop job that runs a specific class of a jar, run:

```
gcloud dataproc jobs submit hadoop --cluster=my-cluster --class=org.my.main.Class --jars=my_jar1.jar,my_jar2.jar -- arg1 arg2
```

To submit a Hadoop job that runs a jar that is already on the cluster, run:

```
gcloud dataproc jobs submit hadoop --cluster=my-cluster --jar=file:///usr/lib/hadoop-op/hadoop-op-examples.jar -- wordcount gs://my_bucket/my_file.txt gs://my_bucket/output
```

**POSITIONAL ARGUMENTS**

: **[-- `JOB_ARGS` …]**:
The arguments to pass to the driver.
The '--' argument must be specified between gcloud specific args on the left and
JOB_ARGS on the right.

**REQUIRED FLAGS**

: **--class**

**--cluster**

**OPTIONAL FLAGS**

: **--archives**:
Comma separated list of archives to be provided to the job. must be one of the
following file formats: .zip, .tar, .tar.gz, or .tgz.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bucket**:
The Cloud Storage bucket to stage files in. Defaults to the cluster's configured
bucket.

**--driver-log-levels**:
A list of package to log4j log level pairs to configure driver logging. For
example: root=FATAL,com.example=INFO

**--driver-required-memory-mb**:
The memory allocation requested by the job driver in megabytes (MB) for
execution on the driver node group (it is used only by clusters with a driver
node group).

**--driver-required-vcores**:
The vCPU allocation requested by the job driver for execution on the driver node
group (it is used only by clusters with a driver node group).

**--files**:
Comma separated list of file paths to be provided to the job. A file path can
either be a path to a local file or a path to a file already in a Cloud Storage
bucket.

**--jars**:
Comma separated list of jar files to be provided to the MR and driver
classpaths.

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
A list of key value pairs to configure Hadoop.

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
gcloud alpha dataproc jobs submit hadoop
```

```
gcloud beta dataproc jobs submit hadoop
```