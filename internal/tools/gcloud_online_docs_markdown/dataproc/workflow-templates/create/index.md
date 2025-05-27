# gcloud dataproc workflow-templates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create)*

**NAME**

: **gcloud dataproc workflow-templates create - create a workflow template**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates create` (`[TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create#TEMPLATE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create#--region)`=`REGION`) [`[--dag-timeout](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create#--dag-timeout)`=`DAG_TIMEOUT`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a workflow template.

**EXAMPLES**

: To create a workflow template named
``my-workflow-template`` in region
``us-central1`` with label params
'key1'='value1' and 'key2'='value2', run:

```
gcloud dataproc workflow-templates create my-workflow-template --region=us-central1 --labels="key1=value1,key2=value2"
```

**POSITIONAL ARGUMENTS**

: **Template resource - The name of the workflow template to create. The arguments
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

: **--dag-timeout**:
The duration for which a DAG of jobs can run before being auto-cancelled, such
as "10m" or "16h". See $ [gcloud
topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats.

**--kms-key**:
The KMS key used to encrypt sensitive data in the workflow template.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud alpha dataproc workflow-templates create
```

```
gcloud beta dataproc workflow-templates create
```