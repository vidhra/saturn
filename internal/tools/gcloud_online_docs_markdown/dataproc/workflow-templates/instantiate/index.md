# gcloud dataproc workflow-templates instantiate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate)*

**NAME**

: **gcloud dataproc workflow-templates instantiate - instantiate a workflow template**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates instantiate` (`[TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate#TEMPLATE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate#--async)`] [`[--parameters](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate#--parameters)`=[`PARAM`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Instantiate a workflow template.

**EXAMPLES**

: To instantiate a workflow template 'my-template' in region 'us-central1' with
parameter set 'param1'='value1' and 'param2'='value2', run:

```
gcloud dataproc workflow-templates instantiate my-template --region=us-central1 --parameters="param1=value1,param2=value2"
```

**POSITIONAL ARGUMENTS**

: **Template resource - The name of the workflow template to run. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--parameters**:
A map from parameter names to values that should be used for those parameters. A
value must be provided for every configured parameter. Parameters can be
configured when creating or updating a workflow template.

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
gcloud alpha dataproc workflow-templates instantiate
```

```
gcloud beta dataproc workflow-templates instantiate
```