# gcloud workflows executions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workflows/executions/describe](https://cloud.google.com/sdk/gcloud/reference/workflows/executions/describe)*

**NAME**

: **gcloud workflows executions describe - show metadata for a workflow execution**

**SYNOPSIS**

: **`gcloud workflows executions describe` (`[EXECUTION](https://cloud.google.com/sdk/gcloud/reference/workflows/executions/describe#EXECUTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/workflows/executions/describe#--location)`=`LOCATION` `[--workflow](https://cloud.google.com/sdk/gcloud/reference/workflows/executions/describe#--workflow)`=`WORKFLOW`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workflows/executions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display all metadata associated with a workflow execution of given ID.

**EXAMPLES**

: To describe an execution with ID 'my-workflow-execution-ID' from a workflow
named 'my-workflow', run:

```
gcloud workflows executions describe my-workflow-execution-ID --workflow=my-workflow
```

**POSITIONAL ARGUMENTS**

: **Execution resource - The name of the workflow execution to describe. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `execution` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`EXECUTION`**:
ID of the execution or fully qualified identifier for the execution.
To set the `execution` attribute:

- provide the argument `execution` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the execution. Alternatively, set the property
[workflows/location].
To set the `location` attribute:

- provide the argument `execution` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `workflows/location`.

**--workflow**:
The Cloud Workflow for the execution.
To set the `workflow` attribute:

- provide the argument `execution` on the command line with a fully
specified name;
- provide the argument `--workflow` on the command line.**

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

**API REFERENCE**

: This command uses the `workflowexecutions/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/workflows](https://cloud.google.com/workflows)

**NOTES**

: This variant is also available:

```
gcloud beta workflows executions describe
```