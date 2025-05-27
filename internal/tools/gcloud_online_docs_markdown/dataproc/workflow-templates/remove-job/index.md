# gcloud dataproc workflow-templates remove-job  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/remove-job](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/remove-job)*

**NAME**

: **gcloud dataproc workflow-templates remove-job - remove a job from workflow template**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates remove-job` (`[TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/remove-job#TEMPLATE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/remove-job#--region)`=`REGION`) [`[--step-id](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/remove-job#--step-id)`=`STEP_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/remove-job#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove a job from workflow template.

**EXAMPLES**

: To remove a job with step ID 'step-id' from a workflow template
'workflow-template' in region 'us-central1', run:

```
gcloud dataproc workflow-templates remove-job workflow-template --region=us-central1 --step-id=step-id
```

**POSITIONAL ARGUMENTS**

: **Template resource - The name of the workflow template to remove job. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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

: **--step-id**:
The step ID of the job in the workflow template to remove.

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
gcloud alpha dataproc workflow-templates remove-job
```

```
gcloud beta dataproc workflow-templates remove-job
```