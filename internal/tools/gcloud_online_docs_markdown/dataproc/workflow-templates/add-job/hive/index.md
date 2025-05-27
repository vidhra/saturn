# gcloud dataproc workflow-templates add-job hive  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive)*

**NAME**

: **gcloud dataproc workflow-templates add-job hive - add a Hive job to the workflow template**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates add-job hive` `[--step-id](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--step-id)`=`STEP_ID` (`[--execute](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--execute)`=`QUERY`, `[-e](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#-e)` `[QUERY](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#QUERY)`     | `[--file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--file)`=`FILE`, `[-f](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#-f)` `[FILE](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#FILE)`) (`[--workflow-template](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--workflow-template)`=`WORKFLOW_TEMPLATE` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--region)`=`REGION`) [`[--continue-on-failure](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--continue-on-failure)`] [`[--jars](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--jars)`=[`JAR`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--labels)`=[`KEY`=`VALUE`,…]] [`[--params](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--params)`=[`PARAM`=`VALUE`,…]] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--properties)`=[`PROPERTY`=`VALUE`,…]] [`[--properties-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--properties-file)`=`PROPERTIES_FILE`] [`[--start-after](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#--start-after)`=`STEP_ID`,[`[STEP_ID](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#STEP_ID)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add a Hive job to the workflow template.

**EXAMPLES**

: To add a Hive job executing query 'QUERY' to a the workflow template
'my-workflow-template' in region 'us-central1' with step-id 'my-step-id' , run:

```
gcloud dataproc workflow-templates add-job hive --step-id=my-step_id -e=QUERY --workflow-template=my-workflow-template --region=us-central1
```

**REQUIRED FLAGS**

: **--step-id**:
The step ID of the job in the workflow template.

**--execute**

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

: **--continue-on-failure**:
Whether to continue if a single query fails.

**--jars**:
Comma separated list of jar files to be provided to the Hive and MR. May contain
UDFs.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--params**:
A list of key value pairs to set variables in the Hive queries.

**--properties**:
A list of key value pairs to configure Hive.

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
gcloud alpha dataproc workflow-templates add-job hive
```

```
gcloud beta dataproc workflow-templates add-job hive
```