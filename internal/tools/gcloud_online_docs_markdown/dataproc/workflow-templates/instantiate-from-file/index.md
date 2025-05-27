# gcloud dataproc workflow-templates instantiate-from-file  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate-from-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate-from-file)*

**NAME**

: **gcloud dataproc workflow-templates instantiate-from-file - instantiate a workflow template from a file**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates instantiate-from-file` `[--file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate-from-file#--file)`=`FILE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate-from-file#--async)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate-from-file#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate-from-file#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Instantiate a workflow template from a file.

**EXAMPLES**

: To instantiate a workflow template from a yaml file 'template.yaml' in region
'us-central1', run:

```
gcloud dataproc workflow-templates instantiate-from-file --file=template.yaml --region=us-central1
```

**REQUIRED FLAGS**

: **--file**:
The YAML file containing the workflow template to run

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha dataproc workflow-templates instantiate-from-file
```

```
gcloud beta dataproc workflow-templates instantiate-from-file
```