# gcloud dataproc jobs submit trino  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino)*

**NAME**

: **gcloud dataproc jobs submit trino - submit a Trino job to a cluster**

**SYNOPSIS**

: **`gcloud dataproc jobs submit trino` (`[--cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--cluster)`=`CLUSTER`     | `[--cluster-labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--cluster-labels)`=[`KEY`=`VALUE`,…]) (`[--execute](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--execute)`=`QUERY`, `[-e](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#-e)` `[QUERY](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#QUERY)`     | `[--file](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--file)`=`FILE`, `[-f](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#-f)` `[FILE](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#FILE)`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--async)`] [`[--bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--bucket)`=`BUCKET`] [`[--client-tags](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--client-tags)`=[`CLIENT_TAG`,…]] [`[--continue-on-failure](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--continue-on-failure)`] [`[--driver-log-levels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--driver-log-levels)`=[`PACKAGE`=`LEVEL`,…]] [`[--driver-required-memory-mb](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--driver-required-memory-mb)`=`DRIVER_REQUIRED_MEMORY_MB`] [`[--driver-required-vcores](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--driver-required-vcores)`=`DRIVER_REQUIRED_VCORES`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-failures-per-hour](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--max-failures-per-hour)`=`MAX_FAILURES_PER_HOUR`] [`[--max-failures-total](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--max-failures-total)`=`MAX_FAILURES_TOTAL`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--properties)`=[`PARAM`=`VALUE`,…]] [`[--properties-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--properties-file)`=`PROPERTIES_FILE`] [`[--query-output-format](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--query-output-format)`=`QUERY_OUTPUT_FORMAT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Submit a Trino job to a cluster

**EXAMPLES**

: To submit a Trino job with a local script, run:

```
gcloud dataproc jobs submit trino --cluster=my-cluster --file=my_script.R
```

To submit a Trino job with inline queries, run:

```
gcloud dataproc jobs submit trino --cluster=my-cluster -e="SELECT * FROM foo WHERE bar > 2"
```

**REQUIRED FLAGS**

: **--cluster**

**--execute**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bucket**:
The Cloud Storage bucket to stage files in. Defaults to the cluster's configured
bucket.

**--client-tags**:
A list of Trino client tags to attach to this query.

**--continue-on-failure**:
Whether to continue if a query fails.

**--driver-log-levels**:
A list of package-to-log4j log level pairs to configure driver logging. For
example: root=FATAL,com.example=INFO

**--driver-required-memory-mb**:
The memory allocation requested by the job driver in megabytes (MB) for
execution on the driver node group (it is used only by clusters with a driver
node group).

**--driver-required-vcores**:
The vCPU allocation requested by the job driver for execution on the driver node
group (it is used only by clusters with a driver node group).

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
A list of key value pairs to set Trino session properties.

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

**--query-output-format**:
The query output display format. See the Trino documentation for supported
output formats.

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
gcloud alpha dataproc jobs submit trino
```

```
gcloud beta dataproc jobs submit trino
```