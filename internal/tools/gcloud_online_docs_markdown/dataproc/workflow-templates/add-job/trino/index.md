# gcloud dataproc workflow-templates add-job trino  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino)*

**NAME**

: **gcloud dataproc workflow-templates add-job trino - add a Trino job to the workflow template**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates add-job trino` `[--step-id](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--step-id)`=`STEP_ID` (`[--execute](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--execute)`=`QUERY`, `[-e](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#-e)` `[QUERY](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#QUERY)`     | `[--file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--file)`=`FILE`, `[-f](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#-f)` `[FILE](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#FILE)`) (`[--workflow-template](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--workflow-template)`=`WORKFLOW_TEMPLATE` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--region)`=`REGION`) [`[--client-tags](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--client-tags)`=[`CLIENT_TAG`,…]] [`[--continue-on-failure](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--continue-on-failure)`] [`[--driver-log-levels](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--driver-log-levels)`=[`PACKAGE`=`LEVEL`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--labels)`=[`KEY`=`VALUE`,…]] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--properties)`=[`PARAM`=`VALUE`,…]] [`[--properties-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--properties-file)`=`PROPERTIES_FILE`] [`[--query-output-format](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--query-output-format)`=`QUERY_OUTPUT_FORMAT`] [`[--start-after](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#--start-after)`=`STEP_ID`,[`[STEP_ID](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#STEP_ID)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add a Trino job to the workflow template.

**EXAMPLES**

: To add a Trino job that executes 'QUERY' to the workflow template
'my-workflow-template' in the 'us-central1' region with 'my-step-id',
run:

```
gcloud dataproc workflow-templates add-job trino --step-id=my-step_id -e=QUERY --workflow-template=my-workflow-template --region=us-central1
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

: **--client-tags**:
A list of Trino client tags to attach to this query.

**--continue-on-failure**:
Whether to continue if a query fails.

**--driver-log-levels**:
A list of package-to-log4j log level pairs to configure driver logging. For
example: root=FATAL,com.example=INFO

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud alpha dataproc workflow-templates add-job trino
```

```
gcloud beta dataproc workflow-templates add-job trino
```