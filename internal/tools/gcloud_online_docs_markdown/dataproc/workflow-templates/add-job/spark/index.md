# gcloud dataproc workflow-templates add-job spark  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark)*

**NAME**

: **gcloud dataproc workflow-templates add-job spark - add a Spark job to the workflow template**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates add-job spark` `[--step-id](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--step-id)`=`STEP_ID` (`[--workflow-template](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--workflow-template)`=`WORKFLOW_TEMPLATE` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--region)`=`REGION`) [`[--archives](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--archives)`=[`ARCHIVE`,…]] [`[--driver-log-levels](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--driver-log-levels)`=[`PACKAGE`=`LEVEL`,…]] [`[--files](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--files)`=[`FILE`,…]] [`[--jars](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--jars)`=[`JAR`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--labels)`=[`KEY`=`VALUE`,…]] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--properties)`=[`PROPERTY`=`VALUE`,…]] [`[--properties-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--properties-file)`=`PROPERTIES_FILE`] [`[--start-after](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--start-after)`=`STEP_ID`,[`[STEP_ID](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#STEP_ID)`,…]] [`[--class](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--class)`=`MAIN_CLASS` `[--jar](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#--jar)`=`MAIN_JAR`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#GCLOUD-WIDE-FLAGS) …`] [-- `[JOB_ARGS](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark#JOB_ARGS)` …]**

**DESCRIPTION**

: Add a Spark job to the workflow template.

**EXAMPLES**

: To add a Spark job with files 'file1' and 'file2' to a the workflow template
'my-workflow-template' in region 'us-central1' with step-id 'my-step-id' , run:

```
gcloud dataproc workflow-templates add-job spark --step-id=my-step_id --files="file1,file2" --workflow-template=my-workflow-template --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **[-- `JOB_ARGS` …]**:
Arguments to pass to the driver.
The '--' argument must be specified between gcloud specific args on the left and
JOB_ARGS on the right.

**REQUIRED FLAGS**

: **--step-id**:
The step ID of the job in the workflow template.

**Template resource - The name of the workflow template to add job to. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--workflow-template` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--workflow-template**:
ID of the template or fully qualified identifier for the template.
To set the `template` attribute:

- provide the argument `--workflow-template` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--region**:
Dataproc region for the template. Each Dataproc region constitutes an
independent resource namespace constrained to deploying instances into Compute
Engine zones inside the region. Overrides the default
`dataproc/region` property value for this command invocation.
To set the `region` attribute:

- provide the argument `--workflow-template` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**OPTIONAL FLAGS**

: **--archives**:
Comma separated list of archives to be extracted into the working directory of
each executor. Must be one of the following file formats: .zip, .tar, .tar.gz,
or .tgz.

**--driver-log-levels**:
List of package to log4j log level pairs to configure driver logging. For
example: root=FATAL,com.example=INFO

**--files**:
Comma separated list of files to be placed in the working directory of both the
app driver and executors.

**--jars**:
Comma separated list of jar files to be provided to the executor and driver
classpaths.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--properties**:
List of key value pairs to configure Spark. For a list of available properties,
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

**--start-after**:
(Optional) List of step IDs to start this job after.

**--class**:
The class containing the main method of the driver. Must be in a provided jar or
jar that is already on the classpath

**--jar**:
The HCFS URI of jar file containing the driver jar.

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
gcloud alpha dataproc workflow-templates add-job spark
```

```
gcloud beta dataproc workflow-templates add-job spark
```