# gcloud dataproc workflow-templates export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/export](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/export)*

**NAME**

: **gcloud dataproc workflow-templates export - export a workflow template**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates export` (`[TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/export#TEMPLATE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/export#--region)`=`REGION`) [`[--destination](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/export#--destination)`=`DESTINATION`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/export#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Exports a workflow template's configuration to a file. This configuration can be
imported at a later time.

**EXAMPLES**

: To export version 1.0 of workflow template for 'my-workflow-template' in region
'us-central1' to template.yaml, run:

```
gcloud dataproc workflow-templates export my-workflow-template --region=us-central1 --destination=path/to/template.yaml --version=1.0
```

**POSITIONAL ARGUMENTS**

: **Template resource - The name of the workflow template to export. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `template` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TEMPLATE`**:
ID of the template or fully qualified identifier for the template.
To set the `template` attribute:

- provide the argument `template` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Dataproc region for the template. Each Dataproc region constitutes an
independent resource namespace constrained to deploying instances into Compute
Engine zones inside the region. Overrides the default
`dataproc/region` property value for this command invocation.
To set the `region` attribute:

- provide the argument `template` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. Alternatively, you
may omit this flag to write to standard output.

**--version**:
The version of the workflow template.

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
gcloud alpha dataproc workflow-templates export
```

```
gcloud beta dataproc workflow-templates export
```